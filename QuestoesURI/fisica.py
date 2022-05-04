import math
import numpy as np

m = 1300
g = 9.8
N=0
v=0
nb = 0
nc = 0
ar = 0
at = 0
a = 0
vb = 0
vc = 0


h = float (input("Digite a altura: "))
R = float (input("Digite o Raio do looping (10 a 20m): "))
h=h*R

if h<=R:  
    ang = (np.arccos(1-(h/R)))
    ang = np.degrees(ang)
    N = m*g*(np.cos(np.radians(ang)))
    print(f"O carro não executa o looping;")
    print(f"O carro para em θ = {ang}")
    print(f"A força normal nessa posição é N = {N}")

elif R<=h<2.5*R:
    ang = np.degrees(np.arccos(((2/3)*(1-(h/R)))))
    v = math.sqrt(2/3*g*(h-R))
    
    print("O carro não executa o looping;")
    print(f"A força normal se anula em θ = {ang}")
    print(f"A velocidade do carro nesta posição é v = {v}")

elif h>=2.5*R:
    nb = m*g*((2*h/R)-5)
    nc = 2*m*g*((h/R)-1)
    ar = 2*g*((h/R)-1)
    at = g
    a = math.sqrt((at*at)+(ar*ar))
    vb = math.sqrt(2*g*(h-(2*R)))
    vc = math.sqrt(2*g*(h-(2*R)))
    
    print("O carro executa o looping;")
    print(f"A velocidade em B é vb = {vb}")
    print(f"A velocidade em C é vc = {vc}")
    print(f"A força normal em B é nb = {nb}")
    print(f"A força normal em B é nc = {nc}")
    print(f"A aceleração tangencial em C é at = {at}")
    print(f"A aceleração radial em C é ar = {ar}g")
    print(f"A aceleração resultante em C é a = {a}g")