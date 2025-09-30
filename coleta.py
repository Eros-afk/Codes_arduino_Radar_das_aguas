import serial
import time
import csv

# --- Configuração da porta ---
PORTA = "COM3"   # troque para a porta do seu Arduino (ex: /dev/ttyUSB0 no Linux)
BAUD = 9600

# --- Arquivo CSV ---
ARQUIVO = "dados.csv"

# --- Conexão Serial ---
ser = serial.Serial(PORTA, BAUD, timeout=1)
time.sleep(2)  # tempo para Arduino resetar

# --- Cabeçalho do CSV ---
with open(ARQUIVO, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["tempo(s)", "temperatura(C)", "distancia(cm)", "nivel(cm)"])

print("Coletando dados... (CTRL+C para parar)")

inicio = time.time()

try:
    with open(ARQUIVO, mode="a", newline="") as f:
        writer = csv.writer(f)
        while True:
            linha = ser.readline().decode("utf-8").strip()
            if linha:
                try:
                    # Exemplo de saída do Arduino:
                    # Temp (C): 25.3 | Distancia (cm): 10.4 | Nivel (cm): 19.6
                    partes = linha.replace(" ", "").split("|")
                    temp = float(partes[0].split(":")[1])
                    dist = float(partes[1].split(":")[1])
                    nivel = float(partes[2].split(":")[1])
                    tempo_atual = round(time.time() - inicio, 2)

                    writer.writerow([tempo_atual, temp, dist, nivel])
                    print(tempo_atual, temp, dist, nivel)
                except Exception as e:
                    print("Linha inválida:", linha)
except KeyboardInterrupt:
    print("\nColeta encerrada.")
    ser.close()
