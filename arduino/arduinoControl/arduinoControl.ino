#include <Servo.h> //include the servo library
 

const int servoPin = 9; //declare pin for the servo
const int outPos = 132; //out position
const int waterPin = 8; //position for the water dispenser
const int sensorPin = 7; //IR sensor   
const int servoDelay =3000; //delay to allow the servo to reach position;
const int waterDelay = 10000; // delay to allow water to drop
const unsigned long timeLimit = 4000; //time out for reward

unsigned long timeStart, timeFinish, timeElapsed;

int pos=90; //declare initial position of the servo

int inCord = 106;
int inCords[] = {106,83,58,36};
int outCount = 0;
int count = 0;
int nPelletsMax = 5;
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
}
 
void loop() 
{
  if(Serial.available()!=0)
  { //wait until information is received from the serial port
    pos = Serial.parseInt(); //read the command from the serial port
    if (pos == 99)
    {
      rewardGiven = false;
     while (!(rewardGiven))
     { 
        timeStart = millis();
        myServo.write(outPos); //write the position into the servo
        digitalWrite(13, HIGH); //signal of servo on
        Serial.print("Servo on \n");
        timeElapsed = 0;
        continueCycle = true;
        while (continueCycle)
        {
          if (!(digitalRead(sensorPin)))
          {
            Serial.print("Sensor on \n");
            rewardGiven = true;
            continueCycle = false;
            Serial.print(timeElapsed);
            Serial.print("\n");
          };
          
          timeFinish = millis();
          timeElapsed = timeFinish - timeStart;
          if (timeElapsed > timeLimit)
          {
            Serial.print("Reward not detected \n");
            continueCycle = false;
          };
        };
        delay(servoDelay); //pauses so the servo can reach its position
        myServo.write(inCord);
        inCord = determineOutput();
        digitalWrite(13, LOW);
        Serial.print("Servo off \n");    
        
     //}
    }
    else if (pos == 88)
    {
      digitalWrite(13, HIGH);
      digitalWrite(waterPin,HIGH);
      delay(waterDelay); //pauses for water to drop
      digitalWrite(13, LOW);
      digitalWrite(waterPin,LOW);
    };
  };
};

void giveReward()
{
  timeStart = millis();
  myServo.write(outPos); //write the position into the servo
  digitalWrite(13, HIGH); //signal of servo on
  Serial.print("Servo on \n"); 
}

int determineOutput()
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
  return inCord
};

