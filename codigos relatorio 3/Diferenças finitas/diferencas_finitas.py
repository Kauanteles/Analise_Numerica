from numpy import *
from math import *

def ler_arquivo():
    global arquivo_leitura, passo, num_pontos, ultimo_x, a_val, b_val, Ta_val

    passo = float(arquivo_leitura.readline())
    ultimo_x = float(arquivo_leitura.readline())
    num_pontos = int(arquivo_leitura.readline())
    a_val = float(arquivo_leitura.readline())
    b_val = float(arquivo_leitura.readline())
    Ta_val = float(arquivo_leitura.readline())


def diferencas_finitas(passo, num_pontos, Dx, a_val, b_val, Ta_val):
    vetor_b = []
    matriz_linear = []
    aux = 0

    for i in range(num_pontos - 1):
        vetor_aux = []
        for j in range(num_pontos - 1):
            vetor_aux.append(0)

        if aux == 0:
            vetor_aux[aux] = (2 + passo * Dx**2)
            vetor_aux[aux + 1] = -1
        elif aux == num_pontos - 2:
            vetor_aux[aux] = (2 + passo * Dx**2)
            vetor_aux[aux - 1] = -1
        else:
            vetor_aux[aux] = (2 + passo * Dx**2)
            vetor_aux[aux + 1] = -1
            vetor_aux[aux - 1] = -1
        matriz_linear.append(vetor_aux)
        aux += 1

    vetor_b.append(passo * (Dx**2) * Ta_val + a_val)

    for j in range(num_pontos - 3):
        vetor_b.append(passo * (Dx**2) * Ta_val)

    vetor_b.append(passo * (Dx**2) * Ta_val + b_val)

    R = linalg.solve(matriz_linear, vetor_b)

    count = 1

    if a_val % 2 == 0:
        arquivo_resultado.write("Iteração " + str(count) + ": ")
        arquivo_resultado.write(str(int(a_val)) + "\n")
    else:
        arquivo_resultado.write("Iteração " + str(count) + ": ")
        arquivo_resultado.write(str(round(a_val, 5)) + "\n")

    for resultado in R:
        count += 1
        if resultado % 2 == 0:
            arquivo_resultado.write("Iteração " + str(count) + ": ")
            arquivo_resultado.write(str(int(resultado)) + "\n")
        else:
            arquivo_resultado.write("Iteração " + str(count) + ": ")
            arquivo_resultado.write(str(round(resultado, 5)) + "\n")

    if b_val % 2 == 0:
        arquivo_resultado.write("Iteração " + str(count + 1) + ": ")
        arquivo_resultado.write(str(int(b_val)) + "\n")
    else:
        arquivo_resultado.write("Iteração " + str(count + 1) + ": ")
        arquivo_resultado.write(str(round(b_val, 5)) + "\n")


def main():
    global passo, num_pontos, ultimo_x, a_val, b_val, Ta_val

    ler_arquivo()

    Dx = ultimo_x / num_pontos

    diferencas_finitas(passo, num_pontos, Dx, a_val, b_val, Ta_val)


arquivo_leitura = open('input.txt', 'r', encoding='utf8')
arquivo_resultado = open('output.txt', 'w', encoding='utf8')

main()