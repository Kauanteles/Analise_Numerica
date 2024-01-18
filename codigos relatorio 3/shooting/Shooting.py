import math
from sympy import *

def ler_arquivo_entrada():
    # Abre o arquivo de entrada para leitura
    arq = open("dados_entrada.txt", "r")
    # Define a variável simbólica x
    x = symbols('x')

    # Inicializa listas para armazenar os dados
    funcoes = []
    y_inicial = []
    intervalos = []
    valor_alvo = []
    passo = []
    n = []

    # Inicializa a variável de linha
    linha = None
    # Loop para ler cada linha do arquivo
    while (linha != ''):
        # Lê uma linha do arquivo
        linha = arq.readline()
        # Verifica se a linha não está vazia
        if (linha != ""):
            # Divide a linha nos pontos e vírgulas para obter os dados
            partes = linha.split(";")

            # Avalia a expressão como uma função em termos de x
            funcao_expr = eval(partes[0])
            # Converte o valor inicial de y para um número
            y_inicial_valor = eval(partes[1])

            # Divide a string do intervalo e converte os valores para números
            intervalo_str = partes[2]
            intervalo_valores = intervalo_str.split(",")
            for i in range(len(intervalo_valores)):
                intervalo_valores[i] = eval(intervalo_valores[i])

            # Converte o valor alvo para um número
            valor_alvo_valor = eval(partes[3])

            # Converte o tamanho do passo para um número
            passo_valor = eval(partes[4])

            # Converte o número de pontos para um número
            n_str = partes[5]
            n_str = n_str.split("\n")
            n_valor = eval(n_str[0])

            # Adiciona os dados às listas correspondentes
            funcoes.append(funcao_expr)
            y_inicial.append(y_inicial_valor)
            intervalos.append(intervalo_valores)
            valor_alvo.append(valor_alvo_valor)
            passo.append(passo_valor)
            n.append(n_valor)

    # Fecha o arquivo após a leitura
    arq.close()

    # Retorna as listas contendo os dados
    return funcoes, y_inicial, intervalos, valor_alvo, passo, n

def resolver_metodo_shooting(funcao, y_inicial, intervalo, valor_alvo, passo, pontos):
    # Define a variável simbólica x
    x = symbols('x')

    # Inicializa a lista para armazenar os valores finais de y
    valores_y_finais = []

    # Inicializa a lista de valores x, y e z
    xyz_valores = [[], [], []]

    # Loop para calcular os valores usando o método de tiro
    for j in range(len(xyz_valores)):
        xyz_valores[0] = [0]
        xyz_valores[1] = [y_inicial]
        if j != 2:
            xyz_valores[2] = [intervalo[j]]
            for i in range(pontos):
                xyz_valores[1].append(xyz_valores[1][i] + passo * xyz_valores[2][i])
                xyz_valores[2].append(xyz_valores[2][i] + passo * funcao.subs(x, xyz_valores[0][i]))
                xyz_valores[0].append(xyz_valores[0][i] + passo)
            valores_y_finais.append(xyz_valores[1][-1])
        else:
            xyz_valores[2] = [intervalo[0] + ((intervalo[1] - intervalo[0]) / (valores_y_finais[1] - valores_y_finais[0])) * (valor_alvo - valores_y_finais[0])]
            for i in range(pontos):
                xyz_valores[1].append(xyz_valores[1][i] + passo * xyz_valores[2][i])
                xyz_valores[2].append(xyz_valores[2][i] + passo * funcao.subs(x, xyz_valores[0][i]))
                xyz_valores[0].append(xyz_valores[0][i] + passo)

        # Verifica se o último valor de y é igual ao valor alvo
        if xyz_valores[1][-1] == valor_alvo:
            # Inicializa a lista para armazenar os resultados
            resultado = []
            # Adiciona os resultados formatados à lista
            for i in range(len(xyz_valores[1])):
                resultado.append([i, round(xyz_valores[1][i], 3)])

            # Retorna os resultados
            return resultado

def principal():
    # Lê os dados do arquivo de entrada
    funcoes, y_inicial, intervalos, valor_alvo, passo, n = ler_arquivo_entrada()
    # Abre o arquivo de saída para escrita
    arq_saida = open("resultado_saida.txt", "w")
    # Loop para processar cada conjunto de dados
    for i in range(len(funcoes)):
        # Resolve o método de tiro para o conjunto atual de dados
        resultado = resolver_metodo_shooting(funcoes[i], y_inicial[i], intervalos[i], valor_alvo[i], passo[i], n[i])
        # Escreve os resultados no arquivo de saída
        arq_saida.write(str(resultado))
        # Adiciona uma quebra de linha se não for o último conjunto de dados
        if (i < len(funcoes) - 1):
            arq_saida.write("\n")
    # Fecha o arquivo de saída
    arq_saida.close()

# Chama a função principal para executar o código
principal()
