int led = 13;
char user_input;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(115200);
  Serial.flush();
}

void loop() {
  if(Serial.available()){
    user_input = Serial.read();
    Serial.print(user_input);

    if(user_input=='1'){
      Serial.print("Turning on LED");
      digitalWrite(led, HIGH);
    }
    else if(user_input=='2'){
      Serial.print("Turning off LED");
      digitalWrite(led, LOW);
    }
    else{
      Serial.print("What is that even?");
    }
  }

}
