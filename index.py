# Repartiendo cartas
""" Programa que crea una baraja de 52 cartas, las baraja y las muestra.
Luego reparte 5 cartas a 4 jugadores. Muestra las cartas de cada jugador,
y finalmente muestra las cartas restantes.
"""

import random
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
palos = ['Espadas', 'Corazones', 'Rombos', 'Tréboles']
baraja = []

print('########## Cartas ##########')
for c in cartas:
  for p in palos:
    carta = '{} de {}'.format(c, p)
    baraja.append(carta)

# Generando de manera aleatoria las cartas
random.shuffle(baraja)

for i in range(0, 52, 4):
  for j in range(4):
    print('{:14}'.format(baraja[i+j]), end=' ')
  print()
print()

""" Repartiendo cartas a 4 jugadores """
jugador_1 = []
jugador_2 = []
jugador_3 = []
jugador_4 = []
for i in range(5):
  carta_1 = baraja.pop(0)
  jugador_1.append(carta_1)

  carta_2 = baraja.pop(0)
  jugador_2.append(carta_2)

  carta_3 = baraja.pop(0)
  jugador_3.append(carta_3)

  carta_4 = baraja.pop(0)
  jugador_4.append(carta_4)

""" Mostrando las cartas de cada jugador """
print('########## Las cartas de los jugadores ##########')
jugadores = [jugador_1, jugador_2, jugador_3, jugador_4]
for i in range(4):
  print('\n')
  print('Jugador {}: '.format(i+1))
  for j in range(5):
    print('{:16}'.format(jugadores[i][j]), end=' ')
    print()
print()

""" Mostrando las cartas restantes """
print('########## Cartas restantes ##########')
for i in range(0, 32, 4):
  for j in range(4):
    print('{:14}'.format(baraja[i+j]), end=' ')
  print()