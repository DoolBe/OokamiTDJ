import sys
import subprocess
import json
import logging
import os
import time
from datetime import datetime

from PySide2.QtWidgets import QMainWindow, QCheckBox, QComboBox, QApplication
from PySide2.QtCore import Qt
from ui_tdj import Ui_mainWindow
import cv2
import pickle
import gzip

logging.getLogger().setLevel(logging.INFO)

with gzip.open('corp.pkl.gz', 'rb') as ff: buttonImgDict = pickle.load(ff)
with gzip.open('task.pkl.gz', 'rb') as ff: taskDict = pickle.load(ff)

configFile = 'config.json'
with open(configFile, 'r') as ff:
    try:
        setting = json.load(ff)
    except ValueError:
        logging.error("Json文件出错！")
cronListCfg = setting["cronListCfg"]
dailyListCfg = setting["dailyListCfg"]
detailCfg = setting["detailCfg"]
device_ip = setting["device_ip"]
app_name = setting["app_name"]
adb_path = setting["adb_path"]

adb_dpi = 240
adb_resolution_x = 1280
adb_resolution_y = 720
adb_path_screenshot = "./"
adb_file_screenshot = "screenshot"

cronList = ["神龛", "历练", "王鼎", "通关文牒", "画境种植", "画境游历", "画境烹饪", "奇遇扫荡", "神龛",
            "天地阁助阵", "天地阁任务", "天地阁远征出发", "天地阁远征结束",
            "山河志-领取", "山河志-星耀行商", "山河志-星耀行商", "山河志-星耀行商", "山河志-星耀行商",
            "幻境挑战", "幻境扫荡", "幻境挑战", "幻境扫荡", "幻境收获", "异闻-创命之间", "神龛"]
dailyList = ["邮件", "好友", "交易", "召唤", "异闻-海捕令", "异闻-剑论九州", "异闻-幻海魂渊-雷鸟",
             "山河志-天乐魂光", "山河志-苍尘召唤", "山河志-忘生所向", "异闻-灵脉光渊", "画境秘制",
             "江湖-循环内修", "江湖-循环收集"]


# region ADB functions

