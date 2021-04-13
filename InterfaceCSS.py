# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Interface2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 377)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
#         MainWindow.setStyleSheet("\n"
# "background-color: rgb(86.3%, 86.3%, 86.3%);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageProcessor = QtWidgets.QPushButton(self.centralwidget)
        self.imageProcessor.setGeometry(QtCore.QRect(670, 20, 111, 41))
#         self.imageProcessor.setStyleSheet("      color: #333;\n"
# "    border: 2px solid #555;\n"
# "    border-radius: 10px;\n"
# "    border-style: outset;\n"
# "")
        self.imageProcessor.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("utils/iconfinder_search__magnify__magnifier__find_2537353.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageProcessor.setIcon(icon)
        self.imageProcessor.setIconSize(QtCore.QSize(80, 32))
        self.imageProcessor.setObjectName("imageProcessor")
        self.image_explorer = QtWidgets.QLineEdit(self.centralwidget)
        self.image_explorer.setGeometry(QtCore.QRect(30, 20, 521, 41))
        self.image_explorer.setObjectName("image_explorer")
        self.fileFinder = QtWidgets.QPushButton(self.centralwidget)
        self.fileFinder.setGeometry(QtCore.QRect(560, 20, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fileFinder.sizePolicy().hasHeightForWidth())
        self.fileFinder.setSizePolicy(sizePolicy)
        self.fileFinder.setMaximumSize(QtCore.QSize(167, 167))
#         self.fileFinder.setStyleSheet("      color: #333;\n"
# "    border: 2px solid #555;\n"
# "    border-radius: 10px;\n"
# "    border-style: outset;\n"
# "")
        self.fileFinder.setObjectName("fileFinder")
        self.fileFinder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("utils/iconfinder_icon-130-cloud-upload_314245.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileFinder.setIcon(icon1)
        self.fileFinder.setIconSize(QtCore.QSize(32, 64))
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(40, 90, 381, 251))
#         self.label_5.setStyleSheet("      color: #333;\n"
# "    border: 2px solid #555;\n"
# "    border-radius: 10px;\n"
# "    border-style: outset;\n"
# "")
#         self.label_5.setText("")
        # self.label_5.setTextFormat(QtCore.Qt.RichText)
        # self.label_5.setPixmap(QtGui.QPixmap("check_default.png"))
        # self.label_5.setScaledContents(True)
        # self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(490, 90, 481, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 80, 61))
        self.pushButton.setStyleSheet(
            "border-radius: 0px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 70, 80, 61))
        self.pushButton_2.setStyleSheet(
            "border-radius: 0px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(380, 10, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(380, 40, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(340, 10, 21, 21))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(
            "../../../Music/ezgif-2-74bdb33bf670.gif"))
        self.label_10.setObjectName("label_10")
        self.movie = QtGui.QMovie("../../../Music/ezgif-2-74bdb33bf670.gif")
        self.label_10.setMovie(self.movie)
        self.movie.start()
        self.label_10.hide()
        # self.label_10.setLayout(QtGui.QHBoxLayout())
        # self.label_10.layout().addWidget(QtWidgets.QLabel('Loading...'))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 30, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 90, 381, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 81, 16))
        self.label_4.setObjectName("label_4")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 150, 381, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_4.setGeometry(QtCore.QRect(10, 210, 381, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 111, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(870, 20, 71, 41))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(
            "../../../Music/magnify_scan_icon_138406.png"))
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 70, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(340, 40, 21, 21))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(340, 70, 21, 21))
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("\n"
"background-color: rgb(113, 113, 113);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(380, 70, 91, 21))
        self.label_23.setObjectName("label_23")
        self.imageWindow = QtWidgets.QLabel(self.centralwidget)
        self.imageWindow.setGeometry(QtCore.QRect(40, 90, 381, 251))
        self.imageWindow.setTextFormat(QtCore.Qt.RichText)
        self.imageWindow.setPixmap(QtGui.QPixmap("check_default.png"))
        self.imageWindow.setScaledContents(True)
        self.imageWindow.setObjectName("imageWindow")
        self.imageWindow.setStyleSheet(
            "    border: 2px solid #555;\n"
            "    border-radius: 10px;\n"
            "    border-style: outset;\n"
            "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "J Image Steganalyzer"))
        # self.imageProcessor.setText(_translate("MainWindow", "Analyse Image"))
        # self.fileFinder.setText(_translate("MainWindow", "Open Image"))
        self.imageProcessor.setToolTip(_translate("MainWindow", "Steganalyse Image"))
        self.fileFinder.setToolTip(_translate("MainWindow", "Insert Image"))
        self.pushButton.setText(_translate("MainWindow", "Stego"))
        self.pushButton_2.setText(_translate("MainWindow", "Cover"))
        self.label_7.setText(_translate("MainWindow", "Cover Image"))
        self.label_8.setText(_translate("MainWindow", "Stego Image"))
        self.label_23.setText(_translate("MainWindow", "Not Analyzed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Binary Classification"))
        self.label.setText(_translate("MainWindow", "Cover Image"))
        self.label_2.setText(_translate("MainWindow", "JMiPOD image"))
        self.label_4.setText(_translate("MainWindow", "UERD image"))
        self.label_3.setText(_translate("MainWindow", "JUNIWARD image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Detailed Results"))
        self.label_6.setText(_translate("MainWindow", "Image Preview"))
