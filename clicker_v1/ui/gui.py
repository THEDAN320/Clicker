# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'g.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import ui.image.hand_rc
import ui.image.animeGirl_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(21, 21, 21);\n"
"	color: rgb(21, 21, 21);\n"
"\n"
"}")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane{\n"
"	border-top:2px solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(86, 23, 102, 255), stop:1 rgba(147, 10, 153, 255));\n"
"	border-radius:1em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar{\n"
"	left:20px;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	background: qlineargradient(spread:pad, x1:0.113, y1:0.851955, x2:1, y2:0, stop:0 rgba(105, 33, 124, 255), stop:1 rgba(251, 140, 255, 255));\n"
"\n"
"    border: 2px solid #6a009f;\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.005, y1:0.476955, x2:1, y2:0.415, stop:0 rgba(105, 33, 124, 255), stop:1 rgba(251, 140, 255, 255));\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 24ex;\n"
"    padding: 2px;\n"
"}")
        self.clicker = QWidget()
        self.clicker.setObjectName(u"clicker")
        self.gridLayout_3 = QGridLayout(self.clicker)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.clicker)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(166666, 166666))
        self.label_3.setPixmap(QPixmap(u":/girl/anime_girl.jpg"))
        self.label_3.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_3, 2, 6, 8, 3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 2, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

        self.label_4 = QLabel(self.clicker)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(166666, 166666))
        self.label_4.setPixmap(QPixmap(u":/girl/a1.jpg"))
        self.label_4.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 8, 3)

        self.cash_label = QLabel(self.clicker)
        self.cash_label.setObjectName(u"cash_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cash_label.sizePolicy().hasHeightForWidth())
        self.cash_label.setSizePolicy(sizePolicy1)
        self.cash_label.setMaximumSize(QSize(16777215, 71))
        self.cash_label.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.cash_label.setFont(font1)
        self.cash_label.setCursor(QCursor(Qt.ArrowCursor))
        self.cash_label.setLayoutDirection(Qt.LeftToRight)
        self.cash_label.setStyleSheet(u"QLabel{\n"
"	border: 2px solid;\n"
"	border-color: #6a009f;\n"
"	border-style: outset;\n"
"	color: #6f00a7;\n"
"	font: 18px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.823955, y2:0.636, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(36, 36, 36, 255));\n"
"	border-top-left-radius: 1em;\n"
"	border-top-right-radius: 1em;\n"
"	border-bottom-left-radius: 1em;\n"
"	border-bottom-right-radius: 1em;\n"
"}")
        self.cash_label.setTextFormat(Qt.AutoText)
        self.cash_label.setScaledContents(False)
        self.cash_label.setAlignment(Qt.AlignCenter)
        self.cash_label.setWordWrap(False)
        self.cash_label.setOpenExternalLinks(False)

        self.gridLayout_3.addWidget(self.cash_label, 0, 1, 1, 7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 2, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 2, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 7, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 1, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 1, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 8, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 1, 8, 1, 1)

        self.cps_label = QLabel(self.clicker)
        self.cps_label.setObjectName(u"cps_label")
        sizePolicy1.setHeightForWidth(self.cps_label.sizePolicy().hasHeightForWidth())
        self.cps_label.setSizePolicy(sizePolicy1)
        self.cps_label.setMinimumSize(QSize(0, 0))
        self.cps_label.setMaximumSize(QSize(16777215, 71))
        self.cps_label.setStyleSheet(u"QLabel{\n"
"	border: 2px solid;\n"
"	border-color: #6a009f;\n"
"	border-style: outset;\n"
"	color: #6f00a7;\n"
"	font: 18px;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.823955, y2:0.636, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(36, 36, 36, 255));\n"
"	border-top-left-radius: 1em;\n"
"	border-top-right-radius: 1em;\n"
"	border-bottom-left-radius: 1em;\n"
"	border-bottom-right-radius: 1em;\n"
"}")
        self.cps_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.cps_label, 1, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 5, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 3, 5, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 4, 5, 1, 1)

        self.click_button = QPushButton(self.clicker)
        self.click_button.setObjectName(u"click_button")
        sizePolicy1.setHeightForWidth(self.click_button.sizePolicy().hasHeightForWidth())
        self.click_button.setSizePolicy(sizePolicy1)
        self.click_button.setMaximumSize(QSize(16777215, 150))
        self.click_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.click_button.setFocusPolicy(Qt.ClickFocus)
        self.click_button.setContextMenuPolicy(Qt.NoContextMenu)
        self.click_button.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-color: #6a009f;\n"
