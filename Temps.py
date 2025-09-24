import matplotlib.pyplot as plt

# --- Dados de Temperatura (Extraídos da sua entrada) ---
# A estrutura é uma lista de tuplas, onde cada tupla representa uma Amostra:
# (Sensor 0, Sensor 1, Sensor 2)
dados_temperatura_brutos = [
    (85.00, 85.00, 85.00),  # Amostra 0 (Será descartada)
    (25.00, 25.00, 25.00),  # Amostra 1 (Será descartada)
    (25.00, 25.00, 25.00),  # Amostra 2 (Será descartada)
    (25.10, 25.00, 25.00),  # Amostra 3 (Será descartada)
    (25.10, 25.10, 25.00),  # Amostra 4 (Será descartada)
    (85.00, 25.10, 25.00),  # Amostra 5 (Será descartada)
    (25.10, 25.10, 25.10),  # Amostra 6 (Será descartada)
    (25.10, 25.10, 25.10),  # Amostra 7 (Será descartada)
    (25.30, 25.30, 25.20),  # Amostra 8 (Será descartada)
    (25.30, 25.60, 25.30),  # Amostra 9 (Será descartada)
    (25.30, 26.00, 25.50),  # Amostra 10 (Será descartada)
    (25.60, 26.50, 25.60),  # Amostra 11 (Será descartada)
    (26.00, 26.80, 25.90),  # Amostra 12 (Será descartada)
    (26.30, 27.30, 26.20),  # Amostra 13 (Será descartada)
    (26.70, 27.80, 26.50),  # Amostra 14 (Será descartada)
    # --- Início dos dados a serem plotados (Amostra 15 em diante) ---
    (27.10, 28.30, 26.90),  # Amostra 15 (Índice 15 no Python)
    (27.60, 28.90, 27.30),  # Amostra 16
    (28.00, 29.50, 27.70),  # Amostra 17
    (28.50, 30.00, 28.10),  # Amostra 18
    (29.00, 30.60, 28.60),  # Amostra 19
    (29.50, 31.10, 29.00),  # Amostra 20
    (29.80, 31.70, 29.50),  # Amostra 21
    (30.30, 32.30, 29.90),  # Amostra 22
    (30.80, 32.70, 30.40),  # Amostra 23
    (31.20, 33.10, 30.80),  # Amostra 24
    (31.60, 33.50, 31.20),  # Amostra 25
    (32.10, 33.80, 31.60),  # Amostra 26
    (32.50, 34.10, 31.90),  # Amostra 27
    (32.80, 34.30, 32.30),  # Amostra 28
    (33.20, 34.60, 32.50),  # Amostra 29
    (33.50, 34.80, 32.90),  # Amostra 30
    (33.80, 35.00, 33.10),  # Amostra 31
    (34.10, 35.10, 33.40),  # Amostra 32
    (34.50, 35.30, 33.60),  # Amostra 33
    (34.70, 35.50, 33.90),  # Amostra 34
    (35.00, 35.70, 34.10),  # Amostra 35
    (35.20, 35.90, 34.30),  # Amostra 36
    (35.40, 36.10, 34.60),  # Amostra 37
    (35.60, 36.30, 34.80),  # Amostra 38
    (35.80, 36.50, 35.00),  # Amostra 39
    (36.00, 36.60, 35.20),  # Amostra 40
    (36.20, 36.90, 35.50),  # Amostra 41
    (36.40, 37.10, 35.60),  # Amostra 42
    (36.60, 37.30, 35.80),  # Amostra 43
    (36.80, 37.50, 36.10),  # Amostra 44
    (37.00, 37.80, 36.30),  # Amostra 45
    (37.10, 37.90, 36.50),  # Amostra 46
    (37.30, 38.00, 36.70),  # Amostra 47
    (37.50, 38.10, 36.90),  # Amostra 48
    (37.60, 38.30, 37.10),  # Amostra 49
    (37.80, 38.50, 37.30),  # Amostra 50
    (38.00, 38.80, 37.50),  # Amostra 51
    (38.10, 39.00, 37.70),  # Amostra 52
    (38.30, 39.20, 37.90),  # Amostra 53
    (38.50, 39.50, 38.10),  # Amostra 54
    (38.60, 39.80, 38.30),  # Amostra 55
    (38.80, 40.00, 38.50),  # Amostra 56
    (39.00, 40.10, 38.80),  # Amostra 57
    (39.20, 40.10, 38.90),  # Amostra 58
    (39.40, 40.20, 39.10),  # Amostra 59
    (39.50, 40.40, 39.20),  # Amostra 60
    (39.60, 40.60, 39.40),  # Amostra 61
    (39.80, 40.70, 39.60),  # Amostra 62
    (40.00, 40.80, 39.70),  # Amostra 63
    (40.10, 40.80, 39.80),  # Amostra 64
    (40.20, 40.80, 40.00),  # Amostra 65
    (40.30, 40.80, 40.10),  # Amostra 66
    (40.40, 40.70, 40.10),  # Amostra 67
    (40.50, 40.80, 40.10),  # Amostra 68
    (40.60, 41.00, 40.30),  # Amostra 69
    (40.60, 41.30, 40.40),  # Amostra 70
    (40.70, 41.60, 40.60),  # Amostra 71
    (40.80, 42.00, 40.80),  # Amostra 72
    (41.00, 42.20, 41.00),  # Amostra 73
    (41.10, 42.30, 41.20),  # Amostra 74
    (41.30, 42.30, 41.30),  # Amostra 75
    (41.40, 42.20, 41.50),  # Amostra 76
    (41.50, 42.20, 41.60),  # Amostra 77
    (41.60, 42.20, 41.60),  # Amostra 78
    (41.70, 42.10, 41.70),  # Amostra 79
    (41.80, 42.10, 41.70),  # Amostra 80
    (41.80, 42.00, 41.80),  # Amostra 81
    (41.90, 42.10, 41.80),  # Amostra 82
    (41.90, 42.20, 41.80),  # Amostra 83
    (42.00, 42.40, 41.90),  # Amostra 84
    (42.00, 42.60, 42.00),  # Amostra 85
    (42.10, 42.60, 42.10),  # Amostra 86
    (42.20, 42.70, 42.30),  # Amostra 87
    (42.20, 42.70, 42.30),  # Amostra 88
    (42.30, 42.70, 42.40),  # Amostra 89
    (42.40, 42.70, 42.50),  # Amostra 90
    (42.50, 42.80, 42.50),  # Amostra 91
    (42.50, 42.80, 42.60),  # Amostra 92
    (42.50, 42.80, 42.60),  # Amostra 93
    (42.60, 42.70, 42.60),  # Amostra 94
    (42.60, 42.70, 42.70),  # Amostra 95
    (42.60, 42.70, 42.70),  # Amostra 96
    (42.70, 42.60, 42.70),  # Amostra 97
    (42.70, 42.60, 42.70),  # Amostra 98
    (42.70, 42.60, 42.70),  # Amostra 99
    (42.80, 42.80, 42.80),  # Amostra 100
    (42.80, 42.80, 42.80),  # Amostra 101
    (42.80, 42.80, 42.90),  # Amostra 102
    (42.90, 42.90, 43.00),  # Amostra 103
    (42.90, 42.90, 43.00),  # Amostra 104
    (43.00, 42.90, 43.00),  # Amostra 105
    (43.00, 42.80, 43.00),  # Amostra 106
    (43.00, 42.90, 43.10),  # Amostra 107
    (43.10, 43.10, 43.10),  # Amostra 108
    (43.10, 43.40, 43.20),  # Amostra 109
    (43.20, 43.70, 43.30),  # Amostra 110
    (43.30, 44.00, 43.50),  # Amostra 111
    (43.40, 44.30, 43.70),  # Amostra 112
    (43.50, 44.60, 43.90),  # Amostra 113
    (43.70, 45.00, 44.10),  # Amostra 114
    (43.80, 45.30, 44.40),  # Amostra 115
    (44.10, 45.60, 44.60),  # Amostra 116
    (44.20, 45.90, 44.90),  # Amostra 117
    (44.40, 46.10, 45.10),  # Amostra 118
    (44.60, 46.30, 45.30),  # Amostra 119
    (44.80, 46.30, 45.50),  # Amostra 120
    (44.90, 46.40, 45.60),  # Amostra 121
    (45.10, 46.50, 45.70),  # Amostra 122
    (45.20, 46.70, 45.80),  # Amostra 123
    (45.30, 46.80, 46.00),  # Amostra 124
    (45.50, 46.80, 46.10),  # Amostra 125
    (45.50, 46.70, 46.10),  # Amostra 126
    (45.60, 46.60, 46.20),  # Amostra 127
    (45.70, 46.80, 46.20),  # Amostra 128
    (45.80, 47.00, 46.30),  # Amostra 129
    (45.90, 47.10, 46.50),  # Amostra 130
    (46.00, 47.20, 46.60),  # Amostra 131
    (46.10, 47.20, 46.60),  # Amostra 132
    (46.10, 47.10, 46.80),  # Amostra 133
    (46.20, 47.10, 46.80),  # Amostra 134
    (46.30, 47.10, 46.80),  # Amostra 135
    (46.30, 47.10, 46.90),  # Amostra 136
    (46.40, 47.30, 47.00),  # Amostra 137
    (46.50, 47.50, 47.10),  # Amostra 138
    (46.50, 47.70, 47.10),  # Amostra 139
    (46.60, 47.90, 47.30),  # Amostra 140
    (46.70, 48.10, 47.50),  # Amostra 141
    (46.80, 48.30, 47.60),  # Amostra 142
    (47.00, 48.50, 47.80),  # Amostra 143
    (47.10, 48.60, 48.00),  # Amostra 144
    (47.20, 48.60, 48.10),  # Amostra 145
    (47.30, 48.50, 48.20),  # Amostra 146
    (47.50, 48.60, 48.30),  # Amostra 147
    (47.50, 48.60, 48.30),  # Amostra 148
    (47.60, 48.60, 48.40),  # Amostra 149
    (47.70, 48.80, 48.50),  # Amostra 150
    (47.80, 49.00, 48.60),  # Amostra 151
    (47.80, 49.10, 48.70),  # Amostra 152
    (48.00, 49.30, 48.80),  # Amostra 153
    (48.00, 49.50, 49.00),  # Amostra 154
    (48.20, 49.60, 49.10),  # Amostra 155
    (48.30, 49.70, 49.20),  # Amostra 156
    (48.40, 49.90, 49.40),  # Amostra 157
    (48.50, 50.10, 49.50),  # Amostra 158
    (48.60, 50.20, 49.70),  # Amostra 159
    (48.70, 50.40, 49.80),  # Amostra 160
    (48.80, 50.50, 50.00),  # Amostra 161
    (49.00, 50.60, 50.10),  # Amostra 162
    (49.10, 50.50, 50.20),  # Amostra 163
    (49.10, 50.50, 50.30),  # Amostra 164
    (49.20, 50.50, 50.30),  # Amostra 165
    (49.30, 50.60, 50.30),  # Amostra 166
    (49.30, 50.60, 50.40),  # Amostra 167
    (49.40, 50.70, 50.50),  # Amostra 168
    (49.50, 50.90, 50.60)   # Amostra 169
]

