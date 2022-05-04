from interface import *
from time import sleep
from arquivo import *

arq = 'banco.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas','Ver Pessoas','Sair'])
    if resposta == 1:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = str(input("Idade: "))
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        print('Adeus!')
        sleep(2)
        break
    else:
        print('Digita um número correto, irmão!')
    sleep(2)
        