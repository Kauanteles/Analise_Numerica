# Bibliotecas usadas
import matplotlib.pyplot as plt

pontos = []

# Leitura das coordenadas x e y de cada ponto do arquivo input
with open('input.txt', 'r') as arquivo:
    for linha in arquivo:
        coordenadas = linha.strip().split()
        if len(coordenadas) == 2:
            x, y = map(float, coordenadas)
            pontos.append((x, y))

# Separa os valores de x e y em listas
x_valores = [x for x, _ in pontos]
y_valores = [y for _, y in pontos]

# Projeta os pontos no gráfico
for i in range(len(pontos)):
    plt.scatter(x_valores[i], y_valores[i])

# Põe em n a quantidade de pontos
n = len(pontos)

sum_xy = sum(x * y for x, y in pontos)
sum_x = sum(x for x, _ in pontos)
sum_x_sqr = sum(x**2 for x, _ in pontos)
sum_y = sum(y for _, y in pontos)

media_x = sum_x / n
media_y = sum_y / n

a1 = (n * sum_xy - sum_x * sum_y) / (n * (sum_x_sqr) - sum_x**2)
a0 = media_y - a1 * media_x

y_valores = [a0 + a1 * x for x in x_valores]

# Projeta a reta que encontramos no gráfico
plt.plot(x_valores, y_valores, color='red', label=f'Reta: y = {a0} + {a1}x')

# Mostrar o gráfico
plt.show()

# Salvar a função final em um arquivo
with open('output.txt', 'w') as output_file:
    output_file.write(f'Funcao de Regressao: {a0} + {a1}x')
