# 라이브러리 호출
import cv2
import os

print(cv2.__version__)

# 영상 경로
filepath = 'eng_ver.mp4'
video = cv2.VideoCapture(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)) # 상대 경로로 영상 경로 설정

# 영상 초기화 실패 시 알려주고 종료
if not video.isOpened():
    print("Could not Open :", filepath)
    exit(0)

#불러온 비디오 파일의 정보 출력
fps = video.get(cv2.CAP_PROP_FPS) # 초당 프레임 수

print("fps :", fps)

#프레임을 저장할 디렉토리를 생성
try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

#영상을 각 프레임마다 캡쳐 후 디렉토리에 저장
count = 0

while (video.isOpened()): # video 열려있는 동안 실행
    retval, image = video.read() # image : 현재 프레임
    # int(video.get(1)) == int(video.get(cv2.CAP_PROP_POS_FRAMES))
    # 읽는 프레임 없으면 while문 나가기
    if (retval == False):
        break
    if (int(video.get(1)) % fps == 0):  # 앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image) # 프레임 저장하기, cv2.imwrite(저장 경로, 저장 이미지)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
# 동영상 파일을 닫고 메모리 해제
video.release()



