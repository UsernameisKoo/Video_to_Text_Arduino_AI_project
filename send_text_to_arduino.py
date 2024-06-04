import easyocr
import cv2
import matplotlib.pyplot as plt
import os
import serial
import time

THRESHOLD = 0.5

reader = easyocr.Reader(['ko', 'en'])



def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        # 파일의 확장자를 가져옴
        _, extension = os.path.splitext(filename)
        # 이미지 파일인지 확인
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            image_files.append(os.path.join(directory, filename))
    return image_files

# 이미지 파일이 들어있는 디렉토리 경로
directory_path = "eng_ver"
image_files_list = get_image_files(directory_path)

# 아두이노와 시리얼 통신 설정
ser = serial.Serial('COM7', 9600)  # 아두이노가 연결된 COM 포트와 속도를 설정합니다.
time.sleep(2)  # 시리얼 포트가 열릴 때까지 잠시 대기

def read(image_files_list):

    r = []

    for img_path in image_files_list:
        str = ""
        img = cv2.imread(img_path)

        result = reader.readtext(img_path)

        for bbox, text, conf in result:
            if conf > THRESHOLD:
                str = str + " " + text
                cv2.rectangle(img, pt1=(int(bbox[0][0]), int(bbox[0][1])), pt2=(int(bbox[2][0]), int(bbox[2][1])), color=(0, 255, 0), thickness=3)

        r.append(str)
        if len(r) > 1 and r[len(r) - 2] == r[len(r) - 1]:
            pass
        else:
            print(r[int(len(r)) - 1])
            plt.figure(figsize=(8, 8))
            plt.imshow(img[:, :, ::-1])

            # OCR 결과를 아두이노로 전송
            ser.write((str + '\n').encode('utf-8'))  # 텍스트를 시리얼 포트를 통해 아두이노로 전송
            time.sleep(1)  # 다음 데이터를 보내기 전에 잠시 대기

            plt.axis('off')
            plt.show()

read(image_files_list)
