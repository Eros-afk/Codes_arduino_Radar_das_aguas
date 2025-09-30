#include <OneWire.h>
#include <DallasTemperature.h>

const int oneWireBus = 2;  // Pino do DS18B20
OneWire oneWire(oneWireBus);
DallasTemperature sensors(&oneWire);

const int trigger = A0;
const int echo = A1;

unsigned long tempo = 0;

void setup() {
  Serial.begin(115200);
  sensors.begin();
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);

  // Cabeçalho CSV
  Serial.println("tempo_ms,temperatura_C,distancia_cm");
}

void loop() {
  tempo = millis();

  // Leitura do DS18B20
  sensors.requestTemperatures();
  float temperatura = sensors.getTempCByIndex(0);

  // Leitura do HC-SR04
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  long duracao = pulseIn(echo, HIGH);
  float distancia = duracao * 0.034 / 2;  // em cm

  // Saída em formato CSV
  Serial.print(tempo);
  Serial.print(",");
  Serial.print(temperatura);
  Serial.print(",");
  Serial.println(distancia);

  delay(1000); // 1s entre leituras
}
