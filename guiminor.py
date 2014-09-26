# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minor.ui'
#
# Created: Fri Sep 26 19:28:47 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from guifunctions import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Steganography(object):
    def __init__(self):
		dataT = []
		ST = 0
		TT = 0
		enT = ""
		dataC = []
		SC = 0
		TC = 0
		enC = ""
    def setupUi(self, Steganography):
        Steganography.setObjectName(_fromUtf8("Steganography"))
        Steganography.resize(250, 550)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Steganography.sizePolicy().hasHeightForWidth())
        Steganography.setSizePolicy(sizePolicy)
        Steganography.setMinimumSize(QtCore.QSize(250, 550))
        Steganography.setMaximumSize(QtCore.QSize(250, 550))
        self.centralwidget = QtGui.QWidget(Steganography)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.cLabel = QtGui.QLabel(self.centralwidget)
        self.cLabel.setObjectName(_fromUtf8("cLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.cLabel)
        self.cBrowse = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBrowse.sizePolicy().hasHeightForWidth())
        self.cBrowse.setSizePolicy(sizePolicy)
        self.cBrowse.setMaximumSize(QtCore.QSize(100, 50))
        self.cBrowse.setObjectName(_fromUtf8("cBrowse"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cBrowse)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.cPath = QtGui.QLineEdit(self.centralwidget)
        self.cPath.setReadOnly(True)
        self.cPath.setObjectName(_fromUtf8("cPath"))
        self.verticalLayout.addWidget(self.cPath)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cLabelSR = QtGui.QLabel(self.centralwidget)
        self.cLabelSR.setObjectName(_fromUtf8("cLabelSR"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.cLabelSR)
        self.cSR = QtGui.QLabel(self.centralwidget)
        self.cSR.setObjectName(_fromUtf8("cSR"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cSR)
        self.cLabelL = QtGui.QLabel(self.centralwidget)
        self.cLabelL.setObjectName(_fromUtf8("cLabelL"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.cLabelL)
        self.cL = QtGui.QLabel(self.centralwidget)
        self.cL.setObjectName(_fromUtf8("cL"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cL)
        self.cLabelE = QtGui.QLabel(self.centralwidget)
        self.cLabelE.setObjectName(_fromUtf8("cLabelE"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cLabelE)
        self.cEncoding = QtGui.QLabel(self.centralwidget)
        self.cEncoding.setObjectName(_fromUtf8("cEncoding"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cEncoding)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.tLabel = QtGui.QLabel(self.centralwidget)
        self.tLabel.setObjectName(_fromUtf8("tLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.tLabel)
        self.tBrowse = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tBrowse.sizePolicy().hasHeightForWidth())
        self.tBrowse.setSizePolicy(sizePolicy)
        self.tBrowse.setMaximumSize(QtCore.QSize(100, 50))
        self.tBrowse.setObjectName(_fromUtf8("tBrowse"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.tBrowse)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.tPath = QtGui.QLineEdit(self.centralwidget)
        self.tPath.setReadOnly(True)
        self.tPath.setObjectName(_fromUtf8("tPath"))
        self.verticalLayout_2.addWidget(self.tPath)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.tLabelSR = QtGui.QLabel(self.centralwidget)
        self.tLabelSR.setObjectName(_fromUtf8("tLabelSR"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.tLabelSR)
        self.tSR = QtGui.QLabel(self.centralwidget)
        self.tSR.setObjectName(_fromUtf8("tSR"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.tSR)
        self.tLabelL = QtGui.QLabel(self.centralwidget)
        self.tLabelL.setObjectName(_fromUtf8("tLabelL"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.tLabelL)
        self.tL = QtGui.QLabel(self.centralwidget)
        self.tL.setObjectName(_fromUtf8("tL"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.tL)
        self.tLabelE = QtGui.QLabel(self.centralwidget)
        self.tLabelE.setObjectName(_fromUtf8("tLabelE"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.tLabelE)
        self.tEncoding = QtGui.QLabel(self.centralwidget)
        self.tEncoding.setObjectName(_fromUtf8("tEncoding"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.tEncoding)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(75, 50))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setAccelerated(True)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(0.09)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", 0.08)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        """
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(75, 50))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        """
        self.verticalLayout_3.addLayout(self.formLayout_5)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        Steganography.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Steganography)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Steganography.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Steganography)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Steganography.setStatusBar(self.statusbar)
        self.cLabel.setBuddy(self.cBrowse)
        self.tLabel.setBuddy(self.tBrowse)
        self.label.setBuddy(self.doubleSpinBox)
        """
        self.label_2.setBuddy(self.comboBox)
        """

        self.retranslateUi(Steganography)
        QtCore.QObject.connect(self.cBrowse, QtCore.SIGNAL(_fromUtf8("released()")), self.opencFile)
        QtCore.QObject.connect(self.tBrowse, QtCore.SIGNAL(_fromUtf8("released()")), self.opentFile)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("released()")), self.stegoFunction)
        QtCore.QMetaObject.connectSlotsByName(Steganography)
        Steganography.setTabOrder(self.cBrowse, self.tBrowse)
        Steganography.setTabOrder(self.tBrowse, self.doubleSpinBox)
        """
        Steganography.setTabOrder(self.doubleSpinBox, self.comboBox)
        """
        Steganography.setTabOrder(self.doubleSpinBox, self.pushButton)
        Steganography.setTabOrder(self.pushButton, self.cPath)
        Steganography.setTabOrder(self.cPath, self.tPath)

    def retranslateUi(self, Steganography):
        Steganography.setWindowTitle(_translate("Steganography", "Steganography", None))
        self.cLabel.setText(_translate("Steganography", "Cover File", None))
        self.cBrowse.setText(_translate("Steganography", "Browse", None))
        self.cLabelSR.setText(_translate("Steganography", "Sampling Rate:", None))
        self.cSR.setText(_translate("Steganography", "0 Hz", None))
        self.cLabelL.setText(_translate("Steganography", "Length:", None))
        self.cL.setText(_translate("Steganography", "0m 0s", None))
        self.cLabelE.setText(_translate("Steganography", "Encoding:", None))
        self.cEncoding.setText(_translate("Steganography", "None", None))
        self.tLabel.setText(_translate("Steganography", "Target File", None))
        self.tBrowse.setText(_translate("Steganography", "Browse", None))
        self.tLabelSR.setText(_translate("Steganography", "Sampling Rate:", None))
        self.tSR.setText(_translate("Steganography", "0 Hz", None))
        self.tLabelL.setText(_translate("Steganography", "Length:", None))
        self.tL.setText(_translate("Steganography", "0m 0s", None))
        self.tLabelE.setText(_translate("Steganography", "Encoding:", None))
        self.tEncoding.setText(_translate("Steganography", "None", None))
        self.label.setText(_translate("Steganography", "Theta (s):", None))
        self.label_2.setText(_translate("Steganography", "Sampling Rate (Hz):", None))
        """
        self.comboBox.setItemText(0, _translate("Steganography", "44100", None))
        self.comboBox.setItemText(1, _translate("Steganography", "22050", None))
        self.comboBox.setItemText(2, _translate("Steganography", "11025", None))
        """
        self.pushButton.setText(_translate("Steganography", "Steg", None))

    def opencFile(self):
    	fileName = QtGui.QFileDialog.getOpenFileName(None, "Open Audio file", "~/", "Audio Files (*.mp3 *.wav)")
    	if(len(fileName)):
    		global dataC
    		global SC
    		global TC
    		global enC
	    	self.cPath.setText(_translate("Steganography", fileName, None))
	    	dataC, SC, TC, enC = openFile(fileName)
	    	self.cSR.setText(str(SC) + ' Hz')
	    	self.cL.setText(str(TC/60) + 'm ' + str(TC%60) + 's')
	    	self.cEncoding.setText(enC)
	    	print "********************************************************************************"
	    	print "Opened the cover audio file: ", str(fileName)
	    	print "*\tSample count: ", str(len(dataC))
	    	print "*\tSampling Frequency: ", str(SC)
	    	print "*\tLength of audio: ", str(TC/60), 'm ', str(TC%60), 's'
	    	print "*\tEncoding: ", enC

    def opentFile(self):
    	fileName = QtGui.QFileDialog.getOpenFileName(None, "Open Audio file", "~/", "Audio Files (*.mp3 *.wav)")
    	if(len(fileName)):
    		global dataT
    		global ST
    		global TT
    		global enT
	    	self.tPath.setText(_translate("Steganography", fileName, None))
	    	dataT, ST, TT, enT = openFile(fileName)
	    	self.tSR.setText(str(ST) + ' Hz')
	    	self.tL.setText(str(TT/60)+ 'm ' + str(TT%60) + 's')
	    	self.tEncoding.setText(enT)
	    	print "********************************************************************************"
	    	print "Opened the target audio file: ", str(fileName)
	    	print "*\tSample count: ", str(len(dataT))
	    	print "*\tSampling Frequency: ", str(ST)
	    	print "*\tLength of audio: ", str(TT/60), 'm ', str(TT%60), 's'
	    	print "*\tEncoding: ", enT

    def stegoFunction(self):
    	theta = self.doubleSpinBox.value()
    	if TC < 3 * TT / theta:
			print "********************************************************************************"
			print "Cover audio file length is insufficient!!! Please use an audio file atleast ", 3*TT/theta, " seconds in length."
			QtGui.QMessageBox.critical(None, "Insufficient length", "Cover audio file length is insufficient!!! Please use an audio file atleast " + str(3*TT/theta) + " seconds in length.");
			return
    	ocount = len(dataC)
    	count = steg(dataC, SC, TC, dataT, ST, TT, theta)
    	print "********************************************************************************"
    	print "File stegoed with parameters: "
    	print "*\tCover File samples: ", str(ocount)
    	print "*\tTarget File samples: ", str(len(dataT))
    	print "*\tSamples written: ", str(count)
    	print "*\tTheta (in seconds): ", str(theta)
    	print "*\tSampling Frequency: ", str(SC)
    	QtGui.QMessageBox.information(None, "Audio file stegoed", "Audio file stegoed");


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Steganography = QtGui.QMainWindow()
    ui = Ui_Steganography()
    ui.setupUi(Steganography)
    Steganography.show()
    sys.exit(app.exec_())
