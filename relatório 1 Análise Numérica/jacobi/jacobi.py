import numpy as np

# Carrega os dados do arquivo em uma matriz
with open('input.txt') as file:
    lines = file.readlines()

# Lê a tolerância de erro da primeira linha do arquivo
tolerancia = float(lines[0])

# Resto do arquivo contém os coeficientes da matriz e os valores do lado direito
matriz = []
for line in lines[1:]:
    matriz.append(list(map(float, line.split())))  # Ignora a última coluna

# Converte a matriz em um array numpy
matriz = np.array(matriz)

# Number of rows (equations) and columns (variables)
n = len(matriz)

b = np.zeros(n)
jacobi = np.zeros((n, n + 1))

for i in range(n):
    jacobi[i, :] = matriz[i, :] / matriz[i, i]
    jacobi[i, n] = matriz[i, n] / matriz[i, i]
    jacobi[i, i] = 0

jacobi = -jacobi
jacobi[:, n] = -jacobi[:, n]

results = np.copy(jacobi[:, n])

jacobi = jacobi[:, :-1]

# Teste de convergência - critério das linhas diagonais dominantes
diagonalmente_dominante = all(abs(matriz[i, i]) >= np.sum(np.abs(matriz[i, :-1])) - abs(matriz[i, i]) for i in range(n))

if not diagonalmente_dominante:
    print("A matriz não é diagonalmente dominante. O método de Jacobi pode não convergir.")
    exit()

# Inicializa as soluções com zeros
x = np.zeros(n)

# Realiza as iterações até que a tolerância seja alcançada
iteracoes = 0
while True:
    x_anterior = x.copy()
    x = np.dot(jacobi, x) + results
    iteracoes += 1

    # Calcula a norma do erro
    erro = np.linalg.norm(x - x_anterior)

    # Verifica se a tolerância foi alcançada
    if erro < tolerancia:
        break

# Cria uma lista de strings representando as equações de solução
solucoes_equacoes = [f'x{i + 1} = {x[i]}' for i in range(n)]

# Salva as soluções em um arquivo "output.txt" junto com as equações e o número de iterações
with open("output.txt", "w") as file:
    file.write('\n'.join(solucoes_equacoes))
    file.write(f'\niteracoes necessarias: {iteracoes}')

# Printa as soluções com seus respectivos nomes
for solucao in solucoes_equacoes:
    print(solucao)

print(f'iteracoes necessarias: {iteracoes}')
