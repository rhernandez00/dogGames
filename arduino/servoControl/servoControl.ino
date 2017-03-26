#include <Servo.h> //include the servo library
 
int pos=90; //declare initial position of the servo
int servoPin = 9; //declare pin for the servo
int servoDelay =2000; //delay to allow the servo to reach position;
int outPos = 132;
int inCord = 106;
int inCords[] = {106,83,58,36};
int outCount = 0;
int count = 0;
int nPelletsMax = 13;
 
Servo myServo; // create a servo object called myServo
 
void setup() {
  Serial.begin(9600); //start serial port
  myServo.attach(servoPin); //declare to which pin is the servo connected
  pinMode(13, OUTPUT);
  delay(100);
  myServo.write(inCords[0]);
}
 
void loop() 
{
  if(Serial.available()!=0)
  { //wait until information is received from the serial port
    pos = Serial.parseInt(); //read the position from the servo
    if (pos == 99)
    {
      myServo.write(outPos); //write the position into the servo
      digitalWrite(13, HIGH);
      delay(servoDelay); //pauses so the servo can reach its position
      myServo.write(inCord);
      digitalWrite(13, LOW);
      count = count + 1;
      if (count >= nPelletsMax)
      {
        count = 0;
        outCount = outCount + 1;
        if (outCount > 3)
        {
          outCount = 0;  
        };
        inCord = inCords[outCount];
      };
    
    };
  };
};
