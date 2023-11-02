# Bibliotecas utilizadas
import sympy as simp

# Criação da lista que receberá os dados do arquivo
Dados_do_arquivo = []

# Leitura do arquivo e separação das linhas em índices da lista
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())

# Separação dos dados em variáveis com nomes mais significativos
a = float(Dados_do_arquivo[0])
b = float(Dados_do_arquivo[1])
n = int(Dados_do_arquivo[2])  # Lê o número de subintervalos do arquivo

# Declaração da função
def f(x):
    return simp.sympify(Dados_do_arquivo[3]).subs({"x": x}).evalf()

# Largura de cada subintervalo
h = (b - a) / n

# Inicializa a soma da integral
I = 0

# Aplica o Método de Simpson 3/8 composto
I = f(a) + f(b)

for i in range(1, n):
    x_i = a + i * h
    if i % 3 == 0:
        I += 2 * f(x_i)
    else:
        I += 3 * f(x_i)

I = (3 * h / 8) * I

print(I)

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Valor da Integral Aproximada:\n')
    arquivo_saida.write(f'I = {I}\n')