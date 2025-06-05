1. Análise de Erros:
Este trabalho avalia a precisão e a convergência de séries numéricas aplicadas ao cálculo do cosseno via série de Maclaurin e à soma de uma p-série.
#Série de Maclaurin para o cosseno:
\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n \cdot x^{2n}}{(2n)!}
As aproximações foram feitas em Python, analisando os erros percentuais estimados e verdadeiros. Os testes revelaram que os métodos numéricos implementados são eficazes e proporcionam alta precisão, com erros tendendo rapidamente a zero à medida que as iterações aumentam.

🌱 2. Cálculo de Raízes de Equações Não Lineares:
Foram aplicados os métodos de Bisseção, Falsa Posição, Newton-Raphson, Secante e Secante Modificada para determinar raízes de funções. Os algoritmos foram avaliados quanto à velocidade de convergência, precisão e robustez. O método de Newton-Raphson se destacou em eficiência quando iniciado com boas estimativas, enquanto os métodos de Bisseção e Falsa Posição mostraram maior estabilidade, mas menor velocidade.

📉 3. Otimização Unidimensional:
O problema de otimização abordou o projeto de um recipiente cilíndrico aberto com volume fixo, buscando o menor custo possível. A função custo foi resolvida analiticamente, por derivada, e numericamente, utilizando Razão Áurea e Interpolação Quadrática. O método da interpolação foi o mais rápido e todos convergiram para o mesmo mínimo global: raio de 5 cm, altura de 15 cm e custo total mínimo de R$ 35,34.

🔢 4. Sistemas Lineares e Não Lineares:
Este estudo aplicou métodos diretos e iterativos para resolver sistemas lineares e não lineares com aplicação em problemas reais da engenharia. Foi analisado um caso de extração de materiais em minas com métodos como Eliminação de Gauss com Pivotamento, Jacobi, Gauss-Seidel e Gauss-Seidel com Relaxamento. Para sistemas não lineares, aplicou-se Newton-Raphson e método gráfico. O trabalho destaca a importância da escolha adequada do método conforme as características do sistema e mostra como ajustes como pivotamento podem viabilizar métodos iterativos mesmo em sistemas inicialmente instáveis.