# Número de amostras a descartar (0 a 14, total de 15)
AMOSTRAS_A_DESCARTAR = 15

# --- Processamento dos dados ---

# 1. Descartar as primeiras 15 amostras
dados_filtrados = dados_temperatura_brutos[AMOSTRAS_A_DESCARTAR:]

# 2. Separar os dados por sensor
# Desembalar os dados em listas separadas para cada sensor
sensor0_temp = [amostra[0] for amostra in dados_filtrados]
sensor1_temp = [amostra[1] for amostra in dados_filtrados]
sensor2_temp = [amostra[2] for amostra in dados_filtrados]

# 3. Criar a lista de índices das amostras (eixo X)
# O primeiro índice (0) corresponde à Amostra 15 original, 
# o último corresponde à Amostra 169 original.
num_amostras_plotadas = len(dados_filtrados)
indices_amostra = list(range(AMOSTRAS_A_DESCARTAR, AMOSTRAS_A_DESCARTAR + num_amostras_plotadas))


# --- Plotagem do Gráfico ---

plt.figure(figsize=(12, 6)) # Define o tamanho da figura (largura, altura)

# Plota as linhas
plt.plot(indices_amostra, sensor0_temp, label='Sensor 0', marker='.', linestyle='-')
plt.plot(indices_amostra, sensor1_temp, label='Sensor 1', marker='.', linestyle='-')
plt.plot(indices_amostra, sensor2_temp, label='Sensor 2', marker='.', linestyle='-')

# Adiciona título e rótulos
plt.title('Variação de Temperatura dos Sensores (Amostras 15 a 169)')
plt.xlabel('Número da Amostra (Início na Amostra 15)')
plt.ylabel('Temperatura (°C)')

# Adiciona legenda para identificar os sensores
plt.legend()

# Adiciona uma grade para melhor visualização
plt.grid(True, linestyle='--', alpha=0.6)

# Exibe o gráfico
plt.show()