from questions_data import *
from api import *

tela_inicial()

# Retorno de uma sentença 'input' após perder em jogo.
# Processando funções de api.
ligado = 's'
while ligado == 's':
    chamada_rodadas(questionsX, questionsY, questionsW, THEFINAL)
    linha_estilo()
    ligado = input('Aqui você fica expert. Deseja jogar novamente? [S/N] ')
    ligado = ligado.lower()
    linha_estilo()

# Note que você só retorna ao jogo se digitar exatamente "S ou s". Fora isso, é uma saída.
