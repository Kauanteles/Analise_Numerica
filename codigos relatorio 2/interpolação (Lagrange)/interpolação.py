from matplotlib import pyplot as plt
import sympy as sp

# Ler os pontos do arquivo
pontos = []

with open('input.txt', 'r') as arquivo:
    for linha in arquivo:
        coordenadas = linha.strip().split()
        if len(coordenadas) == 2:
            x, y = map(float, coordenadas)
            pontos.append((x, y))

# Extrair os valores de x e y dos pontos
x_valores = [x for x, _ in pontos]
y_valores = [y for _, y in pontos]

# Definir o símbolo x como uma variável simbólica
x = sp.symbols('x')

# Número de pontos
n = len(pontos)

# Lista para armazenar as bases de Lagrange
L = []

# Calcular as bases de Lagrange
for i in range(n):
    aux1 = 1
    aux2 = 1
    for j in range(n):
        if j != i:
            aux1 *= (x - x_valores[j])
            aux2 *= (x_valores[i] - x_valores[j])
    aux3 = aux1/aux2
    L.append(aux3)


# Calcular o polinômio interpolador
polinomio_interpolador = sum(y_valores[i] * L[i] for i in range(n))

# Converter o polinômio em uma expressão para visualização
polinomio_interpolador_simplificado = sp.simplify(polinomio_interpolador)

# Imprimir o polinômio interpolador
print(f"Polinômio Interpolador: {polinomio_interpolador_simplificado}")

# Criar uma lista de valores de x para o gráfico
x_grafico = [x_valores[0] + (i / 10) * (x_valores[-1] - x_valores[0]) for i in range(11)]

# Calcular os valores correspondentes de y
y_grafico = [polinomio_interpolador.subs(x, valor) for valor in x_grafico]

# Plotar os pontos originais
for i in range(len(pontos)):
    plt.scatter(x_valores[i], y_valores[i])

# Plotar o polinômio interpolador
plt.plot(x_grafico, y_grafico, label='Polinomio Interpolador', color='red')

plt.xlabel('Valores de x')
plt.ylabel('Valores da Função')
plt.title('Interpolação de Lagrange')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Polinomio Interpolador:\n')
    arquivo_saida.write(f'{polinomio_interpolador_simplificado}\n')