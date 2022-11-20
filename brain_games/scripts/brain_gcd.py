from brain_games.logic import greetings, gameLogic, round, maxRound
from random import randint


name = greetings()
print('Find the greatest common divisor of given numbers.')
while round <= maxRound:
    oneOperand = randint(1, 100)
    twoOperand = randint(1, 100)
    question = (f'{oneOperand} {twoOperand}')
    if oneOperand >= twoOperand:
        solution = twoOperand
    else:
        solution = oneOperand
    for i in range(solution, 0, -1):
        if oneOperand % i == 0 and twoOperand % i == 0:
            solution = i
            break
    round = gameLogic(solution, question, round, name)
