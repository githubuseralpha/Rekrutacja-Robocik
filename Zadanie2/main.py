from Game import Game

# Wprowadzona plansza musi odwzorowywać możliwy scenariusz, czyli:
# - brak pionków w pierwszym rzędzie po swojej stronie,
# - obecność jednego króla u każdej ze stron,
# - brak możliwości natychmiastowegp zbicia jednego z królów.

board = [
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', 'bp', '--'],
    ['--', '--', '--', 'wp', '--', '--', '--', '--'],
    ['br', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', 'wW'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', 'wr', '--', 'bq', '--', 'bW', '--'],
    ['--', '--', '--', 'bb', '--', '--', '--', '--']
]

game1 = Game(board)
game2 = Game(board)

game1.simulate_move('w')
game1.simulate_move('b')
game1.simulate_danger_zone('w')
results = game1.check_if_mate('w')

if len(results) != 0:
    print("Gracz biały może wygrać wykonując ruchy:")
    for result in results:
        print(result)
else:
    game2.simulate_move('b')
    game2.simulate_move('w')
    game2.simulate_danger_zone('b')
    results = game2.check_if_mate('b')
    if len(results) != 0:
        print("Gracz czarny może wygrać wykonując ruchy:")
        for result in results:
            print(result)
    else:
        print("Żaden z graczy nie może wygrać")
