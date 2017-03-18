#include <Servo.h> //include the servo library
 
int pos=90; //declare initial position of the servo
int servoPin = 9; //declare pin for the servo
int servoDelay =500; //delay to allow the servo to reach position;
int pelletsPerTube = 13; //number of pellets before changing tube
int nPelletsGiven = 0; //n pellets given
int rotAngle = 123;
int tube = 1;


 
Servo myServo; // create a servo object called myServo
 
void setup() {
  Serial.begin(9600); //start serial port
  myServo.attach(servoPin); //declare to which pin is the servo connected
  delay(500);
  myServo.write(123); //sends the servo to get the first pellet
}
 
void loop() 
{
  if(Serial.available()==0)
  { //wait until information is received from the serial port
    //Deliver reward
    myServo.write(146);
    delay(servoDelay);

    nPelletsGiven = nPelletsGiven + 1;
    myServo.write(rotAngle); //write the position into the servo
    
    
    if (nPelletsGiven > pelletsPerTube)
    {
      tube = tube + 1;
      if (tube > 4)
      {
        tube = 1;
      };
      switch (tube)
      {
        case 1:
        {
          rotAngle = 123;
        };
        case 2:
        {
          rotAngle = 100;
        };
        case 3:
        {
          rotAngle = 75;
        };
        case 4:
        {
          rotAngle = 50;
        };
      };
    };
  };
  delay(servoDelay); //give time to the servo to reach the position
}
