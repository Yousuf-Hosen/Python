""" my ncamera application
author: Yousuf hasan akash
 """
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage,QIcon
from PyQt5.QtCore import QTimer
import cv2
import datetime
""" main app windows """
class window(QWidget):
    def __init__(self):
        super().__init__()
        # variables for windows
        self.window_width=640
        self.window_height=400
        # image variables 
        self.img_width=640
        self.img_height=400

        # other variables
        self.dt='0-0-0'
        self.record_flag=False                                                


        #load image icon 
        self.camera_icon=QIcon(cap_icon_path)

        # load record icon
        self.rec_icon=QIcon(rec_icon_path)

        # load stop icon
        self.stop_icon=QIcon(stop_icon_path)

        self.fourcc=cv2.VideoWriter_fourcc(*'XVID')


        # setup the windows
        self.setWindowTitle("my camera app")
        self.setGeometry(100,100,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)

        # setup timer
        self.timer=QTimer()
        self.timer.timeout.connect(self.Update)
        self.ui()

      
    def ui(self):
        """ contains all UI thing """
        
        # layout of icon
        grid=QGridLayout()
        self.setLayout(grid)




        #image level
        self.image_level=QLabel(self)
        self.image_level.setGeometry(0,0,self.img_width,self.img_height)
        # Add capture button 
        self.capture_btn=QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius:30;border:2px solid black;border width:3px")
        self.capture_btn.setFixedSize(60,60)
        self.capture_btn.clicked.connect(self.save_image)

        # Add record botton
        self.rec_btn=QPushButton(self)
        # self.rec_btn.setIcon(self.rec_icon)
        self.rec_btn.setStyleSheet("border-radius:30;border:2px solid black;border width:3px")
        self.rec_btn.setFixedSize(60,60)
        self.rec_btn.clicked.connect(self.record)
    



        if not self.timer.isActive():
            self.cap=cv2.VideoCapture(0)
            self.timer.start(20)
        
     # add thing to the layout
        grid.addWidget(self.capture_btn,0,0)
        grid.addWidget(self.image_level,0,1,2,3)
        grid.addWidget(self.rec_btn,1,0)
        

        self.show()

    def Update(self):
        """ Update frame """
        _,self.frame=self.cap.read()
        if self.record_flag==True:
            self.rec_btn.setIcon(self.stop_icon)
            self.frame=cv2.circle(self.frame,(20,70),5,(0,0,255),10)
        else:
            self.rec_btn.setIcon(self.rec_icon)
            


        frame=cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB) # BLUE GREEN RED -> RGB
        height,width,channel=frame.shape
        step=channel *     width
        q_frame=QImage(frame.data,width,height,step,QImage.Format_RGB888)
        self.image_level.setPixmap(QPixmap.fromImage(q_frame))
    def save_image(self):
        """ save image from camera """
        print(" Saving image .....")
        self.get_time() # call the get_time method
        cv2.imwrite(f"{self.dt}.jpg",self.frame)


    def record(self):
        """ record vedio from camrea """
        print(self.record_flag)
        if self.record_flag==True:
            self.record_flag=False
            
        else:
            self.record_flag=True
            self.get_time()
            self.out=cv2.VideoWriter(f"{self.dt}.avi",self.fourcc,20.0,(self.img_height,self.img_width))
             

    def get_time(self):
        now=datetime.datetime.now()
        self.dt=now.strftime("%m-%d-%y,%H-%M-%S")
        print(self.dt)
#run
cap_icon_path='asset/capture.png'
rec_icon_path='asset/video-camera.png'
stop_icon_path='asset/stop-button.png'
app=QApplication(sys.argv)
win=window()
sys.exit(app.exec_())
