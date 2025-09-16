#include <OneWire.h>
#include <DallasTemperature.h>
#include <EEPROM.h>

#define ONE_WIRE_BUS 2
#define INTERVALO_MINUTOS 1
#define INTERVALO_MILIS (INTERVALO_MINUTOS * 60UL * 1000UL)

#define ENDERECO_CONTROLE 0  // Onde salvamos o índice atual
#define ENDERECO_DADOS 2     // Dados começam depois do controle (usamos 2 bytes)

// Objeto OneWire e Dallas
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

unsigned long ultimoMillis = 0;
int enderecoEEPROM = 0;

void setup() {
  Serial.begin(9600);
  sensors.begin();

  // Recupera o último endereço salvo na EEPROM
  enderecoEEPROM = EEPROM.read(ENDERECO_CONTROLE) | (EEPROM.read(ENDERECO_CONTROLE + 1) << 8);
  Serial.print("Endereço inicial da EEPROM: ");
  Serial.println(enderecoEEPROM);

  Serial.println("Iniciando registro de temperatura DS18B20...");
  Serial.println("Comandos disponíveis:");
  Serial.println("  r - Ler dados salvos");
  Serial.println("  c - Limpar dados");
}

void loop() {
  if (millis() - ultimoMillis >= INTERVALO_MILIS) {
    ultimoMillis = millis();
    registrarTemperatura();
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

void registrarTemperatura() {
  if (enderecoEEPROM >= EEPROM.length() - 1) {
    Serial.println("Memória cheia!");
    return;
  }

  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);

  int16_t tempEscalada = (int16_t)(tempC * 10);

  // Escreve temperatura (2 bytes)
  EEPROM.update(ENDERECO_DADOS + enderecoEEPROM, tempEscalada & 0xFF);       // LSB
  EEPROM.update(ENDERECO_DADOS + enderecoEEPROM + 1, (tempEscalada >> 8));   // MSB

  // Atualiza ponteiro salvo na EEPROM
  enderecoEEPROM += 2;
  EEPROM.update(ENDERECO_CONTROLE, enderecoEEPROM & 0xFF);
  EEPROM.update(ENDERECO_CONTROLE + 1, (enderecoEEPROM >> 8));

  Serial.print("Salvo em ");
  Serial.print(enderecoEEPROM);
  Serial.print(": ");
  Serial.print(tempC);
  Serial.println(" °C");
}

void lerTemperaturasSalvas() {
  if (enderecoEEPROM == 0) {
    Serial.println("Nenhum dado salvo.");
    return;
  }

  for (int i = 0; i < enderecoEEPROM; i += 2) {
    byte lsb = EEPROM.read(ENDERECO_DADOS + i);
    byte msb = EEPROM.read(ENDERECO_DADOS + i + 1);
    int16_t tempEscalada = (msb << 8) | lsb;
    float tempReal = tempEscalada / 10.0;

    Serial.print("Leitura ");
    Serial.print(i / 2);
    Serial.print(": ");
    Serial.print(tempReal);
    Serial.println(" °C");
  }
}

void limparEEPROM() {
  Serial.println("Limpando dados da EEPROM...");

  for (int i = 0; i < EEPROM.length(); i++) {
    EEPROM.update(i, 0xFF);  // Apaga com valor padrão
  }

  enderecoEEPROM = 0;

  // Zera controle salvo
  EEPROM.update(ENDERECO_CONTROLE, 0);
  EEPROM.update(ENDERECO_CONTROLE + 1, 0);

  Serial.println("EEPROM limpa com sucesso.");
}