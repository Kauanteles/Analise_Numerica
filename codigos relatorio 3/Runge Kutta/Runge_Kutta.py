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

# Método de Runge-Kutta de 4ª ordem e salva os resultados em output_rk4.txt
with open('output.txt', 'w') as output_file:
    for i in range(n):
        k1 = f(x0, y0)
        k2 = f(x0 + 0.5*h, y0 + 0.5*k1*h)
        k3 = f(x0 + 0.5*h, y0 + 0.5*k2*h)
        k4 = f(x0 + h, y0 + k3*h)

        y0 = y0 + (1/6) * (k1 + 2*k2 + 2*k3 + k4)*h
        x0 = x0 + h

        output_file.write(f'x({i + 1}) = {x0} y({i + 1}) = {y0:.4f}\n')

print("Resultados salvos em output.txt")