import matplotlib.pyplot as plt
import numpy as np

pontos = []

with open('input.txt', 'r') as arquivo:
    for linha in arquivo:
        coordenadas = linha.strip().split()
        if len(coordenadas) == 2:
            x, y = map(float, coordenadas)
            pontos.append((x, y))

n = len(pontos)

x_valores = [x for x, _ in pontos]
y_valores = [y for _, y in pontos]

# Defina o grau do polinômio desejado
grau_do_polinomio = 2  # Ajuste para o grau desejado

# Criar uma lista com números 1 no segundo índice
um_lista = [1] * n

# Calcular os produtos dos valores dos 2 anteriores
produto_lista = [um_lista]
for i in range(1, grau_do_polinomio + 1):
    produto_lista.append([x ** i for x in x_valores])

# Calcular a matriz dos coeficientes do sistema
matriz = np.zeros((grau_do_polinomio + 1, grau_do_polinomio + 2))

for i in range(grau_do_polinomio + 1):
    for j in range(grau_do_polinomio + 1):
        matriz[i][j] = np.sum(np.multiply(produto_lista[i], produto_lista[j]))

for i in range(grau_do_polinomio + 1):
    matriz[i][grau_do_polinomio + 1] = np.sum(np.multiply(produto_lista[i], y_valores))

# Resolver o sistema de equações usando eliminação gaussiana (código que você já tem)

n = len(matriz)
for i in range(n - 1):
    pivot = matriz[i][i]
    for j in range(i + 1, n):
        M_aux = matriz[j][i] / pivot
        aux = matriz[i]
        matriz[j] = matriz[j] - (matriz[i] * M_aux)
        matriz[i] = aux
x = [0] * n
for i in range(n - 1, -1, -1):
    x[i] = matriz[i][grau_do_polinomio + 1] / matriz[i][i]
    for j in range(i - 1, -1, -1):
        matriz[j][grau_do_polinomio + 1] -= matriz[j][i] * x[i]
solucoes_equacoes = [f'x{i + 1} = {x[i]}' for i in range(n)]

# Extrair os coeficientes dos valores das soluções (código que você já tem)

coeficientes = [float(sol.split('=')[1]) for sol in solucoes_equacoes]

# Definir a função polinomial com base nos coeficientes
def funcao_polinomial(x, coeficientes):
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * x ** i
    return resultado

# Criar um vetor de valores de x para o gráfico
x_grafico = np.linspace(min(x_valores), max(x_valores), 100)

# Calcular os valores correspondentes da função polinomial
y_grafico = [funcao_polinomial(x, coeficientes) for x in x_grafico]

# Plotar os pontos originais
for i in range(len(pontos)):
    plt.scatter(x_valores[i], y_valores[i])

# Plotar a função polinomial
plt.plot(x_grafico, y_grafico, label=f'Função Polinomial (Grau {grau_do_polinomio})', color='red')

plt.xlabel('Valores de x')
plt.ylabel('Valores da Função')
plt.title(f'Gráfico da Função Polinomial (Grau {grau_do_polinomio})')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()

# Salvar a função polinomial no arquivo 'output.txt' sem o termo x^0
with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Funcao Polinomial (Grau {grau_do_polinomio}):\n')
    for i, coef in enumerate(coeficientes):
        if i == 0:
            arquivo_saida.write(f'{coef} ')
        else:
            arquivo_saida.write(f'x^{i} * {coef} ')
        if i < grau_do_polinomio:
            arquivo_saida.write('+ ')
    arquivo_saida.write('\n')