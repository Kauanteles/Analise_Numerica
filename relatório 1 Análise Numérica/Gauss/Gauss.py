#biblioteca usada
import numpy as np

# Carrega os dados do arquivo em uma matriz
matriz = np.loadtxt('input.txt')

# Define o tamanho da matriz (quantidade de linhas, a parte das soluções não é considerada)
n = len(matriz)

# Calcula o determinante da matriz original
determinante = np.linalg.det(matriz[:, :-1])  # Exclui a última coluna (coluna de resultados)

# Verifica se o determinante é igual a zero (indicando uma matriz singular)
if abs(determinante) < 1e-10:
    print("A matriz é singular. O método de Gauss não pode ser aplicado.")
else:
    # Continua com o método de Gauss
    # Garante que os valores presentes na diagonal principal são os maiores possíveis e diferentes de 0
    for i in range(n):
        linha_pivo = i
        for j in range(i + 1, n):
            if abs(matriz[j][i]) > abs(matriz[linha_pivo][i]):
                linha_pivo = j
        matriz[i], matriz[linha_pivo] = matriz[linha_pivo], matriz[i]

    # Realiza o método de Gauss. "i" parte da primeira até a penúltima linha
    for i in range(n-1):
        # Seta o pivô como a diagonal na linha analisada na iteração
        pivot = matriz[i][i]
        # j vai da segunda linha até a última
        for j in range(i+1, n):
            # Maux guarda os valores de cada valor abaixo do atual pivô dividido por ele
            M_aux = matriz[j][i] / pivot
            # Aux guarda os valores da linha do pivô, que não deve ser alterada pela multiplicação matriz[i] * M_aux
            aux = matriz[i]
            # É realizado o cálculo da nova linha
            matriz[j] = matriz[j] - (matriz[i] * M_aux)
            # A linha do pivô recebe seu valor de antes
            matriz[i] = aux

    # Resolve o sistema linear de matriz triangular inferior resultante do método de Gauss vindo de baixo para cima
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matriz[i][n] / matriz[i][i]
        for j in range(i - 1, -1, -1):
            matriz[j][n] -= matriz[j][i] * x[i]

    # Cria uma lista de strings representando as equações de solução
    solucoes_equacoes = [f'x{i + 1} = {x[i]}' for i in range(n)]

    # Salva as soluções em um arquivo "output.txt" junto com as equações
    with open("output.txt", "w") as file:
        file.write('\n'.join(solucoes_equacoes))

    # Printa as soluções com seus respectivos nomes
    for solucao in solucoes_equacoes:
        print(solucao)