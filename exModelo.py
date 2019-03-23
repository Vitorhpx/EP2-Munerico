import numpy as np
import matplotlib.pyplot as plt

# Valor Inicial : Dupla no formato [x,y]
VI = [0,1]

# PARÂMETROS DE DISCRETIZAÇÃO
T_LIMITE = 1
H_PASSO = 10
T0 = 0

# tk : Retorna o k-ésimo t da discretização
def tk(k, to):
    return to + k * T_LIMITE/H_PASSO

# y'(t) : Deriv de Y. Editar em função da questão
def derivY(arg, t):
    return -arg * funcao(t)

# y(t) : Solução exata para fins de comparação. Editar em função da questão
def y(arg, t):
    return exp(-arg*t)

# discretizaX() : Retorna um vetor do tempo discretizado
def discretizaX():
    xAxis = []
    for i in range(H_PASSO):
        xAxis.append(tk(i, T0))
    xAxis = np.array(xAxis)
    return xAxis

# erroGlobal(): Devolve o erro global
def erroGlobal(n, arg, yAprox):
    erros = []
    for i in range (n):
        erros.append(abs(y(arg, tk(i, T0)) - yAprox[i]))
    return max(erros)

# tabelaErro(nArray, arg, yAproxMatrix) : Monta a tabela de erro
def tabelaErro(nArray, arg, yAproxMatrix):
    table = [['n','Erro Global']]
    for i in nArray:
        table.append([i,erroGlobal(i, arg, yAprox[i])])
    return table

# plotarGrafico() : Plota
def plotarGrafico(xArray, yAproxMatrix):
    plt.plot(xArray, yAproxMatrix[0], xArray, yAproxMatrix[1])
    plt.show()

