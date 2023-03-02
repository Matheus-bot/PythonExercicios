# 73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.

times = ('América-Mg', 'Athletico-Pr', 'Atético-MG', 'Bahia', 'Botafogo',
         'Corinthias', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense',
         'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino',
         'Santos', 'São Paulo', 'Vasco da Gama')
print('Os 5 primeiros colocados são: ', times[:5])
print('Os últimos 4 colocados são: ', times[-4:])
print('Em Ordem alfabética: ', sorted(times))
print(f'A posição do Cruzeiro esta na {times.index("Cruzeiro") +1}ª posição')