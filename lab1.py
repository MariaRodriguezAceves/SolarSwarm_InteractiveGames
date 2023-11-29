#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time

#from solarswarm.srv import TakeSnapshot

from math import radians

def takesnapshot():
    imgID=1
    return imgID

class PoseSetter:
    def __init__(self):
        self.pose = Pose()

    def setPose(self,msg:Pose):
        self.pose = msg

if __name__=='__main__':
    rospy.init_node("test_node")
    
    pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate=rospy.Rate(2)
    posesetter:Pose = PoseSetter()
    end=0
    i0=0
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    i10=0
    i=0
    listener = rospy.Subscriber("/turtle1/pose",Pose,posesetter.setPose)
    while not rospy.is_shutdown():
        msg=Twist()
        p0 = posesetter.pose
        spd=0.2
        aspd=0.2
        #print(p0)
        if i==0 or i==5 or i==8: # x fahren 
            if i0==0: 
                start=time.time()
                i0=1    
            msg.linear.x=spd#0.5
                
            if end-start>1: #6
                msg.linear.x=0
                if i==8:
                    i7=0
                i=i+1
                
            end=time.time()
            
        elif i==1 or i==4 or i==11: # links 90º drehen
            if i1==0: 
                start=time.time()
                i1=1    
            msg.angular.z=aspd
                
            if end-start>7:#7 s
                msg.angular.z=0
                if i==4:
                    i0=0
                if i==11:
                    i10=0
                i=i+1
            end=time.time()

        elif i==2: #kehrtwende nach recht
            if i2==0: 
                start=time.time()
                i2=1    
            msg.angular.z=-aspd
            msg.linear.x=spd
            #if end-start>6.85:#7 s
            if posesetter.pose.theta<-1.55:
                msg.angular.z=0.0
                msg.linear.x=0.0
                i=i+1
            end=time.time()
        
        elif i==3: # -y fahren 
            if i3==0: 
                start=time.time()
                i3=1    
            
            msg.linear.x=spd
            
            if end-start>1: #6
                msg.linear.x=0
                
                i=i+1
                i1=0
            end=time.time()

        elif i==6: #Kehrtwende nach links 
            if i6==0: 
                start=time.time()
                i6=1    
            msg.angular.z=aspd #0.4
            msg.linear.x=spd #0.3
            
            if end-start>7.3: #7.2
                msg.linear.x=0
                msg.angular.z=0
                i=i+1           
            end=time.time()

        elif i==7 or i==9 or i==13: # rechts 90º drehen
            if i7==0: 
                start=time.time()
                i7=1    
            msg.angular.z=-aspd#0.25
                
            if end-start>5:# 5.5s
                msg.angular.z=0
                if i==7 or i==9:
                    i0=0
                if i==13:
                    i10=0
                i=i+1
            end=time.time() 

        elif i==10 or i==12 or i==14: # x kurz fahren 
            if i10==0: 
                start=time.time()
                i10=1    
            msg.linear.x=spd#0.5
            if end-start>1: #3
                msg.linear.x=0
                if i==10:
                    i1=0
                if i==12:
                    i7=0
                i=i+1
            end=time.time()         
  
        rospy.loginfo(p0)
        pub.publish(msg)
        rate.sleep()
        