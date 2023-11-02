#bibliotecas utilizadas
import sympy as simp
import numpy as np
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

n = 3  # Número de linhas e grau máximo do termo polinomial
x = simp.symbols('x')  # Variável simbólica

# Crie uma lista de termos polinomiais
termos = [x**i for i in range(n)]

# Crie a matriz para armazenar os resultados
matriz = np.zeros((n, n+1), dtype=object)  # Usamos dtype=object para armazenar expressões simbólicas

# Calcule as integrais e preencha a matriz
for i in range(n):
    for j in range(n):
        termo1 = termos[j]
        termo2 = termos[i]
        integral = simp.integrate((termo1*termo2), (x, a, b))  # Adicione os limites de integração
        matriz[i, j] = integral

# Calculando as integrais dos termos de f(x) multiplicados pelos termos polinomiais
for i in range(n):
    termo = termos[i]  # Obtém o termo polinomial correspondente
    integral = simp.integrate(f(x) * termo, (x, a, b))
    matriz[i, -1] = integral

#trecho do algoritimo de gauss do relatorio anterior (retirados os comentarios para compactabilidade)
n = len(matriz)
for i in range(n-1):
    pivot = matriz[i][i]
    for j in range(i+1, n):
        M_aux = matriz[j][i] / pivot
        aux = matriz[i]
        matriz[j] = matriz[j] - (matriz[i] * M_aux)
        matriz[i] = aux
x = [0] * n
for i in range(n - 1, -1, -1):
    x[i] = matriz[i][n] / matriz[i][i]
    for j in range(i - 1, -1, -1):
        matriz[j][n] -= matriz[j][i] * x[i]
solucoes_equacoes = [f'x{i + 1} = {x[i]}' for i in range(n)]
#fim do trecho do algoritimo de gauss do relatorio anterior

def construir_funcao(solucoes):
    n = len(solucoes)
    x = simp.symbols('x')
    funcao = 0
    for i in range(n):
        funcao += simp.sympify(solucoes[i].split('=')[1].strip()) * (x**i)
    return funcao

# Use a função para construir a função desejada
funcao_resultante = construir_funcao(solucoes_equacoes)
print(funcao_resultante)

# Salvar a função final em um arquivo output.txt
with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Funcao Polinomial Resultante:\n')
    arquivo_saida.write(f'f(x) = {funcao_resultante}\n')