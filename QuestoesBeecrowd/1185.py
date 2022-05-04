matriz = []

opc = input()
ac = 0
media = 0
for l in range (0, 12):
    aux = []
    for c in range (0, 12):
        aux.append(float(input()))     
    matriz.append(aux)

for l in range(0, 12):
    for c in range(0, 12):
        if l+c<11:
            ac+=matriz[l][c]
media=ac/66
if opc=='S':
    print(f'{ac:.1f}')
else:
    print(f'{media:.1f}')