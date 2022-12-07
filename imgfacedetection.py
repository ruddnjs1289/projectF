import face_recognition
import cv2
import os
import numpy as np
import pymysql
import time
import threading

class FaceRecog():
    def __init__(self):

        # 모듈 선언
        self.camera = cv2.VideoCamera(0)
        self.known_face_encodings = []
        self.known_face_names = []
      

        # 해당 경로에 있는 이미지로 학습 시작
        dirname = 'dataset'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # 변수 초기화
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

def __del__(self):
        del self.camera

conn=pymysql.connect(host='127.0.0.1',user='root',password='1234',db='project',charset='utf8')

curs = conn.cursor()