# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:42:50 2024

@author: Sinda
"""

import cv2
import numpy as np

image =cv2.imread('monitor.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

if lines is not None:
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(image,(x1,y1),(x2,y2), (50,10,255), 2)
        
cv2.imshow('lines detectée' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()