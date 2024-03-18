from PySide2.QtWidgets import QMainWindow, QCheckBox, QComboBox
from PySide2.QtCore import Qt
import logging
import json

from ui_tdj import Ui_mainWindow

with open('config.json', 'r') as f:
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

logging.getLogger().setLevel(logging.INFO)
configFile = 'setting.json'
currentConfigFile = 'config.json'


class CamShow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(CamShow, self).__init__()
        self.setupUi(self)

        # load elements
        self.checkboxes = self.findChildren(QCheckBox)
        self.comboboxes = self.findChildren(QComboBox)

        # load config file
        self.load_config_file()

        # load main page buttons
        self.main_button_load.clicked.connect(self.button_load)
        self.main_button_save.clicked.connect(self.button_save)
        self.main_button_start.clicked.connect(self.button_start)

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
        self.save_config_file(currentConfigFile)
        logging.info("Start...")
        logging.info("Done...")

    def button_save(self):
        self.save_config_file(configFile)
        logging.info("Config file saved.")

    def button_load(self):
        self.load_config_file()
        self.connection_input_adb.setText(adb_path)
        self.connection_input_port.setText(device_ip)
        self.load_tasks()
        self.load_task_configs()
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
        config = {}
        config["device_ip"] = device_ip
        config["app_name"] = app_name
        config["adb_path"] = adb_path
        config["cronListCfg"] = cronListCfg
        config["dailyListCfg"] = dailyListCfg
        config["detailCfg"] = detailCfg
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

    def update_port(self):
        device_ip = self.sender().text()
        logging.info(f"device_ip -> {device_ip}")

    def update_adb(self):
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