"	border-style: outset;\n"
"	\n"
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
        icon = QIcon()
        icon.addFile(u":/click/hand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.click_button.setIcon(icon)
        self.click_button.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.click_button, 5, 3, 5, 3)

        self.tabWidget.addTab(self.clicker, "")
        self.build = QWidget()
        self.build.setObjectName(u"build")
        self.build.setStyleSheet(u"QPushButton{\n"
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
        self.gridLayout_2 = QGridLayout(self.build)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 0, 1, 1, 1)

        self.Buy_Button = QPushButton(self.build)
        self.Buy_Button.setObjectName(u"Buy_Button")
        self.Buy_Button.setMaximumSize(QSize(16777215, 50))
        self.Buy_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Buy_Button.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout_2.addWidget(self.Buy_Button, 7, 2, 1, 2)

        self.price_label = QLabel(self.build)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setMaximumSize(QSize(16777215, 50))
        self.price_label.setFont(font1)
        self.price_label.setStyleSheet(u"QLabel{\n"
"	color:qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(86, 23, 102, 255), stop:1 rgba(176, 12, 183, 255));\n"
"	font: 18px;\n"
"}")
        self.price_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.price_label, 6, 2, 1, 2)

        self.count_have_label = QLabel(self.build)
        self.count_have_label.setObjectName(u"count_have_label")
        self.count_have_label.setMaximumSize(QSize(16777215, 50))
        self.count_have_label.setStyleSheet(u"QLabel{\n"
"	border: 2px solid;\n"
"	border-color: #6a009f;\n"
"	border-style: outset;\n"
"	color: #6f00a7;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.823955, y2:0.636, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(36, 36, 36, 255));\n"
"	border-top-left-radius: 1em;\n"
"	border-top-right-radius: 1em;\n"
"	border-bottom-left-radius: 1em;\n"
"	border-bottom-right-radius: 1em;\n"
"}")
        self.count_have_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.count_have_label, 4, 2, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.House_button = QPushButton(self.build)
        self.House_button.setObjectName(u"House_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.House_button.sizePolicy().hasHeightForWidth())
        self.House_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.House_button, 0, 0, 1, 1)

        self.Libraly_button = QPushButton(self.build)
        self.Libraly_button.setObjectName(u"Libraly_button")
        sizePolicy2.setHeightForWidth(self.Libraly_button.sizePolicy().hasHeightForWidth())
        self.Libraly_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Libraly_button, 3, 0, 1, 1)

        self.Colosseum_button = QPushButton(self.build)
        self.Colosseum_button.setObjectName(u"Colosseum_button")
        sizePolicy2.setHeightForWidth(self.Colosseum_button.sizePolicy().hasHeightForWidth())
        self.Colosseum_button.setSizePolicy(sizePolicy2)
        self.Colosseum_button.setMinimumSize(QSize(60, 0))
        self.Colosseum_button.setMaximumSize(QSize(16777215, 16666666))

        self.gridLayout.addWidget(self.Colosseum_button, 2, 3, 1, 1)

        self.Church_button = QPushButton(self.build)
        self.Church_button.setObjectName(u"Church_button")
        sizePolicy2.setHeightForWidth(self.Church_button.sizePolicy().hasHeightForWidth())
        self.Church_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Church_button, 3, 1, 1, 1)

        self.Barracks_button = QPushButton(self.build)
        self.Barracks_button.setObjectName(u"Barracks_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Barracks_button.sizePolicy().hasHeightForWidth())
        self.Barracks_button.setSizePolicy(sizePolicy3)
        self.Barracks_button.setMinimumSize(QSize(60, 16))

        self.gridLayout.addWidget(self.Barracks_button, 2, 2, 1, 1)

        self.Market_button = QPushButton(self.build)
        self.Market_button.setObjectName(u"Market_button")
        sizePolicy2.setHeightForWidth(self.Market_button.sizePolicy().hasHeightForWidth())
        self.Market_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Market_button, 1, 3, 1, 1)

        self.Brothel_button = QPushButton(self.build)
        self.Brothel_button.setObjectName(u"Brothel_button")
        sizePolicy2.setHeightForWidth(self.Brothel_button.sizePolicy().hasHeightForWidth())
        self.Brothel_button.setSizePolicy(sizePolicy2)
        self.Brothel_button.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.Brothel_button, 2, 0, 1, 1)

        self.Alchemy_button = QPushButton(self.build)
        self.Alchemy_button.setObjectName(u"Alchemy_button")
        sizePolicy2.setHeightForWidth(self.Alchemy_button.sizePolicy().hasHeightForWidth())
        self.Alchemy_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Alchemy_button, 1, 2, 1, 1)

        self.Tailor_button = QPushButton(self.build)
        self.Tailor_button.setObjectName(u"Tailor_button")
        sizePolicy2.setHeightForWidth(self.Tailor_button.sizePolicy().hasHeightForWidth())
        self.Tailor_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Tailor_button, 1, 1, 1, 1)

        self.Arena_button = QPushButton(self.build)
        self.Arena_button.setObjectName(u"Arena_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Arena_button.sizePolicy().hasHeightForWidth())
        self.Arena_button.setSizePolicy(sizePolicy4)
        self.Arena_button.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.Arena_button, 2, 1, 1, 1)

        self.Cathedral_button = QPushButton(self.build)
        self.Cathedral_button.setObjectName(u"Cathedral_button")
        sizePolicy2.setHeightForWidth(self.Cathedral_button.sizePolicy().hasHeightForWidth())
        self.Cathedral_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Cathedral_button, 3, 2, 1, 1)

        self.Blacksmith_button = QPushButton(self.build)
        self.Blacksmith_button.setObjectName(u"Blacksmith_button")
        sizePolicy2.setHeightForWidth(self.Blacksmith_button.sizePolicy().hasHeightForWidth())
        self.Blacksmith_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Blacksmith_button, 1, 0, 1, 1)

        self.Hotel_button = QPushButton(self.build)
        self.Hotel_button.setObjectName(u"Hotel_button")
        sizePolicy2.setHeightForWidth(self.Hotel_button.sizePolicy().hasHeightForWidth())
        self.Hotel_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Hotel_button, 0, 1, 1, 1)

        self.Restaurant_button = QPushButton(self.build)
        self.Restaurant_button.setObjectName(u"Restaurant_button")
        sizePolicy2.setHeightForWidth(self.Restaurant_button.sizePolicy().hasHeightForWidth())
        self.Restaurant_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Restaurant_button, 0, 3, 1, 1)

        self.Tavern_button = QPushButton(self.build)
        self.Tavern_button.setObjectName(u"Tavern_button")
        sizePolicy2.setHeightForWidth(self.Tavern_button.sizePolicy().hasHeightForWidth())
        self.Tavern_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Tavern_button, 0, 2, 1, 1)

        self.Castle_button = QPushButton(self.build)
        self.Castle_button.setObjectName(u"Castle_button")
        sizePolicy2.setHeightForWidth(self.Castle_button.sizePolicy().hasHeightForWidth())
        self.Castle_button.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Castle_button, 3, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 8, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 0, 4, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 0, 3, 1, 1)

        self.image_build_label = QLabel(self.build)
        self.image_build_label.setObjectName(u"image_build_label")
        sizePolicy.setHeightForWidth(self.image_build_label.sizePolicy().hasHeightForWidth())
        self.image_build_label.setSizePolicy(sizePolicy)
        self.image_build_label.setMinimumSize(QSize(0, 0))
        self.image_build_label.setMaximumSize(QSize(500, 500))
        self.image_build_label.setStyleSheet(u"")
        self.image_build_label.setFrameShape(QFrame.NoFrame)
        self.image_build_label.setScaledContents(True)
        self.image_build_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.image_build_label, 0, 2, 4, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.X1_Radio = QRadioButton(self.build)
        self.X1_Radio.setObjectName(u"X1_Radio")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.X1_Radio.sizePolicy().hasHeightForWidth())
        self.X1_Radio.setSizePolicy(sizePolicy5)
        self.X1_Radio.setMaximumSize(QSize(16666666, 16777215))
        self.X1_Radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.X1_Radio.setStyleSheet(u"QRadioButton[check=\"0\"]{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(86, 23, 102, 255), stop:1 rgba(176, 12, 183, 255));\n"
"	border:2px solid;\n"
"	border-color:qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.937, y2:0.522955, stop:0.346591 rgba(50, 13, 59, 255), stop:1 rgba(109, 7, 113, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  1;\n"
"    height:   1;\n"
"	background:rgb(32, 0, 49);\n"
"}\n"
"\n"
"QRadioButton[check=\"1\"]{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(48, 13, 57, 255), stop:1 rgba(131, 8, 137, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}")
        self.X1_Radio.setCheckable(True)
        self.X1_Radio.setChecked(True)
        self.X1_Radio.setAutoRepeat(False)
        self.X1_Radio.setAutoExclusive(True)
        self.X1_Radio.setProperty("check", 1)

        self.horizontalLayout.addWidget(self.X1_Radio)

        self.X10_Radio = QRadioButton(self.build)
        self.X10_Radio.setObjectName(u"X10_Radio")
        sizePolicy5.setHeightForWidth(self.X10_Radio.sizePolicy().hasHeightForWidth())
        self.X10_Radio.setSizePolicy(sizePolicy5)
        self.X10_Radio.setMaximumSize(QSize(166666, 16777215))
        self.X10_Radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.X10_Radio.setStyleSheet(u"QRadioButton[check=\"0\"]{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(176, 12, 183, 255) , stop:1 rgba(86, 23, 102, 255));;\n"
"	border:2px solid;\n"
"	border-color:qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.937, y2:0.522955, stop:0.346591 rgba(109, 7, 113, 255), stop:1 rgba(50, 13, 59, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  1;\n"
"    height:   1;\n"
"	background:rgb(32, 0, 49);\n"
"}\n"
"\n"
"QRadioButton[check=\"1\"]{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(131, 8, 137, 255), stop:1 rgba(48, 13, 57, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.X10_Radio.setCheckable(True)
        self.X10_Radio.setChecked(False)
        self.X10_Radio.setProperty("check", 0)

        self.horizontalLayout.addWidget(self.X10_Radio)

        self.X100_Radio = QRadioButton(self.build)
        self.X100_Radio.setObjectName(u"X100_Radio")
        sizePolicy5.setHeightForWidth(self.X100_Radio.sizePolicy().hasHeightForWidth())
        self.X100_Radio.setSizePolicy(sizePolicy5)
        self.X100_Radio.setMaximumSize(QSize(1666, 16777215))
        self.X100_Radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.X100_Radio.setStyleSheet(u"QRadioButton[check=\"0\"]{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(86, 23, 102, 255), stop:1 rgba(176, 12, 183, 255));\n"
"	border:2px solid;\n"
"	border-color:qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.937, y2:0.522955, stop:0.346591 rgba(50, 13, 59, 255), stop:1 rgba(109, 7, 113, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  1;\n"
"    height:   1;\n"
"	background:rgb(32, 0, 49);\n"
"}\n"
"\n"
"QRadioButton[check=\"1\"]{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.642, x2:0.994, y2:0.511591, stop:0.329545 rgba(48, 13, 57, 255), stop:1 rgba(131, 8, 137, 255));\n"
"    color: rgb(25, 25, 25);\n"
"	font:20px;\n"
"	font-weight: bold;\n"
"}")
        self.X100_Radio.setCheckable(True)
        self.X100_Radio.setChecked(False)
        self.X100_Radio.setAutoRepeat(False)
        self.X100_Radio.setProperty("check", 0)

        self.horizontalLayout.addWidget(self.X100_Radio)


        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 2, 1, 2)

        self.tabWidget.addTab(self.build, "")
        self.shop = QWidget()
        self.shop.setObjectName(u"shop")
        self.gridLayout_5 = QGridLayout(self.shop)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.shop)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 562, 339))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.upgrade_layout = QVBoxLayout()
        self.upgrade_layout.setObjectName(u"upgrade_layout")

        self.gridLayout_6.addLayout(self.upgrade_layout, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.shop, "")
        self.achievement = QWidget()
        self.achievement.setObjectName(u"achievement")
        self.gridLayout_7 = QGridLayout(self.achievement)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea_2 = QScrollArea(self.achievement)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 562, 339))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.achievement_layout = QVBoxLayout()
        self.achievement_layout.setObjectName(u"achievement_layout")

        self.gridLayout_8.addLayout(self.achievement_layout, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_7.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.achievement, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.cash_label.setText(QCoreApplication.translate("MainWindow", u"0$", None))
        self.cps_label.setText(QCoreApplication.translate("MainWindow", u"0$ cps", None))
        self.click_button.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clicker), QCoreApplication.translate("MainWindow", u"Clicker", None))
        self.Buy_Button.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.price_label.setText("")
        self.count_have_label.setText("")
        self.House_button.setText(QCoreApplication.translate("MainWindow", u"House", None))
        self.Libraly_button.setText(QCoreApplication.translate("MainWindow", u"Libraly", None))
        self.Colosseum_button.setText(QCoreApplication.translate("MainWindow", u"Colosseum", None))
        self.Church_button.setText(QCoreApplication.translate("MainWindow", u"Church", None))
        self.Barracks_button.setText(QCoreApplication.translate("MainWindow", u"Barracks", None))
        self.Market_button.setText(QCoreApplication.translate("MainWindow", u"Market", None))
        self.Brothel_button.setText(QCoreApplication.translate("MainWindow", u"Brothel", None))
        self.Alchemy_button.setText(QCoreApplication.translate("MainWindow", u"Alchemy", None))
        self.Tailor_button.setText(QCoreApplication.translate("MainWindow", u"Tailor", None))
        self.Arena_button.setText(QCoreApplication.translate("MainWindow", u"Arena", None))
        self.Cathedral_button.setText(QCoreApplication.translate("MainWindow", u"Cathedral", None))
        self.Blacksmith_button.setText(QCoreApplication.translate("MainWindow", u"Blacksmith", None))
        self.Hotel_button.setText(QCoreApplication.translate("MainWindow", u"Hotel", None))
        self.Restaurant_button.setText(QCoreApplication.translate("MainWindow", u"Restaurant", None))
        self.Tavern_button.setText(QCoreApplication.translate("MainWindow", u"Tavern", None))
        self.Castle_button.setText(QCoreApplication.translate("MainWindow", u"Castle", None))
        self.image_build_label.setText("")
        self.X1_Radio.setText(QCoreApplication.translate("MainWindow", u"1X", None))
        self.X10_Radio.setText(QCoreApplication.translate("MainWindow", u"10X", None))
        self.X100_Radio.setText(QCoreApplication.translate("MainWindow", u"100X", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.build), QCoreApplication.translate("MainWindow", u"Build", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shop), QCoreApplication.translate("MainWindow", u"Shop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.achievement), QCoreApplication.translate("MainWindow", u"Achievement", None))
    # retranslateUi

