from ui_tdj import Ui_mainWindow
import sys
import logging
import json
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox, QComboBox
from PySide2.QtCore import Qt

logging.getLogger().setLevel(logging.INFO)

# read config.json
with open('config.json', 'r') as f:
    try: config = json.load(f)
    except ValueError: logging.error("Json文件出错！")
cronListCfg = config["cronListCfg"]
dailyListCfg = config["dailyListCfg"]
detailCfg = config["detailCfg"]
device_ip = config["device_ip"]
app_name = config["app_name"]
with open('config2.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

class CamShow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(CamShow, self).__init__()
        self.setupUi(self)

        # load elements
        self.checkboxes = self.findChildren(QCheckBox)
        self.comboboxes = self.findChildren(QComboBox)

        # **********************
        # *** load port info ***
        # **********************
        self.connection_input_port.setText(device_ip)
        self.connection_input_port.textChanged.connect(self.update_port)
        # ******************
        # *** load tasks ***
        # ******************
        self.checkboxes_taskSelect = [
            checkbox for checkbox in self.checkboxes
            if "checkBox_taskSelect_" in checkbox.objectName()
        ]
        # load from settings
        self.load_tasks()
        # start to listen
        for checkbox in self.checkboxes_taskSelect:
            checkbox.stateChanged.connect(self.update_task)
        # ************************
        # *** load task config ***
        # ************************
        self.comboboxes_taskConfig = [
            combobox for combobox in self.comboboxes
            if "combBox_taskConfig_" in combobox.objectName()
        ]
        # load from settings
        self.load_taskConfigs()
        # start to listen
        for combobox in self.comboboxes_taskConfig:
            combobox.currentIndexChanged.connect(self.update_taskConfig)

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

    def update_taskConfig(self):
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

    def update_port(self):
        device_ip = self.sender().text()
        logging.info(f"device_ip -> {device_ip}")

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

    def load_taskConfigs(self):
        for combobox in self.comboboxes_taskConfig:
            task = combobox.whatsThis()
            index = 0
            if task in detailCfg:
                index = detailCfg[task]
            else:
                logging.error(f"ERROR: No such {task}.")
                continue
            text = combobox.itemText(index)
            combobox.setCurrentIndex(index)
            logging.debug(f"config {task} as {text}.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = CamShow()
    MainWindow.show()
    sys.exit(app.exec_())
