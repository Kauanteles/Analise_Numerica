import sympy as simp

# Leitura da função a partir do arquivo input.txt
Dados_do_arquivo = []
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())

# Separa a função
funcao = simp.sympify(Dados_do_arquivo[0])

# Valor do ponto onde a segunda derivada será calculada
x_i = 2.0  # Substitua pelo ponto desejado

# Valor do incremento h (pode ser ajustado)
h = 1e-5

# Cálculo da segunda derivada usando a fórmula de diferença progressiva (forward difference)
segunda_derivada = (funcao.subs({"x": x_i + 2 * h}) - 2 * funcao.subs({"x": x_i + h}) + funcao.subs({"x": x_i})) / (h**2)

print(f"A segunda derivada em x = {x_i} é aproximadamente: {segunda_derivada}")

with open('output.txt', 'w') as arquivo_saida:
    arquivo_saida.write(f'Segunda Derivada Aproximada:\n')
    arquivo_saida.write(f'Segunda derivada em x = {x_i} sera aproximadamente: {segunda_derivada}\n')