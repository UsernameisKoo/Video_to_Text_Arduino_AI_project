# 라이브러리 임포트 하기
import easyocr
import cv2
import matplotlib.pyplot as plt
import os
import serial
import time

THRESHOLD = 0.5

reader = easyocr.Reader(['ko', 'en'])


# 영상이 나눠진 프레임들을 리스트에 담아 반환
def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        # 파일의 확장자를 가져옴
        _, extension = os.path.splitext(filename)
        # 이미지 파일인지 확인
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            # 디렉토리 안의 사진을 리스트에 추가
            image_files.append(os.path.join(directory, filename))
    return image_files

# 이미지 파일이 들어있는 디렉토리 경로
directory_path = "./eng_ver"
image_files_list = get_image_files(directory_path)

# 아두이노와 시리얼 통신 설정
ser = serial.Serial('COM7', 9600)  # 아두이노가 연결된 COM 포트와 속도를 설정
time.sleep(2)  # 시리얼 포트가 열릴 때까지 잠시 대기


# 프레임에서 텍스트 추출 후 아두이노로 전송
def read(image_files_list):

    # 프레임에서 추출한 번호판 텍스트 담을 리스트 생성
    r = []

    # 한 프레임씩
    for img_path in image_files_list:
        # 프레임에서 인식한 텍스트들을 하나로 합칠 변수 초기화
        str = ""
        img = cv2.imread(img_path)

        result = reader.readtext(img_path)

        # bbox : 바운딩 박스  text : 인식한 텍스트  conf : 신뢰도
        for bbox, text, conf in result:
            if conf > THRESHOLD:
                # 프레임에서 추출한 텍스트 str 변수에 사이에 공백 넣어서 하나의 번호판 문자열 완성
                str = str + " " + text
                # 인식한 텍스트에 바운딩 박스 노란색으로 치기
                cv2.rectangle(img, pt1=(int(bbox[0][0]), int(bbox[0][1])), pt2=(int(bbox[2][0]), int(bbox[2][1])), color=(0, 255, 0), thickness=3)
        # 번호판 문자열 리스트에 추가
        r.append(str)

        # 이미 직전에 인식한 번호판이면 pass
        if len(r) > 1 and r[len(r) - 2] == r[len(r) - 1]:
            pass
        # 자동차 번호판 아두이노로 전송
        else:
            # OCR 결과를 아두이노로 전송
            ser.write((str + '\n').encode('utf-8'))  # 텍스트를 시리얼 포트를 통해 아두이노로 전송

            # 번호판 출력 + 프레임 보여주기
            print(r[int(len(r)) - 1])
            plt.figure(figsize=(8, 8))
            plt.imshow(img[:, :, ::-1])
            plt.axis('off')
            plt.show()

            time.sleep(4)  # 다음 데이터를 보내기 전에 잠시 대기 -> 다음 번호판까지 LED, 피엔조 울릴 여유주기 위해서

# 함수 호출
read(image_files_list)
