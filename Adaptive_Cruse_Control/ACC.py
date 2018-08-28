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

class AdaptiveCruseControl:

    Distance = 80
    Stop_Acceleration = 10
    Acc_Speed = 80
    Direction = 0

        
    def Set_Distance(self, distance):
        self.Distance = distance
        
    def Get_Distance(self):
        return self.Distance
        
    def Set_Stop_Acceleration(self, stop_acceleration):
        self.Stop_Acceleration = stop_acceleration
        
    def Get_Stop_Acceleration(self):
        return self.Stop_Acceleration
        
    def Set_Acc_Speed(self, acc_speed):
        self.Acc_Speed = acc_speed
        
    def Get_Acc_Speed(self):
        return self.Acc_Speed
        
    def Set_Direction(self, direction):
        self.Direction = direction
        
    def Get_Direction(self):
        return self.Direction
        
    def ACC_Speed_UP(self):
        if self.ACC_Speed < 10:
            self.ACC_Speed += 1
            
        else:
            print("ACC_Speed is maximum 100")
            
            
    def ACC_Speed_Down(self):
        if self.ACC_Speed > 0:
            self.ACC_Speed -= 1
            
        else:
            print("ACC_Speed is minimum 0")
        
    def Cal_Stop_Distance(self):
        Stop_Distance = pow(self.Acc_Speed, 2) / (2 * self.Stop_Acceleration)
        
        return Stop_Distance
        
    def ACC_Control(self, LCAS):
    
        Stop_Distance = self.Cal_Stop_Distance()
        
        if self.Distance == Stop_Distance:
            self.Distance_Keeping
            
        elif self.Distance < Stop_Distance:
            LCAS.LCAS_Control(self.Direction)
            
           
    def Distance_Keeping(self):
        ACC_Speed_Down()
        car.move_front(self.ACC_Speed)
        print("Deceleration")
        
        
if __name__ == "__main__":

    ACC = AdaptiveCruseControl()
    LCAS = LineChangeAssistSystem()
    
    ACC.ACC_Control(LCAS)
        
    
    
