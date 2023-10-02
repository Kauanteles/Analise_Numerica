import numpy as np

# Carrega os dados do arquivo em uma matriz
matriz = np.loadtxt('input.txt')

# Define o tamanho da matriz (quantidade de linhas, a parte das soluções não é considerada)
n = len(matriz)

# Define o número de colunas com base nos dados do arquivo de entrada
num_colunas = matriz.shape[1]

# Armazena em 'b' os valores dos resultados do sistema
b = matriz[:, num_colunas - 1]

# Cria a matriz 'U' com os valores do sistema tirando as respostas
U = matriz[:, :num_colunas - 1]

# Cria um vetor onde serão guardados os valores de M_aux
valores_L = []

# Executa o mesmo trecho do algoritmo de Gauss para fazer 'U' ser uma matriz triangular superior
for i in range(n):
    linha_pivo = i
    for j in range(i + 1, n):
        if abs(U[j][i]) > abs(U[linha_pivo][i]):
            linha_pivo = j

    U[i], U[linha_pivo] = U[linha_pivo], U[i]

for i in range(n - 1):
    pivot = U[i][i]
    for j in range(i + 1, n):
        M_aux = U[j][i] / pivot
        valores_L.append(M_aux)
        aux = U[i]
        U[j] = U[j] - (U[i] * M_aux)
        U[i] = aux

# Cria a matriz 'L' com diagonal 1 e 0 no resto
L = np.identity(n)

# Carrega os valores de 'M_aux' guardados em 'valores_L' do método de Gauss na matriz triangular inferior 'L'
for i in range(1, n):
    for j in range(i):
        L[i][j] = valores_L.pop(0)

# Inicializa 'y' como um vetor de 0
y = np.zeros(n)

# Realiza as operações para preencher 'y' seguindo a fórmula L*y=b
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

# Inicializa 'x' como um vetor de 0
x = np.zeros(n)

# Faz a solução do sistema de baixo para cima seguindo a fórmula U*x=y
for i in range(n - 1, -1, -1):
    if U[i][i] == 0:
        x[i] = 0
    else:
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i][i]

# Cria uma lista de strings representando as equações de solução
solucoes_equacoes = [f'x{i + 1} = {x[i]}' for i in range(n)]

# Salva as soluções em um arquivo "output.txt" junto com as equações
with open("output.txt", "w") as file:
    file.write('\n'.join(solucoes_equacoes))

# Printa as soluções com seus respectivos nomes
for solucao in solucoes_equacoes:
    print(solucao)
