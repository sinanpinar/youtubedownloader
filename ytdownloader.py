from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
import requests 
import sys
from mainwindow import Ui_MainWindow
from pytube import YouTube


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.yt=None
        self.setWindowIcon(QIcon("downloads.ico"))
        self.setWindowTitle("Youtube Downloader")

        self.ui.btnBul.clicked.connect(self.videoGet)
        self.ui.btnTemizle.clicked.connect(self.windowClear)
        self.ui.btnIndir.clicked.connect(self.videoDownload)

    def videoGet(self):
        
        self.ui.btnBul.setEnabled(False)
        self.ui.btnTemizle.setEnabled(True)
        self.ui.btnIndir.setEnabled(True)
        self.ui.cbxStreams.setVisible(True)
        self.ui.btnIndir.setVisible(True)

        link = self.ui.tbxLink.text()

        try:
            self.yt=YouTube(link)
        except:
            return False
        finally:

            vTitle=self.yt.title
            self.downloadImage(self.yt.thumbnail_url)
            self.ui.labelimg.setPixmap(QPixmap("videoImage.jpg"))

            for i in self.yt.streams:
                if(i.type=="video"):
                    item = f"itag:{i.itag} mime_type:{i.mime_type} resolution:{i.resolution} fps:{i.fps} type:{i.type}" 
                else:
                    item = f"itag:{i.itag} mime_type:{i.mime_type} abr:{i.abr} type:{i.type}" 
                self.ui.cbxStreams.addItem(item)
            self.ui.lblVideoTitle.setText(vTitle)

    def downloadImage(self,url):
        response = requests.get(url)
        with open("videoImage.jpg","wb") as file:
            file.write(response.content)

    def windowClear(self):
        self.ui.btnBul.setEnabled(True)
        self.ui.btnTemizle.setEnabled(False)
        self.ui.btnIndir.setEnabled(False)
        self.ui.tbxLink.setText("")
        self.ui.lblVideoTitle.setText("")
        self.ui.labelimg.setPixmap(QPixmap())
        self.ui.cbxStreams.clear()
        self.ui.cbxStreams.setVisible(False)
        self.ui.btnIndir.setVisible(False)

    def videoDownload(self):
        index=self.ui.cbxStreams.currentIndex()
        streamtext=self.yt.streams[index]
        stream=self.yt.streams.get_by_itag(int(streamtext.itag))
        stream.download()

        msg=QtWidgets.QMessageBox()
        msg.setText("Video İndirildi")
        x=msg.exec_()

        self.tbxTemizle()

def main():
    app=QtWidgets.QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

main()


