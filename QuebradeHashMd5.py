#Item 1 #############################################################################################################
import hashlib
from random import randint
def cadastrar(nome,senha):
    senhaReal = senha
    senhaHash = (hashlib.md5(senhaReal.encode('utf-8')).hexdigest())
    with open("UsuariosCadastrados.txt", "a") as stream:  # usa "w" para não armazenar mais de 1 palavra
        print(nome, senhaHash, file=stream)

def md5(senha):
    senhaNova = (hashlib.md5(senha.encode('utf-8')).hexdigest())
    return senhaNova

def autenticar(nome,senha):
    if nome in listaUsu:
        z = listaUsu.index(nome)
        if senha == listaUsu[z+1]:
            print("Autentificacao efetuada com sucesso. Bem vindo ", nome)
        else:
            print("Nome ou senha invalidos.")
    else:
        print("Nome ou senha invalidos.")
listaUsu = []
listaHash = []
a = 1
while a == 1:
    nomeCadast = input("Digite um nome (de 4 caracteres) para cadastro: ")
    senhaCadast = input("Digite uma senha (de 4 caracteres) para cadastro: ")
    ativa = 1
    if ativa ==1:
        if (len(nomeCadast) or len(senhaCadast)) >4:
            print("Nome ou Senha digitado esta fora dos limites.")
        else:
            listaUsu.append(nomeCadast)
            listaUsu.append(senhaCadast)
            senhaHash = md5(senhaCadast)
            listaHash.append(senhaHash)
            cadastrar(nomeCadast, senhaCadast)
    a = int(input("Digite (0) se quiser parar de fazer cadastros, ou (1) para continuar: "))

fazer = int(input("Digite (1) se deseja autentificar, ou (0) para sair: "))
if fazer == 1:
    nomeAutent = input("Digite seu nome para Login: ")
    senhaAutent = input("Digite sua senha para Login: ")
    autenticar(nomeAutent,senhaAutent)
print("\n")

##Item 2: quebra md5 ################################################################################################
#import hashlib
import string
import datetime
from datetime import timedelta
def quebraMd5(senha1,senha2,senha3,senha4):
    hashes = [senha1, senha2, senha3, senha4]
    startTime = datetime.datetime.now()
    tempo_comeco = datetime.datetime.now()
    x = 0
    # diminui = timedelta(seconds=1) --> SE QUISER DIMINUIR UM TEMPO DETERMINADO
    for a in string.printable:
        for b in string.printable:
            for c in string.printable:
                for d in string.printable:
                    word = a + b + c + d
                    hash = hashlib.md5(word.encode("utf-8")).hexdigest()
                    # print(str(hash))
                    if hash in hashes:
                        end_time = str(datetime.datetime.now() - startTime).split('.')[0]
                        print("Senha Hash quebrada com sucesso!!")
                        print("Senha original: ", word)
                        print("Codigo HASH: ", hash)
                        print("Tempo necessário: ", end_time)
                        print("\n")
                        startTime = datetime.datetime.now()
                        x = x + 1
                        if x >= len(hashes):
                            tempo_final = str(datetime.datetime.now() - tempo_comeco).split('.')[0]
                            print("Tempo total: ", tempo_final)
                            break

senha1 = listaHash[0]
senha2 = listaHash[1]
senha3 = listaHash[2]
senha4 = listaHash[3]
quebraMd5(senha1,senha2,senha3,senha4)

#Item 3 ##############################################################################################################
def crip(texto,chave): #pode usar numeros tbm
    aq = []
    for cont in range (len(texto)):
        if texto[cont] == (chr(32)) or (chr(97)<=texto[cont]<=chr(122)):
            if texto[cont] == " ":
                aq.append(" ")
            else:
                crip = ord(texto[cont])
                if chr(crip+chave) <= chr(122):
                    crip = chr(crip + chave)
                    aq.append(crip)
                elif chr(crip+chave) > chr(122):
                    numero = (crip + chave)
                    numero = numero - 122
                    crip = chr(96 + numero)
                    aq.append(crip)
        if chr(48)<=texto[cont]<=chr(57):
            crip = ord(texto[cont])
            if chr(crip+chave) <= chr(57):
                crip = chr(crip+chave)
                aq.append(crip)
            elif chr(crip+chave) > chr(57):
                numero = (crip+chave)
                numero = numero - 57
                crip = chr(47 + numero)
                aq.append(crip)
    aq = "".join(aq)
    return(aq)
chaveRandom1 = randint(1,9)
senhaProte1 = crip(senha1,chaveRandom1)
chaveRandom2 = randint(1,9)
senhaProte2 = crip(senha2,chaveRandom2)
chaveRandom3 = randint(1,9)
senhaProte3 = crip(senha3,chaveRandom3)
chaveRandom4 = randint(1,9)
senhaProte4 = crip(senha4,chaveRandom4)
with open("HASHSModificados.txt", "a") as stream:  # usa "w" para não armazenar mais de 1 palavra
    print(senhaProte1, senhaProte2, senhaProte3, senhaProte4, file=stream)
print("\n")
print(f"Novo Hash Protegido de {listaUsu[0]} - {senhaProte1}")
print(f"Novo Hash Protegido de {listaUsu[2]} - {senhaProte2}")
print(f"Novo Hash Protegido de {listaUsu[4]} - {senhaProte3}")
print(f"Novo Hash Protegido de {listaUsu[6]} - {senhaProte4}")