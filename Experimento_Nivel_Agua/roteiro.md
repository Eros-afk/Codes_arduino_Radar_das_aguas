# Roteiro do experimento HC-SR04 medindo nível da água

### 1. Preparação

* Materiais: recipiente (balde/cisterna), HC-SR04, Arduino, protoboard, fios, régua, torneira ou válvula para drenar.
* Fixe o sensor **na parte superior**, apontado para baixo, alinhado ao centro do recipiente.
* Meça a **distância do sensor até o fundo** do recipiente (altura total (H)).

---

### 2. Calibração inicial

* Com o recipiente vazio, registre a leitura do sensor (deve ser próxima de (H)).
* Coloque volumes conhecidos (ex.: 1 L, 2 L, 3 L) e confira se a leitura do sensor bate com a régua.
* Anote valores para montar uma tabela de calibração.

---

### 3. Execução do teste

1. Encha o recipiente até **3 L** (ou até uma altura conhecida).
2. Espere **2 minutos** para a superfície da água estabilizar.
3. Comece a coleta de dados:

   * Arduino envia medidas de distância a cada **0,1 s (10 Hz)** para o PC (Serial Monitor ou salvando em CSV).
4. Abra a torneira e deixe a água drenar naturalmente.
5. Continue coletando dados até o recipiente esvaziar.

---

### 4. Repetição

* Repita o procedimento pelo menos **3 vezes** para ter dados confiáveis.
* Em cada repetição, anote temperatura ambiente (influencia na velocidade do som).

---

### 5. Registro

* Tire **fotos da montagem** (sensor, recipiente, torneira).
* Tire **foto do nível inicial e final** da água.
* Salve os dados em planilha (tempo vs distância).

---

### 6. Análise

1. Converta distância do sensor em **nível de água**:
   [
   \text{Nível} = H - d
   ]
   onde (d) = distância medida, (H) = altura sensor-fundo.
2. Plote gráfico: **nível de água (cm) × tempo (s)**.
3. Se quiser, calcule **vazão média** observando a inclinação do gráfico.

---

### 7. Resultados no artigo

* Coloque:

  * **Foto da montagem**.
  * **Tabela com valores exemplo** (tempo, distância, nível).
  * **Gráfico nível × tempo**.
* Explique: o sensor detecta a variação do nível conforme a água escoa.
* Discuta: limitações (espuma, ângulo, temperatura).

---