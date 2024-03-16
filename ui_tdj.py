# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tdjvjAaua.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(476, 555)
        font = QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        mainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_18 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_MainPage = QWidget()
        self.tab_MainPage.setObjectName(u"tab_MainPage")
        self.verticalLayout_12 = QVBoxLayout(self.tab_MainPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.main_label_manual = QLabel(self.tab_MainPage)
        self.main_label_manual.setObjectName(u"main_label_manual")

        self.verticalLayout_12.addWidget(self.main_label_manual)

        self.line = QFrame(self.tab_MainPage)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_button_load = QPushButton(self.tab_MainPage)
        self.main_button_load.setObjectName(u"main_button_load")

        self.horizontalLayout.addWidget(self.main_button_load)

        self.main_button_save = QPushButton(self.tab_MainPage)
        self.main_button_save.setObjectName(u"main_button_save")

        self.horizontalLayout.addWidget(self.main_button_save)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.main_button_start = QPushButton(self.tab_MainPage)
        self.main_button_start.setObjectName(u"main_button_start")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.main_button_start.setFont(font1)

        self.verticalLayout_12.addWidget(self.main_button_start)

        self.line_2 = QFrame(self.tab_MainPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.main_label_Log = QHBoxLayout()
        self.main_label_Log.setObjectName(u"main_label_Log")
        self.main_label_Log_spacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.main_label_Log.addItem(self.main_label_Log_spacer1)

        self.main_label_Log_text = QLabel(self.tab_MainPage)
        self.main_label_Log_text.setObjectName(u"main_label_Log_text")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.main_label_Log_text.setFont(font2)

        self.main_label_Log.addWidget(self.main_label_Log_text)

        self.main_label_Log_spacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.main_label_Log.addItem(self.main_label_Log_spacer2)


        self.verticalLayout_12.addLayout(self.main_label_Log)

        self.main_textBox_Log = QPlainTextEdit(self.tab_MainPage)
        self.main_textBox_Log.setObjectName(u"main_textBox_Log")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_textBox_Log.sizePolicy().hasHeightForWidth())
        self.main_textBox_Log.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.main_textBox_Log)

        self.tabWidget.addTab(self.tab_MainPage, "")
        self.tab_Tasks = QWidget()
        self.tab_Tasks.setObjectName(u"tab_Tasks")
        self.verticalLayout_14 = QVBoxLayout(self.tab_Tasks)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_18 = QLabel(self.tab_Tasks)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_18)

        self.area_taskLoop_2 = QHBoxLayout()
        self.area_taskLoop_2.setObjectName(u"area_taskLoop_2")
        self.area_runSingle_2 = QVBoxLayout()
        self.area_runSingle_2.setObjectName(u"area_runSingle_2")
        self.checkBox_taskSelect_shenkan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shenkan.setObjectName(u"checkBox_taskSelect_shenkan")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_shenkan)

        self.checkBox_taskSelect_lilian = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_lilian.setObjectName(u"checkBox_taskSelect_lilian")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_lilian)

        self.checkBox_taskSelect_wangdin = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_wangdin.setObjectName(u"checkBox_taskSelect_wangdin")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_wangdin)

        self.checkBox_taskSelect_youjian = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_youjian.setObjectName(u"checkBox_taskSelect_youjian")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_youjian)

        self.checkBox_taskSelect_haoyou = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_haoyou.setObjectName(u"checkBox_taskSelect_haoyou")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_haoyou)

        self.checkBox_taskSelect_jiaoyi = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_jiaoyi.setObjectName(u"checkBox_taskSelect_jiaoyi")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_jiaoyi)

        self.checkBox_taskSelect_zhaohuan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_zhaohuan.setObjectName(u"checkBox_taskSelect_zhaohuan")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_zhaohuan)

        self.checkBox_taskSelect_tongguanwendie = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tongguanwendie.setObjectName(u"checkBox_taskSelect_tongguanwendie")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_tongguanwendie)

        self.checkBox_taskSelect_qiyusaodang = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_qiyusaodang.setObjectName(u"checkBox_taskSelect_qiyusaodang")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_qiyusaodang)

        self.checkBox_taskSelect_huajinpenren = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huajinpenren.setObjectName(u"checkBox_taskSelect_huajinpenren")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_huajinpenren)

        self.checkBox_taskSelect_huajinmizhi = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huajinmizhi.setObjectName(u"checkBox_taskSelect_huajinmizhi")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_huajinmizhi)

        self.checkBox_taskSelect_huajinzhongzhi = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huajinzhongzhi.setObjectName(u"checkBox_taskSelect_huajinzhongzhi")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_huajinzhongzhi)

        self.checkBox_taskSelect_huajinyouli = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huajinyouli.setObjectName(u"checkBox_taskSelect_huajinyouli")

        self.area_runSingle_2.addWidget(self.checkBox_taskSelect_huajinyouli)


        self.area_taskLoop_2.addLayout(self.area_runSingle_2)

        self.line_21 = QFrame(self.tab_Tasks)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.area_taskLoop_2.addWidget(self.line_21)

        self.area_runLoop_2 = QVBoxLayout()
        self.area_runLoop_2.setObjectName(u"area_runLoop_2")
        self.checkBox_taskSelect_huanjin_tiaozhan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huanjin_tiaozhan.setObjectName(u"checkBox_taskSelect_huanjin_tiaozhan")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_huanjin_tiaozhan)

        self.checkBox_taskSelect_huanjin_saodang = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huanjin_saodang.setObjectName(u"checkBox_taskSelect_huanjin_saodang")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_huanjin_saodang)

        self.checkBox_taskSelect_huanjin_shouhuo = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_huanjin_shouhuo.setObjectName(u"checkBox_taskSelect_huanjin_shouhuo")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_huanjin_shouhuo)

        self.checkBox_taskSelect_yiwen_haibulin = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_yiwen_haibulin.setObjectName(u"checkBox_taskSelect_yiwen_haibulin")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_yiwen_haibulin)

        self.checkBox_taskSelect_yiwen_jianlunjiuzhou = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_yiwen_jianlunjiuzhou.setObjectName(u"checkBox_taskSelect_yiwen_jianlunjiuzhou")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_yiwen_jianlunjiuzhou)

        self.checkBox_taskSelect_yiwen_huanhaihunyuan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_yiwen_huanhaihunyuan.setObjectName(u"checkBox_taskSelect_yiwen_huanhaihunyuan")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_yiwen_huanhaihunyuan)

        self.checkBox_taskSelect_yiwen_linmaiguangyuan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_yiwen_linmaiguangyuan.setObjectName(u"checkBox_taskSelect_yiwen_linmaiguangyuan")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_yiwen_linmaiguangyuan)

        self.checkBox_taskSelect_yiwen_chuangmin = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_yiwen_chuangmin.setObjectName(u"checkBox_taskSelect_yiwen_chuangmin")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_yiwen_chuangmin)

        self.checkBox_taskSelect_jiuruta_jinyuan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_jiuruta_jinyuan.setObjectName(u"checkBox_taskSelect_jiuruta_jinyuan")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_jiuruta_jinyuan)

        self.checkBox_taskSelect_jiuruta_wuzhi = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_jiuruta_wuzhi.setObjectName(u"checkBox_taskSelect_jiuruta_wuzhi")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_jiuruta_wuzhi)

        self.checkBox_taskSelect_jianghu_neixiu = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_jianghu_neixiu.setObjectName(u"checkBox_taskSelect_jianghu_neixiu")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_jianghu_neixiu)

        self.checkBox_taskSelect_jianghu_shouji = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_jianghu_shouji.setObjectName(u"checkBox_taskSelect_jianghu_shouji")

        self.area_runLoop_2.addWidget(self.checkBox_taskSelect_jianghu_shouji)


        self.area_taskLoop_2.addLayout(self.area_runLoop_2)

        self.line_20 = QFrame(self.tab_Tasks)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.area_taskLoop_2.addWidget(self.line_20)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_taskSelect_tiandige_zhuzhen = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tiandige_zhuzhen.setObjectName(u"checkBox_taskSelect_tiandige_zhuzhen")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_tiandige_zhuzhen)

        self.checkBox_taskSelect_tiandige_renwu = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tiandige_renwu.setObjectName(u"checkBox_taskSelect_tiandige_renwu")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_tiandige_renwu)

        self.checkBox_taskSelect_tiandige_huigui = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tiandige_huigui.setObjectName(u"checkBox_taskSelect_tiandige_huigui")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_tiandige_huigui)

        self.checkBox_taskSelect_tiandige_chufa = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tiandige_chufa.setObjectName(u"checkBox_taskSelect_tiandige_chufa")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_tiandige_chufa)

        self.checkBox_taskSelect_shanhezhi_shouqu = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_shouqu.setObjectName(u"checkBox_taskSelect_shanhezhi_shouqu")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_shouqu)

        self.checkBox_taskSelect_shanhezhi_sanhun1 = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_sanhun1.setObjectName(u"checkBox_taskSelect_shanhezhi_sanhun1")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_sanhun1)

        self.checkBox_taskSelect_shanhezhi_sanhun2 = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_sanhun2.setObjectName(u"checkBox_taskSelect_shanhezhi_sanhun2")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_sanhun2)

        self.checkBox_taskSelect_shanhezhi_sanhun3 = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_sanhun3.setObjectName(u"checkBox_taskSelect_shanhezhi_sanhun3")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_sanhun3)

        self.checkBox_taskSelect_shanhezhi_cangchenzhaohuan = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_cangchenzhaohuan.setObjectName(u"checkBox_taskSelect_shanhezhi_cangchenzhaohuan")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_cangchenzhaohuan)

        self.checkBox_taskSelect_shanhezhi_wangshensuoxiang = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_wangshensuoxiang.setObjectName(u"checkBox_taskSelect_shanhezhi_wangshensuoxiang")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_wangshensuoxiang)

        self.checkBox_taskSelect_tianlehunguang = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_tianlehunguang.setObjectName(u"checkBox_taskSelect_tianlehunguang")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_tianlehunguang)

        self.checkBox_taskSelect_shanhezhi_xinyaoxinshang = QCheckBox(self.tab_Tasks)
        self.checkBox_taskSelect_shanhezhi_xinyaoxinshang.setObjectName(u"checkBox_taskSelect_shanhezhi_xinyaoxinshang")

        self.verticalLayout_15.addWidget(self.checkBox_taskSelect_shanhezhi_xinyaoxinshang)


        self.area_taskLoop_2.addLayout(self.verticalLayout_15)


        self.verticalLayout_14.addLayout(self.area_taskLoop_2)

        self.label_14 = QLabel(self.tab_Tasks)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.label_14)

        self.tabWidget.addTab(self.tab_Tasks, "")
        self.tab_ConnectionSetting = QWidget()
        self.tab_ConnectionSetting.setObjectName(u"tab_ConnectionSetting")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab_ConnectionSetting.sizePolicy().hasHeightForWidth())
        self.tab_ConnectionSetting.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.tab_ConnectionSetting)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tab_ConnectionSetting)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label_2)

        self.connection_input_adb = QLineEdit(self.tab_ConnectionSetting)
        self.connection_input_adb.setObjectName(u"connection_input_adb")

        self.verticalLayout_5.addWidget(self.connection_input_adb)

        self.label_13 = QLabel(self.tab_ConnectionSetting)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label_13)

        self.connection_input_port = QLineEdit(self.tab_ConnectionSetting)
        self.connection_input_port.setObjectName(u"connection_input_port")

        self.verticalLayout_5.addWidget(self.connection_input_port)

        self.label_17 = QLabel(self.tab_ConnectionSetting)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label_17)

        self.connection_button_connect = QPushButton(self.tab_ConnectionSetting)
        self.connection_button_connect.setObjectName(u"connection_button_connect")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.connection_button_connect.sizePolicy().hasHeightForWidth())
        self.connection_button_connect.setSizePolicy(sizePolicy4)

        self.verticalLayout_5.addWidget(self.connection_button_connect)

        self.connection_log = QPlainTextEdit(self.tab_ConnectionSetting)
        self.connection_log.setObjectName(u"connection_log")

        self.verticalLayout_5.addWidget(self.connection_log)

        self.tabWidget.addTab(self.tab_ConnectionSetting, "")
        self.tab_Setting_jianghu = QWidget()
        self.tab_Setting_jianghu.setObjectName(u"tab_Setting_jianghu")
        self.verticalLayout_2 = QVBoxLayout(self.tab_Setting_jianghu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.tab_Setting_jianghu)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_15)

        self.line_14 = QFrame(self.tab_Setting_jianghu)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_14)

        self.label_7 = QLabel(self.tab_Setting_jianghu)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label = QLabel(self.tab_Setting_jianghu)
        self.label.setObjectName(u"label")

        self.horizontalLayout_20.addWidget(self.label)

        self.comboBox_taskConfig_jianghu_shouji1 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.addItem("")
        self.comboBox_taskConfig_jianghu_shouji1.setObjectName(u"comboBox_taskConfig_jianghu_shouji1")

        self.horizontalLayout_20.addWidget(self.comboBox_taskConfig_jianghu_shouji1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_3 = QLabel(self.tab_Setting_jianghu)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_25.addWidget(self.label_3)

        self.comboBox_taskConfig_jianghu_shouji2 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.addItem("")
        self.comboBox_taskConfig_jianghu_shouji2.setObjectName(u"comboBox_taskConfig_jianghu_shouji2")

        self.horizontalLayout_25.addWidget(self.comboBox_taskConfig_jianghu_shouji2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.tab_Setting_jianghu)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_24.addWidget(self.label_4)

        self.comboBox_taskConfig_jianghu_shouji3 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.addItem("")
        self.comboBox_taskConfig_jianghu_shouji3.setObjectName(u"comboBox_taskConfig_jianghu_shouji3")

        self.horizontalLayout_24.addWidget(self.comboBox_taskConfig_jianghu_shouji3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.line_12 = QFrame(self.tab_Setting_jianghu)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_12)

        self.label_21 = QLabel(self.tab_Setting_jianghu)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_21)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.tab_Setting_jianghu)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.comboBox_taskConfig_jianghu_neixiu1 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu1.setObjectName(u"comboBox_taskConfig_jianghu_neixiu1")

        self.horizontalLayout_21.addWidget(self.comboBox_taskConfig_jianghu_neixiu1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.tab_Setting_jianghu)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_22.addWidget(self.label_20)

        self.comboBox_taskConfig_jianghu_neixiu2 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu2.setObjectName(u"comboBox_taskConfig_jianghu_neixiu2")

        self.horizontalLayout_22.addWidget(self.comboBox_taskConfig_jianghu_neixiu2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.tab_Setting_jianghu)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_23.addWidget(self.label_22)

        self.comboBox_taskConfig_jianghu_neixiu3 = QComboBox(self.tab_Setting_jianghu)
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.addItem("")
        self.comboBox_taskConfig_jianghu_neixiu3.setObjectName(u"comboBox_taskConfig_jianghu_neixiu3")

        self.horizontalLayout_23.addWidget(self.comboBox_taskConfig_jianghu_neixiu3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)

        self.line_13 = QFrame(self.tab_Setting_jianghu)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_13)

        self.label_19 = QLabel(self.tab_Setting_jianghu)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label_19)

        self.tabWidget.addTab(self.tab_Setting_jianghu, "")
        self.tab_Setting_jiuruta = QWidget()
        self.tab_Setting_jiuruta.setObjectName(u"tab_Setting_jiuruta")
        self.verticalLayout = QVBoxLayout(self.tab_Setting_jiuruta)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.tab_Setting_jiuruta)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font1)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_23 = QLabel(self.tab_Setting_jiuruta)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_2.addWidget(self.label_23)

        self.comboBox_taskConfig_jiuruta_jinyuan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_jinyuan1.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan1.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan1.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan1.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan1.setObjectName(u"comboBox_taskConfig_jiuruta_jinyuan1")

        self.horizontalLayout_2.addWidget(self.comboBox_taskConfig_jiuruta_jinyuan1)

        self.label_24 = QLabel(self.tab_Setting_jiuruta)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_2.addWidget(self.label_24)

        self.comboBox_taskConfig_jiuruta_jinyuan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_jinyuan2.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan2.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan2.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan2.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan2.setObjectName(u"comboBox_taskConfig_jiuruta_jinyuan2")

        self.horizontalLayout_2.addWidget(self.comboBox_taskConfig_jiuruta_jinyuan2)

        self.label_25 = QLabel(self.tab_Setting_jiuruta)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_2.addWidget(self.label_25)

        self.comboBox_taskConfig_jiuruta_jinyuan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_jinyuan3.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan3.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan3.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan3.addItem("")
        self.comboBox_taskConfig_jiuruta_jinyuan3.setObjectName(u"comboBox_taskConfig_jiuruta_jinyuan3")

        self.horizontalLayout_2.addWidget(self.comboBox_taskConfig_jiuruta_jinyuan3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_7 = QFrame(self.tab_Setting_jiuruta)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.label_8 = QLabel(self.tab_Setting_jiuruta)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font1)

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_28 = QLabel(self.tab_Setting_jiuruta)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_3.addWidget(self.label_28)

        self.comboBox_taskConfig_jiuruta_rizhilan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_rizhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan1.setObjectName(u"comboBox_taskConfig_jiuruta_rizhilan1")

        self.horizontalLayout_3.addWidget(self.comboBox_taskConfig_jiuruta_rizhilan1)

        self.label_26 = QLabel(self.tab_Setting_jiuruta)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_3.addWidget(self.label_26)

        self.comboBox_taskConfig_jiuruta_rizhilan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_rizhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan2.setObjectName(u"comboBox_taskConfig_jiuruta_rizhilan2")

        self.horizontalLayout_3.addWidget(self.comboBox_taskConfig_jiuruta_rizhilan2)

        self.label_27 = QLabel(self.tab_Setting_jiuruta)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_3.addWidget(self.label_27)

        self.comboBox_taskConfig_jiuruta_rizhilan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_rizhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_rizhilan3.setObjectName(u"comboBox_taskConfig_jiuruta_rizhilan3")

        self.horizontalLayout_3.addWidget(self.comboBox_taskConfig_jiuruta_rizhilan3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_9 = QLabel(self.tab_Setting_jiuruta)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font1)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_29 = QLabel(self.tab_Setting_jiuruta)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_8.addWidget(self.label_29)

        self.comboBox_taskConfig_jiuruta_chuanzhilan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setObjectName(u"comboBox_taskConfig_jiuruta_chuanzhilan1")

        self.horizontalLayout_8.addWidget(self.comboBox_taskConfig_jiuruta_chuanzhilan1)

        self.label_35 = QLabel(self.tab_Setting_jiuruta)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_8.addWidget(self.label_35)

        self.comboBox_taskConfig_jiuruta_chuanzhilan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setObjectName(u"comboBox_taskConfig_jiuruta_chuanzhilan2")

        self.horizontalLayout_8.addWidget(self.comboBox_taskConfig_jiuruta_chuanzhilan2)

        self.label_36 = QLabel(self.tab_Setting_jiuruta)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_8.addWidget(self.label_36)

        self.comboBox_taskConfig_jiuruta_chuanzhilan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setObjectName(u"comboBox_taskConfig_jiuruta_chuanzhilan3")

        self.horizontalLayout_8.addWidget(self.comboBox_taskConfig_jiuruta_chuanzhilan3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.label_12 = QLabel(self.tab_Setting_jiuruta)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font1)

        self.verticalLayout.addWidget(self.label_12)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_30 = QLabel(self.tab_Setting_jiuruta)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_7.addWidget(self.label_30)

        self.comboBox_taskConfig_jiuruta_shanzhilan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_shanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setObjectName(u"comboBox_taskConfig_jiuruta_shanzhilan1")

        self.horizontalLayout_7.addWidget(self.comboBox_taskConfig_jiuruta_shanzhilan1)

        self.label_43 = QLabel(self.tab_Setting_jiuruta)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_7.addWidget(self.label_43)

        self.comboBox_taskConfig_jiuruta_shanzhilan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_shanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setObjectName(u"comboBox_taskConfig_jiuruta_shanzhilan2")

        self.horizontalLayout_7.addWidget(self.comboBox_taskConfig_jiuruta_shanzhilan2)

        self.label_37 = QLabel(self.tab_Setting_jiuruta)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_7.addWidget(self.label_37)

        self.comboBox_taskConfig_jiuruta_shanzhilan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_shanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setObjectName(u"comboBox_taskConfig_jiuruta_shanzhilan3")

        self.horizontalLayout_7.addWidget(self.comboBox_taskConfig_jiuruta_shanzhilan3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label_11 = QLabel(self.tab_Setting_jiuruta)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setFont(font1)

        self.verticalLayout.addWidget(self.label_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_31 = QLabel(self.tab_Setting_jiuruta)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_6.addWidget(self.label_31)

        self.comboBox_taskConfig_jiuruta_songzhilan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_songzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan1.setObjectName(u"comboBox_taskConfig_jiuruta_songzhilan1")

        self.horizontalLayout_6.addWidget(self.comboBox_taskConfig_jiuruta_songzhilan1)

        self.label_38 = QLabel(self.tab_Setting_jiuruta)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_6.addWidget(self.label_38)

        self.comboBox_taskConfig_jiuruta_songzhilan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_songzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan2.setObjectName(u"comboBox_taskConfig_jiuruta_songzhilan2")

        self.horizontalLayout_6.addWidget(self.comboBox_taskConfig_jiuruta_songzhilan2)

        self.label_41 = QLabel(self.tab_Setting_jiuruta)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_6.addWidget(self.label_41)

        self.comboBox_taskConfig_jiuruta_songzhilan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_songzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_songzhilan3.setObjectName(u"comboBox_taskConfig_jiuruta_songzhilan3")

        self.horizontalLayout_6.addWidget(self.comboBox_taskConfig_jiuruta_songzhilan3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_10 = QLabel(self.tab_Setting_jiuruta)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font1)

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_32 = QLabel(self.tab_Setting_jiuruta)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_4.addWidget(self.label_32)

        self.comboBox_taskConfig_jiuruta_yuezhilan1 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_yuezhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan1.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setObjectName(u"comboBox_taskConfig_jiuruta_yuezhilan1")

        self.horizontalLayout_4.addWidget(self.comboBox_taskConfig_jiuruta_yuezhilan1)

        self.label_40 = QLabel(self.tab_Setting_jiuruta)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_4.addWidget(self.label_40)

        self.comboBox_taskConfig_jiuruta_yuezhilan2 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_yuezhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan2.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setObjectName(u"comboBox_taskConfig_jiuruta_yuezhilan2")

        self.horizontalLayout_4.addWidget(self.comboBox_taskConfig_jiuruta_yuezhilan2)

        self.label_39 = QLabel(self.tab_Setting_jiuruta)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_4.addWidget(self.label_39)

        self.comboBox_taskConfig_jiuruta_yuezhilan3 = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_yuezhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan3.addItem("")
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setObjectName(u"comboBox_taskConfig_jiuruta_yuezhilan3")

        self.horizontalLayout_4.addWidget(self.comboBox_taskConfig_jiuruta_yuezhilan3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_9 = QFrame(self.tab_Setting_jiuruta)
        self.line_9.setObjectName(u"line_9")
        sizePolicy4.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy4)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_33 = QLabel(self.tab_Setting_jiuruta)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_16.addWidget(self.label_33)

        self.comboBox_taskConfig_jiuruta_saturaday = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.addItem("")
        self.comboBox_taskConfig_jiuruta_saturaday.setObjectName(u"comboBox_taskConfig_jiuruta_saturaday")

        self.horizontalLayout_16.addWidget(self.comboBox_taskConfig_jiuruta_saturaday)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_34 = QLabel(self.tab_Setting_jiuruta)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_9.addWidget(self.label_34)

        self.comboBox_taskConfig_jiuruta_sunday = QComboBox(self.tab_Setting_jiuruta)
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.addItem("")
        self.comboBox_taskConfig_jiuruta_sunday.setObjectName(u"comboBox_taskConfig_jiuruta_sunday")
        sizePolicy1.setHeightForWidth(self.comboBox_taskConfig_jiuruta_sunday.sizePolicy().hasHeightForWidth())
        self.comboBox_taskConfig_jiuruta_sunday.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.comboBox_taskConfig_jiuruta_sunday)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.label_5 = QLabel(self.tab_Setting_jiuruta)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_5)

        self.tabWidget.addTab(self.tab_Setting_jiuruta, "")

        self.horizontalLayout_18.addWidget(self.tabWidget)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"OokamiTDJ", None))
        self.main_label_manual.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>1.\u5148\u5728<span style=\" font-weight:600;\">\u8fde\u63a5\u8bbe\u5907</span>\u4e2d\u8fde\u63a5\u8bbe\u5907</p><p>2.\u9009\u62e9<span style=\" font-weight:600;\">\u4efb\u52a1\u9009\u62e9</span>\u4e2d\u9700\u8981\u7684\u5185\u5bb9</p><p>3.\u7ec6\u8282\u8bbe\u5b9a\u6c5f\u6e56\u3001\u4e5d\u5982\u5854</p><p>4.\u786e\u5b9a\u8fc7\u573a\u52a8\u753b\u7b49\u7686\u5df2\u9605</p><p>5.<span style=\" font-weight:600;\">START</span></p></body></html>", None))
        self.main_button_load.setText(QCoreApplication.translate("mainWindow", u"LOAD", None))
        self.main_button_save.setText(QCoreApplication.translate("mainWindow", u"SAVE", None))
        self.main_button_start.setText(QCoreApplication.translate("mainWindow", u"START", None))
        self.main_label_Log_text.setText(QCoreApplication.translate("mainWindow", u"LOG", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MainPage), QCoreApplication.translate("mainWindow", u"\u4e3b\u9875", None))
        self.label_18.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u8bbe\u7f6e</p><p><span style=\" font-weight:400;\">\u6c5f\u6e56\u3001\u4e5d\u5982\u5854\u9700\u8981\u989d\u5916\u8bbe\u7f6e</span></p></body></html>", None))
        self.checkBox_taskSelect_shenkan.setText(QCoreApplication.translate("mainWindow", u"\u795e\u9f9b", None))
        self.checkBox_taskSelect_lilian.setText(QCoreApplication.translate("mainWindow", u"\u5386\u7ec3", None))
        self.checkBox_taskSelect_wangdin.setText(QCoreApplication.translate("mainWindow", u"\u738b\u9f0e", None))
        self.checkBox_taskSelect_youjian.setText(QCoreApplication.translate("mainWindow", u"\u90ae\u4ef6", None))
        self.checkBox_taskSelect_haoyou.setText(QCoreApplication.translate("mainWindow", u"\u597d\u53cb", None))
        self.checkBox_taskSelect_jiaoyi.setText(QCoreApplication.translate("mainWindow", u"\u4ea4\u6613", None))
        self.checkBox_taskSelect_zhaohuan.setText(QCoreApplication.translate("mainWindow", u"\u53ec\u5524", None))
        self.checkBox_taskSelect_tongguanwendie.setText(QCoreApplication.translate("mainWindow", u"\u901a\u5173\u6587\u7252", None))
        self.checkBox_taskSelect_qiyusaodang.setText(QCoreApplication.translate("mainWindow", u"\u5947\u9047\u626b\u8361", None))
        self.checkBox_taskSelect_huajinpenren.setText(QCoreApplication.translate("mainWindow", u"\u753b\u5883\u70f9\u996a", None))
        self.checkBox_taskSelect_huajinmizhi.setText(QCoreApplication.translate("mainWindow", u"\u753b\u5883\u79d8\u5236", None))
        self.checkBox_taskSelect_huajinzhongzhi.setText(QCoreApplication.translate("mainWindow", u"\u753b\u5883\u79cd\u690d", None))
        self.checkBox_taskSelect_huajinyouli.setText(QCoreApplication.translate("mainWindow", u"\u753b\u5883\u6e38\u5386", None))
        self.checkBox_taskSelect_huanjin_tiaozhan.setText(QCoreApplication.translate("mainWindow", u"\u5e7b\u5883\u6311\u6218", None))
        self.checkBox_taskSelect_huanjin_saodang.setText(QCoreApplication.translate("mainWindow", u"\u5e7b\u5883\u626b\u8361", None))
        self.checkBox_taskSelect_huanjin_shouhuo.setText(QCoreApplication.translate("mainWindow", u"\u5e7b\u5883\u6536\u83b7", None))
        self.checkBox_taskSelect_yiwen_haibulin.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u6d77\u6355\u4ee4", None))
        self.checkBox_taskSelect_yiwen_jianlunjiuzhou.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u5251\u8bba\u4e5d\u5dde", None))
        self.checkBox_taskSelect_yiwen_huanhaihunyuan.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u5e7b\u6d77\u9b42\u6e0a-\u96f7\u9e1f", None))
        self.checkBox_taskSelect_yiwen_linmaiguangyuan.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u7075\u8109\u5149\u6e0a", None))
        self.checkBox_taskSelect_yiwen_chuangmin.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u521b\u547d\u4e4b\u95f4", None))
        self.checkBox_taskSelect_jiuruta_jinyuan.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u4e5d\u5982\u5854-\u955c\u6e0a", None))
        self.checkBox_taskSelect_jiuruta_wuzhi.setText(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u4e5d\u5982\u5854-\u4e94\u70bd", None))
        self.checkBox_taskSelect_jianghu_neixiu.setText(QCoreApplication.translate("mainWindow", u"\u6c5f\u6e56-\u5185\u4fee", None))
        self.checkBox_taskSelect_jianghu_shouji.setText(QCoreApplication.translate("mainWindow", u"\u6c5f\u6e56-\u6536\u96c6", None))
        self.checkBox_taskSelect_tiandige_zhuzhen.setText(QCoreApplication.translate("mainWindow", u"\u5929\u5730\u9601\u52a9\u9635", None))
        self.checkBox_taskSelect_tiandige_renwu.setText(QCoreApplication.translate("mainWindow", u"\u5929\u5730\u9601\u4efb\u52a1", None))
        self.checkBox_taskSelect_tiandige_huigui.setText(QCoreApplication.translate("mainWindow", u"\u5929\u5730\u9601\u8fdc\u5f81\u7ed3\u675f", None))
        self.checkBox_taskSelect_tiandige_chufa.setText(QCoreApplication.translate("mainWindow", u"\u5929\u5730\u9601\u8fdc\u5f81\u51fa\u53d1", None))
        self.checkBox_taskSelect_shanhezhi_shouqu.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u9886\u53d6", None))
        self.checkBox_taskSelect_shanhezhi_sanhun1.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u4e09\u9b42\u4e00", None))
        self.checkBox_taskSelect_shanhezhi_sanhun2.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u4e09\u9b42\u4e8c", None))
        self.checkBox_taskSelect_shanhezhi_sanhun3.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u4e09\u9b42\u4e09", None))
        self.checkBox_taskSelect_shanhezhi_cangchenzhaohuan.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u82cd\u5c18\u53ec\u5524", None))
        self.checkBox_taskSelect_shanhezhi_wangshensuoxiang.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u5fd8\u751f\u6240\u5411", None))
        self.checkBox_taskSelect_tianlehunguang.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u5929\u4e50\u9b42\u5149", None))
        self.checkBox_taskSelect_shanhezhi_xinyaoxinshang.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u6cb3\u5fd7-\u661f\u8000\u884c\u5546", None))
        self.label_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Tasks), QCoreApplication.translate("mainWindow", u"\u4efb\u52a1\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"ADB Path:", None))
        self.connection_input_adb.setText("")
        self.connection_input_adb.setPlaceholderText(QCoreApplication.translate("mainWindow", u"C:\\123\\456\\adb.exe", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"Bluestack Port:", None))
        self.connection_input_port.setText("")
        self.connection_input_port.setPlaceholderText(QCoreApplication.translate("mainWindow", u"127.0.0.1:5585", None))
        self.label_17.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Resolution=1280 x 720<br/>DPI=240<br/>Recommand Emulator=<a href=\"https://cloud.bluestacks.com/api/getdownloadnow?platform=win&amp;win_version=10&amp;mac_version=&amp;client_uuid=18acae9d-f267-4a00-9df1-61921b892314&amp;app_pkg=&amp;platform_cloud=%257B%2522description%2522%253A%2522Chrome%2520122.0.0.0%2520on%2520Windows%252010%252064-bit%2522%252C%2522layout%2522%253A%2522Blink%2522%252C%2522manufacturer%2522%253Anull%252C%2522name%2522%253A%2522Chrome%2522%252C%2522prerelease%2522%253Anull%252C%2522product%2522%253Anull%252C%2522ua%2522%253A%2522Mozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F122.0.0.0%2520Safari%252F537.36%2522%252C%2522version%2522%253A%2522122.0.0.0%2522%252C%2522os%2522%253A%257B%2522architecture%2522%253A64%252C%2522family%2522%253A%2522Windows%2522%252C%2522version%2522%253A%252210%2522%257D%257D&amp;preferred_lang=en&amp;utm_source=&amp;utm_medium=&amp;gaCook"
                        "ie=&amp;gclid=&amp;clickid=&amp;msclkid=&amp;affiliateId=&amp;offerId=&amp;transaction_id=&amp;aff_sub=&amp;first_landing_page=&amp;referrer=&amp;download_page_referrer=https%3A%2F%2Fwww.bluestacks.com%2Fbluestacks-5.html&amp;utm_campaign=bluestacks5-en&amp;user_id=&amp;exit_utm_campaign=bluestacks5-en&amp;incompatible=false&amp;bluestacks_version=bs5&amp;device_memory=8&amp;device_cpu_cores=12\"><span style=\" text-decoration: underline; color:#0000ff;\">BlueStack 5</span></a></p></body></html>", None))
        self.connection_button_connect.setText(QCoreApplication.translate("mainWindow", u"CONNECT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ConnectionSetting), QCoreApplication.translate("mainWindow", u"\u8fde\u63a5\u8bbe\u5907", None))
        self.label_15.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>AUTO \u5219\u4e3a\u6bcf\u9879\u5185\u5bb9\u6bcf\u5929\u5faa\u73af</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u6536\u96c6", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u6536\u96c6-1", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9ec4-\u5229\u5203\u5251\u80c6", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u7ea2-\u7075\u5492\u7384\u7b26", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u84dd-\u5b9a\u6d77\u7384\u94c1", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u7eff-\u8424\u714c\u4e4b\u74a7", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u7ea2-\u8840\u7edc\u7389\u9ad3", None))
        self.comboBox_taskConfig_jianghu_shouji1.setItemText(6, QCoreApplication.translate("mainWindow", u"6.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_shouji1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6536\u96c61", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.comboBox_taskConfig_jianghu_shouji1.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u6536\u96c6-2", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9ec4-\u5229\u5203\u5251\u80c6", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u7ea2-\u7075\u5492\u7384\u7b26", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u84dd-\u5b9a\u6d77\u7384\u94c1", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u7eff-\u8424\u714c\u4e4b\u74a7", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u7ea2-\u8840\u7edc\u7389\u9ad3", None))
        self.comboBox_taskConfig_jianghu_shouji2.setItemText(6, QCoreApplication.translate("mainWindow", u"6.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_shouji2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6536\u96c62", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.comboBox_taskConfig_jianghu_shouji2.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u6536\u96c6-3", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9ec4-\u5229\u5203\u5251\u80c6", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u7ea2-\u7075\u5492\u7384\u7b26", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u84dd-\u5b9a\u6d77\u7384\u94c1", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u7eff-\u8424\u714c\u4e4b\u74a7", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u7ea2-\u8840\u7edc\u7389\u9ad3", None))
        self.comboBox_taskConfig_jianghu_shouji3.setItemText(6, QCoreApplication.translate("mainWindow", u"6.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_shouji3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6536\u96c63", None))
#endif // QT_CONFIG(whatsthis)
        self.label_21.setText(QCoreApplication.translate("mainWindow", u"\u5185\u4fee", None))
        self.label_16.setText(QCoreApplication.translate("mainWindow", u"\u5185\u4fee-1", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9b42-\u7075\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u9b44-\u795e\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u9b42-\u771f\u6c14", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u9b44-\u4ed9\u6cd5", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u9b42-\u5251\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(6, QCoreApplication.translate("mainWindow", u"6.\u9b44-\u7f61\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu1.setItemText(7, QCoreApplication.translate("mainWindow", u"7.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_neixiu1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5185\u4fee1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_20.setText(QCoreApplication.translate("mainWindow", u"\u5185\u4fee-2", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9b42-\u7075\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u9b44-\u795e\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u9b42-\u771f\u6c14", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u9b44-\u4ed9\u6cd5", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u9b42-\u5251\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(6, QCoreApplication.translate("mainWindow", u"6.\u9b44-\u7f61\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu2.setItemText(7, QCoreApplication.translate("mainWindow", u"7.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_neixiu2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5185\u4fee2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_22.setText(QCoreApplication.translate("mainWindow", u"\u5185\u4fee-3", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u9b42-\u7075\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u9b44-\u795e\u8bc6", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u9b42-\u771f\u6c14", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(4, QCoreApplication.translate("mainWindow", u"4.\u9b44-\u4ed9\u6cd5", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(5, QCoreApplication.translate("mainWindow", u"5.\u9b42-\u5251\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(6, QCoreApplication.translate("mainWindow", u"6.\u9b44-\u7f61\u610f", None))
        self.comboBox_taskConfig_jianghu_neixiu3.setItemText(7, QCoreApplication.translate("mainWindow", u"7.AUTO", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jianghu_neixiu3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5185\u4fee3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_19.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Setting_jianghu), QCoreApplication.translate("mainWindow", u"\u6c5f\u6e56\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u955c\u6e0a", None))
        self.label_23.setText(QCoreApplication.translate("mainWindow", u"\u955c\u6e0a-1", None))
        self.comboBox_taskConfig_jiuruta_jinyuan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_jinyuan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_jinyuan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_jinyuan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(statustip)
        self.comboBox_taskConfig_jiuruta_jinyuan1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_jinyuan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u4e5d\u5982\u5854-\u955c\u6e0a1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_24.setText(QCoreApplication.translate("mainWindow", u"\u955c\u6e0a-2", None))
        self.comboBox_taskConfig_jiuruta_jinyuan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_jinyuan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_jinyuan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_jinyuan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(statustip)
        self.comboBox_taskConfig_jiuruta_jinyuan2.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_jinyuan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u4e5d\u5982\u5854-\u955c\u6e0a2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_25.setText(QCoreApplication.translate("mainWindow", u"\u955c\u6e0a-3", None))
        self.comboBox_taskConfig_jiuruta_jinyuan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_jinyuan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_jinyuan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_jinyuan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(statustip)
        self.comboBox_taskConfig_jiuruta_jinyuan3.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_jinyuan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5f02\u95fb-\u4e5d\u5982\u5854-\u955c\u6e0a3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u65e5\u4e4b\u5c9a(\u7ea2)", None))
        self.label_28.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-1", None))
        self.comboBox_taskConfig_jiuruta_rizhilan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_rizhilan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_rizhilan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_rizhilan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(statustip)
        self.comboBox_taskConfig_jiuruta_rizhilan1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_rizhilan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_26.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-2", None))
        self.comboBox_taskConfig_jiuruta_rizhilan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_rizhilan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_rizhilan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_rizhilan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_rizhilan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_27.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-3", None))
        self.comboBox_taskConfig_jiuruta_rizhilan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_rizhilan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_rizhilan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_rizhilan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_rizhilan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a-3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u5ddd\u4e4b\u5c9a\uff08\u84dd\uff09", None))
        self.label_29.setText(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-1", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_chuanzhilan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_35.setText(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-2", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_chuanzhilan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_36.setText(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-3", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_chuanzhilan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a-3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u5c71\u4e4b\u5c9a\uff08\u7eff\uff09", None))
        self.label_30.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-1", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_shanzhilan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_43.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-2", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_shanzhilan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_37.setText(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-3", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_shanzhilan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a-3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u677e\u4e4b\u5c9a\uff08\u5149\uff09", None))
        self.label_31.setText(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-1", None))
        self.comboBox_taskConfig_jiuruta_songzhilan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_songzhilan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_songzhilan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_songzhilan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_songzhilan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_38.setText(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-2", None))
        self.comboBox_taskConfig_jiuruta_songzhilan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_songzhilan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_songzhilan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_songzhilan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_songzhilan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_41.setText(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-3", None))
        self.comboBox_taskConfig_jiuruta_songzhilan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_songzhilan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_songzhilan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_songzhilan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_songzhilan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a-3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854-\u6708\u4e4b\u5c9a\uff08\u6697\uff09", None))
        self.label_32.setText(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-1", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_yuezhilan1.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-1", None))
#endif // QT_CONFIG(whatsthis)
        self.label_40.setText(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-2", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_yuezhilan2.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-2", None))
#endif // QT_CONFIG(whatsthis)
        self.label_39.setText(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-3", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setItemText(0, QCoreApplication.translate("mainWindow", u"0.\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setItemText(1, QCoreApplication.translate("mainWindow", u"1.\u5353", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setItemText(2, QCoreApplication.translate("mainWindow", u"2.\u6781", None))
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setItemText(3, QCoreApplication.translate("mainWindow", u"3.\u7edd", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_yuezhilan3.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a-3", None))
#endif // QT_CONFIG(whatsthis)
        self.label_33.setText(QCoreApplication.translate("mainWindow", u"\u5468\u516d", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(0, QCoreApplication.translate("mainWindow", u"\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(1, QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(2, QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(3, QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(4, QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_saturaday.setItemText(5, QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_saturaday.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5468\u516d", None))
#endif // QT_CONFIG(whatsthis)
        self.label_34.setText(QCoreApplication.translate("mainWindow", u"\u5468\u65e5", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(0, QCoreApplication.translate("mainWindow", u"\u5173\u95ed", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(1, QCoreApplication.translate("mainWindow", u"\u65e5\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(2, QCoreApplication.translate("mainWindow", u"\u5ddd\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(3, QCoreApplication.translate("mainWindow", u"\u5c71\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(4, QCoreApplication.translate("mainWindow", u"\u677e\u4e4b\u5c9a", None))
        self.comboBox_taskConfig_jiuruta_sunday.setItemText(5, QCoreApplication.translate("mainWindow", u"\u6708\u4e4b\u5c9a", None))

#if QT_CONFIG(whatsthis)
        self.comboBox_taskConfig_jiuruta_sunday.setWhatsThis(QCoreApplication.translate("mainWindow", u"\u5468\u65e5", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Setting_jiuruta), QCoreApplication.translate("mainWindow", u"\u4e5d\u5982\u5854\u8bbe\u7f6e", None))
    # retranslateUi

