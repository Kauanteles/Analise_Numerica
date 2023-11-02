#bibliotecas utilizadas
import sympy as simp
import math

#criação da lista que recebera os dados do arquivo
Dados_do_arquivo = []

#leitura do arquivo e separação das linhas em indices da lista
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())  

#separamento dos dados em variaveis com nomes mais significativos
a = float(Dados_do_arquivo[0])
b = float(Dados_do_arquivo[1])

#declaração da função
def f(x):
    return simp.sympify(Dados_do_arquivo[2]).subs({"x": x}).evalf()

h = a-b

I = (h/2)*(f(a)+f(b))

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Valor da Integral Aproximada:\n')
    arquivo_saida.write(f'I = {I}\n')