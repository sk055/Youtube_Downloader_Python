import pytube
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_YoutubeVideoDownloader(QtWidgets.QMainWindow):
    def setupUi(self, YoutubeVideoDownloader):
        YoutubeVideoDownloader.setObjectName("YoutubeVideoDownloader")
        YoutubeVideoDownloader.resize(682, 434)
        YoutubeVideoDownloader.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(YoutubeVideoDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(440, 300, 221, 61))
        self.Download.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 20pt \"Berlin Sans FB\";\n"
"color: rgb(0, 0, 255);")
        self.Download.setObjectName("Download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 170, 121, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 20pt \"Berlin Sans FB\";\n"
"")
        self.label.setObjectName("label")
        self.Url = QtWidgets.QLineEdit(self.centralwidget)
        self.Url.setGeometry(QtCore.QRect(220, 170, 381, 41))
        self.Url.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font:14pt \"Berlin Sans FB\";\n"
"color: rgb(255, 85, 0);")
        self.Url.setText("")
        self.Url.setObjectName("Url")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 581, 51))
        self.label_2.setStyleSheet("\n"
"font: 36pt \"Berlin Sans FB\";\n"
"color: rgb(255, 255, 127);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 350, 351, 31))
        self.label_3.setStyleSheet("color: rgb(255, 85, 0);\n"
"font: 20pt \"Berlin Sans FB\";\n"
"")
        self.label_3.setObjectName("label_3")
        YoutubeVideoDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YoutubeVideoDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        YoutubeVideoDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YoutubeVideoDownloader)
        self.statusbar.setObjectName("statusbar")
        YoutubeVideoDownloader.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(YoutubeVideoDownloader)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(YoutubeVideoDownloader)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(YoutubeVideoDownloader)
        QtCore.QMetaObject.connectSlotsByName(YoutubeVideoDownloader)

    def retranslateUi(self, YoutubeVideoDownloader):
        _translate = QtCore.QCoreApplication.translate
        YoutubeVideoDownloader.setWindowTitle(_translate("YoutubeVideoDownloader", "YouTube Video Downloader"))
        self.Download.setText(_translate("YoutubeVideoDownloader", "Download Video"))
        self.label.setText(_translate("YoutubeVideoDownloader", "Enter Url"))
        self.label_2.setText(_translate("YoutubeVideoDownloader", "Youtube Video Downloader"))
        self.label_3.setText(_translate("YoutubeVideoDownloader", "Designed by : Sagar Kaushik"))
        self.menuFile.setTitle(_translate("YoutubeVideoDownloader", "File"))
        self.actionAbout.setText(_translate("YoutubeVideoDownloader", "About"))
        self.actionQuit.setText(_translate("YoutubeVideoDownloader", "Quit"))

        self.Download.clicked.connect(self.download)

    def download(self):

        try:
            video_url = self.Url.text()

        except ValueError:
            QMessageBox.about(self, "Error", "Please enter a correct Url...")

        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()

        video.download()

        choice = QtWidgets.QMessageBox.question(self, 'Download Completed..', 'Do you want to download another video??',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            self.Url.setText("")
        else:
            QtCore.QCoreApplication.instance().quit()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoutubeVideoDownloader = QtWidgets.QMainWindow()
    ui = Ui_YoutubeVideoDownloader()
    ui.setupUi(YoutubeVideoDownloader)
    YoutubeVideoDownloader.show()
    sys.exit(app.exec_())
