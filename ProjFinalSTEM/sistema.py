usu = f"{nomeusu}.txt"

def usuExiste(usu):
    try:
        a = open(usu, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def RotinaUsu(usu, texto_resposta_lista):
    try:
        a = open(usu, 'rt')
    except:
        print('Erro ao ver as rotinas do usuário. :(')
    else:
        print(a.read())
            

def CadRotina(usu, rotina, hora, texto_resposta_cadastro):
    try:
        a = open(usu, 'at')
    except:
        print('Erro ao abrir as rotinas anteriores! :(')
    else:
        try:
            a.write(f'{hora} - {rotina}\n')
        except:
            print('Aconteceu um erro ao alocar a rotina do usuário')
        else:
            print('Rotina cadastrada com sucesso.')
            a.close()               
