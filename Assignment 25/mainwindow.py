# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(120, 60, 551, 361))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_ir_worldclock = QPushButton(self.tab)
        self.btn_ir_worldclock.setObjectName(u"btn_ir_worldclock")
        self.btn_ir_worldclock.setGeometry(QRect(50, 260, 121, 31))
        font = QFont()
        font.setFamily(u"MRT_Nil 3")
        font.setPointSize(13)
        self.btn_ir_worldclock.setFont(font)
        self.label_worldclock = QLabel(self.tab)
        self.label_worldclock.setObjectName(u"label_worldclock")
        self.label_worldclock.setGeometry(QRect(180, 80, 171, 51))
        font1 = QFont()
        font1.setFamily(u"Seven Segment")
        font1.setPointSize(40)
        self.label_worldclock.setFont(font1)
        self.label_worldclock.setAlignment(Qt.AlignCenter)
        self.btn_de_worldclock = QPushButton(self.tab)
        self.btn_de_worldclock.setObjectName(u"btn_de_worldclock")
        self.btn_de_worldclock.setGeometry(QRect(210, 260, 121, 31))
        self.btn_de_worldclock.setFont(font)
        self.btn_us_worldclock = QPushButton(self.tab)
        self.btn_us_worldclock.setObjectName(u"btn_us_worldclock")
        self.btn_us_worldclock.setGeometry(QRect(370, 260, 121, 31))
        self.btn_us_worldclock.setFont(font)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.le_name_alarm = QLineEdit(self.tab_3)
        self.le_name_alarm.setObjectName(u"le_name_alarm")
        self.le_name_alarm.setGeometry(QRect(160, 20, 141, 21))
        self.le_name_alarm.setAlignment(Qt.AlignCenter)
        self.le_name_alarm.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.le_time_alarm = QLineEdit(self.tab_3)
        self.le_time_alarm.setObjectName(u"le_time_alarm")
        self.le_time_alarm.setGeometry(QRect(10, 20, 140, 20))
        self.le_time_alarm.setAlignment(Qt.AlignCenter)
        self.te_description__alarm = QTextEdit(self.tab_3)
        self.te_description__alarm.setObjectName(u"te_description__alarm")
        self.te_description__alarm.setGeometry(QRect(73, 90, 161, 180))
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 60, 100, 20))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_add_alarm = QPushButton(self.tab_3)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setGeometry(QRect(100, 290, 111, 31))
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(310, 0, 241, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_stopwatch = QLabel(self.tab_4)
        self.label_stopwatch.setObjectName(u"label_stopwatch")
        self.label_stopwatch.setGeometry(QRect(180, 60, 171, 51))
        self.label_stopwatch.setFont(font1)
        self.label_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_4)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(50, 240, 121, 31))
        self.btn_stop_stopwatch = QPushButton(self.tab_4)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(370, 240, 121, 31))
        self.btn_reset_stopwatch = QPushButton(self.tab_4)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(210, 240, 121, 31))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tb_h = QLineEdit(self.tab_2)
        self.tb_h.setObjectName(u"tb_h")
        self.tb_h.setGeometry(QRect(141, 50, 70, 70))
        self.tb_h.setMinimumSize(QSize(70, 70))
        self.tb_h.setMaximumSize(QSize(70, 70))
        self.tb_h.setFont(font1)
        self.tb_h.setAlignment(Qt.AlignCenter)
        self.tb_m = QLineEdit(self.tab_2)
        self.tb_m.setObjectName(u"tb_m")
        self.tb_m.setGeometry(QRect(240, 50, 70, 70))
        self.tb_m.setMinimumSize(QSize(70, 70))
        self.tb_m.setMaximumSize(QSize(70, 70))
        self.tb_m.setFont(font1)
        self.tb_m.setAlignment(Qt.AlignCenter)
        self.tb_s = QLineEdit(self.tab_2)
        self.tb_s.setObjectName(u"tb_s")
        self.tb_s.setGeometry(QRect(340, 50, 70, 70))
        self.tb_s.setMinimumSize(QSize(70, 70))
        self.tb_s.setMaximumSize(QSize(70, 70))
        self.tb_s.setFont(font1)
        self.tb_s.setAlignment(Qt.AlignCenter)
        self.btn_stop_timer = QPushButton(self.tab_2)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(290, 260, 121, 31))
        self.btn_start_timer = QPushButton(self.tab_2)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(130, 260, 121, 31))
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(218, 50, 15, 70))
        self.lineEdit_2.setMinimumSize(QSize(15, 70))
        self.lineEdit_2.setMaximumSize(QSize(15, 70))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(317, 50, 15, 70))
        self.lineEdit_3.setMinimumSize(QSize(15, 70))
        self.lineEdit_3.setMaximumSize(QSize(15, 70))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 763, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_ir_worldclock.setText(QCoreApplication.translate("MainWindow", u"IR", None))
        self.label_worldclock.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_de_worldclock.setText(QCoreApplication.translate("MainWindow", u"DE", None))
        self.btn_us_worldclock.setText(QCoreApplication.translate("MainWindow", u"us", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
#if QT_CONFIG(tooltip)
        self.le_name_alarm.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.le_name_alarm.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.le_name_alarm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.le_time_alarm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"time", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.label_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.tb_h.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tb_m.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.tb_s.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

