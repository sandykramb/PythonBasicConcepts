largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"


def retângulo(caractere, altura,largura):

    linha = caractere * largura

    for i in range(altura):
        print(linha)

retângulo(caractere, altura, largura)