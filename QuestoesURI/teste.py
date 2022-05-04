total_cidade = int(input())

matriz = []
for i in range (0, total_cidade):
    aux = []
    for j in range (0, total_cidade):
        if i==j:
            aux.append(0)
        elif i<j:
            aux.append(int(input()))
        elif i>j:
            aux.append(matriz[j][i])
    matriz.append(aux)

rota = int(input())
guarda_rota = []
somatorio = 0

for b in range(rota):
    guarda_rota.append(int(input()))

c=0
while guarda_rota[c]!=guarda_rota[len(guarda_rota)-1]:
    somatorio+=matriz[guarda_rota[c]-1][guarda_rota[c+1]-1]
    c+=1

somatorio+=matriz[guarda_rota[0]-1][guarda_rota[-1]-1]


diesel = 0
diesel = float(input())
valortotal = 0

valortotal = (somatorio/3)*diesel

print(f"R$ {valortotal:.2f}")