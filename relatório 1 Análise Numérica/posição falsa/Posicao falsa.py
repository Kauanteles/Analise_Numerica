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
taxa_erro = float(Dados_do_arquivo[2])

#contador de iterações
qnt_iteracoes = 0

#declaração da função
def f(x):
    return simp.sympify(Dados_do_arquivo[3]).subs({"x": x}).evalf()

#checagem se existe uma intersecção nesse intervalo
if(f(a)*f(b) < 0):
    
    #condição de parada, se a função ja esta suficientemente proxima a taxa de erro
    while (math.fabs(f((a*f(b) - b*f(a))/(f(b)-f(a)))) >= taxa_erro):

        #pega o ponto da reta entre a e b que toca o eixo x
        X = (a*f(b) - b*f(a))/(f(b)-f(a))
        
        #checa qual dos valores a ou b sera substituido pelo X
        if (f(X)*f(a)<0):  
            b = X
        else:
            a = X
        
        #incrementa o contador de iterações
        qnt_iteracoes += 1                
                
    #printa os valores do ponto, a função nele e a quantia de iterações no terminal
    print("ponto do zero da função: ",X)
    print("valor da função nesse ponto: ",f(X))
    print("quantidade de passou até atingir a tolerancia de erro: ",qnt_iteracoes)   
    
    #escreve no arquivo os mesmos dados printados acima
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(f"ponto de zero: {X}\nfuncao no ponto: {f(X)}\niteracoes necessarias: {qnt_iteracoes}")  

#printa mensagem de erro quando a intersecção não se encontra no intervalo dado       
else:
    print("o 0 da função não se encontra no intervalo dado!")