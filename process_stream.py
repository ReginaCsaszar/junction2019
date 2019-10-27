import cv2
import numpy as np

#video_uri = '/mnt/c/data/jx/vonat22.mp4'
video_uri = 'http://192.168.0.190:8080/stream/video.mjpeg'

mask = [[0.45, 0.65],[0.50,0.65],[0.6,0.95],[0.35,0.95]]

def can_we_go_now():
    video = cv2.VideoCapture(video_uri)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    while True:
        retval, frame = video.read()
        if not retval:
            return
        # hist eq
        frameYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        channels = cv2.split(frameYCrCb)
        channels[0] = clahe.apply(channels[0])
        frameYCrCb = cv2.merge(channels)
        frame = cv2.cvtColor(frameYCrCb, cv2.COLOR_YCrCb2BGR)
        # convert to hsv for detection
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frameHSV, np.array([0,80,0]), np.array([255,220,255]))
        # erode/dilate for nose reduction
        frame_threshold = cv2.erode(frame_threshold, np.array([5,5]))
        frame_threshold = cv2.dilate(frame_threshold, np.array([5,5]))
        maskImage = np.zeros(shape=[frame_threshold.shape[0], frame_threshold.shape[1]], dtype=np.uint8)
        intMask=np.array(list((int(x*frame.shape[1]),int(y*frame.shape[0])) for (x,y) in mask))
        cv2.fillPoly(maskImage,  np.int32([intMask])  ,(255,255,255))
        masked = np.bitwise_and(frame_threshold, maskImage)
        if np.sum(masked)//255 > 400:
            print('stop')
        else:
            cv2.destroyAllWindows()
            return
        key = cv2.waitKey(1)


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
        cv2.imshow('hsv', frameHSV)
        frame_threshold = cv2.inRange(frameHSV, np.array([0,80,0]), np.array([255,220,255]))
        frame_threshold = cv2.erode(frame_threshold, np.array([5,5]))
        frame_threshold = cv2.dilate(frame_threshold, np.array([5,5]))
        maskImage = np.zeros(shape=[frame_threshold.shape[0], frame_threshold.shape[1]], dtype=np.uint8)
        intMask=np.array(list((int(x*frame.shape[1]),int(y*frame.shape[0])) for (x,y) in mask))
        cv2.fillPoly(maskImage,  np.int32([intMask])  ,(255,255,255))
        masked = np.bitwise_and(frame_threshold, maskImage)
        cv2.imshow('filtered',frame_threshold)
        cv2.imshow('masked', masked)
        if np.sum(masked)//255 > 400:
            print('stop')
        else:
            print('go')
        for i in range(-1,3,1):
            cv2.line(frame,
                (int(mask[i][0]*frame.shape[1]),int(mask[i][1]*frame.shape[0])),
                (int(mask[i+1][0]*frame.shape[1]),int(mask[i+1][1]*frame.shape[0])),
                (0,0,255))
        cv2.imshow('area', frame)
        key = cv2.waitKey(1)
        if key is 27: # ESC
            break
        if key is ord('p'):
            cv2.waitKey(0)

    if key is not 27: # if not ESC wait for keypress
        cv2.waitKey(0)
