

import numpy as np
import math as m
import matplotlib.pyplot as plt

# Valor Inicial : Dupla no formato [x,y]
VI = [0,0]

# PARÂMETROS DE DISCRETIZAÇÃO
T_LIMITE = 2*m.pi
T0 = 0

# Parâmetros de exercício
Lambda = 10000

# tk : Retorna o k-ésimo t da discretização
def tk(k, to, passos):
    H_PASSO = T_LIMITE / passos
    return to + k * H_PASSO

# y'(t) : Deriv de Y. Editar em função da questão
def derivY(arg, t):
    return arg*(-y(arg,t) + m.sin(t))

# y(t) : Solução exata para fins de comparação. Editar em função da questão
def y(arg, t):
    C = arg/(1 + arg**2)
    return C * (m.exp(-arg * t) + arg * m.sin(t) - m.cos(t))

# discretizaX() : Retorna um vetor do tempo discretizado
def discretizaX(passos):
    xAxis = []
    for i in range(passos):
        xAxis.append(tk(i, T0, passos))
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

def f(arg, t, ynsoma, yatual):
    #print("\t{}, {}, {}, {}".format(arg,t,ynsoma,yatual))
    return arg*(-(yatual + ynsoma) + m.sin(t))

#RK4 : Retorna array de y
def RK4(yanterior, to, h_passo):
    k1 = derivY(Lambda, to)
    k2 = f(Lambda, to + h_passo/2, h_passo * k1/2, yanterior)
    k3 = f(Lambda, to + h_passo/2, h_passo * k2/2, yanterior)
    k4 = f(Lambda, to + h_passo, h_passo * k3, yanterior)
    inclinacao = ((k1 + 2*k2 + 2*k3 + k4)/6)
    #print("{}, {}, {}, {}, {}".format(k1,k2,k3,k4,inclinacao))
    #input()
    return yanterior + h_passo * inclinacao

def RK4Valores(n):
    rk4valores = [VI[1]] # y(0) = 0
    for i in range(n - 1):
        rk4valores.append(RK4(rk4valores[-1], tk(i, T0, n), T_LIMITE/n))
    return np.array(rk4valores)

# plotarGrafico() : Plota
def plotarGrafico(xArray, yAproxMatrix, y):
    plt.plot(xArray, yAproxMatrix[0],'bs',
             xArray, yAproxMatrix[1],'gs',
             xArray, yAproxMatrix[2],'rs',
             xArray, yAproxMatrix[3],'bv',
             xArray, yAproxMatrix[4],'g^',
             xArray, yAproxMatrix[5],'gd',
             xArray,  y, 'r--')
    ax = plt.gca()
    ax.set_ylim([-2,2])
    plt.show()

N = 50
xAxis = discretizaX(N)
yAxis50 = RK4Valores(N)
yAxis100 = RK4Valores(N * 2)
yAxis100 = yAxis100[::2]
yAxis150 = RK4Valores(N * 3)
yAxis150 = yAxis150[::3]
yAxis200 = RK4Valores(N * 4)
yAxis200 = yAxis200[::4]
yAxis250 = RK4Valores(N * 5)
yAxis250 = yAxis250[::5]
yAxis1000 = RK4Valores(N * 500000)
yAxis1000 = yAxis250[::500000]
yAprox = [yAxis50, yAxis100, yAxis150, yAxis200, yAxis200, yAxis250, yAxis1000]
yval = []
for i in range (N):
    yval.append(y(Lambda, tk(i, T0, N)))
plotarGrafico(xAxis, yAprox, yval)
