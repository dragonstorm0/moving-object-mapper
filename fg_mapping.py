#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import re
import cv2 # opencv library
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt
vdo=cv2.VideoCapture("cut.mp4")
col_images=[]
while(True):
    flag,img=vdo.read()
    if(flag==False):
        break
    else:
        col_images.append(img)


# In[6]:


for frame in range(len(col_images)-1):
    #frames converted to grayscale
    grayA = cv2.cvtColor(col_images[frame], cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(col_images[frame+1], cv2.COLOR_BGR2GRAY)
    #frame differencing
    diff_image = cv2.absdiff(grayB, grayA)
    #image thresholding
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)
    #image dilation
    kernel = np.ones((3,3),np.uint8)
    dilated = cv2.dilate(thresh,kernel,iterations = 1)
    # plot dilated image
    cv2.imshow('image',dilated)
    k=cv2.waitKey(10)
    if(k==ord('q')):
        break
vdo.release()
cv2.destroyAllWindows()


# In[ ]:




