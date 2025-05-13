
'''

A transformada de Hough é uma técnica usada em processamento de imagens para detectar formas,
como linhas, em uma imagem. Para ilustrar o cálculo da transformada de Hough de duas retas paralelas,
vamos seguir um exemplo passo a passo.
### Passo 1: Representação das Retas Vamos considerar duas retas paralelas em um espaço cartesiano:
- Reta 1: \( y = mx + c_1 \)
- Reta 2: \( y = mx + c_2 \)
Para simplificar, vamos usar: - \( m = 1 \) - \( c_1 = 2 \) - \( c_2 = 4 \)
Portanto, as retas são: - Reta 1: \( y = x + 2 \)
- Reta 2: \( y = x + 4 \)
### Passo 2: Espaço da Imagem Vamos definir um espaço de imagem, por exemplo, uma grade de 10x10 pixels,
onde cada pixel pode ter um valor de (x, y).
### Passo 3: Espaço de Hough Na transformada de Hough, cada ponto (x, y) no espaço da imagem é
transformado em uma linha no espaço de Hough.
A forma comum é a parametrização \(\rho = x \cos(\theta) + y \sin(\theta)\), onde: - \(\rho\)
é a distância perpendicular da linha até a origem. - \(\theta\)
é o ângulo que a linha faz com o eixo x. #
## Passo 4: Cálculo da Transformada Para cada ponto da imagem que pertence a uma reta,
calculamos uma linha no espaço de Hough. Vamos considerar alguns pontos das nossas duas retas:
#### Reta 1: \( y = x + 2 \) -
Ponto (0, 2): \(\rho = 0 \cdot \cos(\theta) + 2 \cdot \sin(\theta) = 2 \sin(\theta)\) -
Ponto (1, 3): \(\rho = 1 \cdot \cos(\theta) + 3 \cdot \sin(\theta) = \cos(\theta) + 3 \sin(\theta)\)
Ponto (2, 4): \(\rho = 2 \cdot \cos(\theta) + 4 \cdot \sin(\theta) = 2 \cos(\theta) + 4 \sin(\theta)\)

#### Reta 2: \( y = x + 4 \) -
Ponto (0, 4): \(\rho = 0 \cdot \cos(\theta) + 4 \cdot \sin(\theta) = 4 \sin(\theta)\) -
Ponto (1, 5): \(\rho = 1 \cdot \cos(\theta) + 5 \cdot \sin(\theta) = \cos(\theta) + 5 \sin(\theta)\)
- Ponto (2, 6): \(\rho = 2 \cdot \cos(\theta) + 6 \cdot \sin(\theta) = 2 \cos(\theta) + 6 \sin(\theta)\)
### Passo 5: Acumulação no Espaço de Hough Para cada ponto (x, y),
traçamos uma curva \(\rho = x \cos(\theta) + y \sin(\theta)\) no espaço de Hough (\(\theta\), \(\rho\)) e
incrementamos os valores em uma matriz de acumulação.

### Passo 6: Identificação dos Picos Os picos na matriz de acumulação correspondem às linhas detectadas.
No caso de retas paralelas, elas terão \(\theta\) iguais, mas diferentes \(\rho\).
Por exemplo, se \(\theta = 45^\circ\) (\(\cos(45^\circ) = \sin(45^\circ) = \frac{\sqrt{2}}{2}\)):
- Para Reta 1: \( \rho_1 = x \cdot \frac{\sqrt{2}}{2} + (x+2) \cdot \frac{\sqrt{2}}{2} = \sqrt{2}(x+1) \)
- Para Reta 2: \( \rho_2 = x \cdot \frac{\sqrt{2}}{2} + (x+4) \cdot \frac{\sqrt{2}}{2} = \sqrt{2}(x+2) \)
Assim, os picos no espaço de Hough serão (\(\theta\), \(\rho_1\)) e (\(\theta\), \(\rho_2\)).
### Conclusão Detectamos as duas retas paralelas através dos picos na matriz de acumulação do espaço de Hough.
Esses picos indicam a presença das duas retas, com \(\theta\) iguais e \(\rho\) diferentes,
refletindo a diferença na interceptação com o eixo y (c1 e c2).
