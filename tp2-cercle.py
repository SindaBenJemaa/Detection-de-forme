# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:09:16 2024

@author: Sinda
"""

import cv2
import numpy as np

image =cv2.imread('planet.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.GaussianBlur(gray, (9,9), 2)
circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT, dp=1, minDist=50,param1=200,param2=30,minRadius=0,maxRadius=0)
if circles is not None:
    circles =np.round(circles[0, :]).astype("int")
    for(x,y,r) in circles :
        cv2.circle(image,(x,y),r,(50,10,255),4)
cv2.imshow('Circles detectée' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()