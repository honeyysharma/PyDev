#Simple example of QProgressBar and QThread

import sys
from PyQt4 import QtCore, QtGui
import time

class MyCustomWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)
        layout = QtGui.QVBoxLayout(self)       

        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setRange(0,100)
        button = QtGui.QPushButton("Stop", self)
        layout.addWidget(self.progressBar)
        layout.addWidget(button)

        button.clicked.connect(self.onStart)

        self.myLongTask = TaskThread()
        self.myLongTask.notifyProgress.connect(self.onProgress)
        self.myLongTask.start()


    def onStart(self):
        self.myLongTask.stop()
        self.close()

    def onProgress(self, i):
        self.progressBar.setValue(i)
        if self.progressBar.value() >= self.progressBar.maximum():
            self.close()


class TaskThread(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(TaskThread, self).__init__(parent)
        self.stopFlag = False
    
    def __del__(self):
        self.quit()
        self.wait()
        
    def stop(self):
        self.stopFlag = True
        
    def run(self):
        for i in range(101):
            if self.stopFlag:
                self.stopFlag = False
                break
            else:
                self.notifyProgress.emit(i)
                time.sleep(0.1)

if __name__ == __main__:
  test = MyCustomWidget()
  test.show()
