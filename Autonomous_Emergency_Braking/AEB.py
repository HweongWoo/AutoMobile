import os
import numpy as np
import sys
import cv2
import threading
import time
sys.path.insert(0, os.path.abspath('..'))
from vehicle_control.rc_car_control import RCCarControl
import LineChangeAssistSystem


EPS = 0.00001
MAX_SPEED = 10
MIN_SPEED = 0
MIN_FRONT_PWM = 326
MAX_BACK_PWM = 289
MID_PWM = 307
MIN_RADIAN = -0.3491

lock = threading.Lock()
car = RCCarControl()
car_speed = 1

class AutonomousEmergencyBraking:

    Distance = 0
    Stop_Acceleration = 0
    Current_speed = 0
    
    def Set_Distance(self, distance):
        self.Distance = distance
        
    def Get_Distance(self):
        return self.Distance
        
    def Set_Current_Speed(self, current_speed):
        self.Current_Speed = current_speed
        
    def Get_Current_Speed(self):
        return self.Current_Speed
        
    def Set_Stop_Acceleration(self, stop_acceleration):
        self.Stop_Acceleration = stop_acceleration
        
    def Get_Stop_Acceleration(self):
        return self.Stop_Acceleration
        
    def Cal_Stop_Distance(self):
        Stop_Distance = pow(self.Current_Speed, 2) / (2 * self.Stop_Acceleration)
        
        return Stop_Distance
        
    def Stop_Decision(self):
        
        if self.Distance <= self.Cal_Stop_Distance():
            return True
            
        else:
            return False
            
            
    def AEB_Control(self):
    
        if self.Stop_Decision():
            car.move_front(MID_PWM)
            print("Complete AEB")
            
        else:
            print("AEB ERROR")
    
    def Obstacle_Judge():
    
    def Stop():
    
    def AEB():
