# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Upgrade.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_upgradeWidget(object):
    def setupUi(self, upgradeWidget):
        if not upgradeWidget.objectName():
            upgradeWidget.setObjectName(u"upgradeWidget")
        upgradeWidget.resize(516, 110)
        upgradeWidget.setMinimumSize(QSize(350, 0))
        upgradeWidget.setMaximumSize(QSize(16777215, 110))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        upgradeWidget.setFont(font)
        upgradeWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(upgradeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(upgradeWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 70))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 10px;\n"
"	color: rgb(109, 0, 163);\n"
"	background: qlineargradient(spread:pad, x1:0.028, y1:1, x2:0.949, y2:0.130455, stop:0 rgba(124, 8, 129, 255), stop:0.505682 rgba(201, 13, 209, 255), stop:0.994318 rgba(246, 16, 255, 255));\n"
"}")
        self.groupBox.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_lbl = QLabel(self.groupBox)
        self.icon_lbl.setObjectName(u"icon_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_lbl.sizePolicy().hasHeightForWidth())
        self.icon_lbl.setSizePolicy(sizePolicy)
        self.icon_lbl.setStyleSheet(u"QLabel{\n"
"	background:transparent;\n"
"}")
        self.icon_lbl.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.info_upgrade_lbl = QLabel(self.groupBox)
        self.info_upgrade_lbl.setObjectName(u"info_upgrade_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_upgrade_lbl.sizePolicy().hasHeightForWidth())
        self.info_upgrade_lbl.setSizePolicy(sizePolicy1)
        self.info_upgrade_lbl.setFont(font1)
        self.info_upgrade_lbl.setAutoFillBackground(False)
        self.info_upgrade_lbl.setStyleSheet(u"QLabel{\n"
"	color: rgb(21, 21, 21);\n"
"	background:transparent;\n"
"}")
        self.info_upgrade_lbl.setFrameShape(QFrame.NoFrame)
        self.info_upgrade_lbl.setFrameShadow(QFrame.Plain)
        self.info_upgrade_lbl.setAlignment(Qt.AlignCenter)
        self.info_upgrade_lbl.setWordWrap(False)

        self.horizontalLayout.addWidget(self.info_upgrade_lbl)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buy_upgrade_btn = QPushButton(self.groupBox)
        self.buy_upgrade_btn.setObjectName(u"buy_upgrade_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buy_upgrade_btn.sizePolicy().hasHeightForWidth())
        self.buy_upgrade_btn.setSizePolicy(sizePolicy2)
        self.buy_upgrade_btn.setMinimumSize(QSize(50, 50))
        self.buy_upgrade_btn.setFont(font1)
        self.buy_upgrade_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.buy_upgrade_btn.setFocusPolicy(Qt.NoFocus)
        self.buy_upgrade_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.buy_upgrade_btn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-color: #6a009f;\n"
"	border-style: outset;\n"
"	color: #6f00a7;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.823955, y2:0.636, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(36, 36, 36, 255));\n"
"	border-top-left-radius: 1em;\n"
"	border-top-right-radius: 1em;\n"
"	border-bottom-left-radius: 1em;\n"
"	border-bottom-right-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	stop:0 rgba(41, 41, 41, 255), stop:1 rgba(124, 124, 124, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.114, x2:1, y2:0, 	 stop:0 rgba(91, 91, 91, 255), stop:1 rgba(178, 178, 178, 255));\n"
"	border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.buy_upgrade_btn)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(upgradeWidget)

        QMetaObject.connectSlotsByName(upgradeWidget)
    # setupUi

    def retranslateUi(self, upgradeWidget):
        upgradeWidget.setWindowTitle(QCoreApplication.translate("upgradeWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.icon_lbl.setText("")
        self.info_upgrade_lbl.setText("")
        self.buy_upgrade_btn.setText(QCoreApplication.translate("upgradeWidget", u"BUY", None))
    # retranslateUi

