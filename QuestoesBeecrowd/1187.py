matriz = []

opc = input()
ac = 0
media = 0
d=0

for l in range (0, 12):
    aux = []
    for c in range (0, 12):
        aux.append(float(input()))     
    matriz.append(aux)

for l in range(0, 12):
    for c in range(0, 12):
        if c>l and c+l<11:
            ac+=matriz[l][c]
            d+=1
media=ac/d
if opc=='S':
    print(f'{ac:.1f}')
else:
    print(f'{media:.1f}')