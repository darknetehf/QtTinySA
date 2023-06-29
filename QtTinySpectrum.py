# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtTinySpectrum.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.analyserTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyserTab.sizePolicy().hasHeightForWidth())
        self.analyserTab.setSizePolicy(sizePolicy)
        self.analyserTab.setObjectName("analyserTab")
        self.gridLayout = QtWidgets.QGridLayout(self.analyserTab)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lna_button = QtWidgets.QPushButton(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lna_button.setFont(font)
        self.lna_button.setObjectName("lna_button")
        self.gridLayout_3.addWidget(self.lna_button, 2, 1, 1, 1)
        self.trace3 = QtWidgets.QCheckBox(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trace3.setFont(font)
        self.trace3.setObjectName("trace3")
        self.gridLayout_3.addWidget(self.trace3, 13, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1)
        self.t4_type = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t4_type.sizePolicy().hasHeightForWidth())
        self.t4_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.t4_type.setFont(font)
        self.t4_type.setObjectName("t4_type")
        self.gridLayout_3.addWidget(self.t4_type, 14, 1, 1, 1)
        self.t1_type = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1_type.sizePolicy().hasHeightForWidth())
        self.t1_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.t1_type.setFont(font)
        self.t1_type.setObjectName("t1_type")
        self.gridLayout_3.addWidget(self.t1_type, 11, 1, 1, 1)
        self.version = QtWidgets.QLabel(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.gridLayout_3.addWidget(self.version, 18, 0, 1, 2)
        self.avgSlider = QtWidgets.QSlider(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avgSlider.sizePolicy().hasHeightForWidth())
        self.avgSlider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.avgSlider.setFont(font)
        self.avgSlider.setToolTip("")
        self.avgSlider.setMinimum(1)
        self.avgSlider.setMaximum(50)
        self.avgSlider.setProperty("value", 10)
        self.avgSlider.setOrientation(QtCore.Qt.Horizontal)
        self.avgSlider.setInvertedAppearance(False)
        self.avgSlider.setInvertedControls(False)
        self.avgSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.avgSlider.setObjectName("avgSlider")
        self.gridLayout_3.addWidget(self.avgSlider, 16, 0, 1, 3)
        self.trace4 = QtWidgets.QCheckBox(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trace4.setFont(font)
        self.trace4.setObjectName("trace4")
        self.gridLayout_3.addWidget(self.trace4, 14, 0, 1, 1)
        self.t3_type = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t3_type.sizePolicy().hasHeightForWidth())
        self.t3_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.t3_type.setFont(font)
        self.t3_type.setObjectName("t3_type")
        self.gridLayout_3.addWidget(self.t3_type, 13, 1, 1, 1)
        self.atten_box = QtWidgets.QSpinBox(self.analyserTab)
        self.atten_box.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.atten_box.setFont(font)
        self.atten_box.setReadOnly(False)
        self.atten_box.setMinimum(0)
        self.atten_box.setMaximum(31)
        self.atten_box.setProperty("value", 0)
        self.atten_box.setObjectName("atten_box")
        self.gridLayout_3.addWidget(self.atten_box, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 6, 1, 1, 1)
        self.spur_button = QtWidgets.QPushButton(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.spur_button.setFont(font)
        self.spur_button.setObjectName("spur_button")
        self.gridLayout_3.addWidget(self.spur_button, 3, 1, 1, 1)
        self.atten_auto = QtWidgets.QCheckBox(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.atten_auto.setFont(font)
        self.atten_auto.setChecked(True)
        self.atten_auto.setObjectName("atten_auto")
        self.gridLayout_3.addWidget(self.atten_auto, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 8, 1, 1, 1)
        self.vbw_box = QtWidgets.QComboBox(self.analyserTab)
        self.vbw_box.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vbw_box.sizePolicy().hasHeightForWidth())
        self.vbw_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.vbw_box.setFont(font)
        self.vbw_box.setObjectName("vbw_box")
        self.gridLayout_3.addWidget(self.vbw_box, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 15, 0, 1, 2)
        self.trace1 = QtWidgets.QCheckBox(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trace1.setFont(font)
        self.trace1.setChecked(False)
        self.trace1.setTristate(False)
        self.trace1.setObjectName("trace1")
        self.gridLayout_3.addWidget(self.trace1, 11, 0, 1, 1)
        self.t2_type = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2_type.sizePolicy().hasHeightForWidth())
        self.t2_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.t2_type.setFont(font)
        self.t2_type.setObjectName("t2_type")
        self.gridLayout_3.addWidget(self.t2_type, 12, 1, 1, 1)
        self.rbw_box = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbw_box.sizePolicy().hasHeightForWidth())
        self.rbw_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.rbw_box.setFont(font)
        self.rbw_box.setEditable(True)
        self.rbw_box.setObjectName("rbw_box")
        self.gridLayout_3.addWidget(self.rbw_box, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 10, 1, 1, 1)
        self.trace2 = QtWidgets.QCheckBox(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trace2.setFont(font)
        self.trace2.setTristate(False)
        self.trace2.setObjectName("trace2")
        self.gridLayout_3.addWidget(self.trace2, 12, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 17, 0, 1, 1)
        self.points_box = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_box.sizePolicy().hasHeightForWidth())
        self.points_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.points_box.setFont(font)
        self.points_box.setObjectName("points_box")
        self.gridLayout_3.addWidget(self.points_box, 5, 1, 1, 1)
        self.battery = QtWidgets.QLabel(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.battery.setFont(font)
        self.battery.setObjectName("battery")
        self.gridLayout_3.addWidget(self.battery, 19, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 19, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.marker3 = QtWidgets.QCheckBox(self.analyserTab)
        self.marker3.setObjectName("marker3")
        self.gridLayout_2.addWidget(self.marker3, 1, 6, 1, 1)
        self.graphWidget = PlotWidget(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setAutoFillBackground(False)
        self.graphWidget.setStyleSheet("")
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 0, 1, 12)
        self.stop_freq = QtWidgets.QDoubleSpinBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_freq.sizePolicy().hasHeightForWidth())
        self.stop_freq.setSizePolicy(sizePolicy)
        self.stop_freq.setDecimals(6)
        self.stop_freq.setMinimum(0.1)
        self.stop_freq.setMaximum(6000.0)
        self.stop_freq.setSingleStep(1.0)
        self.stop_freq.setProperty("value", 108.0)
        self.stop_freq.setObjectName("stop_freq")
        self.gridLayout_2.addWidget(self.stop_freq, 1, 10, 1, 1)
        self.marker4 = QtWidgets.QCheckBox(self.analyserTab)
        self.marker4.setObjectName("marker4")
        self.gridLayout_2.addWidget(self.marker4, 1, 7, 1, 1)
        self.start_freq = QtWidgets.QDoubleSpinBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_freq.sizePolicy().hasHeightForWidth())
        self.start_freq.setSizePolicy(sizePolicy)
        self.start_freq.setPrefix("")
        self.start_freq.setDecimals(6)
        self.start_freq.setMinimum(0.1)
        self.start_freq.setMaximum(6000.0)
        self.start_freq.setSingleStep(1.0)
        self.start_freq.setProperty("value", 87.5)
        self.start_freq.setObjectName("start_freq")
        self.gridLayout_2.addWidget(self.start_freq, 1, 1, 1, 1)
        self.marker1 = QtWidgets.QCheckBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marker1.sizePolicy().hasHeightForWidth())
        self.marker1.setSizePolicy(sizePolicy)
        self.marker1.setObjectName("marker1")
        self.gridLayout_2.addWidget(self.marker1, 1, 4, 1, 1)
        self.marker2 = QtWidgets.QCheckBox(self.analyserTab)
        self.marker2.setAutoFillBackground(False)
        self.marker2.setObjectName("marker2")
        self.gridLayout_2.addWidget(self.marker2, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 9, 1, 1)
        self.m2_type = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m2_type.sizePolicy().hasHeightForWidth())
        self.m2_type.setSizePolicy(sizePolicy)
        self.m2_type.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.m2_type.setFont(font)
        self.m2_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.m2_type.setMinimumContentsLength(0)
        self.m2_type.setIconSize(QtCore.QSize(16, 16))
        self.m2_type.setPlaceholderText("")
        self.m2_type.setObjectName("m2_type")
        self.gridLayout_2.addWidget(self.m2_type, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.band_box = QtWidgets.QComboBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.band_box.sizePolicy().hasHeightForWidth())
        self.band_box.setSizePolicy(sizePolicy)
        self.band_box.setMaximumSize(QtCore.QSize(65, 16777215))
        self.band_box.setObjectName("band_box")
        self.gridLayout_2.addWidget(self.band_box, 1, 0, 1, 1)
        self.m4_type = QtWidgets.QComboBox(self.analyserTab)
        self.m4_type.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.m4_type.setFont(font)
        self.m4_type.setObjectName("m4_type")
        self.gridLayout_2.addWidget(self.m4_type, 2, 7, 1, 1)
        self.m1_type = QtWidgets.QComboBox(self.analyserTab)
        self.m1_type.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(7)
        self.m1_type.setFont(font)
        self.m1_type.setObjectName("m1_type")
        self.gridLayout_2.addWidget(self.m1_type, 2, 4, 1, 1)
        self.scan_button = QtWidgets.QPushButton(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy)
        self.scan_button.setCheckable(False)
        self.scan_button.setObjectName("scan_button")
        self.gridLayout_2.addWidget(self.scan_button, 1, 11, 1, 1)
        self.m3_type = QtWidgets.QComboBox(self.analyserTab)
        self.m3_type.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.m3_type.setFont(font)
        self.m3_type.setObjectName("m3_type")
        self.gridLayout_2.addWidget(self.m3_type, 2, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.analyserTab)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 8, 1, 1)
        self.mkr_start = QtWidgets.QToolButton(self.analyserTab)
        self.mkr_start.setArrowType(QtCore.Qt.LeftArrow)
        self.mkr_start.setObjectName("mkr_start")
        self.gridLayout_2.addWidget(self.mkr_start, 2, 3, 1, 1)
        self.mPeak = QtWidgets.QSpinBox(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mPeak.sizePolicy().hasHeightForWidth())
        self.mPeak.setSizePolicy(sizePolicy)
        self.mPeak.setMaximumSize(QtCore.QSize(83, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.mPeak.setFont(font)
        self.mPeak.setMinimum(-120)
        self.mPeak.setMaximum(-20)
        self.mPeak.setProperty("value", -90)
        self.mPeak.setObjectName("mPeak")
        self.gridLayout_2.addWidget(self.mPeak, 2, 8, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.analyserTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 11, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.analyserTab, "")
        self.TimeTab = QtWidgets.QWidget()
        self.TimeTab.setEnabled(True)
        self.TimeTab.setObjectName("TimeTab")
        self.openGLWidget = GLViewWidget(self.TimeTab)
        self.openGLWidget.setEnabled(True)
        self.openGLWidget.setGeometry(QtCore.QRect(155, 10, 841, 481))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label_7 = QtWidgets.QLabel(self.TimeTab)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 58, 18))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.TimeTab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_Help = QtWidgets.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionlevel = QtWidgets.QAction(MainWindow)
        self.actionlevel.setObjectName("actionlevel")
        self.actionanother = QtWidgets.QAction(MainWindow)
        self.actionanother.setObjectName("actionanother")
        self.actionAbout_QtTinySA = QtWidgets.QAction(MainWindow)
        self.actionAbout_QtTinySA.setObjectName("actionAbout_QtTinySA")
        self.menu_Help.addAction(self.actionAbout_QtTinySA)
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.points_box.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtTinySA"))
        self.lna_button.setText(_translate("MainWindow", "LNA off"))
        self.trace3.setText(_translate("MainWindow", "T3"))
        self.label_2.setText(_translate("MainWindow", "Points"))
        self.version.setText(_translate("MainWindow", "Version"))
        self.trace4.setText(_translate("MainWindow", "T4"))
        self.atten_box.setSuffix(_translate("MainWindow", "dB"))
        self.label_3.setText(_translate("MainWindow", "RBW kHz"))
        self.spur_button.setText(_translate("MainWindow", "SPUR auto"))
        self.atten_auto.setText(_translate("MainWindow", "Auto"))
        self.label_4.setText(_translate("MainWindow", "VBW"))
        self.label_8.setText(_translate("MainWindow", "Averaging"))
        self.trace1.setText(_translate("MainWindow", "T1"))
        self.label.setText(_translate("MainWindow", "Traces"))
        self.trace2.setText(_translate("MainWindow", "T2"))
        self.label_5.setText(_translate("MainWindow", "Attenuator"))
        self.battery.setText(_translate("MainWindow", "Battery"))
        self.label_6.setText(_translate("MainWindow", "Battery:"))
        self.marker3.setText(_translate("MainWindow", "M3"))
        self.stop_freq.setSuffix(_translate("MainWindow", "MHz"))
        self.marker4.setText(_translate("MainWindow", "M4"))
        self.start_freq.setSuffix(_translate("MainWindow", "MHz"))
        self.marker1.setText(_translate("MainWindow", "M1"))
        self.marker2.setText(_translate("MainWindow", "M2"))
        self.scan_button.setText(_translate("MainWindow", "Run"))
        self.label_9.setText(_translate("MainWindow", "Peak Marker"))
        self.mkr_start.setText(_translate("MainWindow", "..."))
        self.mPeak.setSuffix(_translate("MainWindow", "dBm"))
        self.mPeak.setPrefix(_translate("MainWindow", "> "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyserTab), _translate("MainWindow", "Analyser"))
        self.label_7.setText(_translate("MainWindow", "To Do"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TimeTab), _translate("MainWindow", "3D Spectrum"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.actionsetting.setText(_translate("MainWindow", "setting"))
        self.actionlevel.setText(_translate("MainWindow", "level"))
        self.actionanother.setText(_translate("MainWindow", "another"))
        self.actionAbout_QtTinySA.setText(_translate("MainWindow", "About QtTinySA"))
from pyqtgraph import PlotWidget
from pyqtgraph.opengl import GLViewWidget
