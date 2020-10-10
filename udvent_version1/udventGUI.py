from udvent import *
from settingForm import *
import random
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import sys
from collections import deque
    

class GUI(QtWidgets.QMainWindow,Ui_Ventilator):
    def __init__(self,parent=None):
        super(GUI,self).__init__(parent)
        self.setupUi(self);
        self.d=deque()
        self.customCodes()
        

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.plotGraph)
        self.timer.start()
        
        
    def customCodes(self):
        self.ecGraph.setBackground((42, 42, 42))
        self.pGraph.setBackground((42, 42, 42))
        self.frGraph.setBackground((42, 42, 42))
        self.tvGraph.setBackground((42, 42, 42))
        self.setting.clicked.connect(self.settingWindow)
        pen = pg.mkPen(color=(255, 0, 0))
        #self.curve = self.pGraph.plot( self.y, pen=pen)

        
        
    def HideWidgets(self):
        self.ecGraph.hide()
        
    def settingWindow(self):
        self.setting=settingForm()
        self.setting.show()
        
    def plotGraph(self):
        if len(self.d)>20:
           self.d.popleft()
        self.d.append(random.randint(0,5))
        print(self.d)
        #self.curve.setData( self.d)

        
        
        
        
        
        

def main():
    app=QtWidgets.QApplication(sys.argv)
    form=GUI()
    form.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
