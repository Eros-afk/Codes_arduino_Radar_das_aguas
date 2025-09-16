#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "Adafruit_VL53L0X.h"

// --- Configurações dos Pinos I2C para o ESP8266 (NodeMCU/Wemos) ---
#define I2C_SDA 4 // GPIO4 (geralmente o pino D2)
#define I2C_SCL 5 // GPIO5 (geralmente o pino D1)

// --- Configurações do Display OLED ---
#define SCREEN_WIDTH 128 // Largura do display em pixels
#define SCREEN_HEIGHT 64 // Altura do display em pixels
#define OLED_RESET      -1 // Pino de reset (-1 se não for usado)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// --- Objeto para o Sensor VL53L0X ---
Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200); // Inicia a serial para debug

  // --- Inicia a comunicação I2C nos pinos específicos do ESP8266 ---
  Wire.begin(I2C_SDA, I2C_SCL);

  // --- Inicia o Display OLED ---
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("Falha ao iniciar o display OLED"));
    while(true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("Iniciando sensor...");
  display.display();

  // --- Inicia o Sensor VL53L0X ---
  if (!lox.begin()) {
    Serial.println(F("Falha ao iniciar o sensor VL53L0X"));
    display.clearDisplay();
    display.setCursor(0,0);
    display.println("Falha no Sensor!");
    display.display();
    while(true);
  }
  
  Serial.println(F("ESP8266: Sensor e Display prontos!"));
  delay(1000);
}

void loop() {
  VL53L0X_RangingMeasurementData_t measure;
    
  lox.rangingTest(&measure, false);

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Distancia:");
  display.drawFastHLine(0, 10, display.width(), SSD1306_WHITE);

  if (measure.RangeStatus != 4) {
    // Calcula a distância em cm e m
    float distancia_cm = measure.RangeMilliMeter / 10.0;
    float distancia_m = measure.RangeMilliMeter / 1000.0;
    
    // Exibe em CENTIMETROS (fonte grande)
    display.setCursor(10, 20);
    display.setTextSize(3);
    display.print(distancia_cm);
    display.setTextSize(1);
    display.print(" cm");
    
    // Exibe em METROS (fonte pequena)
    display.setCursor(10, 50);
    display.setTextSize(2);
    display.print("(");
    display.print(distancia_m, 2); // 2 casas decimais para metros
    display.print(" m)");
  } else {
    display.setCursor(15, 35);
    display.setTextSize(2);
    display.println("FORA DE");
    display.setCursor(15, 50);
    display.println("ALCANCE");
  }

  display.display();

  delay(100);
}