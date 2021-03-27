from PyQt5.QtWidgets import QFileDialog, QMessageBox
import argparse

# from Interface import Ui_MainWindow
from InterfaceNew import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
from efficientNetClassify import predict
from efficientNetClassify import PredictReponse

args=None
class InterfaceProcess(qtw.QMainWindow):
    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.fileFinder.clicked.connect(lambda: self.addImage())
        self.ui.imageProcessor.clicked.connect(lambda: self.processImage())

    def addImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_3.setValue(0)
        self.ui.progressBar_4.setValue(0)
        if(args.c == 3):
            self.ui.progressBar_9.hide()
        self.ui.progressBar_9.setValue(0)
        self.ui.imageWindow.setPixmap(QtGui.QPixmap(QtGui.QPixmap()))
        self.ui.pushButton_2.setStyleSheet(
            "background-color: rgb(41.2%, 41.2%, 41.2%);")
        self.ui.pushButton.setStyleSheet(
            "background-color: rgb(41.2%, 41.2%, 41.2%);")
        if fileName:
            if fileName.endswith(".jpeg") or fileName.endswith(".jpg"):
                self.ui.image_explorer.setText(fileName)
                self.ui.imageWindow.setPixmap(QtGui.QPixmap(fileName))
            else:
                qtw.QMessageBox.critical(
                    self, "Fail", "Only JPEG images are supported")

# Edit This method
    def processImage(self):
        image_location = self.ui.image_explorer.text()
        if image_location != "":
            if image_location.endswith(".jpeg") or image_location.endswith(".jpg"):
                predictedResults = predict(image_location)
                percentage_array = predictedResults.multiClassArray
                binary_percentage_array = predictedResults.binaryArray
                if(binary_percentage_array < 50):
                    self.ui.pushButton_2.setStyleSheet(
                        "background-color: rgb(4.6%, 51.9%, 4.6%);")
                else:
                    self.ui.pushButton.setStyleSheet(
                        "background-color: rgb(54.5%, 0%, 0%);")
                # percentage_array=(45,50,12,32)
                self.ui.progressBar.setValue(percentage_array[0])
                self.ui.progressBar_2.setValue(percentage_array[1])
                self.ui.progressBar_3.setValue(percentage_array[2])
                if(3 in percentage_array):
                    self.ui.progressBar_4.setValue(percentage_array[3])
                else:
                    self.ui.progressBar_3.setValue(percentage_array[2])
                self.ui.progressBar_9.setValue(binary_percentage_array[0])
            else:
                qtw.QMessageBox.critical(
                    self, "Fail", "Image Format is Invalud")
        else:
            qtw.QMessageBox.critical(self, "Fail", "Select Image First")


if __name__ == "__main__":
    print("argsiit: ",args)
    parser = argparse.ArgumentParser(description='JImage Steganalyzer')
    parser.add_argument('--c', metavar='N', type=int,
                    help='number of classes')

    args = parser.parse_args()
    print("args: ",args.c)
    app = qtw.QApplication([])
    widget = InterfaceProcess()
    widget.show()
    sys.exit(app.exec_())
