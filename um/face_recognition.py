import cv2
import numpy as np
import os
import datetime
import db2






recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
won : id=1
IU : id=2

# names related to ids: example ==> loze: id=1,  etc
# 이런식으로 사용자의 이름을 사용자 수만큼 추가해준다.
names = ['None', 'won', 'IU', 'chs', 'ksw']

# 카메라 영상 받아올 객체 선언(영상 소스,해상도 설정)
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

is_record = False                           # 녹화상태는 처음엔 거짓으로 설정
on_record = False
cnt_record = 0      # 영상 녹화 시간 관련 변수
max_cnt_record = 5  # 최소 촬영시간
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # 영상을 기록할 코덱 설정


face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml') 




# 초기 프레임으로 사용할 프레임들을 저장
#ret, frame_a = cam.read()
#ret, frame_b = cam.read()


# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    #캡처 구문dat
     # 현재시각을 불러와 문자열로저장
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    nowDatetime_path = now.strftime('%Y-%m-%d %H_%M_%S') # 파일이름으로는 :를 못쓰기 때문에 따로 만들어줌

    ret, img =cam.read()
    # img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 영상을 흑백으로 바꿔줌
    
    #얼굴인식
    Mfaces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor= 1.5, 
        minNeighbors=3, 
        minSize=(20,20))
    
    #특정 얼굴인식
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
     # 찾은 얼굴이 있으면
    if len(faces) :
        is_record = True    # 녹화 준비
        if on_record == False:
            video = cv2.VideoWriter("video/"+ nowDatetime_path + ".avi", fourcc, 1, (img.shape[1], img.shape[0]))
        cnt_record = max_cnt_record
    #if type(cam) == type(None):
     #   break
    if is_record == True:   # 녹화중이면
        print('녹화 중')
        video.write(img)    # 현재 프레임 저장
        cnt_record -= 1     # 녹화시간 1 감소
        on_record = True    # 녹화중 여부를 참으로
    if cnt_record == 0:     # 녹화시간이 다 되면
        is_record = False   # 녹화관련 변수들을 거짓으로
        on_record = False
        
    #특정 얼굴 인식    
    for(x,y,w,h) in faces:
        
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 130):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    
   
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif k == ord('q'):  # q를 누르면 캡쳐 
        print("캡쳐")
        cv2.imwrite("capture/"+str(id) + nowDatetime_path + ".png",img)
        db2.insert_data(picture=str(id) + nowDatetime_path + ".png",name=str(id) )
      
        
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
