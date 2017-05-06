#include <Stepper.h>

#define SWITCH_DELAY 50
const int stepPin = 3;
const int directionPin = 8;
const int enablePin = 9;
const int switchPin = 4;

int stepState = 0;
char user_input;
int x;


// setup code, runs once
void setup() {

  // 220_TODO: initialize serial communication at a baud rate of 1200
  Serial.begin(1200);
  // 220_TODO: set ledPin to OUTPUT and write ledState to ledPin
  pinMode(stepPin,OUTPUT);
  pinMode(directionPin,OUTPUT);
  digitalWrite(directionPin,LOW);
  digitalWrite(enablePin, HIGH);
  pinMode(switchPin,INPUT);
//  setPwmFrequency(2,1);
}

void zero(){
  while(digitalRead(switchPin) == LOW){
    digitalWrite(directionPin, LOW);
    nSteps(1);
  }
}

void nSteps(int n){
  for(x = 0; x < 16 * n; x++){
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(SWITCH_DELAY);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(SWITCH_DELAY);
  }
}

void oneRotation(){
  for(x = 0; x < 16*200; x++){
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(SWITCH_DELAY);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(SWITCH_DELAY);
  }
}
void oneStick(){
  int i;
  for(i = 0; i < 35; i++){
    for(x = 0; x < 16*200; x++){
      digitalWrite(stepPin,HIGH);
      delayMicroseconds(SWITCH_DELAY);
      digitalWrite(stepPin,LOW);
      delayMicroseconds(SWITCH_DELAY);
    }
  }
}

// loop code, runs indefinitely
void loop() {
  if(Serial.available()){
    user_input = Serial.read();
    Serial.print(user_input);
    digitalWrite(enablePin, LOW);
    if(user_input == '0'){
      zero();
    }
    else if(user_input == '1'){
      digitalWrite(directionPin, LOW);
      nSteps(1);
    }
    else if(user_input == '2'){
      digitalWrite(directionPin, HIGH);
      nSteps(1);
    }
    else if(user_input == '3'){
      digitalWrite(directionPin, LOW);
      oneRotation();
    }
    else if(user_input == '4'){
      digitalWrite(directionPin, HIGH);
      oneRotation();
    }
    else if(user_input == '5'){
      digitalWrite(directionPin, LOW);
      oneStick();
    }
    else if(user_input == '6'){
      digitalWrite(directionPin, HIGH);
      oneStick();
    }
    else if(user_input == '7'){
      delay(2000);
      digitalWrite(directionPin, LOW);
      oneStick();
      delay(2000);
      digitalWrite(directionPin, HIGH);
      oneStick();
    }
    else if(digitalRead(switchPin) == HIGH){
      Serial.write("switch is pressed\n");
    }
    digitalWrite(enablePin, HIGH);
    Serial.write("done\n");
  }
 }

 
