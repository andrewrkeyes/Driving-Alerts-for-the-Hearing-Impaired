void setup() {
  Serial.begin(9600);  
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}
 
void loop() {
  float my_val;
  float my_val1;
  float my_val2;
  int ms = millis();
  float sum = 0;
  float sum1 = 0;
  float sum2 = 0;
  for (int i = 0; i <4; i++){
    my_val = analogRead(A0);
    sum = sum + my_val;
    my_val1 = analogRead(A1);
    sum1 = sum1 + my_val1;
    my_val2 = analogRead(A2);
    sum2 = sum2 + my_val2;
  }
  float redThreshold = 22.27;
  float blueThreshold = 29.27;
  float greenThreshold = 32;
  float final0 = sum/4;
  float final1 = sum1/4;
  float final2 = sum2/4;
  if (final0 > redThreshold) {  
    digitalWrite(8, HIGH);
    Serial.println("RED TRIGGERED at time:");
    Serial.println(ms);
    Serial.println("Loudness:");
    Serial.println(final0); 
  
 }if (final1 > blueThreshold) {  
   digitalWrite(9, HIGH);
    Serial.println("BLUE TRIGGERED at time:");
    Serial.println(ms);
    Serial.println("Loudness:");
    Serial.println(final1); 
  }
  if (final2 > greenThreshold) {  
  digitalWrite(10, HIGH);
    Serial.println("GREEN TRIGGERED at time:");
    Serial.println(ms);
    Serial.println("Loudness:");
    Serial.println(final2); 
  }if (final0 >redThreshold or final1 > blueThreshold or final2 > greenThreshold){
    delay(500);
  }
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
 digitalWrite(10, LOW);
}
