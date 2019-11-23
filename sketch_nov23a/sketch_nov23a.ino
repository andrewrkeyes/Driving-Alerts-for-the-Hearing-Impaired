void setup() {
  Serial.begin(9600);  
  pinMode(8, OUTPUT);
}
 
void loop() {
  int my_val;
  int ms = millis();
  int sum = 0;
  for (int i = 0; i <4; i++){
    my_val = analogRead(A0);
    sum = sum + my_val;
  }
  int final = sum/4;
  if (final > 31) {  
    digitalWrite(8, HIGH);
    Serial.println("TRIGGERED at time:");
    Serial.println(ms);
    Serial.println("Loudness:");
    Serial.println(final); 
    delay(500);
  }
  digitalWrite(8, LOW);
}
