import sys
import math

data = [int(i) for i in sys.stdin.read().split()]

groups = data[0]

data.pop(0)
coords = []

for pos in range(0, len(data), 2):
    coords.append([data[pos], data[pos + 1]])

distances = []
for i in range(0, 2 * groups - 1):
    for j in range(i + 1, 2 * groups):
        p1 = coords[i]
        p2 = coords[j]
        distances.append(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

distances.sort()

custo = sum(distances[0:groups])

print(f"{custo:.2f}")