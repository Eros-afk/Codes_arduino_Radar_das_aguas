const int echo=A1;
const int trigger=A0;
long tempo;
float distancia;


void setup() 
{
  pinMode(echo,INPUT);
  pinMode(trigger,OUTPUT);
  Serial.begin(9600);
  delay(1000);
}

void loop() 
{
  medir();
  
  Serial.print("Distancia: ");
  Serial.print(distancia);    
  Serial.print("cm");
  Serial.println();
}

void medir()
{
  digitalWrite(trigger,LOW);
  delayMicroseconds(2);
  digitalWrite(trigger,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger,LOW);
  
  tempo=pulseIn(echo,HIGH);
  distancia = float(tempo*0.0343)/2;
  delay(10);
}