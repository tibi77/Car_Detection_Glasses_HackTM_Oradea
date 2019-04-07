import time
import cv2
import numpy as np
from imutils.video import VideoStream
import io
import socket
import struct
import pickle
import zlib
import math 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.86.114', 50001))
connection = client_socket.makefile('wb')

HEIGHT = 250
WIDTH = 460

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText1 = (10,250)
bottomLeftCornerOfText2 = (10,230)
bottomLeftCornerOfText3 = (10,210)
bottomLeftCornerOfText4 = (10,190)
fontScale = 0.5
fontColor = (255,255,255)
lineType = 1


img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:

    try:
        with open('cardata.txt') as f:
            content = f.readlines()
    except:
        continue

    content = [x.strip() for x in content] 

    try:
        x1 = math.floor(float(content[4]) * WIDTH) + 1
        y1 = math.floor(float(content[5]) * HEIGHT) + 1
        x2 = math.floor(float(content[6]) * WIDTH) + 1 
        y2 = math.floor(float(content[7]) * HEIGHT) + 1
    except:
        continue
        
    blank_image = np.zeros((250,460,3), np.uint8)
    
    cv2.rectangle(blank_image,(x1, y1),(x2, y2),(0,255,0),2)
    cv2.putText(blank_image,content[0], bottomLeftCornerOfText1, font, fontScale, fontColor, lineType)
    cv2.putText(blank_image,content[1], bottomLeftCornerOfText2, font, fontScale, fontColor, lineType)
    cv2.putText(blank_image,content[2], bottomLeftCornerOfText3, font, fontScale, fontColor, lineType)
    cv2.putText(blank_image,content[3], bottomLeftCornerOfText4, font, fontScale, fontColor, lineType)

    result, blank_image = cv2.imencode('.jpg', blank_image, encode_param)
    data = pickle.dumps(blank_image, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    client_socket.sendall(struct.pack(">L", size) + data)
    img_counter += 1

cam.release()