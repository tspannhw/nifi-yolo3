import time
import sys
import datetime
import subprocess
import sys
import os
import datetime
import traceback
import math
import random, string
import base64
import json
from time import gmtime, strftime
import cv2
import math
import random, string
import time

from time import gmtime, strftime
start = time.time()
cap = cv2.VideoCapture(1)

packet_size=3000

ret, frame = cap.read()

filename = 'images/yolo_image_{0}_{1}.jpg'.format('img',strftime("%Y%m%d%H%M%S",gmtime()))
cv2.imwrite(filename, frame)
print(filename)

# this is an OpenCV2 Python script to capture from video camera #1 - this is the second camera for me
# when my mac is docked and I am using the webcam in the monitor
# use VideoCapture(0) if you only have one webcam or powerbook is open

# create an images directory in the darknet directory for both original and market up images
