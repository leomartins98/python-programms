import random 
x=True
while x==True:
    x = int(input("Aperte 1 para gerar uma senha de 8 dígitos\nDigite -1 para sair\n"))
    if x==1:
        print(random.randint(10000000, 10000000000))
        x==True
    else:
        x==False
    