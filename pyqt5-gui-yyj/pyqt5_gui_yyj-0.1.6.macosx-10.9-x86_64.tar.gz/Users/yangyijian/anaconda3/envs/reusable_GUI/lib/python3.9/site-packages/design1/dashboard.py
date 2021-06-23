
import sys, os, time, threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation,QRect,Qt, QParallelAnimationGroup
from PyQt5.QtGui import QColor
from ui_Dashboard import Ui_MainWindow
from multiprocessing import Process
import pyqtgraph as pg

class Dashboard(Ui_MainWindow, QMainWindow):
 
    def __init__(self):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        # self.setFixedSize(self.width(), self.height())

        # self.setWindowOpacity(0.5) # 设置窗口透明度（包括所有控件）
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框（上面的标题，缩小，关闭按钮）
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明, 
        '''出现UpdateLayeredWindowIndirect failed for ptDst'''
        self.pushButton.clicked.connect(self.mini)
        self.pushButton_14.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.menu)
        self.pushButton_7.clicked.connect(self.menu)
        self.pushButton_6.clicked.connect(self.chart)
        self.pushButton_8.clicked.connect(self.chart)
        self.pushButton_3.clicked.connect(self.forum)
        self.pushButton_9.clicked.connect(self.forum)
        self.pushButton_4.clicked.connect(self.profile)
        self.pushButton_10.clicked.connect(self.profile)
        self.pushButton_5.clicked.connect(self.settings)
        self.pushButton_11.clicked.connect(self.settings)

        self.widget_16.hide()
        self.pushButton_15.hide()
        self.hamburger_init()   #初始化导航栏抽屉动画
        self.pushButton_12.clicked.connect(self.hamburger)    #利用Qthread（不利用了。。。GUI动作必须在GUI主线程里）


        # self.menubar.hide()
        # self.statusbar.hide()     #已直接在qt designer中移除
        # self.lineEdit_4.setAttribute(Qt.WA_MacShowFocusRect, 0)     #MAC下去掉奇怪的东西
        # self.stackedWidget.setAttribute(Qt.WA_MacShowFocusRect, 0)     #MAC下去掉奇怪的东西

        #阴影效果
        self.add_shadow()

        #pyqt plots
        self.plots()

        self.m_flag=False

    #实现窗口移动
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(Qt.OpenHandCursor)  #更改鼠标图标
        
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(Qt.ArrowCursor)
        
    # def hamburgerThread(self):
    #     # Thread = threading.Thread(target=self.hamburger,args=(1,))
    #     self.hamburger_Thread.start()
    #     self.hamburger_Thread.terminate()

    def hamburger_init(self):
        self.hamburger_state=0
        # self.hamburger_Thread=hamburgerThread(self)
        self.anim = QPropertyAnimation(self.label_4, b"geometry")
        self.anim.setDuration(20)
        self.anim.setStartValue(QRect(20, 30, 35, 35))
        self.anim.setEndValue(QRect(0, 30, 35, 35))

        self.anim2 = QPropertyAnimation(self.navigation, b"geometry")
        self.anim2.setDuration(20)
        self.anim2.setStartValue(QRect(0, 90, 171, 552))
        self.anim2.setEndValue(QRect(0, 90, 41, 552))

        self.anim3 = QPropertyAnimation(self.pushButton_12, b"geometry")
        self.anim3.setDuration(20)
        self.anim3.setStartValue(QRect(120, 10, 37, 33))
        self.anim3.setEndValue(QRect(0, 10, 37, 33))
        
        self.anim4 = QPropertyAnimation(self.widget_2, b"geometry")
        self.anim4.setDuration(20)
        self.anim4.setStartValue(QRect(0, 0, 171, 91))
        self.anim4.setEndValue(QRect(0, 0, 41, 91))

        self.anim5 = QPropertyAnimation(self.stackedWidget, b"geometry")
        self.anim5.setDuration(20)
        self.anim5.setStartValue(QRect(171, 44, 801, 595))
        self.anim5.setEndValue(QRect(41, 44, 931, 595))


        self.anim6 = QPropertyAnimation(self.widget_15, b"geometry")    #搜索区
        self.anim6.setDuration(20)
        self.anim6.setStartValue(QRect(172,0,721,40))
        self.anim6.setEndValue(QRect(41, 0, 850, 40))

        self.anim7 = QPropertyAnimation(self.label_4, b"geometry")
        self.anim7.setDuration(20)
        self.anim7.setStartValue(QRect(0, 30, 35, 35))
        self.anim7.setEndValue(QRect(20, 30, 35, 35))

        self.anim8 = QPropertyAnimation(self.navigation, b"geometry")
        self.anim8.setDuration(20)
        self.anim8.setStartValue(QRect(0, 90, 41, 552))
        self.anim8.setEndValue(QRect(0, 90, 171, 552))

        self.anim9 = QPropertyAnimation(self.pushButton_12, b"geometry")
        self.anim9.setDuration(20)
        self.anim9.setStartValue(QRect(0, 10, 37, 33))
        self.anim9.setEndValue(QRect(120, 10, 37, 33))
        
        self.anim10 = QPropertyAnimation(self.widget_2, b"geometry")
        self.anim10.setDuration(20)
        self.anim10.setStartValue(QRect(0, 0, 41, 91))
        self.anim10.setEndValue(QRect(0, 0, 171, 91))

        self.anim11 = QPropertyAnimation(self.stackedWidget, b"geometry")
        self.anim11.setDuration(20)
        self.anim11.setStartValue(QRect(41, 44, 931, 595))
        self.anim11.setEndValue(QRect(171, 44, 801, 595))

        self.anim12 = QPropertyAnimation(self.widget_15, b"geometry") #搜索框
        self.anim12.setDuration(20)
        self.anim12.setStartValue(QRect(41, 0, 850, 40))
        self.anim12.setEndValue(QRect(172,0,721,40))
        self.animGroup1=QParallelAnimationGroup(self)
        self.animGroup2=QParallelAnimationGroup(self)
        self.animGroup1.addAnimation(self.anim)
        self.animGroup1.addAnimation(self.anim2)
        self.animGroup1.addAnimation(self.anim3)
        self.animGroup1.addAnimation(self.anim4)
        self.animGroup1.addAnimation(self.anim5)
        self.animGroup1.addAnimation(self.anim6)
        self.animGroup2.addAnimation(self.anim7)
        self.animGroup2.addAnimation(self.anim8)
        self.animGroup2.addAnimation(self.anim9)
        self.animGroup2.addAnimation(self.anim10)
        self.animGroup2.addAnimation(self.anim11)
        self.animGroup2.addAnimation(self.anim12)
        
        # self.hamburgerThread()      #先运行一次克服了第一次点不灵且初始化为栏收缩



    def hamburger(self):   #实现导航栏缩放

        if self.hamburger_state==0:
            self.hamburger_state=1
            self.animGroup1.start()     #加了thread下面要反过来，可能是Qthread和animation冲突(不用了)
            # time.sleep(1)
            self.widget.hide()
            self.pushButton_13.hide()
            self.widget_16.show()
            self.pushButton_15.show()
            # self.widget_16.hide()
            # self.pushButton_15.hide()
            # self.widget.show()
            # self.pushButton_13.show()


        else:
            self.hamburger_state=0
            self.animGroup2.start()
            # time.sleep(1)
            self.widget_16.hide()
            self.pushButton_15.hide()
            self.widget.show()
            self.pushButton_13.show()
            # self.widget.hide()
            # self.pushButton_13.hide()
            # self.widget_16.show()
            # self.pushButton_15.show()

    def add_shadow(self):       #   必须要在function里
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(4,4) # 偏移
        self.effect_shadow.setBlurRadius(20) # 阴影半径
        self.effect_shadow.setColor(QColor(0,0,0,100)) # 阴影颜色
        self.setGraphicsEffect(self.effect_shadow) # 将设置套用到widget窗口中,导致抽屉栏收放卡顿

    def menu(self):
        self.pushButton_2.setChecked(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_5.setChecked(False)
        #       小icon
        self.pushButton_7.setChecked(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.stackedWidget.setCurrentIndex(0)
    def chart(self):
        self.pushButton_2.setChecked(False)
        self.pushButton_6.setChecked(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_5.setChecked(False)
       #       小icon
        self.pushButton_7.setChecked(False)
        self.pushButton_8.setChecked(True)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.stackedWidget.setCurrentIndex(1)
    def forum(self):
        self.pushButton_2.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_3.setChecked(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_5.setChecked(False)
       #       小icon
        self.pushButton_7.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_9.setChecked(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_11.setChecked(False)

        self.stackedWidget.setCurrentIndex(2)
    def profile(self):
        self.pushButton_2.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(True)
        self.pushButton_5.setChecked(False)
       #       小icon
        self.pushButton_7.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(True)
        self.pushButton_11.setChecked(False)
        self.stackedWidget.setCurrentIndex(3)
    def settings(self):
        self.pushButton_2.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_5.setChecked(True)
       #       小icon
        self.pushButton_7.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_11.setChecked(True)
        self.stackedWidget.setCurrentIndex(4)

    
    def exit(self):         #退出
        # def Thread():
        #     for i in reversed(range(0, 11)):
        #         self.setWindowOpacity(i / 10)
        #         time.sleep(0.03)                    #渐渐隐去效果
        # Thread = threading.Thread(target=Thread)
        # Thread.start()
        for i in reversed(range(0, 11)):
            self.setWindowOpacity(i / 10)
            time.sleep(0.03)     
        # time.sleep(0.3)
        os._exit(-1) #放在thread里会出现warning：Timers cannot be stopped from another thread


    def mini(self):
        # self.showMinimized()
        #上面mac风格,下面window风格
        # def Thread():
        #     for i in reversed(range(0, 11)):
        #         self.setWindowOpacity(i / 10)
        #         time.sleep(0.03)                    #渐渐隐去效果
        #     self.showMinimized()
        #     self.setWindowOpacity(1)
        # Thread = threading.Thread(target=Thread)
        # Thread.start()
        for i in reversed(range(0, 11)):
            self.setWindowOpacity(i / 10)
            time.sleep(0.03)                    #渐渐隐去效果
        self.showMinimized()
        self.setWindowOpacity(1)

    def plots(self):
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.widget_13.setTitle("气温趋势",color='008080',size='12pt')

        # 设置上下左右的label
        self.widget_13.setLabel("left","气温(摄氏度)")
        self.widget_13.setLabel("bottom","时间")
        self.widget_13.setBackground('w')
        self.widget_13.plot(hour, temperature, pen=pg.mkPen('b',width=6) # 线条颜色
                            )  #widget_13已在designer中提升为pyqtgraph中的plot_widget



# class hamburgerThread(QThread):

#     def __init__(self, dashboard):
#         super().__init__()
#         self.dashboard=dashboard

#     def run(self):
#         self.dashboard.hamburger()
 
def main():
    # print(os.getcwd())
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) #导致界面出现在最顶上
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()


def test():
    print(1)
