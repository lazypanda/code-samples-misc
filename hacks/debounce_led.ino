/*
Multi-color LED toggle with debouncing logic
*/

int redPin = 13;      //Pin that controls the red light in the status LED
int greenPin = 12;    //Pin that controls the green light in the status LED
int bluePin = 11;     //Pin that controls the blue light in the status LED
int circuitPin = 10;  //Pin to which the electrode is attached
int buttonPin = 9;    //Pin to which button is attached

boolean buttonStatus;
boolean lastButtonStatus = LOW;
long lastDebounceTime = 0;
long debounceDelay = 50;
boolean ledOn = LOW;
int color = -1;

void setup()
{

  pinMode(circuitpin, OUTPUT);
  Serial.begin(9600);
  pinMode(buttonpin, INPUT);
  pinMode(greenpin, OUTPUT);
  pinMode(bluepin, OUTPUT);
  pinMode(redpin, OUTPUT);
  digitalWrite(redpin, LOW);
  digitalWrite(greenpin, LOW);
  digitalWrite(bluepin, LOW);
}



void loop()
{   
  boolean reading = digitalRead(buttonPin);
  if (reading != lastbuttonStatus) {
    if (reading)
    {
      color++;
      color%=8;
    }
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) 
  {
    buttonStatus = reading;
  }
  digitalWrite(redPin, (color & 1));
  digitalWrite(greenPin, (color & 2)>>1);
  digitalWrite(bluePin, (color & 4)>>2);
  lastButtonStatus = reading;
}