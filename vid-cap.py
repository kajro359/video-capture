import cv2
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('-c', '--camera', type=str, help='camera to use: axis1, axis2, dlink1, dlink2')
ap.add_argument('-o', '--output', type=str, help='output filename')
args = vars(ap.parse_args())
if args['camera'] == 'axis1':
    stream_url = 'rtsp://root:bildg@192.168.8.14/mpeg4/media.amp'
    video_header = 'AXIS 214 PTZ #1'
if args['camera'] == 'axis2':
    stream_url = 'rtsp://root:bildg@192.168.8.15/mpeg4/media.amp'
    video_header = 'AXIS 214 PTZ #2'
if args['camera'] == 'dlink1':
    stream_url = 'rtsp://admin:@192.168.8.20:554/play1.sdp'
    video_header = 'D-Link DCS-960L'
if args['camera'] == 'dlink2':
    stream_url = 'rtsp://admin:@192.168.8.16/live1.sdp'
    video_header = 'D-Link DCS-2330L'

capture = cv2.VideoCapture(stream_url)

ret, frame = capture.read() #read a frame to get size
height, width, layers = frame.shape
size = (width, height)
fps = 15 #make same as setting in camera web-interface

pathOut = args['output'] + '.avi'

outVid = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

while True:
    hasFrame, frame = capture.read()
    cv2.imshow(video_header, frame)
    outVid.write(frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
capture.release()
outVid.release()
