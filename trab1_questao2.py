import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definindo a função da série infinita
def serie_infinita(i):
    return 1 / (i**4)

# Valor verdadeiro da série
u = (np.pi**4) / 90

# Número de algarismos significativos
n = 6

# Critério de Scarborough para precisão de 6 algarismos
Eppara = 0.5 * 10**(2-n)

# Definição de variáveis
soma = 0
v_old = soma
i = 1
estimativa = []
Ept = 100
Epest = 100
EPT = []
EPEST = []
nn = []

# Loop para calcular a série até atingir a precisão desejada
while Ept >= Eppara:
    soma = soma + serie_infinita(i)
    v_new = soma

    # Cálculo dos erros
    Ept = abs((u - soma) / u) * 100
    Epest = abs((v_new - v_old) / v_new) * 100

    # Atualização da variável para o próximo ciclo
    i = i + 1
    v_old = v_new

    # Salvando os cálculos para análise
    nn.append(i)
    estimativa.append(soma)
    EPT.append(Ept)
    EPEST.append(Epest)

# Criando um DataFrame com os resultados
table = pd.DataFrame()
table['n'] = nn
table['Estimativa'] = estimativa
table['Ept'] = EPT
table['Epest'] = EPEST

# Exibindo os resultados
print(table)
print(f"Número de termos necessários: {i-1}")
print(f"Valor aproximado da série: {soma}")
print(f"Erro percentual verdadeiro: {Ept:.6f}%")
print(f"Erro percentual estimado: {Epest:.6f}%")



# Criando os gráficos
plt.figure(figsize=(14, 6))

# Gráfico 1: Estimativa da soma versus número de termos
plt.subplot(1, 2, 1)
plt.plot(nn, estimativa, label='Estimativa da Soma', color='b')
plt.axhline(y=u, color='r', linestyle='--', label=f'Valor Verdadeiro ({u:.6f})')
plt.title('Estimativa da Soma da Série')
plt.xlabel('Número de Termos (n)')
plt.ylabel('Estimativa da Soma')
plt.legend()

# Gráfico 2: Erro Percentual (verdadeiro e estimado) versus número de termos
plt.subplot(1, 2, 2)
plt.plot(nn, EPT, label='Erro Percentual Verdadeiro', color='g')
plt.plot(nn, EPEST, label='Erro Percentual Estimado', color='orange')
plt.title('Erro Percentual ao Longo das Iterações')
plt.xlabel('Número de Termos (n)')
plt.ylabel('Erro Percentual (%)')
plt.legend()

plt.tight_layout()
plt.show()

