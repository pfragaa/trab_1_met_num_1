import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Definindo o valor de x1
x1 = 1
# definindo a série
def serie_cos(x1, n):
  return ((-1)**n) * ((x1**(2*n))/math.factorial(2*n))

# Definindo variáveis
u = math.cos(x1)    # valor verdadeiro
soma = 0    #soma da serie começa em zero
v_old = soma   #Armazena o valor anterior da soma, erro estimado
estimativa = []  # valores estimados da serie
EPT = []  # valor verdadeiro
EPEST = []  # valor estimado
nn = []  # numero de iteraçoes

for n in range(0, 10):
  soma = soma + serie_cos(x1, n)
  v_new = soma  # atualiza para a iteração atual (soma)

  #Cálculo dos erros
  ept = abs(((u - soma)/ u) * 100)
  epest = abs(((v_new - v_old)/ v_new) * 100)

  v_old = v_new
  estimativa.append(soma)
  EPT.append(ept)
  EPEST.append(epest)
  nn.append(n)

# Data Frame
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativa
table['Ept'] = EPT
table['Epest'] = EPEST
print(table)

#Grafico 1: Erro Percentual (verdadeiro e estimado) versus número de iterações
plt.plot(nn, EPT, 'o--', color='b', label='$E_{pt}$ (%)')
plt.plot(nn, EPEST, 'o--', color='r', label='$E_{pest}$ (%)')
plt.plot(nn, [math.cos(x1)] * len(table['n']), 'o--', color='c', label='Valor Real')
plt.xlabel('Número de iterações')
plt.ylabel('Erro Percentual (%)')
plt.title('Convergência da Série de McLaurin para cos(1)')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

# Gráfico 2: Estimativa da soma versus número de termos
plt.plot(nn, estimativa, label='Estimativa da Soma', color='r')
plt.xlabel('Número de iterações')
plt.ylabel('Estimativa da Soma')
plt.title('Estimativa da Soma da Série')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

# Definindo o valor de x2
x2 = -2
# definindo a série
def serie_cos(x2, w):
  return ((-1)**w) * ((x2**(2*w))/math.factorial(2*w))

# Definindo variáveis
u2 = math.cos(x2)    # valor verdadeiro
soma2 = 0    #soma da serie começa em zero
v_old2 = soma2  #Armazena o valor anterior da soma, erro estimado
estimativa2 = []  # valores estimados da serie
EPT2 = []  # valor verdadeiro
EPEST2 = []  # valor estimado
nn2 = []  # numero de iteraçoes

for w in range(0, 10):
  soma2 = soma2 + serie_cos(x2, w)
  v_new2 = soma2  # atualiza para a iteração atual (soma)

  #Cálculo dos erros
  ept2 = abs(((u2 - soma2)/ u2) * 100)
  epest2 = abs(((v_new2 - v_old2)/ v_new2) * 100)

  v_old2 = v_new2
  estimativa2.append(soma2)
  EPT2.append(ept2)
  EPEST2.append(epest2)
  nn2.append(w)

# Data Frame
table = pd.DataFrame()
table['n'] = nn2
table['Estimativa'] = estimativa2
table['Ept'] = EPT2
table['Epest'] = EPEST2
print(table)


#Gráfico 3: Erro Percentual (verdadeiro e estimado) versus número de iterações
plt.plot(table['n'], table['Ept'], 'o--', color='b', label='$E_{pt}$ (%)')
plt.plot(table['n'], table['Epest'], 'o--', color='r', label='$E_{pest}$ (%)')
plt.plot(table['n'], [math.cos(-2)] * len(table['n']), 'o--', color='c', label='Valor Real')
plt.xlabel('Número de iterações')
plt.ylabel('Erro Percentual (%)')
plt.title('Convergência da Série de McLaurin para cos(-2)')
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()

# Gráfico 4: Estimativa da soma versus número de termos
plt.plot(nn2, estimativa2, label='Estimativa da Soma', color='r')
plt.xlabel('Número de iterações')
plt.ylabel('Estimativa da Soma')
plt.title('Estimativa da Soma da Série')
plt.tight_layout()
plt.grid()
plt.legend()
plt.show()



# Determinar o número de termos necessários para aproximar cos(x) com 8 algarismos significativos usando a série de Maclaurin

x = 0.3 * np.pi
u = np.cos(x)

n = 8
Eppara = 0.5 * 10**(2 - n)

i = 0
Ept = 100
soma = 0


def f(x, i):
    return (-1)**i * (x**(2*i)) / math.factorial(2*i)

print(f"valor de cos(x): {u:.10f}")

while Ept > Eppara:
    soma += f(x, i)
    i += 1
    Ept = abs((u - soma) / u) * 100
    print(f"{i} termo: aproximação = {soma:.10f}, Erro percentual verdadeiro = {Ept:.10f}%")

# Listas para armazenar os valores de aproximação e os erros em cada iteração
aproximacoes = []
erros = []

# Reinicializar variáveis
i = 0
Ept = 100
soma = 0

# Calcular novamente, agora armazenando os dados para o gráfico
while Ept > Eppara:
    soma += f(x, i)
    Ept = abs((u - soma) / u) * 100
    aproximacoes.append(soma)
    erros.append(Ept)
    i += 1

# Plotando o gráfico de aproximação
plt.figure(figsize=(10, 5))
plt.plot(range(1, i+1), aproximacoes, marker='o', label='Aproximação da série')
plt.axhline(y=u, color='r', linestyle='--', label='Valor real de cos(x)')
plt.title('Convergência da Série de Maclaurin para cos(x)')
plt.xlabel('Número de termos')
plt.ylabel('Aproximação de cos(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

