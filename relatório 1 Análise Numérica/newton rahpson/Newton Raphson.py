#bibliotecas utilizadas
import sympy as symp

#criação da lista que recebera os dados do arquivo
Dados_do_arquivo = []

#leitura do arquivo e separação das linhas em indices da lista
with open('input.txt', 'r') as file:
    for line in file:
        Dados_do_arquivo.append(line.strip())  

#separamento dos dados em variaveis com nomes mais significativos
a = float(Dados_do_arquivo[0])
taxa_erro = float(Dados_do_arquivo[1])

#contador de iterações
qnt_iteracoes = 0

#declaração da função
def f(x):
    return symp.sympify(Dados_do_arquivo[2]).subs({"x": x}).evalf()
  
#declaração da função que faz a derivada da função principal
def df(x):
    return symp.diff(symp.sympify(Dados_do_arquivo[2]), "x").subs({"x": x}).evalf()
  
#condição de parada, se a função ja esta suficientemente proxima a taxa de erro
while (symp.Abs(f(a)) >= taxa_erro):

    #o ponto é atualizado com o calculo da tangente da curva
    a = a - (f(a) / df(a))
        
    #incrementa o contador de iterações
    qnt_iteracoes += 1                
                
#printa os valores do ponto, a função nele e a quantia de iterações no terminal
print("ponto do zero da função: ", a)
print(f"valor da função nesse ponto: {f(a):.9f}")
print("quantidade de passos até atingir a tolerância de erro: ", qnt_iteracoes)

#escreve no arquivo os mesmos dados printados acima
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(f"ponto de zero: {a}\nfuncao no ponto: {f(a):.9f}\niteracoes necessarias: {qnt_iteracoes}")