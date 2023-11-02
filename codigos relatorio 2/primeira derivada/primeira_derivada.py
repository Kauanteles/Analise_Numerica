import sympy as simp

# Leitura da função e do ponto onde a derivada será calculada a partir do arquivo input.txt
Dados_do_arquivo = []
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())

# Separa a função e o ponto onde a derivada será calculada
funcao = simp.sympify(Dados_do_arquivo[0])
x_i = float(Dados_do_arquivo[1])

# Valor do incremento h (pode ser ajustado)
h = 1e-5

# Cálculo da derivada usando a fórmula de diferença progressiva (forward difference)
derivada = (funcao.subs({"x": x_i + h}) - funcao.subs({"x": x_i})) / h

print(f"A derivada em x = {x_i} é aproximadamente: {derivada}")

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Derivada Aproximada:\n')
    arquivo_saida.write(f'Derivada em x = {x_i} sera aproximadamente: {derivada}\n')