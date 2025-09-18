const int echo = A1;
const int trigger = A0;
long tempo;
float distancia;
unsigned long tempoAnterior = 0;  // Variável para armazenar o tempo anterior
const long intervalo = 20000;  // Intervalo de 20 segundos (20000 milissegundos)

void setup() {
  pinMode(echo, INPUT);
  pinMode(trigger, OUTPUT);
  Serial.begin(9600);
  delay(1000);
}

void loop() {
  // Verifica se passaram 20 segundos (20000 ms)
  if (millis() - tempoAnterior >= intervalo) {
    tempoAnterior = millis();  // Atualiza o tempo anterior
    medir();  // Realiza a medição
    // Imprime a distância a cada 20 segundos
    Serial.print("Distancia: ");
    Serial.print(distancia);
    Serial.print(" cm");
    Serial.println();
  }
}

void medir() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  
  tempo = pulseIn(echo, HIGH);
  distancia = float(tempo * 0.0343) / 2;
}