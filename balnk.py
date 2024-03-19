import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.rectangle(blank,(100,100),(200,200),(255,0,0),thickness=2)
cv.circle(blank,(200,200),50,(0,255,0),2)
cv.imshow('blank',blank)

cv.waitKey(0)