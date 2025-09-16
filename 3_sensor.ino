#include <OneWire.h>
#include <DallasTemperature.h>
#include <EEPROM.h>

#define ONE_WIRE_BUS 2
#define INTERVALO_MINUTOS 1
#define INTERVALO_MILIS (INTERVALO_MINUTOS * 60UL * 1000UL)

#define ENDERECO_CONTROLE 0
#define ENDERECO_DADOS 2

#define NUM_SENSORES 3

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

DeviceAddress enderecosSensores[NUM_SENSORES];

unsigned long ultimoMillis = 0;
int enderecoEEPROM = 0;

void setup() {
  Serial.begin(9600);
  sensors.begin();

  // Recupera último endereço salvo
  enderecoEEPROM = EEPROM.read(ENDERECO_CONTROLE) | (EEPROM.read(ENDERECO_CONTROLE + 1) << 8);

  Serial.print("Endereço inicial da EEPROM: ");
  Serial.println(enderecoEEPROM);

  // Localiza sensores conectados
  Serial.print("Sensores encontrados: ");
  Serial.println(sensors.getDeviceCount());

  if (sensors.getDeviceCount() < NUM_SENSORES) {
    Serial.println("ERRO: Nem todos os sensores foram encontrados!");
    while (1);  // trava o sistema
  }

  for (int i = 0; i < NUM_SENSORES; i++) {
    if (!sensors.getAddress(enderecosSensores[i], i)) {
      Serial.print("Erro ao obter endereço do sensor ");
      Serial.println(i);
      while (1);
    }
  }

  Serial.println("Sistema pronto.");
  Serial.println("Comandos disponíveis:");
  Serial.println("  r - Ler dados salvos");
  Serial.println("  c - Limpar dados");
}

void loop() {
  if (millis() - ultimoMillis >= INTERVALO_MILIS) {
    ultimoMillis = millis();
    registrarTemperaturas();
  }

  if (Serial.available()) {
    char comando = Serial.read();
    if (comando == 'r') {
      Serial.println("Lendo dados da EEPROM:");
      lerTemperaturasSalvas();
    } else if (comando == 'c') {
      limparEEPROM();
    }
  }
}

void registrarTemperaturas() {
  if (enderecoEEPROM + (NUM_SENSORES * 2) > EEPROM.length()) {
    Serial.println("Memória cheia!");
    return;
  }

  sensors.requestTemperatures();

  for (int i = 0; i < NUM_SENSORES; i++) {
    float tempC = sensors.getTempC(enderecosSensores[i]);
    int16_t tempEscalada = (int16_t)(tempC * 10);

    // Grava 2 bytes por sensor
    EEPROM.update(ENDERECO_DADOS + enderecoEEPROM, tempEscalada & 0xFF);
    EEPROM.update(ENDERECO_DADOS + enderecoEEPROM + 1, (tempEscalada >> 8));

    enderecoEEPROM += 2;

    Serial.print("Sensor ");
    Serial.print(i);
    Serial.print(": ");
    Serial.print(tempC);
    Serial.println(" °C");
  }

  // Atualiza endereço de controle
  EEPROM.update(ENDERECO_CONTROLE, enderecoEEPROM & 0xFF);
  EEPROM.update(ENDERECO_CONTROLE + 1, (enderecoEEPROM >> 8));
}

void lerTemperaturasSalvas() {
  if (enderecoEEPROM == 0) {
    Serial.println("Nenhum dado salvo.");
    return;
  }

  for (int i = 0; i < enderecoEEPROM; i += (NUM_SENSORES * 2)) {
    Serial.print("Amostra ");
    Serial.print(i / (NUM_SENSORES * 2));
    Serial.println(":");

    for (int j = 0; j < NUM_SENSORES; j++) {
      byte lsb = EEPROM.read(ENDERECO_DADOS + i + (j * 2));
      byte msb = EEPROM.read(ENDERECO_DADOS + i + (j * 2) + 1);
      int16_t tempEscalada = (msb << 8) | lsb;
      float tempReal = tempEscalada / 10.0;

      Serial.print("  Sensor ");
      Serial.print(j);
      Serial.print(": ");
      Serial.print(tempReal);
      Serial.println(" °C");
    }
  }
}

void limparEEPROM() {
  Serial.println("Limpando EEPROM...");

  for (int i = 0; i < EEPROM.length(); i++) {
    EEPROM.update(i, 0xFF);
  }

  enderecoEEPROM = 0;
  EEPROM.update(ENDERECO_CONTROLE, 0);
  EEPROM.update(ENDERECO_CONTROLE + 1, 0);

  Serial.println("EEPROM limpa com sucesso.");
}