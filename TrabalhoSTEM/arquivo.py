from interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome, texto_resposta):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        texto_resposta["text"]='Não conseguimos criar o arquivo. F total!'
    else: 
        texto_resposta["text"]=f'''Arquivo {nome} criado com sucesso! Vamo família!'''

def lerArquivo(nome, texto_resposta_lista):
    try:
        a = open(nome, 'rt')
    except:
        texto_resposta_lista["text"]='Erro ao ver as pessoas cadastradas. :('
    else:
        texto_resposta_lista["text"]=a.read()
            

def cadastrar(arq, nome, idade, texto_resposta_cadastro):
    try:
        a = open(arq, 'at')
    except:
        texto_resposta_cadastro["text"]='Erro ao cadastrar nova pessoa. :('
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            texto_resposta_cadastro["text"]='Aconteceu um erro na hora de alocar ao arquivo'
        else:
            texto_resposta_cadastro["text"]='Usuário cadastrado com sucesso.'
            a.close()               
