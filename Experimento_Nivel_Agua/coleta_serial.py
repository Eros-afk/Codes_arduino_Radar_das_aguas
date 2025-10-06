import serial
import time
import csv

# CONFIGURAÇÃO
PORTA = "COM3"
BAUD = 115200
ARQUIVO = "dados.csv"

# CONEXÃO SERIAL
ser = serial.Serial(PORTA, BAUD, timeout=1)
time.sleep(2)  # tempo para Arduino resetar

# CABEÇALHO CSV
with open(ARQUIVO, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["tempo_ms", "temperatura_C", "distancia_cm"])

print("Coletando dados do Arduino... (CTRL+C para parar)")

try:
    with open(ARQUIVO, mode="a", newline="") as f:
        writer = csv.writer(f)
        while True:
            linha = ser.readline().decode("utf-8").strip()
            if linha:
                try:
                    # Linha já no formato CSV do Arduino:
                    # tempo_ms,temperatura_C,distancia_cm
                    valores = linha.split(",")
                    if len(valores) == 3:
                        writer.writerow(valores)
                        print(valores)
                except Exception as e:
                    print("Linha inválida:", linha)
except KeyboardInterrupt:
    print("\nColeta encerrada.")
    ser.close()
