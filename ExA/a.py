import sys

"""
5 3
1 2
0 4
0 2
"""

data = sys.stdin.read().split('\n')
command = data[0].split()
data.pop(0)

teclas = [int(i) for i in range(int(command[0]))]
notes = [1 for i in teclas]

for i in range(int(command[1])):
    line = data[i].split()
    de = int(line[0])
    para = int(line[1])
    indexespercorrer = [i for i in range(de, para+1)]
    valorespercorrer = notes[de:para+1]
    maisrepete = None
    for j in valorespercorrer:
        print(j)
        if maisrepete == None:
            maisrepete = j
        if valorespercorrer.count(j) > valorespercorrer.count(maisrepete):
            maisrepete = j
        if valorespercorrer.count(j) == valorespercorrer.count(maisrepete):
            maisrepete = max(j, maisrepete)
    for k in indexespercorrer:
        notes[k] = (notes[k] + maisrepete)%9

print(notes)
# for i in range(0, len(notes)):
#     print(notes[i])