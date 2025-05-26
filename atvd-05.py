#ATIVIDADE 05 - MÓDULOS E PACOTES
import statistics
dados = [7, 8, 9, 11, 13, 15, 16, 20, 22, 24, 26, 30, 33, 40]
media = statistics.mean(dados)
mediana = statistics.median(dados)
print('media: ', media)
print('mediana: ', mediana)

import statistics as st
media = st.mean(dados)
mediana = st.median(dados)
print('media com st: ', media)
print('mediana com st: ', mediana)

from statistics import mean, median
media = mean(dados)
mediana = median(dados)
print('media com função mean: ', media)
print('mediana com função median: ', mediana)

from statistics import *
media = mean(dados)
mediana = median(dados)
print('media com todas importações: ', media)
print('mediana com todas importações: ', mediana)