# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(628, 510)
        setting.setStyleSheet("QWidget{\n"
"background-color: rgb(42, 42, 42);\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    margin: -2px 0; \n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox{\n"
"color:rgb(194, 52, 11);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet("background-color: rgb(194, 52, 11);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 0, 91, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/resources/icons8_services_64px.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.confirmChanges = QtWidgets.QPushButton(self.frame)
        self.confirmChanges.setGeometry(QtCore.QRect(460, 10, 141, 51))
        self.confirmChanges.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirmChanges.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"background:rgb(188, 82, 51);")
        self.confirmChanges.setAutoDefault(False)
        self.confirmChanges.setDefault(False)
        self.confirmChanges.setFlat(False)
        self.confirmChanges.setObjectName("confirmChanges")
        self.verticalLayout_11.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:18px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider.setStyleSheet("border: 1px solid #222;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   \n"
"    margin: 2px 0;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.lineWeight = QtWidgets.QFrame(self.frame_2)
        self.lineWeight.setMinimumSize(QtCore.QSize(50, 20))
        self.lineWeight.setMaximumSize(QtCore.QSize(50, 20))
        self.lineWeight.setStyleSheet("")
        self.lineWeight.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineWeight.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineWeight.setObjectName("lineWeight")
        self.horizontalLayout_3.addWidget(self.lineWeight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.transparency = QtWidgets.QSlider(self.frame_2)
        self.transparency.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.transparency.setStyleSheet("border: 1px solid #222;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   \n"
"    margin: 2px 0;")
        self.transparency.setMaximum(100)
        self.transparency.setSingleStep(0)
        self.transparency.setPageStep(2)
        self.transparency.setProperty("value", 30)
        self.transparency.setOrientation(QtCore.Qt.Horizontal)
        self.transparency.setObjectName("transparency")
        self.horizontalLayout_4.addWidget(self.transparency)
        self.transValue = QtWidgets.QLabel(self.frame_2)
        self.transValue.setMinimumSize(QtCore.QSize(40, 20))
        self.transValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.transValue.setAlignment(QtCore.Qt.AlignCenter)
        self.transValue.setObjectName("transValue")
        self.horizontalLayout_4.addWidget(self.transValue)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_anatomical_heart_96px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_5.setIcon(icon)
        self.checkBox_5.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.checkBox_5)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_lungs_96px_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_6.setIcon(icon1)
        self.checkBox_6.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_11.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:16px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem7 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.dial = QtWidgets.QDial(self.frame_3)
        self.dial.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(0.7)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.horizontalLayout_11.addWidget(self.dial)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_11.addWidget(self.line_3)
        self.dial_2 = QtWidgets.QDial(self.frame_3)
        self.dial_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.dial_2.setNotchTarget(19.7)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName("dial_2")
        self.horizontalLayout_11.addWidget(self.dial_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.pdValue = QtWidgets.QLabel(self.frame_3)
        self.pdValue.setMinimumSize(QtCore.QSize(40, 20))
        self.pdValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.pdValue.setAlignment(QtCore.Qt.AlignCenter)
        self.pdValue.setObjectName("pdValue")
        self.horizontalLayout_9.addWidget(self.pdValue)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)
        spacerItem9 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.peepValue = QtWidgets.QLabel(self.frame_3)
        self.peepValue.setMinimumSize(QtCore.QSize(40, 20))
        self.peepValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.peepValue.setAlignment(QtCore.Qt.AlignCenter)
        self.peepValue.setObjectName("peepValue")
        self.horizontalLayout_10.addWidget(self.peepValue)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_18.addWidget(self.horizontalSlider_2)
        self.brValue = QtWidgets.QLabel(self.frame_3)
        self.brValue.setMinimumSize(QtCore.QSize(40, 20))
        self.brValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.brValue.setAlignment(QtCore.Qt.AlignCenter)
        self.brValue.setObjectName("brValue")
        self.horizontalLayout_18.addWidget(self.brValue)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem11 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_16.addWidget(self.line_4)
        spacerItem12 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem12)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        spacerItem14 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.dial_3 = QtWidgets.QDial(self.frame_3)
        self.dial_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.dial_3.setMaximum(1000)
        self.dial_3.setWrapping(False)
        self.dial_3.setNotchTarget(10.7)
        self.dial_3.setNotchesVisible(True)
        self.dial_3.setObjectName("dial_3")
        self.verticalLayout_8.addWidget(self.dial_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        self.tvValue = QtWidgets.QLabel(self.frame_3)
        self.tvValue.setMinimumSize(QtCore.QSize(40, 20))
        self.tvValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.tvValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tvValue.setObjectName("tvValue")
        self.horizontalLayout_15.addWidget(self.tvValue)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem16)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_21.addWidget(self.label_14)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider_3.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_21.addWidget(self.horizontalSlider_3)
        self.frValue = QtWidgets.QLabel(self.frame_3)
        self.frValue.setMinimumSize(QtCore.QSize(40, 20))
        self.frValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.frValue.setAlignment(QtCore.Qt.AlignCenter)
        self.frValue.setObjectName("frValue")
        self.horizontalLayout_21.addWidget(self.frValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_21)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_17.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.verticalLayout_11.addWidget(self.frame_3)
        setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(setting)
        self.dial.valueChanged['int'].connect(self.pdValue.setNum)
        self.dial_2.valueChanged['int'].connect(self.peepValue.setNum)
        self.transparency.valueChanged['int'].connect(self.transValue.setNum)
        self.dial_3.valueChanged['int'].connect(self.tvValue.setNum)
        self.horizontalSlider_2.valueChanged['int'].connect(self.brValue.setNum)
        self.horizontalSlider_3.valueChanged['int'].connect(self.frValue.setNum)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "MainWindow"))
        self.confirmChanges.setText(_translate("setting", "Confirm Changes"))
        self.label_2.setText(_translate("setting", "Appearance"))
        self.label_3.setText(_translate("setting", "Hide/Show"))
        self.checkBox.setText(_translate("setting", "ECG Graph"))
        self.checkBox_2.setText(_translate("setting", "pressure Graph"))
        self.checkBox_3.setText(_translate("setting", "frow rate Graph"))
        self.checkBox_4.setText(_translate("setting", "tidal volume Graph"))
        self.label_4.setText(_translate("setting", "Graph Line weight"))
        self.label_5.setText(_translate("setting", "GUI Transparency"))
        self.transValue.setText(_translate("setting", "1"))
        self.label_6.setText(_translate("setting", "Hide/Show "))
        self.label_7.setText(_translate("setting", "Control Variables"))
        self.label_8.setText(_translate("setting", "Pressure"))
        self.label_9.setText(_translate("setting", "Pdelta"))
        self.pdValue.setText(_translate("setting", "1"))
        self.label_10.setText(_translate("setting", "Peep"))
        self.peepValue.setText(_translate("setting", "1"))
        self.label_13.setText(_translate("setting", "Breath rate"))
        self.brValue.setText(_translate("setting", "1"))
        self.label_11.setText(_translate("setting", "Tidal Volume"))
        self.label_12.setText(_translate("setting", "Volume"))
        self.tvValue.setText(_translate("setting", "1"))
        self.label_14.setText(_translate("setting", "flow Rate"))
        self.frValue.setText(_translate("setting", "1"))

import udvent_rc
