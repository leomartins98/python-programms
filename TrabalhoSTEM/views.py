from tkinter import *
from arquivo import *

arq = "banco.txt"

janela = Tk()

def cadastro ():
    texto_resposta_cadastro = Label(janela, text="")
    
    label_nome = Label(janela, text="Nome: ")
    textbox_nome = Entry(janela)
    label_idade = Label(janela, text="Idade ")
    textbox_idade = Entry(janela)
    button_register = Button(janela, text="Cadastrar", command = lambda : cadastrar(arq, textbox_nome.get(), textbox_idade.get(), texto_resposta_cadastro))

    label_nome.grid(row=3, column=0)
    textbox_nome.grid(row=3, column=1)
    label_idade.grid(row=4, column=0)
    textbox_idade.grid(row=4, column=1)
    button_register.grid(row=5, column=1)
    texto_resposta_cadastro.grid(column=0, row=6, padx=10, pady=10)

janela.title('Cadastro de Pessoas')

texto_resposta_lista = Label(janela, text="")

botao = Button(janela, text="Visualizar pessoas cadastradas", command = lambda:lerArquivo(arq, texto_resposta_lista))

botao2 = Button(janela, text="Cadastrar novas pessoas", command = cadastro)

botao.grid(column=0, row=1, padx=10, pady=10)
botao2.grid(column=0, row=2, padx=10, pady=10)
texto_resposta_lista.grid(column=0, row=7, padx=10, pady=10)

janela.mainloop()