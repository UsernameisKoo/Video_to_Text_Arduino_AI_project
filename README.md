# 🚗 Video_to_Text_Arduino_AI_project
## :zero: STEPS  -  프로젝트 실행 방법  
---------------------------------------
__1.__ 깃허브에서 zip파일 다운받아 압축을 풀고 파이썬 IDE(VSCODE, PYCHARM)에서 연다.

  
__2. 영상에서 프레임을 추출하는 과정__ → __cap.py__ 파일을 실행


__3. 추출한 프레임에서 자동차 번호판 인식__


아두이노가 준비된 경우 → __send_text_to_arduino.py__ 실행
- __send_text_to_arduino.py__ 의 포트가 올바른 포트인 지 확인 !

```python
ser = serial.Serial('COM7', 9600)  # 아두이노가 연결된 COM 포트에 맞게 설정
```

인식한 번호판만 파이썬에서 확인하고 싶은 경우 →  __video_to_text.py__ 실행

✔️ 프로젝트에는 총 3개의 영상이 준비되어 있습니다.

__eng_ver.mp4 :__ 영어 자동차 번호판 5개로 이루어진 영상

__kor_ver.mp4 :__ 한글 자동차 번호판 5개로 이루어진 영상

✔️ 다른 번호판 영상으로 바꿔서 실행하고 싶은 경우
__cap.py__ 의 영상 경로를 변경해줍니다.

```python
filepath = 'eng_ver.mp4'  # 해당 영상의 경로로 변경
```

__send_text_to_arduino.py__ 와 __video_to_text.py__ 의 디렉토리 경로를 변경해줍니다.

```python
directory_path = "./eng_ver" # 해당 영상의 프레임이 저장된 디렉토리의 경로로 변경
```


## :one: About our project  -  프로젝트 설명
---------------------------------------
자동차가 주차장 입구를 통과할 때 번호판이 자동으로 인식되며 경광등에서 사이렌과 반짝거리며 사이렌이 울리는 것에서 아이디어를 얻어 프로젝트 목표를 세우게 되었습니다.
영상에서 텍스트를 인식하여 아두이노로 전송하고, 이를 통해 다음과 같은 작업을 수행합니다 :

-  번호판을 LCD에 출력
-  LED 점멸
-  피에조 부저 울림

경광등으로 자동차가 인식되면 경고하는 것을 표현하기 위해 LED와 피엔조 부저는 각 번호판 당 4번씩 빠르게 작동합니다.


## :two: Additional libraries required - 추가 설치 라이브러리
---------------------------------------
-  Python packages that must be installed
    - EasyOCR

    pip install easyocr

    - OpenCV

    pip install opencv-python

    - Matplotlib
  
    pip install matplotlib

    - PySerial

    pip install serial
   
- Arduino library that must be installed
    - LiquidCrystal_I2C

## :three: Video References - 영상 출처
---------------------------------------
- kor_ver.mp4
  
"자동차 번호판 색깔의 의미", YouTube, uploaded by 이거알면인정 13 Jun. 2023,
https://www.youtube.com/shorts/kEYTpOo7-tI

- eng_ver.mp4

https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXKhxuMTxNXfPb9hOZfUUbAeuZ2fLEyTUasTaNXOWwEnOjehP0iQs24CcfkNIgQHobHWo&usqp=CAU

https://img4.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202105/22/chutcha/20210522110338247bprp.jpg

https://www.shutterstock.com/image-vector/car-number-plate-delhi-vehicle-260nw-2093983801.jpg

https://upload.wikimedia.org/wikipedia/commons/0/02/Greek_license_plate.svg

https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202105/22/chutcha/20210522110351401foby.jpg
