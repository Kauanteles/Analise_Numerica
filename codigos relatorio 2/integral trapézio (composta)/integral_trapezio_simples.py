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

# Aplica o método do trapézio composto
for i in range(n):
    x0 = a + i * h
    x1 = a + (i + 1) * h
    I += (h / 2) * (f(x0) + f(x1))

print(I)

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Valor da Integral Aproximada:\n')
    arquivo_saida.write(f'I = {I}\n')