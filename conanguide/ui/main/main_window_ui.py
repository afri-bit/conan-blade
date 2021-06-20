# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from conanguide.ui.res import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1071, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        icon = QIcon()
        icon.addFile(u":/icon/conan_guide_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionViewProfile = QAction(MainWindow)
        self.actionViewProfile.setObjectName(u"actionViewProfile")
        self.actionViewProfile.setChecked(False)
        self.actionFileExit = QAction(MainWindow)
        self.actionFileExit.setObjectName(u"actionFileExit")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon1 = QIcon()
        icon1.addFile(u":/icon/ws_refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon1)
        self.actionConanCreate = QAction(MainWindow)
        self.actionConanCreate.setObjectName(u"actionConanCreate")
        icon2 = QIcon()
        icon2.addFile(u":/icon/conan_create.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanCreate.setIcon(icon2)
        self.actionConanInstall = QAction(MainWindow)
        self.actionConanInstall.setObjectName(u"actionConanInstall")
        icon3 = QIcon()
        icon3.addFile(u":/icon/conan_install.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanInstall.setIcon(icon3)
        self.actionConanBuild = QAction(MainWindow)
        self.actionConanBuild.setObjectName(u"actionConanBuild")
        icon4 = QIcon()
        icon4.addFile(u":/icon/conan_build.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanBuild.setIcon(icon4)
        self.actionConanSource = QAction(MainWindow)
        self.actionConanSource.setObjectName(u"actionConanSource")
        icon5 = QIcon()
        icon5.addFile(u":/icon/conan_source.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanSource.setIcon(icon5)
        self.actionConanPackage = QAction(MainWindow)
        self.actionConanPackage.setObjectName(u"actionConanPackage")
        icon6 = QIcon()
        icon6.addFile(u":/icon/conan_package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanPackage.setIcon(icon6)
        self.actionConanExport = QAction(MainWindow)
        self.actionConanExport.setObjectName(u"actionConanExport")
        icon7 = QIcon()
        icon7.addFile(u":/icon/conan_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanExport.setIcon(icon7)
        self.actionConanExportPackage = QAction(MainWindow)
        self.actionConanExportPackage.setObjectName(u"actionConanExportPackage")
        icon8 = QIcon()
        icon8.addFile(u":/icon/conan_package_export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConanExportPackage.setIcon(icon8)
        self.actionViewPackage = QAction(MainWindow)
        self.actionViewPackage.setObjectName(u"actionViewPackage")
        self.actionViewPackage.setChecked(False)
        self.actionHelpConanio = QAction(MainWindow)
        self.actionHelpConanio.setObjectName(u"actionHelpConanio")
        icon9 = QIcon()
        icon9.addFile(u":/icon/conan_io_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelpConanio.setIcon(icon9)
        self.actionHelpAbout = QAction(MainWindow)
        self.actionHelpAbout.setObjectName(u"actionHelpAbout")
        self.actionHelpAbout.setIcon(icon)
        self.actionViewHome = QAction(MainWindow)
        self.actionViewHome.setObjectName(u"actionViewHome")
        self.actionViewWorkspace = QAction(MainWindow)
        self.actionViewWorkspace.setObjectName(u"actionViewWorkspace")
        self.actionViewRemote = QAction(MainWindow)
        self.actionViewRemote.setObjectName(u"actionViewRemote")
        self.actionViewSettings = QAction(MainWindow)
        self.actionViewSettings.setObjectName(u"actionViewSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.tabWidgetMain = QTabWidget(self.centralwidget)
        self.tabWidgetMain.setObjectName(u"tabWidgetMain")
        self.tabWidgetMain.setTabPosition(QTabWidget.West)
        self.tabWidgetMain.setTabShape(QTabWidget.Rounded)
        self.tabHome = QWidget()
        self.tabHome.setObjectName(u"tabHome")
        self.tabHome.setEnabled(True)
        self.tabWidgetMain.addTab(self.tabHome, "")
        self.tabPackage = QWidget()
        self.tabPackage.setObjectName(u"tabPackage")
        self.horizontalLayout_4 = QHBoxLayout(self.tabPackage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter_5 = QSplitter(self.tabPackage)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.frame_6 = QFrame(self.splitter_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(300, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setLayoutDirection(Qt.LeftToRight)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 0, 2)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 0))
        self.label_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_15.addWidget(self.label_10)

        self.checkBoxOpenExplorer = QCheckBox(self.frame_16)
        self.checkBoxOpenExplorer.setObjectName(u"checkBoxOpenExplorer")
        self.checkBoxOpenExplorer.setMaximumSize(QSize(90, 16777215))
        self.checkBoxOpenExplorer.setChecked(False)

        self.horizontalLayout_15.addWidget(self.checkBoxOpenExplorer)

        self.checkBoxCopyClipboard = QCheckBox(self.frame_16)
        self.checkBoxCopyClipboard.setObjectName(u"checkBoxCopyClipboard")
        self.checkBoxCopyClipboard.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBoxCopyClipboard)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_16)

        self.splitter_3 = QSplitter(self.frame_6)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.treeViewRecipe = QTreeView(self.splitter_3)
        self.treeViewRecipe.setObjectName(u"treeViewRecipe")
        self.treeViewRecipe.setEnabled(True)
        self.splitter_3.addWidget(self.treeViewRecipe)
        self.treeViewRecipeInspect = QTreeView(self.splitter_3)
        self.treeViewRecipeInspect.setObjectName(u"treeViewRecipeInspect")
        self.splitter_3.addWidget(self.treeViewRecipeInspect)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_5.addWidget(self.frame_6)
        self.frame_15 = QFrame(self.splitter_5)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.splitter_6 = QSplitter(self.frame_15)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.splitter_6.setFrameShape(QFrame.NoFrame)
        self.splitter_6.setFrameShadow(QFrame.Plain)
        self.splitter_6.setLineWidth(1)
        self.splitter_6.setOrientation(Qt.Vertical)
        self.splitter_6.setHandleWidth(5)
        self.frame_19 = QFrame(self.splitter_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 135))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_19)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEditCachePath = QLineEdit(self.frame)
        self.lineEditCachePath.setObjectName(u"lineEditCachePath")
        self.lineEditCachePath.setEnabled(True)
        self.lineEditCachePath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditCachePath)

        self.btnCopyCachePath = QPushButton(self.frame)
        self.btnCopyCachePath.setObjectName(u"btnCopyCachePath")

        self.horizontalLayout.addWidget(self.btnCopyCachePath)

        self.btnOpenCachePath = QPushButton(self.frame)
        self.btnOpenCachePath.setObjectName(u"btnOpenCachePath")

        self.horizontalLayout.addWidget(self.btnOpenCachePath)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_21 = QFrame(self.groupBox)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_21.addWidget(self.label_20)

        self.lineEditDataPath = QLineEdit(self.frame_21)
        self.lineEditDataPath.setObjectName(u"lineEditDataPath")
        self.lineEditDataPath.setEnabled(True)
        self.lineEditDataPath.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEditDataPath)

        self.btnCopyDataPath = QPushButton(self.frame_21)
        self.btnCopyDataPath.setObjectName(u"btnCopyDataPath")

        self.horizontalLayout_21.addWidget(self.btnCopyDataPath)

        self.btnOpenDataPath = QPushButton(self.frame_21)
        self.btnOpenDataPath.setObjectName(u"btnOpenDataPath")

        self.horizontalLayout_21.addWidget(self.btnOpenDataPath)


        self.verticalLayout_8.addWidget(self.frame_21)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEditRealPath = QLineEdit(self.frame_2)
        self.lineEditRealPath.setObjectName(u"lineEditRealPath")
        self.lineEditRealPath.setEnabled(True)
        self.lineEditRealPath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEditRealPath)

        self.btnCopyRealPath = QPushButton(self.frame_2)
        self.btnCopyRealPath.setObjectName(u"btnCopyRealPath")

        self.horizontalLayout_2.addWidget(self.btnCopyRealPath)

        self.btnOpenRealPath = QPushButton(self.frame_2)
        self.btnOpenRealPath.setObjectName(u"btnOpenRealPath")

        self.horizontalLayout_2.addWidget(self.btnOpenRealPath)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 0))
        self.label_3.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditPackagePath = QLineEdit(self.frame_3)
        self.lineEditPackagePath.setObjectName(u"lineEditPackagePath")
        self.lineEditPackagePath.setEnabled(True)
        self.lineEditPackagePath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditPackagePath)

        self.btnCopyPackagePath = QPushButton(self.frame_3)
        self.btnCopyPackagePath.setObjectName(u"btnCopyPackagePath")

        self.horizontalLayout_3.addWidget(self.btnCopyPackagePath)

        self.btnOpenPackagePath = QPushButton(self.frame_3)
        self.btnOpenPackagePath.setObjectName(u"btnOpenPackagePath")

        self.horizontalLayout_3.addWidget(self.btnOpenPackagePath)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.splitter_6.addWidget(self.frame_19)
        self.frameWebView = QFrame(self.splitter_6)
        self.frameWebView.setObjectName(u"frameWebView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frameWebView.sizePolicy().hasHeightForWidth())
        self.frameWebView.setSizePolicy(sizePolicy3)
        self.frameWebView.setFrameShape(QFrame.StyledPanel)
        self.frameWebView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frameWebView)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_15 = QLabel(self.frameWebView)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.graphicsView = QGraphicsView(self.frameWebView)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setSceneRect(QRectF(0, 0, 0, 0))

        self.verticalLayout_7.addWidget(self.graphicsView)

        self.splitter_6.addWidget(self.frameWebView)

        self.verticalLayout_13.addWidget(self.splitter_6)

        self.splitter_5.addWidget(self.frame_15)

        self.horizontalLayout_4.addWidget(self.splitter_5)

        self.tabWidgetMain.addTab(self.tabPackage, "")
        self.tabWorkspace = QWidget()
        self.tabWorkspace.setObjectName(u"tabWorkspace")
        self.verticalLayout_6 = QVBoxLayout(self.tabWorkspace)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_8 = QSplitter(self.tabWorkspace)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Vertical)
        self.frame_24 = QFrame(self.splitter_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 228))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_24)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.frame_24)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEditUser = QLineEdit(self.frame_4)
        self.lineEditUser.setObjectName(u"lineEditUser")

        self.horizontalLayout_5.addWidget(self.lineEditUser)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.lineEditChannel = QLineEdit(self.frame_4)
        self.lineEditChannel.setObjectName(u"lineEditChannel")

        self.horizontalLayout_5.addWidget(self.lineEditChannel)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.frame_24)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEditRecipePath = QLineEdit(self.frame_8)
        self.lineEditRecipePath.setObjectName(u"lineEditRecipePath")
        self.lineEditRecipePath.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditRecipePath)

        self.toolBtnExplorerRecipePath = QToolButton(self.frame_8)
        self.toolBtnExplorerRecipePath.setObjectName(u"toolBtnExplorerRecipePath")

        self.horizontalLayout_6.addWidget(self.toolBtnExplorerRecipePath)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_24)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEditInstallPath = QLineEdit(self.frame_9)
        self.lineEditInstallPath.setObjectName(u"lineEditInstallPath")

        self.horizontalLayout_7.addWidget(self.lineEditInstallPath)

        self.toolBtnExplorerInstallPath = QToolButton(self.frame_9)
        self.toolBtnExplorerInstallPath.setObjectName(u"toolBtnExplorerInstallPath")

        self.horizontalLayout_7.addWidget(self.toolBtnExplorerInstallPath)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_24)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEditBuildPath = QLineEdit(self.frame_10)
        self.lineEditBuildPath.setObjectName(u"lineEditBuildPath")

        self.horizontalLayout_8.addWidget(self.lineEditBuildPath)

        self.toolBtnExplorerBuildPath = QToolButton(self.frame_10)
        self.toolBtnExplorerBuildPath.setObjectName(u"toolBtnExplorerBuildPath")

        self.horizontalLayout_8.addWidget(self.toolBtnExplorerBuildPath)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_24)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEditSourcePath = QLineEdit(self.frame_11)
        self.lineEditSourcePath.setObjectName(u"lineEditSourcePath")

        self.horizontalLayout_9.addWidget(self.lineEditSourcePath)

        self.toolBtnExplorerSourcePath = QToolButton(self.frame_11)
        self.toolBtnExplorerSourcePath.setObjectName(u"toolBtnExplorerSourcePath")

        self.horizontalLayout_9.addWidget(self.toolBtnExplorerSourcePath)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_24)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEditPackageExpPath = QLineEdit(self.frame_13)
        self.lineEditPackageExpPath.setObjectName(u"lineEditPackageExpPath")

        self.horizontalLayout_12.addWidget(self.lineEditPackageExpPath)

        self.toolBtnExplorerPackagePath = QToolButton(self.frame_13)
        self.toolBtnExplorerPackagePath.setObjectName(u"toolBtnExplorerPackagePath")

        self.horizontalLayout_12.addWidget(self.toolBtnExplorerPackagePath)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_24)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEditAdditionalParams = QLineEdit(self.frame_12)
        self.lineEditAdditionalParams.setObjectName(u"lineEditAdditionalParams")

        self.horizontalLayout_10.addWidget(self.lineEditAdditionalParams)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.frame_24)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(75, 0))
        self.label_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.label_12)

        self.comboBoxProfile = QComboBox(self.frame_14)
        self.comboBoxProfile.setObjectName(u"comboBoxProfile")

        self.horizontalLayout_13.addWidget(self.comboBoxProfile)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.splitter_8.addWidget(self.frame_24)
        self.frame_25 = QFrame(self.splitter_8)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy3.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy3)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_25)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButtonClearConsole = QToolButton(self.frame_5)
        self.toolButtonClearConsole.setObjectName(u"toolButtonClearConsole")
        self.toolButtonClearConsole.setMinimumSize(QSize(25, 25))
        self.toolButtonClearConsole.setCheckable(False)

        self.verticalLayout_5.addWidget(self.toolButtonClearConsole)

        self.toolButtonConsoleScrollToEnd = QToolButton(self.frame_5)
        self.toolButtonConsoleScrollToEnd.setObjectName(u"toolButtonConsoleScrollToEnd")
        self.toolButtonConsoleScrollToEnd.setMinimumSize(QSize(25, 25))
        self.toolButtonConsoleScrollToEnd.setCheckable(True)
        self.toolButtonConsoleScrollToEnd.setChecked(True)

        self.verticalLayout_5.addWidget(self.toolButtonConsoleScrollToEnd)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_18.addWidget(self.frame_5)

        self.console = QPlainTextEdit(self.groupBox_4)
        self.console.setObjectName(u"console")
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(8)
        self.console.setFont(font)
        self.console.setReadOnly(True)
        self.console.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.console.setCenterOnScroll(False)

        self.horizontalLayout_18.addWidget(self.console)


        self.horizontalLayout_17.addWidget(self.groupBox_4)

        self.splitter_8.addWidget(self.frame_25)

        self.verticalLayout_6.addWidget(self.splitter_8)

        self.tabWidgetMain.addTab(self.tabWorkspace, "")
        self.tabProfile = QWidget()
        self.tabProfile.setObjectName(u"tabProfile")
        self.horizontalLayout_14 = QHBoxLayout(self.tabProfile)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.splitter_7 = QSplitter(self.tabProfile)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.frame_22 = QFrame(self.splitter_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(300, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_22)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_18 = QFrame(self.frame_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.toolButtonProfileAdd = QToolButton(self.frame_18)
        self.toolButtonProfileAdd.setObjectName(u"toolButtonProfileAdd")
        self.toolButtonProfileAdd.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.toolButtonProfileAdd)

        self.toolButtonProfileRemove = QToolButton(self.frame_18)
        self.toolButtonProfileRemove.setObjectName(u"toolButtonProfileRemove")
        self.toolButtonProfileRemove.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.toolButtonProfileRemove)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_18)

        self.splitter = QSplitter(self.frame_22)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.listViewProfile = QListView(self.splitter)
        self.listViewProfile.setObjectName(u"listViewProfile")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listViewProfile.sizePolicy().hasHeightForWidth())
        self.listViewProfile.setSizePolicy(sizePolicy4)
        self.splitter.addWidget(self.listViewProfile)

        self.verticalLayout_2.addWidget(self.splitter)

        self.pushButton = QPushButton(self.frame_22)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.splitter_7.addWidget(self.frame_22)
        self.frame_23 = QFrame(self.splitter_7)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_23)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.groupBox_2 = QGroupBox(self.frame_23)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.frame_20 = QFrame(self.groupBox_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 2, 2, 2)
        self.toolButtonProfileSettingsAdd = QToolButton(self.frame_20)
        self.toolButtonProfileSettingsAdd.setObjectName(u"toolButtonProfileSettingsAdd")
        self.toolButtonProfileSettingsAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileSettingsAdd.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.toolButtonProfileSettingsAdd)

        self.toolButtonProfileSettingsRemove = QToolButton(self.frame_20)
        self.toolButtonProfileSettingsRemove.setObjectName(u"toolButtonProfileSettingsRemove")
        self.toolButtonProfileSettingsRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileSettingsRemove.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.toolButtonProfileSettingsRemove)

        self.toolButtonProfileSettingsClear = QToolButton(self.frame_20)
        self.toolButtonProfileSettingsClear.setObjectName(u"toolButtonProfileSettingsClear")
        self.toolButtonProfileSettingsClear.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileSettingsClear.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_20.addWidget(self.toolButtonProfileSettingsClear)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.tableViewProfileSettings = QTableView(self.groupBox_2)
        self.tableViewProfileSettings.setObjectName(u"tableViewProfileSettings")

        self.verticalLayout_11.addWidget(self.tableViewProfileSettings)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_23)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.frame_27 = QFrame(self.groupBox_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setSpacing(2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 2, 2, 2)
        self.toolButtonProfileOptionsAdd = QToolButton(self.frame_27)
        self.toolButtonProfileOptionsAdd.setObjectName(u"toolButtonProfileOptionsAdd")
        self.toolButtonProfileOptionsAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileOptionsAdd.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButtonProfileOptionsAdd)

        self.toolButtonProfileOptionsRemove = QToolButton(self.frame_27)
        self.toolButtonProfileOptionsRemove.setObjectName(u"toolButtonProfileOptionsRemove")
        self.toolButtonProfileOptionsRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileOptionsRemove.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButtonProfileOptionsRemove)

        self.toolButtonProfileOptionsClear = QToolButton(self.frame_27)
        self.toolButtonProfileOptionsClear.setObjectName(u"toolButtonProfileOptionsClear")
        self.toolButtonProfileOptionsClear.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileOptionsClear.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_22.addWidget(self.toolButtonProfileOptionsClear)

        self.horizontalSpacer_5 = QSpacerItem(636, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)


        self.verticalLayout_15.addWidget(self.frame_27)

        self.tableViewProfileOptions = QTableView(self.groupBox_3)
        self.tableViewProfileOptions.setObjectName(u"tableViewProfileOptions")

        self.verticalLayout_15.addWidget(self.tableViewProfileOptions)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.frame_23)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.frame_28 = QFrame(self.groupBox_5)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setSpacing(2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 2, 2, 2)
        self.toolButtonProfileBuildReqsAdd = QToolButton(self.frame_28)
        self.toolButtonProfileBuildReqsAdd.setObjectName(u"toolButtonProfileBuildReqsAdd")
        self.toolButtonProfileBuildReqsAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileBuildReqsAdd.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_23.addWidget(self.toolButtonProfileBuildReqsAdd)

        self.toolButtonProfileBuildReqsRemove = QToolButton(self.frame_28)
        self.toolButtonProfileBuildReqsRemove.setObjectName(u"toolButtonProfileBuildReqsRemove")
        self.toolButtonProfileBuildReqsRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileBuildReqsRemove.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_23.addWidget(self.toolButtonProfileBuildReqsRemove)

        self.toolButtonProfileBuildReqsClear = QToolButton(self.frame_28)
        self.toolButtonProfileBuildReqsClear.setObjectName(u"toolButtonProfileBuildReqsClear")
        self.toolButtonProfileBuildReqsClear.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileBuildReqsClear.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_23.addWidget(self.toolButtonProfileBuildReqsClear)

        self.horizontalSpacer_6 = QSpacerItem(636, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_6)


        self.verticalLayout_16.addWidget(self.frame_28)

        self.tableViewProfileBuildRequires = QTableView(self.groupBox_5)
        self.tableViewProfileBuildRequires.setObjectName(u"tableViewProfileBuildRequires")

        self.verticalLayout_16.addWidget(self.tableViewProfileBuildRequires)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_23)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.frame_29 = QFrame(self.groupBox_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setSpacing(2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 2, 2, 2)
        self.toolButtonProfileEnvAdd = QToolButton(self.frame_29)
        self.toolButtonProfileEnvAdd.setObjectName(u"toolButtonProfileEnvAdd")
        self.toolButtonProfileEnvAdd.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileEnvAdd.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.toolButtonProfileEnvAdd)

        self.toolButtonProfileEnvRemove = QToolButton(self.frame_29)
        self.toolButtonProfileEnvRemove.setObjectName(u"toolButtonProfileEnvRemove")
        self.toolButtonProfileEnvRemove.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileEnvRemove.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.toolButtonProfileEnvRemove)

        self.toolButtonProfileEnvClear = QToolButton(self.frame_29)
        self.toolButtonProfileEnvClear.setObjectName(u"toolButtonProfileEnvClear")
        self.toolButtonProfileEnvClear.setMinimumSize(QSize(25, 25))
        self.toolButtonProfileEnvClear.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.toolButtonProfileEnvClear)

        self.horizontalSpacer_7 = QSpacerItem(636, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)


        self.verticalLayout_10.addWidget(self.frame_29)

        self.tableViewProfileEnvironment = QTableView(self.groupBox_6)
        self.tableViewProfileEnvironment.setObjectName(u"tableViewProfileEnvironment")

        self.verticalLayout_10.addWidget(self.tableViewProfileEnvironment)


        self.verticalLayout_9.addWidget(self.groupBox_6)

        self.splitter_7.addWidget(self.frame_23)

        self.horizontalLayout_14.addWidget(self.splitter_7)

        self.tabWidgetMain.addTab(self.tabProfile, "")
        self.tabRemote = QWidget()
        self.tabRemote.setObjectName(u"tabRemote")
        self.verticalLayout_4 = QVBoxLayout(self.tabRemote)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame_7 = QFrame(self.tabRemote)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_7)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(25, 25))
        self.toolButton.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_16.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy5)
        self.toolButton_2.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_16.addWidget(self.toolButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.tableViewRemoteList = QTableView(self.tabRemote)
        self.tableViewRemoteList.setObjectName(u"tableViewRemoteList")
        self.tableViewRemoteList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_4.addWidget(self.tableViewRemoteList)

        self.tabWidgetMain.addTab(self.tabRemote, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.tabWidgetMain.addTab(self.tabSettings, "")

        self.verticalLayout_12.addWidget(self.tabWidgetMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1071, 21))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuConan = QMenu(self.menubar)
        self.menuConan.setObjectName(u"menuConan")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy5.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy5)
        self.toolBar.setMinimumSize(QSize(0, 0))
        self.toolBar.setBaseSize(QSize(0, 50))
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(30, 30))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuConan.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuView.addAction(self.actionViewHome)
        self.menuView.addAction(self.actionViewPackage)
        self.menuView.addAction(self.actionViewWorkspace)
        self.menuView.addAction(self.actionViewProfile)
        self.menuView.addAction(self.actionViewRemote)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewSettings)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExit)
        self.menuHelp.addAction(self.actionHelpConanio)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelpAbout)
        self.menuConan.addAction(self.actionConanCreate)
        self.menuConan.addAction(self.actionConanInstall)
        self.menuConan.addAction(self.actionConanBuild)
        self.menuConan.addAction(self.actionConanSource)
        self.menuConan.addAction(self.actionConanPackage)
        self.menuConan.addAction(self.actionConanExport)
        self.menuConan.addAction(self.actionConanExportPackage)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConanCreate)
        self.toolBar.addAction(self.actionConanInstall)
        self.toolBar.addAction(self.actionConanBuild)
        self.toolBar.addAction(self.actionConanSource)
        self.toolBar.addAction(self.actionConanPackage)
        self.toolBar.addAction(self.actionConanExport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConanExportPackage)

        self.retranslateUi(MainWindow)
        self.actionFileExit.triggered.connect(MainWindow.close)
        self.toolButtonClearConsole.pressed.connect(self.console.clear)

        self.tabWidgetMain.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conan GUIde", None))
        self.actionViewProfile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
