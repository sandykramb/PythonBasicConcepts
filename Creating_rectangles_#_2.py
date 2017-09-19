largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"

def retângulo(largura, altura, caractere):

    preenchido = caractere * largura
    if largura > 2:
        n_preenchido = caractere + (" " * (largura - 2)) + caractere
    else:
        n_preenchido = preenchido

    if altura >= 1:
        print(preenchido)
    for i in range(altura - 2):
        print(n_preenchido)
    if altura >= 2:
        print(preenchido)

retângulo(largura, altura, caractere)