#!/usr/bin/env python3


from brain_games.logic import greetings, round, maxRound, gameLogic
from random import randint, shuffle


name = greetings()
print('What is the result of the expression?')
lst = ['+', '-', '*']
shuffle(lst)
while round <= maxRound:
    oneOperand = randint(1, 100)
    twoOperand = randint(1, 100)
    if lst[round-1] == '+':
        solution = oneOperand + twoOperand
        question = (f'{oneOperand} + {twoOperand}')
    elif lst[round-1] == '-':
        solution = oneOperand - twoOperand
        question = (f'{oneOperand} - {twoOperand}')
    else:
        solution = oneOperand * twoOperand
        question = (f'{oneOperand} * {twoOperand}')
    round = gameLogic(solution, question, round, name)
