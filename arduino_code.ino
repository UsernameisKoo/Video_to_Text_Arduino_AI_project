#include <Wire.h>
#include<LiquidCrystal_I2C_Hangul.h>

LiquidCrystal_I2C_Hangul lcd(0x27, 16, 2);  // I2C 주소는 LCD 모듈에 따라 다를 수 있습니다.

void setup() {
  Serial.begin(9600);
  lcd.begin(0,0);
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Waiting for data");
  pinMode(13,OUTPUT);
  analogWrite(9, 0);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // '\n'까지의 문자열을 읽어옵니다.
    lcd.clear();  // LCD를 지웁니다.
    lcd.setCursor(0, 0);  // 커서를 첫 번째 줄의 첫 번째 위치로 이동합니다.

    // 데이터가 16자보다 길면 두 줄로 나누어 출력합니다.
    if (data.length() <= 16) {
      lcd.print(data);  // 데이터가 16자 이하면 한 줄에 출력합니다.
      for(int i =0;i < 5;i++)
      {
        digitalWrite(13,HIGH);
        delay(400);
        digitalWrite(13,LOW);
        delay(400);
        tone(11, 261, 400); delay(800);
      }
      
    } else {
      String line1 = data.substring(0, 16);  // 첫 16자를 첫 번째 줄에 출력합니다.
      String line2 = data.substring(16);  // 나머지 문자를 두 번째 줄에 출력합니다.
      lcd.print(line1);
      lcd.setCursor(0, 1);
      lcd.print(line2);
      for(int i =0 ; i < 5;i++)
      {
        digitalWrite(13,HIGH);
        delay(400);
        digitalWrite(13,LOW);
        delay(400);
        tone(11, 261, 400); delay(800);
      }
    }
  }

}
