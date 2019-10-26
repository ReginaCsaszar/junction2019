import cv2
import numpy as np

video_uri = '/mnt/c/data/jx/vonat22.mp4'
#video_uri = 'http://192.168.0.190:8080/stream/video.mjpeg'

def can_we_go_now(sensor_id: int) -> bool:
    video = cv2.VideoCapture(video_uri)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    for _ in range(5):
        retval, frame = video.read()
        if not retval:
            return False
        # hist eq
        frameYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(frameYCrCb)
        channels[0] = clahe.apply(channels[0])
        frameYCrCb = cv2.merge(channels)
        frame = cv2.cvtColor(frameYCrCb, cv2.COLOR_YCrCb2BGR)
        # convert to hsv for detection
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frameHSV, np.array([150,0,0]), np.array([200,100,250]))
        # erode/dilate for nose reduction
        frame_threshold = cv2.erode(frame_threshold, np.array([5,5]))
        frame_threshold = cv2.dilate(frame_threshold, np.array([5,5]))


if __name__ == '__main__':
    video = cv2.VideoCapture(video_uri)
    while True:
        retval, frame = video.read()
        if not retval:
            break
        cv2.imshow('video', frame)
        frameYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(frameYCrCb)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        channels[0] = clahe.apply(channels[0])
        frameYCrCb = cv2.merge(channels)
        frame = cv2.cvtColor(frameYCrCb, cv2.COLOR_YCrCb2BGR)
        cv2.imshow('histeq', frame)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frameHSV, np.array([150,0,0]), np.array([200,100,250]))
        frame_threshold = cv2.erode(frame_threshold, np.array([5,5]))
        frame_threshold = cv2.dilate(frame_threshold, np.array([5,5]))
        cv2.imshow('filtered',frame_threshold)
        key = cv2.waitKey(30)
        if key is 27: # ESC
            break
        if key is ord(p):
            cv2.waitKey(0)
            
    if key is not 27: # if not ESC wait for keypress
        cv2.waitKey(0)
