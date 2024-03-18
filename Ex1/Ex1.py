"""
2
1 1
8 6
6 8
1 3
"""


import sys # biblioteca de sistema p/ leitura de arquivos
import math # biblioteca p/ funções matemáticas

data = [int(i) for i in sys.stdin.read().split()]

"""
stdin = standard input = padrão de entrada
read = ler
split = dividir como (), dividir quando encontrar espaço em branco
"""

# quantidade de grupos = primeiro elemento da lista de dados
groups = data[0]

# trabalhar com a lista de dados, retirando a quantidade de grupos, evitando uma nova variável
data.pop(0)
coords = []

# for iniciando a lista do 0, indo até o tamanho da lista, pulando de 2 em 2
for pos in range(0, len(data), 2):
    coords.append([data[pos], data[pos + 1]])

distances = []
for i in range(0, 2 * groups - 1): # 0, 1, 2
    for j in range(i + 1, 2 * groups): # 1 2 3
        p1 = coords[i]
        p2 = coords[j]
        distances.append(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

"""
** = elevado, então **2  elevado a 2
p1[0] é o valor de x do ponto
p1[1] é o valor de y do ponto
"""

# ordenar as distâncias - sort
distances.sort()

custo = sum(distances[0:groups])

print(f"{custo:.2f}")

"""
.2f = duas casas após a vírgula
f = float = flutuante = após a vírgula
"""