#include <Wire.h>  // I2C 통신을 위한 라이브러리
#include <LiquidCrystal_I2C.h>  // I2C를 통해 LCD를 제어하기 위한 라이브러리

// I2C 주소가 0x27이고 16x2 크기의 LCD 객체 생성
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);  // 시리얼 통신을 9600bps로 설정
  lcd.begin(0, 0);  // LCD 초기화
  lcd.backlight();  // LCD 백라이트 켜기
  lcd.setCursor(0, 0);  // 커서를 첫 번째 줄의 첫 번째 위치로 이동
  lcd.print("Waiting for data");  // 초기 메시지를 LCD에 출력
  pinMode(13, OUTPUT);  // 핀 13을 출력 모드로 설정
  analogWrite(9, 0);  // 핀 9에 아날로그 값을 0으로 설정
}

void loop() {
  // 시리얼로부터 데이터가 수신되었는지 확인
  if (Serial.available() > 0) {
    // '\n' 문자가 나올 때까지 문자열을 읽어옴
    String data = Serial.readStringUntil('\n');
    lcd.clear();  // LCD 화면 지우기
    lcd.setCursor(0, 0);  // 커서를 첫 번째 줄의 첫 번째 위치로 이동

    // 수신된 데이터가 16자 이하인 경우
    if (data.length() <= 16) {
      lcd.print(data);  // 데이터를 한 줄에 출력
      // LED 깜빡임과 소리 발생
      for(int i = 0; i < 5; i++) {
        digitalWrite(13, HIGH);  // LED 켜기
        delay(400);  // 400ms 대기
        digitalWrite(13, LOW);  
        delay(400); 
        tone(11, 261, 400);  // 261Hz 소리 발생 (C4 음)
        delay(800); 
      }
    } else {
      // 수신된 데이터가 16자보다 긴 경우
      // 첫 번째 16자를 첫 번째 줄에 출력
      String line1 = data.substring(0, 16);
      // 나머지 문자를 두 번째 줄에 출력
      String line2 = data.substring(16);
      lcd.print(line1);
      lcd.setCursor(0, 1);  // 커서를 두 번째 줄의 첫 번째 위치로 이동
      lcd.print(line2);
      // LED 깜빡임과 소리 발생
      for(int i = 0; i < 5; i++) {
        digitalWrite(13, HIGH); 
        delay(400); 
        digitalWrite(13, LOW);  
        delay(400);  
        tone(11, 261, 400);  
        delay(800);  
      }
    }
  }
}