#if QT_CONFIG(shortcut)
        self.actionViewProfile.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionFileExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.actionConanCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.actionConanInstall.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionConanBuild.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.actionConanSource.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.actionConanPackage.setText(QCoreApplication.translate("MainWindow", u"Package", None))
        self.actionConanExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionConanExportPackage.setText(QCoreApplication.translate("MainWindow", u"Export Package", None))
        self.actionViewPackage.setText(QCoreApplication.translate("MainWindow", u"Package", None))
#if QT_CONFIG(tooltip)
        self.actionViewPackage.setToolTip(QCoreApplication.translate("MainWindow", u"Package", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionViewPackage.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelpConanio.setText(QCoreApplication.translate("MainWindow", u"conan.io", None))
        self.actionHelpAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionViewHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(shortcut)
        self.actionViewHome.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionViewWorkspace.setText(QCoreApplication.translate("MainWindow", u"Workspace", None))
#if QT_CONFIG(shortcut)
        self.actionViewWorkspace.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionViewRemote.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
#if QT_CONFIG(shortcut)
        self.actionViewRemote.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionViewSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionViewSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabHome), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Double Click", None))
        self.checkBoxOpenExplorer.setText(QCoreApplication.translate("MainWindow", u"Open Explorer", None))
        self.checkBoxCopyClipboard.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Local Cache", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cache Path", None))
        self.btnCopyCachePath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenCachePath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Data Path", None))
        self.btnCopyDataPath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenDataPath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Real Path", None))
        self.btnCopyRealPath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenRealPath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Package Path", None))
        self.btnCopyPackagePath.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.btnOpenPackagePath.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dependencies Graph", None))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabPackage), QCoreApplication.translate("MainWindow", u"Package", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recipe Path", None))
        self.toolBtnExplorerRecipePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Install Path", None))
        self.toolBtnExplorerInstallPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Build Path", None))
        self.toolBtnExplorerBuildPath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Source Path", None))
        self.toolBtnExplorerSourcePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Package Path", None))
        self.toolBtnExplorerPackagePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Console", None))
        self.toolButtonClearConsole.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.toolButtonConsoleScrollToEnd.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.console.setPlainText("")
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabWorkspace), QCoreApplication.translate("MainWindow", u"Workspace", None))
        self.toolButtonProfileAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButtonProfileRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SET", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.toolButtonProfileSettingsAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButtonProfileSettingsRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolButtonProfileSettingsClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.toolButtonProfileOptionsAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButtonProfileOptionsRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolButtonProfileOptionsClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Build Requires", None))
        self.toolButtonProfileBuildReqsAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButtonProfileBuildReqsRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolButtonProfileBuildReqsClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Environment", None))
        self.toolButtonProfileEnvAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButtonProfileEnvRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolButtonProfileEnvClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabProfile), QCoreApplication.translate("MainWindow", u"Profile", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabRemote), QCoreApplication.translate("MainWindow", u"Remote", None))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuConan.setTitle(QCoreApplication.translate("MainWindow", u"Conan", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

