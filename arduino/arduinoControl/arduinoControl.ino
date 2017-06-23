#include <Servo.h> //include the servo library
 

const int servoPin = 9; //declare pin for the servo
const int piezoPin = 6;
const int outPos = 132; //out position
const int waterPin = 8; //position for the water dispenser
const int sensorPin = 7; //IR sensor   
const int servoDelay =3000; //delay to allow the servo to reach position;
const int delayToBack = 1000;
const int waterDelay = 10000; // delay to allow water to drop
const unsigned long timeLimit = 1000; //time out for reward

unsigned long timeStart, timeFinish, timeElapsed;

int pos=90; //declare initial position of the servo

int inCord = 106;
int inCords[] = {106,83,58,36};
int outCount = 0;
int count = 0;
int nPelletsMax = 100;
boolean rewardGiven = false;
boolean continueCycle = false;
 
Servo myServo; // create a servo object called myServo
 
void setup() {
  Serial.begin(9600); //start serial port
  myServo.attach(servoPin); //declare to which pin is the servo connected
  pinMode(13, OUTPUT);
  pinMode(waterPin, OUTPUT);
  pinMode(sensorPin, INPUT);
  delay(100);
  myServo.write(inCords[0]);
  delay(100);
  myServo.detach(servoPin);
}
 
void loop() 
{
  if(Serial.available()!=0)
  { //wait until information is received from the serial port
    pos = Serial.parseInt(); //read the command from the serial port
    switch (pos)
    {
      case 99:   
        rewardGiven = false;
        tone(piezoPin, 5000, 150);
        delay(200);
        tone(piezoPin, 4000, 150);
        
        while (!(rewardGiven))
        {
          timeStart = millis();
          
          giveReward();  
          while(true)
          {
            timeFinish = millis();
            timeElapsed = timeFinish - timeStart;
            if (!(digitalRead(sensorPin)))
            {
              Serial.print("Reward detected \n");
              Serial.print(timeElapsed);
              rewardGiven = true;
              backToStart();
              break;
            }
            else if (timeElapsed > timeLimit)
            {
              Serial.print("Time out \n");
              delay(delayToBack);
              backToStart();
              break;
            };
          };
        };
        break;
      case 88:
        digitalWrite(13, HIGH);
        digitalWrite(waterPin,HIGH);
        delay(waterDelay); //pauses for water to drop
        digitalWrite(13, LOW);
        digitalWrite(waterPin,LOW);
        break;
      case 77:
        tone(piezoPin, 1000, 300);
        delay(200);
        tone(piezoPin, 500, 300);
        delay(400);
        tone(piezoPin, 500, 600);
        break;
      default:
        Serial.print(pos);
        break;
    };
      
  };
};

void giveReward()
{
  //timeStart = millis();
  myServo.attach(servoPin);
  myServo.write(outPos); //write the position into the servo
  digitalWrite(13, HIGH); //signal of servo on
  Serial.print("Servo on \n");
  myServo.detach(servoPin);
   
}

void backToStart()
{
  myServo.attach(servoPin);
  inCord = determineInput();
  myServo.write(inCord); //write the position into the servo
  digitalWrite(13, LOW); //signal of servo on
  Serial.print("Servo back to start \n"); 
  delay(servoDelay);
  myServo.detach(servoPin);
  //Serial.print(inCord); 
}

int determineInput()
{
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
  return inCord;
};

