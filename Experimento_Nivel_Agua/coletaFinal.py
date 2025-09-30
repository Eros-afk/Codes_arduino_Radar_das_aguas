import serial
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO ---
PORTA = "COM3"      # Altere para sua porta COM
BAUD = 9600
ARQUIVO = "dados.csv"
ALTURA_RECIPIENTE = 30.0  # cm

# --- CONEXÃO SERIAL ---
ser = serial.Serial(PORTA, BAUD, timeout=1)
time.sleep(2)  # tempo para Arduino resetar

# --- CABEÇALHO CSV ---
with open(ARQUIVO, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["tempo_ms", "temperatura_C", "distancia_cm"])

print("Coletando dados do Arduino... (CTRL+C para parar)")

# --- COLETA SERIAL ---
try:
    with open(ARQUIVO, mode="a", newline="") as f:
        writer = csv.writer(f)
        while True:
            linha = ser.readline().decode("utf-8").strip()
            if linha:
                # Ignora linhas de cabeçalho repetidas
                if "tempo_ms" in linha:
                    continue
                try:
                    valores = linha.split(",")
                    if len(valores) == 3:
                        writer.writerow(valores)
                        print(valores)
                except Exception:
                    print("Linha inválida:", linha)
except KeyboardInterrupt:
    print("\nColeta encerrada.")
    ser.close()

# --- ANÁLISE E GRÁFICOS ---
print("Gerando gráficos...")

df = pd.read_csv(ARQUIVO)

# Converter colunas para numérico (remove possíveis strings)
df["tempo_ms"] = pd.to_numeric(df["tempo_ms"], errors="coerce")
df["temperatura_C"] = pd.to_numeric(df["temperatura_C"], errors="coerce")
df["distancia_cm"] = pd.to_numeric(df["distancia_cm"], errors="coerce")
df.dropna(inplace=True)

# Tempo em segundos
df["tempo_s"] = df["tempo_ms"] / 1000.0

# Nível da água
df["nivel_agua"] = ALTURA_RECIPIENTE - df["distancia_cm"]

# Gráfico 1: Nível vs Tempo
plt.figure()
plt.plot(df["tempo_s"], df["nivel_agua"], marker="o")
plt.xlabel("Tempo (s)")
plt.ylabel("Nível da água (cm)")
plt.title("Nível da água vs Tempo")
plt.grid(True)
plt.savefig("nivel_vs_tempo.png", dpi=300)

# Gráfico 2: Temperatura vs Tempo
plt.figure()
plt.plot(df["tempo_s"], df["temperatura_C"], marker="o", color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura vs Tempo")
plt.grid(True)
plt.savefig("temperatura_vs_tempo.png", dpi=300)

plt.show()
print("Gráficos gerados com sucesso!")
