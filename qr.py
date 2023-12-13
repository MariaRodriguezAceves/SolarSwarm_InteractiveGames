#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import cv2
from pyzbar import pyzbar

from sys import argv
#from solarswarm.srv import TakeSnapshot
import aspose.barcode as barcode
from math import radians

def takesnapshot():
    #imgID=1
    return imgID

class PoseSetter:
    def __init__(self):
        self.pose = Pose()

    def setPose(self,msg:Pose):
        self.pose = msg

if __name__=='__main__':
    
    
    rospy.init_node("test_node")
    
    image=cv2.imread("imgID.png")
    qr=pyzbar.decode(image)
    
    data=qr[0].data.decode()
    pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate=rospy.Rate(2)
    posesetter:Pose = PoseSetter()
    end=0
    i0=0
    i1=0
    i2=0
    i6=0
    i7=0
    i10=0
    listener = rospy.Subscriber("/turtle1/pose",Pose,posesetter.setPose)
    w=0
    while not rospy.is_shutdown() & w==0:
        msg=Twist()
        
        if data=="Fahren": # x fahren 
            if i0==0: 
                start=time.time()
                i0=1    
            msg.linear.x=0.5
                
            if end-start>6: #6
                msg.linear.x=0
                break
            end=time.time()
        
        elif data=="Links drehen": # links 90º drehen
            if i1==0: 
                start=time.time()
                i1=1    
            msg.angular.z=0.2
                
            if end-start>7:#7 s
                msg.angular.z=0
                break
            end=time.time()

        elif data=="Kehrtwende rechts": #kehrtwende nach recht
            if i2==0: 
                start=time.time()
                i2=1    
            msg.angular.z=-0.2
            msg.linear.x=0.2
            #if end-start>6.85:#7 s
            if posesetter.pose.theta<-1.55:
                msg.angular.z=0.0
                msg.linear.x=0.0
                break
            end=time.time()
 

        elif data=="Kehrtwende": #Kehrtwende nach links 
            if i6==0: 
                start=time.time()
                i6=1    
            msg.angular.z=0.4
            msg.linear.x=0.3
            
            if end-start>7.3: #7.2
                msg.linear.x=0
                msg.angular.z=0 
                break   
            end=time.time()

        elif data=="Rechts drehen": # rechts 90º drehen
            if i7==0: 
                start=time.time()
                i7=1    
            msg.angular.z=-0.25
                
            if end-start>5.5:# s
                msg.angular.z=0
                break
            end=time.time() 

        elif data=="Wenig fahren": # x kurz fahren 
            if i10==0: 
                start=time.time()
                i10=1    
            msg.linear.x=0.5
                
            if end-start>3: #3
                msg.linear.x=0
                break
            end=time.time()         
        
        rospy.loginfo(data)
        pub.publish(msg)
        rate.sleep()

