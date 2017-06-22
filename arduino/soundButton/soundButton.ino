// LED pin
const int ledPin = 13;
const int buttonPin = 7;
const int pitch = 500;

void setup() {
  // Make the LED pin an output and turn it on
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop() {
  //read the input from A0 and store it in a variable

  if (digitalRead(buttonPin))
  {
  // play the tone for 20 ms on pin 8
    tone(8, 5000, 150);
    delay(200);
    tone(8, 4000, 150);
  };

  // wait for a moment
  delay(10);
}

