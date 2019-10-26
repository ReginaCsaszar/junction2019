import cv2
import numpy as np

video = cv2.VideoCapture('/mnt/c/data/jx/pivideo3.mp4')
while True:
    retval, frame = video.read()
    if not retval:
        break
    cv2.imshow('video', frame)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frameHSV, np.array([30,0,0]), np.array([180,100,250]))
    frame_threshold = cv2.erode(frame_threshold, np.array([5,5]))
    frame_threshold = cv2.dilate(frame_threshold, np.array([5,5]))
    cv2.imshow('filtered',frame_threshold)
    key = cv2.waitKey(10)
    if key is 27: # ESC
        break
if key is not 27: # if not ESC wait for keypress
    cv2.waitKey(0)
