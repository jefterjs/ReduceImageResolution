import os
import sys
import time
from PIL import Image


# Função para verificar se diretório existe, caso nao, cria a pasta
def create_folder(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)


def reduzir_resolucao_img(diretorio, img):
    dirimg = diretorio + '\\' + img
    largura_desejada = 1000
    im = Image.open(dirimg)
    largura_imagem = im.size[0]
    altura_imagem = im.size[1]
    percentual_largura = float(largura_desejada) / float(largura_imagem)
    altura_nova = int((altura_imagem * percentual_largura))
    size = largura_desejada, altura_nova

    dirimgnew = diretorio + r'\results' + '\\' + img
    create_folder(diretorio + r'\results')

    im = im.resize(size, Image.ANTIALIAS)
    im.save(dirimgnew)


def main():
    lista = []
    dircurrent = os.getcwd()
    dir_imags = dircurrent  # r"C:\Users\XXXX\Pictures\Resolução Normal"
    #  Ler arquivos no diretório selecionado
    caminhos = [os.path.join(dir_imags, nome) for nome in os.listdir(dir_imags)]
    arqs = [arq for arq in caminhos if os.path.isfile(arq)]
    #  Percorre arquivos do diretório e armazena somente imagens em uma lista
    for arq in arqs:
        nomearq = arq.replace(dir_imags, '').replace('\\', '').lower()
        if nomearq.find('.jpg') > 0 or nomearq.find('.jpeg') > 0 or nomearq.find('.png') > 0:
            lista.append(nomearq)
    #  Percorre lista fazendo conversão
    for img in lista:
        reduzir_resolucao_img(dir_imags, img)


if __name__ == '__main__':
    try:
        main()
        print("Finalizado com sucesso!!!")
        time.sleep(0.5)

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print("Error ao converter dados para inteiro.")
    except Exception:
        print("Error desconhecido:", sys.exc_info()[0])
        raise

