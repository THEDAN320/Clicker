# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Achievement.ui'
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
    QLabel, QProgressBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AchievementWidget(object):
    def setupUi(self, AchievementWidget):
        if not AchievementWidget.objectName():
            AchievementWidget.setObjectName(u"AchievementWidget")
        AchievementWidget.resize(350, 110)
        AchievementWidget.setMinimumSize(QSize(350, 110))
        AchievementWidget.setMaximumSize(QSize(16777215, 110))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        AchievementWidget.setFont(font)
        AchievementWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(AchievementWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(AchievementWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 70))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border-radius: 10px;\n"
"	background: rgb(133, 1, 185);\n"
"}    ")
        self.groupBox.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.achievement_label = QLabel(self.groupBox)
        self.achievement_label.setObjectName(u"achievement_label")
        font2 = QFont()
        font2.setBold(True)
        self.achievement_label.setFont(font2)
        self.achievement_label.setStyleSheet(u"QLabel{\n"
"	background: rgb(133, 1, 185);\n"
"	color: rgb(21,21,21);\n"
"}")
        self.achievement_label.setFrameShape(QFrame.NoFrame)
        self.achievement_label.setFrameShadow(QFrame.Plain)
        self.achievement_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.achievement_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(0, 40))
        self.progressBar.setFont(font2)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background:rgb(124,113,116);\n"
"	border-radius: 10px;\n"
"	color: rgb(21,21,21);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background: qlineargradient(spread:pad, x1:0,y1:0,x2:1,y2:0,stop:0 rgba(201,87,149,255),stop:1 rgba(179,65,244,255));\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(AchievementWidget)

        QMetaObject.connectSlotsByName(AchievementWidget)
    # setupUi

    def retranslateUi(self, AchievementWidget):
        AchievementWidget.setWindowTitle(QCoreApplication.translate("AchievementWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.achievement_label.setText(QCoreApplication.translate("AchievementWidget", u"make a 100 click", None))
    # retranslateUi

