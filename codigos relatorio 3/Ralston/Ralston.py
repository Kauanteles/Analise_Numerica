import sympy as sp

# Leitura do arquivo input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

    # Extrai informações do arquivo
    func_str = lines[0].strip()
    x0 = float(lines[1].strip())
    y0 = float(lines[2].strip())
    h = float(lines[3].strip())
    n = int(lines[4].strip())

# Trecho que torna a função lida do arquivo de string para uma função utilizável
expression = sp.sympify(func_str)
x, y = sp.symbols('x y')

def f(x_value, y_value):
    result = expression.subs({x: x_value, y: y_value})
    return result

# Realiza o método de Euler e salva os resultados em output.txt
with open('output.txt', 'w') as output_file:
    for i in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + (3/4)*h, y0 + (3/4)*m1*h)
        y1 = y0 + h * ((1/3)*m1 + (2/3)*m2)
        x0 = x0 + h
        y0 = y1
        output_file.write(f'x({i + 1}) = {x0:.4f} y({i + 1}) = {y0:.4f}\n')

print("Resultados salvos em output.txt")