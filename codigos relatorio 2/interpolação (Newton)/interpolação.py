import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular as diferenças divididas
def dif_divided_diff(x, y):
    n = len(x)
    coef = np.zeros(n)
    for j in range(n):
        coef[j] = y[j]
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            coef[j] = (coef[j] - coef[j-1]) / (x[j] - x[j-i])
    return coef

# Função para construir o polinômio interpolador de Newton
def newton_interpolation(x, y):
    n = len(x)
    coef = dif_divided_diff(x, y)
    X = sp.symbols('X')
    poly = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (X - x[j])
        poly += term
    return poly

# Leitura dos pontos do arquivo input.txt
Dados_do_arquivo = []
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())

# Separa os pontos em x e y
xy_pairs = [line.split() for line in Dados_do_arquivo]
x = [float(pair[0]) for pair in xy_pairs]
y = [float(pair[1]) for pair in xy_pairs]

# Calcula o polinômio interpolador
polinomio = newton_interpolation(x, y)

# Tenta simplificar o polinômio
polinomio_simplificado = sp.simplify(polinomio)

# Cria símbolos diferentes para a variável x e o polinômio
X = sp.symbols('X')
funcao_interp = sp.lambdify(X, polinomio_simplificado, 'numpy')

# Cria um conjunto de pontos para plotar a função
x_valores = np.linspace(min(x), max(x), 100)
y_valores = funcao_interp(x_valores)

# Plota os pontos
plt.scatter(x, y, label='Pontos', color='red')

# Plota o polinômio interpolador
plt.plot(x_valores, y_valores, label='Polinômio Interpolador', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Interpolação de Newton')
plt.show()

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Polinomio Interpolador de Newton:\n')
    arquivo_saida.write(f'{polinomio_simplificado}\n')