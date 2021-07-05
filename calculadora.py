# Calculadora de alcance de anúncio.
#Autor: Jéssica Silva de Assis.

from time import sleep
from math import ceil

print('-=-'*18)
print('CALCULE AQUI O ALCANCE DO SEU ANÚNCIO!')
investimento = float(input('Quanto será investido? R$'))
print('Analisando as informações...')
sleep(2)

    #Cálculos
'''Visualizações iniciais'''
visualizacao1 = investimento * 30
'''Total de cliques'''
clique = visualizacao1 * 0.12
'''Total de compartilhamentos'''
compartilhamento = (clique * 0.15) / 4
'''Visualizações secundárias'''
visualizacao2 = compartilhamento * 40
'''Alcance total'''
alcance = (investimento * 30) + (visualizacao1 * 0.12) + (clique * 0.15) + (compartilhamento * 40)

print('Aproximadamente {} pessoas visualizarão o anúncio.'.format(ceil(alcance)))
print('-=-'*18)
