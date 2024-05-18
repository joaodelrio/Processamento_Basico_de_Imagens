## Ferramentas
- [OpenCV](https://opencv.org/)
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## Implementação

### 1. [Processamento de Cores](processamento_cores.py)
Foi utilizada a imagem `RGB.png` para realizar o processamento de cores. Foram extraídos os canais de cores r, g e b através da função `cv2.split()`.

### 2. [Conversão de Espaço de Cores](conversao.py)
Foi utilizada a imagem `cria.png` para realizar a conversão de espaço de cores. A imagem foi convertida para os espaços de cores `Cinza` através da função `cv2.cvtColor()` e para `Binário` através da função `cv2.threshold()`. Além disso, foi feita manualmente a limiarização para `Binário`, transformando os pixels com valor maior que 127 para 255 (branco) e com valor menor para 0 (preto).

### 3. [Filtros](filtros.py)
Foi utilizada a imagem `tigre.png` para a aplicação de filtros. Foram aplicados os filtros `Média` e `Mediana` através da passagem de um elemento estruturante de 3x3 pela imagem.

### 4. [Transformações Geométricas](transformacoes.py)
Foi utilizada a imagem `cria.png` para realizar as transformações geométricas. Foram aplicadas as transformações `Reflexão` e `Rotação` através das funções `cv2.flip()` e `cv2.rotate()`.