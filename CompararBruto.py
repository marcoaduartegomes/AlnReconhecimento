import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.image as pimg
import os
import json
#Numero utilizado para comparar as normas
comparative = 99999999999


diretorio = ""
diretorioNovo = "recdev/comparar/"
def fotoNum(c,caminho):
    your_path = caminho
    files = os.listdir(your_path)
    keyword = '-'
    y = ""
    contador = 0
    for file in files:
        for x in file:
            if keyword in x:
                y = grupo(file)
                if c==y:
                    contador = contador +1
    return contador



# agrupa em conjuntos cada grupo das fotos, fazendo validação cruzada, escolhendo um numero aleatorio para teste
# e o resto para comparação
def conjuntos(mapeamento,caminho, ext):
    global diretorio , diretorioNovo
    diretorio = caminho
    conjuntoTreino = mapeamento
    for c in conjuntoTreino:
        quantidade = fotoNum(c,caminho)
        for i in range(0,quantidade):
            arquivo = c + '-' + str(i+1) + ext
            # onde ocorre a separação de teste ou treino
            conjuntoTreino[c] = np.ndarray.tolist(np.append(arquivo, conjuntoTreino[c]))
    print(conjuntoTreino)
    return conjuntoTreino

def conjuntosdois(mapeamento,caminho, ext):
    global diretorio , diretorioNovo
    conjuntoTeste = {'original': []}
    conjuntoTreino = mapeamento
    for c in conjuntoTreino:
        quantidade = fotoNum(c,caminho)
        for i in range(0,quantidade):
            arquivo = c + '-' + str(i+1) + ext
            # onde ocorre a separação de teste ou treino
            conjuntoTeste['original'] = np.ndarray.tolist(np.append(arquivo, conjuntoTeste['original']))
    print(conjuntoTeste)
    return  conjuntoTeste


# usa o split para separar os dados das fotos que tem formado Numero - numero
def grupo(foto):
    return foto.split("-")[0]


#compara a img do teste com todas a do treino, retornando a que tem a menor norma de diferença.
def grupoBruto(img,conjuntoTreino):
    diferenca = comparative
    result = []
    group = 0
    for c in conjuntoTreino:
        for i in conjuntoTreino[c]:
            comparar = pimg.imread(diretorio + i)
            normal = np.linalg.norm(img[:,:,0:3]-comparar[:,:,0:3])
            if normal < diferenca:
                diferenca = normal
                result = comparar
                group = c
    return diferenca, result, group


def reconhecimentoBruto(conjuntoTeste,conjuntoTreino,dados):
    erro = 0
    acerto = 0
    salvando = 0
    for foto in conjuntoTeste['original']:
        salvando = salvando +1
        img = pimg.imread(diretorioNovo + foto)
        norma, result, group = grupoBruto(img,conjuntoTreino)
        if grupo(foto) == str(group):
            acerto = acerto + 1
        else:
            erro = erro + 1
        if (dados == 1):
            if grupo(foto) == str(group):
                print("Igual")
            else:
                print("Diferente: " + grupo(foto) + " != " + str(group))
                #Sub plot padrao encontrado na internet
            f, (esquerda, direita) = plt.subplots(1, 2, figsize=(10,5))
            if grupo(foto) == str(group):
                f.suptitle('Igual')
            else:
                f.suptitle('Diferente')
            esquerda.imshow(img)
            esquerda.set_title('Grupo = ' + grupo(foto))
            direita.imshow(result)
            direita.set_title('Grupo = ' + str(group))
            plt.show()
            #plt.savefig(str(salvando) + '.jpg')
    print("Erros :",erro)
    print("Acertos :",acerto)
    return ((acerto)/(acerto+erro))*100.





def teste(base,base2,PATH,PATH2,fotos,vezes,ext):
    taxa = 0
    t = vezes
    for i in range(t):
        conjuntoTreino = {}
        conjuntoTeste = {}
        nulo = {}
        conjuntoTreino = conjuntos(base, 'recdev/' + PATH + '/', ext)
        conjuntoTeste = conjuntosdois(base2, 'recdev/' + PATH2 + '/', ext)
        taxa = taxa + reconhecimentoBruto(conjuntoTeste,conjuntoTreino,fotos)
    print("Teste com base : "+PATH+" "+str(taxa/t) + "% de acerto medio   (Teste rodado "+str(t)+"x)")

# função para criar uma base de dados tipo json, para facilitar a criação dos testes e treinos

def jsons(PATH):
    your_path = 'recdev/'+PATH
    files = os.listdir(your_path)
    keyword = '-'
    y = ""
    for file in files:
        for x in file:
            if keyword in x:
                y = y + '"'+grupo(file)+ '" : [],'
    y = y[0:len(y)-1]
    y = "{"+y+"}"

    data  = json.loads(y)
    return data

teste(jsons('very-easy'),jsons('comparar'),"very-easy","comparar",1,1,'.jpg')
#teste(jsons('easy'),"easy",1,1,'.jpg')
#teste(jsons('diferente'),"diferente",0,4,'.jpg')
#teste(jsons("medium"),"medium",0,4,'.jpg')
#teste(jsons("extras/facebookfaces/crop-inner"),"extras/facebookfaces/crop-inner",0,4,'.jpg')
#teste(jsons("extras/facebookfaces/crop-outer"),"extras/facebookfaces/crop-outer",0,4,'.jpg')
#teste(jsons("extras/facebookfaces/crop-inner"),"extras/facebookfaces-2/crop-inner",0,4,'.png')
#teste(jsons("extras/facebookfaces/crop-outer"),"extras/facebookfaces-2/crop-outer",0,4,'.png')
#teste(jsons("uerj/novo"),"uerj/novo",0,4,'.jpg')

#teste(jsons('very-easy'),"very-easy",1,1,'.jpg')
#teste(jsons('easy'),"easy",1,1,'.jpg')
#teste(jsons('diferente'),"diferente",1,1,'.jpg')
#teste(jsons("medium"),"medium",1,1,'.jpg')
#teste(jsons("extras/facebookfaces/crop-inner"),"extras/facebookfaces/crop-inner",1,1,'.jpg')
#teste(jsons("extras/facebookfaces/crop-outer"),"extras/facebookfaces/crop-outer",1,1,'.jpg')
#teste(jsons("extras/facebookfaces/crop-inner"),"extras/facebookfaces-2/crop-inner",1,1,'.png')
#teste(jsons("extras/facebookfaces/crop-outer"),"extras/facebookfaces-2/crop-outer",1,1,'.png')
#teste(jsons("uerj/novo"),"uerj/novo",1,1,'.jpg')
