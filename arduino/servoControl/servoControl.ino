#include <Servo.h> //include the servo library
 
int pos=90; //declare initial position of the servo
int servoPin = 9; //declare pin for the servo
int servoDelay =60; //delay to allow the servo to reach position;
int initialPos = 106;
int outCord = 106;
int outCords[] = {106,83,58,36};
int outCount = 1;
int count = 0;
 
Servo myServo; // create a servo object called myServo
 
void setup() {
  Serial.begin(9600); //start serial port
  myServo.attach(servoPin); //declare to which pin is the servo connected
  pinMode(13, OUTPUT);
  delay(100);
  myServo.write(initialPos);
}
 
void loop() {
  if(Serial.available()!=0)
  { //wait until information is received from the serial port
    pos = Serial.parseInt(); //read the position from the servo
    if (pos == 132){
      myServo.write(pos); //write the position into the servo
    }
    else if (pos == 106){
      myServo.write(outCord);
      count = count + 1;
      if (count >= 13)
      {
        count = 0;
        outCount = outCount + 1;
        if (outCount > 4){
          outCount = 1;
          
        };
        outCord = outCords[outCount];
      };
    };
    
    digitalWrite(13, HIGH);
    Serial.print(pos*2);
    //Serial.print("/n");
    delay(servoDelay); //give time to the servo to reach the position
    digitalWrite(13, LOW);
  };
  
}
