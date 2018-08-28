import os
import numpy as np
import sys
import cv2
import threading
import time
sys.path.insert(0, os.path.abspath('..'))
from vehicle_control.rc_car_control import RCCarControl

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

class LineChangeAssistSystem:

    Left_Angle = 0
    Right_Angle = 0
    
    def Set_Left_Angle(self, left_angle):
        self.Left_Angle = left_angle
        
    def Set_Right_Angle(self, right_angle):
        self.Right_Angle = right_angle
        
    def Get_Left_Angle(self):
        return self.Left_Angle
        
    def Get_Right_Angle(self):
        return self.Right_Angle
        
    def Move_Angle(self, direction):
        if direction == 0:
            car.steer_wheel(10)
            
        elif direction == 1:
            car.steer_wheel(350)
            
        else:
            print("Direction Error")
            
    def LCAS_Control(self, direction):
    
        i = 0
        
        while i<3:
        
            self.Move_Angle(direction)
            print("Moving")
            time.sleep(1)
            
            i+=1
            
        print("Complete LCAS")
        
        
if __name__ == "__main__":

    
    LCAS = LineChangeAssistSystem()
    LCAS.LCAS_Control(0)
