import easyocr
import cv2
import matplotlib.pyplot as plt
import os
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
directory_path = "3"
image_files_list = get_image_files(directory_path)


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
            plt.axis('off')
            plt.show()

read(image_files_list)
