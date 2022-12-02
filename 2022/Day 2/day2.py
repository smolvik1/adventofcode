import os

scores = []  # scores for part 1
scores2 = []  # scores for part 2

rpc_mapping = {'A': 'rock', 'B': 'paper', 'C': 'scissor', 'X': 'rock', 'Y': 'paper', 'Z': 'scissor'}
symbol_values = {'rock': 1, 'paper': 2, 'scissor': 3}
match_values = {'win': 6, 'loss': 0, 'draw': 3}

input = os.path.join(os.path.dirname(__file__),'input.txt')

for line in open(input, 'r').readlines():
    opponent = line.split()[0]
    me = line.split()[1]

    for letter, symbol in rpc_mapping.items():
        opponent = opponent.replace(letter, symbol)  # rock, paper, scissor
        me = me.replace(letter, symbol)  # rock, paper, scissor

    if opponent == 'rock':
        if me == 'rock': # part 1 = draw, part 2: Need to lose
            scores.append(match_values['draw'] + symbol_values[me])
            scores2.append(match_values['loss'] + symbol_values['scissor'])
        if me == 'paper': # part 1 = win, part 2: Need to draw
            scores.append(match_values['win'] + symbol_values[me])
            scores2.append(match_values['draw'] + symbol_values['rock'])
        if me == 'scissor': # part 1 = loss, part 2: Need to win
            scores.append(match_values['loss'] + symbol_values[me])
            scores2.append(match_values['win'] + symbol_values['paper'])
    
    elif opponent == 'paper':
        if me == 'rock': # part 1 = loss, part 2: Need to lose
            scores.append(match_values['loss'] + symbol_values[me])
            scores2.append(match_values['loss'] + symbol_values['rock'])
        if me == 'paper': # part 1 = draw, part 2: Need to draw
            scores.append(match_values['draw'] + symbol_values[me])
            scores2.append(match_values['draw'] + symbol_values['paper'])
        if me == 'scissor': # part 1 = win, part 2: Need to win
            scores.append(match_values['win'] + symbol_values[me])
            scores2.append(match_values['win'] + symbol_values['scissor'])

    elif opponent == 'scissor':
        if me == 'rock': # part 1 = win, part 2: Need to lose
            scores.append(match_values['win'] + symbol_values[me])
            scores2.append(match_values['loss'] + symbol_values['paper'])
        if me == 'paper': # part 1 = loss, part 2: Need to draw
            scores.append(match_values['loss'] + symbol_values[me])
            scores2.append(match_values['draw'] + symbol_values['scissor'])
        if me == 'scissor': # part 1 = draw, part 2: Need to win
            scores.append(match_values['draw'] + symbol_values[me])
            scores2.append(match_values['win'] + symbol_values['rock'])


print('Solution to problem #1: ' + str(sum(scores)) + ' points' )
print('Solution to problem #2: ' + str(sum(scores2)) + ' points' )
