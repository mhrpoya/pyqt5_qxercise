from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("Kari.ui", self)
        self.show()

        self.addbtn.clicked.connect(self.add)
        self.donebtn.clicked.connect(self.done)
        self.clearbtn.clicked.connect(self.clear)


    def add(self):
        if self.nameline.text() and self.ageline.text() and self.jobline.text():
            str_ = self.nameline.text() + " " + self.ageline.text() + " " + self.jobline.text()
            self.joblineEdit.addItem(str_)
            self.nameline.setText("")
            self.ageline.setText("")
            self.jobline.setText("")
            self.nameline.setFocus()
            self.ageline.setFocus()
            self.jobline.setFocus()


    def done(self):
        click_index = self.joblineEdit.currentRow()
        self.joblineEdit.takeItem(click_index)

    
    def clear(self):
        self.joblineEdit.clear()



app = QtWidgets.QApplication(sys.argv)
win = Ui()
app.exec_()