from PyQt5.QtWidgets import QFileDialog, QMessageBox

from Interface import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
from efficientNetClassify import predict
class InterfaceProcess(qtw.QWidget):
    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.fileFinder.clicked.connect(lambda:self.addImage())
        self.ui.imageProcessor.clicked.connect(lambda:self.processImage())


    def  addImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)
        if fileName:
            self.ui.image_explorer.setText(fileName)
            self.ui.imageWindow.setPixmap(QtGui.QPixmap(fileName))

#Edit This method
    def processImage(self):
        image_location=self.ui.image_explorer.text()
        if image_location!="":
            #retrieve your array
            percentage_array=predict(image_location)[0]
            # percentage_array=(45,50,12,32)
            self.ui.progressBar.setValue(percentage_array[0])
            self.ui.progressBar_2.setValue(percentage_array[1])
            self.ui.progressBar_3.setValue(percentage_array[2])
            self.ui.progressBar_4.setValue(percentage_array[3])
        else:
            qtw.QMessageBox.critical(self,"Fail","Select Image First")

if __name__ == "__main__":
    app=qtw.QApplication([])
    widget=InterfaceProcess()
    widget.show()
    sys.exit(app.exec_())
