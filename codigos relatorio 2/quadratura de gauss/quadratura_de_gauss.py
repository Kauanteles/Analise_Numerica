import sympy as simp

# Função que será integrada
def f(x):
    return simp.sympify(Dados_do_arquivo[2]).subs({"x": x}).evalf()

# Pontos e pesos para a quadratura Gaussiana com 2 pontos
pontos = [-1 / (3 ** 0.5), 1 / (3 ** 0.5)]
pesos = [1, 1]

# Leitura dos limites de integração e da função do arquivo input.txt
Dados_do_arquivo = []
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())

a = float(Dados_do_arquivo[0])
b = float(Dados_do_arquivo[1])

# Calcula a integral usando a quadratura Gaussiana
integral = 0
for i in range(2):
    integral += pesos[i] * f(0.5 * (b - a) * pontos[i] + 0.5 * (a + b))

integral *= 0.5 * (b - a)

print(integral)

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Valor da Integral Aproximada:\n')
    arquivo_saida.write(f'I = {integral}\n')