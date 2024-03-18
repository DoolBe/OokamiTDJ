import subprocess
import logging
import json

adb_dpi = 240
adb_resolution_x = 1280
adb_resolution_y = 720
adb_path_screenshot = "./"
adb_file_screenshot = "screenshot"

with open('config.json', 'r') as f:
    try:
        adb_config = json.load(f)
    except ValueError:
        logging.error("Json文件出错！")
adb_cronListCfg = adb_config["cronListCfg"]
adb_dailyListCfg = adb_config["dailyListCfg"]
adb_detailCfg = adb_config["detailCfg"]
adb_device_ip = adb_config["device_ip"]
adb_app_name = adb_config["app_name"]
adb_adb_path = adb_config["adb_path"]




# 运行ADB命令的函数
def adb_run_adb_command(cmd):
    result = subprocess.run((adb_adb_path + " -s " + adb_device_ip + " " + cmd).split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


# 连接到Android设备
def adb_connect_to_device(device_ip):
    cmd = adb_adb_path + " connect " + device_ip
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    if "connected" in result.stdout.decode('utf-8'):
        logging.debug("成功连接到设备：%s", device_ip)
        return True
    else:
        logging.error("无法连接到设备：%s", device_ip)
        return False


# 启动应用程序
def adb_start_app(package_name, activity_name):
    cmd = "shell am start -n " + package_name + "/" + activity_name
    output = adb_run_adb_command(cmd)
    if "Error" not in output:
        logging.debug("应用程序已成功启动！")
        return True
    else:
        logging.error("启动应用程序时出现错误。")
        return False


# 关闭应用程序
def adb_stop_app(package_name):
    cmd = "shell am force-stop " + package_name
    output = adb_run_adb_command(cmd)
    if "Error" not in output:
        logging.debug("应用程序已成功关闭！")
        return True
    else:
        logging.error("关闭应用程序时出现错误。")
        return False


# 获取应用程序名称，活动名称
def adb_find_app(pkg_str, act_str):
    cmd = "shell pm list packages -3"
    apps = adb_run_adb_command(cmd).split('\r\n')
    indices = [i for i, s in enumerate(apps) if pkg_str.lower() in s.lower()]
    if not indices:
        logging.error("应用程序未安装！")
        return False
    package_name = apps[indices[0]].split('package:')[1]
    cmd = "shell dumpsys package " + package_name + " | grep -E 'Activity|\bname='"
    activities = adb_run_adb_command(cmd).split('\r\n')
    indices = [i for i, s in enumerate(activities) if act_str.lower() in s.lower()]
    activity = activities[indices[0]].split(' ')
    indices = [i for i, s in enumerate(activity) if act_str.lower() in s.lower()]
    activity_name = activity[indices[0]].split('/')[1]

    return package_name, activity_name


def adb_get_resolution():
    cmd = "shell wm size"
    output = adb_run_adb_command(cmd)
    if "x" not in output:
        logging.debug("shell wm size: " + output)
        return False
    resolution = output.split(":")[1]
    resolutionx = int(resolution.split("x")[0])
    resolutiony = int(resolution.split("x")[1])
    logging.debug("current resolution %dx%d.", resolutionx, resolutiony)
    return resolutionx, resolutiony


def adb_get_dpi():
    cmd = "shell wm density"
    output = adb_run_adb_command(cmd)
    dpi = int(output.split(":")[1])
    logging.debug("current dpi %d.", dpi)
    return dpi


def adb_connect_emulator():
    # 连接到设备
    if not adb_connect_to_device(adb_device_ip): return False
    logging.debug("connect_to_device()！")
    # 检查分辨率
    out = adb_get_resolution()
    if not out:
        logging.error("get_resolution() 出错！")
        subprocess.run((adb_adb_path + " kill-server").split(), stdout=subprocess.PIPE)
        return False
    if adb_resolution_x * adb_resolution_y != out[0] * out[1]:
        logging.error("resolution 出错！")
        return False
    logging.debug("resolution成功！")
    # 检查dpi
    if adb_dpi != adb_get_dpi():
        logging.error("dpi 出错！")
        return False
    logging.info("connect emulator successfully.")
    return True


def adb_connect_app():
    # 测试是否安装应用程序
    found_app = adb_find_app(adb_app_name, "MainActivity")
    if not found_app:
        logging.error("未安装应用程序！")
        return False
    package_name, activity_name = found_app
    if not adb_start_app(package_name, activity_name):
        return False
    logging.info("connect app successfully.")
    return True


def adb_restart_app():
    package_name, activity_name = adb_find_app(adb_app_name, "MainActivity")
    if not adb_stop_app(package_name):
        return False
    if not adb_start_app(package_name, activity_name):
        return False
    logging.info("restart app successfully.")
    return True


def adb_do_screenshot(file=adb_file_screenshot, path=""):
    cmd = "shell screencap -p /sdcard/screenshot.png"
    output = adb_run_adb_command(cmd)
    cmd = "pull /sdcard/screenshot.png " + adb_path_screenshot + path + file + ".png"
    output = adb_run_adb_command(cmd)
    logging.debug("screenshot saved.")


def adb_click_at(x, y):
    cmd = "shell input tap " + str(x) + " " + str(y)
    output = adb_run_adb_command(cmd)
    logging.debug("clicked at <%d,%d>.", x, y)


def adb_click_back():
    cmd = "shell input keyevent 4"
    output = adb_run_adb_command(cmd)
    logging.debug("clicked <back>.")


def adb_click_home():
    cmd = "shell input keyevent 3"
    output = adb_run_adb_command(cmd)
    logging.debug("clicked <home>.")


def adb_swipe(x1, y1, x2, y2, dt=500):
    cmd = "shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(dt)
    # cmd = "shell input swipe "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)
    output = adb_run_adb_command(cmd)
    logging.debug("swipe from <%d,%d> to <%d,%d> from %fms.", x1, y1, x2, y2, dt)


def adb_textInput(text):
    cmd = 'shell input text "' + text + '"'
    output = adb_run_adb_command(cmd)
    logging.debug("input Text:" + text)


def adb_keyInput(keynum):
    cmd = 'shell input keyevent ' + keynum
    output = adb_run_adb_command(cmd)
    logging.debug("input keyboard:" + keynum)





