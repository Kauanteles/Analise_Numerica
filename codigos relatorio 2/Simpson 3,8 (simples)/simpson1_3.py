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

# Declaração da função
def f(x):
    return simp.sympify(Dados_do_arquivo[2]).subs({"x": x}).evalf()

# Largura do intervalo
h = (b - a) / 3

# Inicializa a soma da integral
I = 0

# Aplica o Método de Simpson 3/8 simples
I = f(a) + 3 * f((2 * a + b) / 3) + 3 * f((a + 2 * b) / 3) + f(b)

I = (3 * h / 8) * I

print(I)