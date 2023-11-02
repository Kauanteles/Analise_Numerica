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
h = (b - a)/2

# Aplica o Método de Simpson 1/3 simples
I = (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b))

print(I)

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Valor da Integral Aproximada:\n')
    arquivo_saida.write(f'I = {I}\n')