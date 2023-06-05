int data = 0;

void setup() {
  Serial.begin(9600);
  while(!Serial){}
  pinMode(2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print(data);

    if (data != NULL) {
      if (data == "1") {
        digitalWrite(2, LOW);    // Encender Ventosa
        delay(2000);
      }
      if (data == "0") {
        digitalWrite(2, HIGH);   // Apagar Ventosa
      }
    }
  }
}