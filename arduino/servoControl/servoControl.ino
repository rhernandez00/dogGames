#include <Servo.h> //include the servo library
 
int pos=90; //declare initial position of the servo
int servoPin = 9; //declare pin for the servo
int servoDelay =30; //delay to allow the servo to reach position;
 
Servo myServo; // create a servo object called myServo
 
void setup() {
  Serial.begin(9600); //start serial port
  myServo.attach(servoPin); //declare to which pin is the servo connected
}
 
void loop() {
  while(Serial.available()==0){}; //wait until information is received from the serial port
  pos = Serial.parseInt(); //read the position from the servo
  myServo.write(pos); //write the position into the servo
  Serial.print(pos);
  Serial.print("/n");
  delay(servoDelay); //give time to the servo to reach the position
}
