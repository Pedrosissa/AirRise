#define MQ_analog A2
#define MQ_dig 7
int valor_analog;
int valor_dig;
void setup() {
   Serial.begin(9600);
   pinMode(MQ_analog, INPUT);
   pinMode(MQ_dig, INPUT);
   pinMode(8, OUTPUT);
   pinMode(10, OUTPUT);
}
void loop() {
   valor_analog = analogRead(MQ_analog); //  
   Serial.println(valor_analog);
   if(valor_analog <= 100){
     digitalWrite(10, HIGH);
     digitalWrite(8, LOW);
   }else{ 
     digitalWrite(8, HIGH);
     digitalWrite(10, LOW);
   }
   delay(60000);
}
