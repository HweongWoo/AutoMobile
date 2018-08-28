import os
import numpy as np
import sys
import cv2
import threading
import time

class AdaptiveCruseControl(object):

    Distance = 0

    def __init__(self, Distance):
        self.Distance = Distance
    
   # def Distance_Keeping(float Distance, int Speed):
    
    #def Decide_Speed(int My_Speed, float Current_Speed):
    
        def Decide_LCAS():
           
         if Distance < 90.00:
               print("LCAS")
