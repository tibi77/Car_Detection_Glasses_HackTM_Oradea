import os
import socket
import socket
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib

HOST = '192.168.86.103' 
PORT = 50000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)
print("Listening")
s = server_socket.accept()[0]
print("Connected")

data = b""
payload_size = struct.calcsize(">L")
# print("payload_size: {}".format(payload_size))

counter_delay = 0

while True:
    while len(data) < payload_size:
        # print("Recv: {}".format(len(data)))
        data += s.recv(1024)

    # print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    # print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += s.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    if counter_delay % 10 == 0:
        counter_delay = 0
        cv2.imwrite('img.jpg', frame)
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)
    counter_delay += 1
