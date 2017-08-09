
float data;
int tempPin=0;
int tipo = 1;
int num_sensor = 1;

void setup(){
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT); //LED
}

void loop(){
    data = analogRead(tempPin);
    data = (5 * data * 100) / 1024;

    Serial.print(tipo);
    Serial.print(" ");
    Serial.print(num_sensor);
    Serial.print(" ");
    Serial.println(data);

    //LED
    digitalWrite(LED_BUILTIN,HIGH);
    delay(5000);
    digitalWrite(LED_BUILTIN,LOW);

    delay(55000);
}