# 运行ADB命令的函数
def adb_run_adb_command(cmd):
    result = subprocess.run((adb_path + " -s " + device_ip + " " + cmd).split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


# 连接到Android设备
def adb_connect_to_device():
    cmd = adb_path + " connect " + device_ip
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
    if not adb_connect_to_device(): return False
    logging.debug("connect_to_device()！")
    # 检查分辨率
    out = adb_get_resolution()
    if not out:
        logging.error("get_resolution() 出错！")
        subprocess.run((adb_path + " kill-server").split(), stdout=subprocess.PIPE)
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
    found_app = adb_find_app(app_name, "MainActivity")
    if not found_app:
        logging.error("未安装应用程序！")
        return False
    package_name, activity_name = found_app
    if not adb_start_app(package_name, activity_name):
        return False
    logging.info("connect app successfully.")
    return True


def adb_restart_app():
    package_name, activity_name = adb_find_app(app_name, "MainActivity")
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


# endregion ADB functions


# region CV functions

def match_Mask(template_img, target_img):
    # input:  template_img(np.array),target_img(np.array)
    # output: similarity(float),top_left(x,y),size(w,h)
    if template_img.shape[2] < 4:
        # 若仅有RGB，无alpha数据
        match_result_b = cv2.matchTemplate(target_img[:, :, 0], template_img[:, :, 0], cv2.TM_CCOEFF_NORMED)
        match_result_g = cv2.matchTemplate(target_img[:, :, 1], template_img[:, :, 1], cv2.TM_CCOEFF_NORMED)
        match_result_r = cv2.matchTemplate(target_img[:, :, 2], template_img[:, :, 2], cv2.TM_CCOEFF_NORMED)
    else:
        template_masak = template_img[:, :, 3]
        match_result_b = cv2.matchTemplate(target_img[:, :, 0], template_img[:, :, 0], cv2.TM_CCORR_NORMED,
                                           mask=template_masak)
        match_result_g = cv2.matchTemplate(target_img[:, :, 1], template_img[:, :, 1], cv2.TM_CCORR_NORMED,
                                           mask=template_masak)
        match_result_r = cv2.matchTemplate(target_img[:, :, 2], template_img[:, :, 2], cv2.TM_CCORR_NORMED,
                                           mask=template_masak)
    match_result_b[match_result_b == float('inf')] = 0
    match_result_g[match_result_g == float('inf')] = 0
    match_result_r[match_result_r == float('inf')] = 0
    match_result = (match_result_b + match_result_g + match_result_r) / 3.0
    # 找到匹配程度最高的像素位置
    min_val, similarity, min_loc, top_left = cv2.minMaxLoc(match_result)
    size = template_img.shape[:-1:][::-1]
    return similarity, top_left, size


def compare_screen(templateName):
    # input: templateName(str)
    # output: similarity(float),center(x,y)
    target = adb_path_screenshot + adb_file_screenshot + ".png"
    target_img = cv2.imread(target, cv2.IMREAD_UNCHANGED)

    template_imgs = [val for key, val in buttonImgDict.items() if templateName in key]
    largerSimilarity, center = 0, (0, 0)
    if template_imgs:
        for template_img in template_imgs:
            similarity, top_left, size = match_Mask(template_img, target_img)
            if similarity > largerSimilarity:
                largerSimilarity = similarity
                center = (top_left[0] + int(size[0] / 2), top_left[1] + int(size[1] / 2))
    return largerSimilarity, center


def saveOldScreenshot():
    target_path = adb_path_screenshot + adb_file_screenshot + ".png"
    oldTarget_path = adb_path_screenshot + adb_file_screenshot + "_old.png"
    if os.path.isfile(target_path):
        with open(target_path, 'rb') as fsrc:
            with open(oldTarget_path, 'wb') as fdst:
                fdst.write(fsrc.read())


threashold_screenshot_dup = 0.94


def isNewScreenshot():
    target_path = adb_path_screenshot + adb_file_screenshot + ".png"
    oldTarget_path = adb_path_screenshot + adb_file_screenshot + "_old.png"
    if os.path.isfile(target_path):
        with open(target_path, 'rb') as fsrc:
            with open(oldTarget_path, 'wb') as fdst:
                fdst.write(fsrc.read())
    get_screenshot()
    target_img = cv2.imread(target_path, cv2.IMREAD_UNCHANGED)
    oldscreen_img = cv2.imread(oldTarget_path, cv2.IMREAD_UNCHANGED)
    similarity = match_Mask(oldscreen_img, target_img)[0]
    if similarity > threashold_screenshot_dup:
        logging.debug("无新画面.")
        return False
    logging.debug("新画面, similarity = %f.", similarity)
    return True


threshold_isInScreen = 0.98
retryTime_isInScreen = 2
sleepTime_isInScreen = 0.1


def isInScreen(template, takeScreenshot=False, isNot=False):
    if not len(template): return True ^ isNot
    retryChance = retryTime_isInScreen

    while retryChance:
        if takeScreenshot: get_screenshot()
        similarity, center = compare_screen(template)
        if similarity > threshold_isInScreen:
            logging.debug("Successfully found <%s>.", template)
            logging.debug("locate at <%s>, similarity is %f.", center, similarity)
            return True ^ isNot
        else:
            logging.debug("Didn't find button <%s>...threshold=%f, retry.", template, similarity)
        retryChance -= 1
        time.sleep(sleepTime_isInScreen)
    logging.debug("Cannot find <%s>", template)
    return False ^ isNot


sleepTime_loading = 1
threshold_loading = 0.98


def get_screenshot(retry=20):
    if not retry:
        logging.error("get_screenshot卡住.")
        quit()
        # restart

    # here target_img is the new screenshot
    target_path = adb_path_screenshot + adb_file_screenshot + ".png"
    adb_do_screenshot()
    target_img = cv2.imread(target_path, cv2.IMREAD_UNCHANGED)

    # check if waiting
    template_img = buttonImgDict["重连-载入中1"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("载入中.")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)
    # check if waiting
    template_img = buttonImgDict["重连-载入中2"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("载入中.")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)
    # check black
    template_img = buttonImgDict["重连-黑屏"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("黑屏中.")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)
    # check if waiting
    template_img = buttonImgDict["重连-战斗载入"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("战斗载入中.")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)
    # check reconnect
    template_img = buttonImgDict["重连-断线重连"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("断线重连.")
        step_decoder("button", "重连-重连")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)
    # check reconnect
    template_img = buttonImgDict["重连-恢复体力"]
    if match_Mask(template_img, target_img)[0] > threshold_loading:
        logging.info("恢复体力.")
        step_decoder("button", "重连-烤鱼")
        time.sleep(sleepTime_loading)
        return get_screenshot(retry - 1)


threshold_click_on_button = 0.98
sleepTime_click_on_button = 0.1


# endregion cv functions


# region Operate Screen functions

def click_on_button(buttonName):
    similarity, center = compare_screen(buttonName)
    if similarity > threshold_click_on_button:
        adb_click_at(*center)
        logging.debug("Clicked button <%s>.", buttonName)
        logging.debug("locate at <%s>, similarity is %f.", center, similarity)
        time.sleep(sleepTime_click_on_button)
        return True
    else:
        logging.error("Cannot find button <%s>...threshold=%f", buttonName, similarity)
        return False


xuanren_charaName = "夏侯仪"


def choose_Chara():
    if "人物-" + xuanren_charaName not in buttonImgDict:
        logging.error("Don't have Chara <%s>", xuanren_charaName)
        return False
    attempt = 1
    x1, y1, y2 = 293, 500, 250
    get_screenshot()
    while attempt:
        if isInScreen("人物-" + xuanren_charaName):
            logging.debug("Found Chara <%s>.", xuanren_charaName)
            click_on_button("人物-" + xuanren_charaName)
            return True
        adb_swipe(x1, y1, x1, y2, 1000)
        time.sleep(1)
        attempt += 1
        if not isNewScreenshot():
            attempt = 0
        if attempt > 15:
            logging.error("Too much attemps to find Chara <%s>", xuanren_charaName)
            return False
    logging.error("Can't find Chara <%s>", xuanren_charaName)
    return False


retryTime_step = 5
sleepTime_step = 1


def runStep(checkbefore="", stepName="", stepPara="", checkafter="", beforeIsNot=False, afterIsNot=False):
    # will take screenshot for checkBefore and checkAfter.
    logging.debug("STEP=%s(%s),%s%s,%s(%s).", checkbefore, not beforeIsNot, stepName, stepPara, checkafter,
                  not afterIsNot)
    if not isInScreen(checkbefore, takeScreenshot=True, isNot=beforeIsNot):
        logging.debug("Check-before failed--%s(%s).", checkbefore, not beforeIsNot)
        return False
    else:
        logging.debug("Check-before successful--%s(%s).", checkbefore, not beforeIsNot)

    for i in range(retryTime_step):
        step_decoder(stepName, stepPara)
        time.sleep(sleepTime_step)
        if isInScreen(checkafter, takeScreenshot=True, isNot=afterIsNot):
            logging.debug("Check-after successful--%s(%s).", checkafter, not afterIsNot)
            return True
        else:
            logging.debug("Check-after failed %d time, sleep %ds and retry.", i + 1, sleepTime_step)
    logging.debug("Check-after failed %s(%s).", checkafter, not afterIsNot)
    return False


sleepTime_swipe = 0.5
jiurutaNum, neixiuNum, wuchiNum, shoujiNum = 1, 1, 1, 1
jiurutaButton = ["异闻-九如塔-按钮-扫荡一", "异闻-九如塔-按钮-扫荡二", "异闻-九如塔-按钮-扫荡三"]
neixiuButton = ["江湖-按钮-黄一", "江湖-按钮-黄二", "江湖-按钮-紫一", "江湖-按钮-紫二", "江湖-按钮-蓝一",
                "江湖-按钮-蓝二"]
shoujiButton = ["江湖-收集-黄一", "江湖-收集-红二", "江湖-收集-蓝三", "江湖-收集-绿四", "江湖-收集-红五"]
wuchiButton = ["异闻-九如塔-五炽-日之岚未选中", "异闻-九如塔-五炽-川之岚未选中",
               "异闻-九如塔-五炽-山之岚未选中", "异闻-九如塔-五炽-松之岚未选中", "异闻-九如塔-五炽-月之岚未选中"]


def step_decoder(stepName, stepPara=""):
    logging.debug("Run step <%s,%s>.", stepName, stepPara)
    if stepName == "button":
        click_on_button(stepPara)
    if stepName == "click":
        adb_click_at(int(stepPara.split(',')[0]), int(stepPara.split(',')[1]))
    if stepName == "clickback":
        adb_click_back()
    if stepName == "text":
        adb_textInput(stepPara)
    if stepName == "key":
        if stepPara == "enter": adb_keyInput("66")
    if stepName == "mainpage":
        mainpage()
    if stepName == "wait":
        time.sleep(int(stepPara))
    if stepName == "swipe":
        direction, times = stepPara[0], int(stepPara[1:])
        dx = int(adb_resolution_x / 8)
        dy = int(adb_resolution_y / 8)
        x1, y1 = dx * 4, dy * 4
        for i in range(times):
            if direction == '左': adb_swipe(x1, y1, x1 - dx, y1)
            if direction == '右': adb_swipe(x1, y1, x1 + dx, y1)
            if direction == '上': adb_swipe(x1, y1, x1, y1 - dy)
            if direction == '下': adb_swipe(x1, y1, x1, y1 + dy)
            # logging.info("swipe "+direction)
            time.sleep(sleepTime_swipe)
    if stepName == "jiuruta":
        click_on_button(jiurutaButton[jiurutaNum - 1])
    if stepName == "wuchi":
        click_on_button(wuchiButton[wuchiNum - 1])
    if stepName == "neixiu":
        click_on_button(neixiuButton[neixiuNum - 1])
    if stepName == "shouji":
        click_on_button(shoujiButton[shoujiNum - 1])
    if stepName == "xuanren":
        choose_Chara()


threshold_login = 0.998
retryTime_login = 5
sleepTime_login = 2


def buttonList_from_substr(button_substr):
    buttonList = []
    for button in buttonImgDict:
        if button_substr not in button: continue
        buttonList.append(button)
    return buttonList


def login_script():
    # check mainpage or not
    get_screenshot()
    if isInScreen("主页-汉堡"):
        logging.debug("Already Login.")
        return True
    if isInScreen("按钮-返回") and not isInScreen("登录-页面-游戏公告"):
        logging.debug("Already Login.")
        return True

    # check if still LOADING
    if not isInScreen("登录-页面-游戏公告") and not isInScreen("登录-页面-适龄提示"):
        i = 0
        while i < retryTime_login:
            get_screenshot()
            i += 1
            # 检查是否还在等待登录，是则重置i
            if compare_screen("登录-等待-")[0] > threshold_login:
                logging.info("登录-等待...")
                i = 0
                # 检查是否登录，是则设置i
            if i and isInScreen("登录-页面-游戏公告"):
                logging.info("登录-游戏公告...")
                i = retryTime_login + 1
                break
            time.sleep(sleepTime_login)

        if i == retryTime_login:
            logging.error("Login retry fail")
            return False
        if i == retryTime_login + 1:
            logging.debug("Login...登录-页面-游戏公告")

    runStep("登录-页面-游戏公告", "button", "按钮-关闭", "登录-页面-适龄提示")
    time.sleep(5)
    xy = str(int(adb_resolution_x / 2)) + ',' + str(int(adb_resolution_y / 2))
    if runStep("登录-页面-适龄提示", "click", xy, ""): time.sleep(5)
    logging.info("完成登录")
    # runStep("登录-页面-每月签到","button","按钮-关闭","主页-1书阁")
    return True


def task_script(task_name):
    # input: task_name(str)
    task = taskDict[task_name]
    # 返回主页
    mainpage()
    for step in task:
        # 翻译执行每一步
        logging.info("%s:%s", task_name, step)
        stepRes = runStep(task[step]["checkbefore"], task[step]["stepName"], task[step]["stepPara"],
                          task[step]["checkafter"], task[step]["beforeIsNot"], task[step]["afterIsNot"])
        if task[step]["stepName"] == "mainpage" and stepRes:
            return "Return"
    logging.info("%s:%s", task_name, "返回主页")
    mainpage()
    # mainpage() # optional* This makes it looks cleaner.
    return "Done"


sleepTime_mainpage = 0.3


def mainpage(retry=20):
    time.sleep(sleepTime_mainpage)
    get_screenshot()
    # logging.debug("mainpage retry=%d.",retry)

    if isInScreen("登录-退出游戏"):
        step_decoder("clickback", "")
        return mainpage(retry - 1)
    # 若已经主页
    if isInScreen("主页-1书阁") and isInScreen("主页-1启程"):
        logging.info("至主页")
        return True
    if isInScreen("按钮-关闭"):
        step_decoder("button", "按钮-关闭")
        return mainpage(retry - 1)
    if isInScreen("按钮-返回"):
        step_decoder("button", "按钮-返回")
        return mainpage(retry - 1)
    if isInScreen("主页-2扎营"):
        step_decoder("button", "主页-2扎营")
        return mainpage(retry - 1)

    if isInScreen("按钮-获得物品"):
        step_decoder("click", "600,700")
    elif isInScreen("登录-本期活动"):
        step_decoder("click", "1200,360")
    elif isInScreen("重连-载入中"):
        step_decoder("wait", "1")
    else:
        logging.error("Main page--No found.")
        saveOldScreenshot()
        step_decoder("clickback", "")

    return mainpage(retry - 1)


# endregion Operate Screen functions


# region Task functions

def every_x_days(x):
    start_date = datetime(2024, 1, 1)  # 默认起始日期为20240101
    today = datetime.now()
    days_since_start = (today - start_date).days
    cycle_index = days_since_start % x
    return cycle_index + 1


def connect_test():
    # 启动，连接模拟器
    if not adb_connect_emulator(): return False
    # 启动app
    if not adb_connect_app(): return False
    return "Connected"


def cronTasks():
    for job in cronList:
        try:
            if not cronListCfg[job]:
                ret = "Skip"
            else:
                ret = task_script(job)
        except KeyError:
            ret = "Skip"
        print(job, ret)


def dailyTasks():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    for job in dailyList:
        try:
            if not dailyListCfg[job]:
                ret = "Skip"
            else:
                ret = task_script(job)
        except KeyError:
            ret = "Skip"
        if ret == "Skip":
            print(job, ret)
        if ret == "Done":
            dailyListCfg[job] = False
            print(job, ret)

    global xuanren_charaName
    for job in ["山河志-三魂一", "山河志-三魂二", "山河志-三魂三"]:
        xuanren_charaName = detailCfg[job]
        if not dailyListCfg[job]:
            ret = "Skip"
        else:
            ret = task_script(job)
        if ret == "Skip":
            print(job, xuanren_charaName, ret)
        if ret == "Done":
            dailyListCfg[job] = False
            print(job, ret)

    global jiurutaNum
    if not dailyListCfg["异闻-九如塔-镜渊"]:
        print("异闻-九如塔-镜渊 skip")
    else:
        for job in ["异闻-九如塔-镜渊1", "异闻-九如塔-镜渊2", "异闻-九如塔-镜渊3"]:
            jiurutaNum = detailCfg[job]
            if not jiurutaNum:
                ret = "Skip"
            else:
                ret = task_script("异闻-九如塔-镜渊")
            if ret == "Skip":
                print(job, jiurutaNum, ret)
            if ret == "Done":
                detailCfg[job] = 0
                print(job, ret)

    global wuchiNum
    wuchiNum = detailCfg["异闻-九如塔-五炽"]
    if not dailyListCfg["异闻-九如塔-五炽"]:
        print("异闻-九如塔-五炽 skip")
    elif not wuchiNum:
        print("skip 异闻-九如塔-五炽")
    else:
        for job in ["异闻-九如塔-五炽1", "异闻-九如塔-五炽2", "异闻-九如塔-五炽3"]:
            jiurutaNum = detailCfg[job]
            if not jiurutaNum:
                ret = "Skip"
            else:
                ret = task_script("异闻-九如塔-五炽")
            if ret == "Skip":
                print(job, wuchiNum, jiurutaNum, ret)
            if ret == "Done":
                detailCfg[job] = 0
                print(job, ret)

    global neixiuNum
    if not dailyListCfg["江湖-内修"]:
        print("江湖-内修 skip")
    else:
        for job in ["内修1", "内修2", "内修3"]:
            neixiuNum = detailCfg[job]
            if neixiuNum > 6:
                neixiuNum = every_x_days(6)
            if not neixiuNum:
                ret = "Skip"
            else:
                ret = task_script("江湖-内修")
            if ret == "Skip":
                print(job, neixiuNum, ret)
            if ret == "Done":
                detailCfg[job] = 0
                print(job, ret)

    global shoujiNum
    if not dailyListCfg["江湖-收集"]:
        print("江湖-收集 skip")
    else:
        for job in ["收集1", "收集2", "收集3"]:
            shoujiNum = detailCfg[job]
            if shoujiNum > 5:
                shoujiNum = every_x_days(5)
            if not shoujiNum:
                ret = "Skip"
            else:
                ret = task_script("江湖-收集")
            if ret == "Skip":
                print(job, shoujiNum, ret)
            if ret == "Done":
                detailCfg[job] = 0
                print(job, ret)


def job_script():
    login_script()
    # 至主页
    mainpage()
    cronTasks()
    dailyTasks()
    cronTasks()


# endregion Task functions



class CamShow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(CamShow, self).__init__()
        self.setupUi(self)

        # load elements
        self.checkboxes = self.findChildren(QCheckBox)
        self.comboboxes = self.findChildren(QComboBox)

        # load log window
        self.log_select = 0  # 1-connection_log, 0-main_textBox_Log
        self.stdout = sys.stdout
        sys.stdout = self

        # load config file
        self.load_config_file()

        # load buttons
        self.main_button_load.clicked.connect(self.button_load)
        self.main_button_save.clicked.connect(self.button_save)
        self.main_button_start.clicked.connect(self.button_start)
        self.connection_button_connect.clicked.connect(self.button_connect)

        # load port
        self.connection_input_port.setText(device_ip)
        self.connection_input_port.textChanged.connect(self.update_port)
        # load adb
        self.connection_input_adb.setText(adb_path)
        self.connection_input_adb.textChanged.connect(self.update_adb)

        # load task config
        self.comboboxes_taskConfig = [
            combobox for combobox in self.comboboxes
            if "comboBox_taskConfig_" in combobox.objectName()
        ]
        self.load_task_configs()
        for combobox in self.comboboxes_taskConfig:
            combobox.currentIndexChanged.connect(self.update_task_config)
            combobox.setEnabled(False)
        # dis/enable config according to task selected
        self.checkBox_taskSelect_jiuruta_wuzhi.stateChanged.connect(self.disable_jiuruta_wuzhi)
        self.checkBox_taskSelect_jiuruta_jinyuan.stateChanged.connect(self.disable_jiuruta_jinyuan)
        self.checkBox_taskSelect_jianghu_neixiu.stateChanged.connect(self.disable_jianghu_neixiu)
        self.checkBox_taskSelect_jianghu_shouji.stateChanged.connect(self.disable_jianghu_shouji)
        # load tasks
        self.checkboxes_taskSelect = [
            checkbox for checkbox in self.checkboxes
            if "checkBox_taskSelect_" in checkbox.objectName()
        ]
        self.load_tasks()
        for checkbox in self.checkboxes_taskSelect:
            checkbox.stateChanged.connect(self.update_task)

    def button_start(self):
        logging.info("Start...")
        print("Start...")
        job_script()
        print("Finish...")
        logging.info("Finish...")

    def button_connect(self):
        logging.info("Start...")
        self.log_select = 1
        print(connect_test())
        self.log_select = 0
        logging.info("Done...")

    def write(self, text):
        # 将输出文本添加到 QPlainTextEdit
        if self.log_select:
            cursor = self.connection_log.textCursor()
        else:
            cursor = self.main_textBox_Log.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)

    def __del__(self):
        # 在程序结束时恢复原始的标准输出流
        sys.stdout = self.stdout

    def button_save(self):
        self.save_config_file(configFile)
        print("Saved")
        logging.info("Config file saved.")

    def button_load(self):
        self.load_config_file()
        self.connection_input_adb.setText(adb_path)
        self.connection_input_port.setText(device_ip)
        self.load_tasks()
        self.load_task_configs()
        print("Loaded")
        logging.info("Config file loaded.")

    def load_config_file(self):
        global cronListCfg, dailyListCfg, detailCfg, device_ip, app_name, adb_path
        with open(configFile, 'r') as f:
            try:
                config = json.load(f)
            except ValueError:
                logging.error("Json文件出错！")
        cronListCfg = config["cronListCfg"]
        dailyListCfg = config["dailyListCfg"]
        detailCfg = config["detailCfg"]
        device_ip = config["device_ip"]
        app_name = config["app_name"]
        adb_path = config["adb_path"]

    def save_config_file(self, file):
        global cronListCfg, dailyListCfg, detailCfg, device_ip, app_name, adb_path
        config = {"device_ip": device_ip, "app_name": app_name, "adb_path": adb_path, "cronListCfg": cronListCfg,
                  "dailyListCfg": dailyListCfg, "detailCfg": detailCfg}
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

    def update_port(self):
        global device_ip
        device_ip = self.sender().text()
        logging.info(f"device_ip -> {device_ip}")

    def update_adb(self):
        global adb_path
        adb_path = self.sender().text()
        logging.info(f"adb path -> {adb_path}")

    def update_task(self, state):
        task = self.sender().text()
        value = bool(state)
        # update
        if task in cronListCfg:
            cronListCfg[task] = value
        elif task in dailyListCfg:
            dailyListCfg[task] = value
        else:
            logging.error(f"ERROR: No such {task}.")
            return
        logging.info(f"{task} -> {value}")

    def load_tasks(self):
        for checkbox in self.checkboxes_taskSelect:
            task = checkbox.text()
            state = False
            if task in dailyListCfg:
                state = dailyListCfg[task]
            elif task in cronListCfg:
                state = cronListCfg[task]
            else:
                logging.error(f"ERROR: No such {task}.")
                continue
            if state:
                checkbox.setCheckState(Qt.CheckState.Checked)
            else:
                checkbox.setCheckState(Qt.CheckState.Unchecked)
            logging.debug(f"load {task} as {state}.")

    def update_task_config(self):
        task = self.sender().whatsThis()
        index = self.sender().currentIndex()
        text = self.sender().itemText(index)
        # update
        if task in detailCfg:
            detailCfg[task] = index
        else:
            logging.error(f"ERROR: No such {task}.")
            return
        logging.info(f"{task} -> {text}")

    def load_task_configs(self):
        for combobox in self.comboboxes_taskConfig:
            task = combobox.whatsThis()
            if task in detailCfg:
                index = detailCfg[task]
            else:
                logging.error(f"ERROR: No such {task}.")
                continue
            text = combobox.itemText(index)
            combobox.setCurrentIndex(index)
            logging.debug(f"config {task} as {text}.")

    def disable_jiuruta_wuzhi(self, state):
        for combobox in self.comboboxes_taskConfig:
            if "comboBox_taskConfig_jiuruta_" not in combobox.objectName(): continue
            if "comboBox_taskConfig_jiuruta_jinyuan" in combobox.objectName(): continue
            combobox.setEnabled(bool(state))

    def disable_jiuruta_jinyuan(self, state):
        for combobox in self.comboboxes_taskConfig:
            if "comboBox_taskConfig_jiuruta_jinyuan" in combobox.objectName():
                combobox.setEnabled(bool(state))

    def disable_jianghu_neixiu(self, state):
        for combobox in self.comboboxes_taskConfig:
            if "comboBox_taskConfig_jianghu_neixiu" in combobox.objectName():
                combobox.setEnabled(bool(state))

    def disable_jianghu_shouji(self, state):
        for combobox in self.comboboxes_taskConfig:
            if "comboBox_taskConfig_jianghu_shouji" in combobox.objectName():
                combobox.setEnabled(bool(state))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = CamShow()

    # special config
    MainWindow.checkBox_taskSelect_jiuruta_wuzhi.setEnabled(False)

    MainWindow.show()
    sys.exit(app.exec_())
