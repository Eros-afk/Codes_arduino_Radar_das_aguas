import pandas as pd
import matplotlib.pyplot as plt

# Carregar o CSV (gerado pelo Arduino)
df = pd.read_csv("dados.csv")

# Converter tempo de ms para segundos
df["tempo_s"] = df["tempo_ms"] / 1000.0

# Gráfico 1: Nível da água (distância invertida) vs tempo
# Supondo altura do recipiente = 21 cm
ALTURA_RECIPIENTE = 21.0
df["nivel_agua"] = ALTURA_RECIPIENTE - df["distancia_cm"]

plt.figure()
plt.plot(df["tempo_s"], df["nivel_agua"], marker="o")
plt.xlabel("Tempo (s)")
plt.ylabel("Nível da água (cm)")
plt.title("Nível da água vs Tempo")
plt.grid(True)
plt.savefig("nivel_vs_tempo.png", dpi=300)

# Gráfico 2: Temperatura vs tempo
plt.figure()
plt.plot(df["tempo_s"], df["temperatura_C"], marker="o", color="red")
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura vs Tempo")
plt.grid(True)
plt.savefig("temperatura_vs_tempo.png", dpi=300)

plt.show()
