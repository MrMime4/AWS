from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings


class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(1, cv2.CAP_DSHOW)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		ret, im = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		frame_flip = cv2.flip(im,1)
		ret, jpg = cv2.imencode('.jpg', frame_flip)
		return jpg.tobytes()
