// In this code, the servo (steering system) is simply being tested to make sure the servo can move freely and smoothly in its full range.
#include <Servo.h>

Servo myservo;

int pos = 0;

void setup() {
  myservo.attach(9);
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);              
    delay(15);                    
  }
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);              
    delay(15);                      
  }
}
