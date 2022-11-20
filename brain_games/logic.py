round = 1
maxRound = 3


def greetings():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}')
    return name


def gameLogic(solution, question, round, name):
    print(f'Question: {question}')
    answer = input('Your answer: ')
    if str(solution) == answer:
        print('Correct!')
        round += 1
        if round > maxRound:
            print(f'Congratulations, {name}!')
        return round
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{solution}'.")
        print(f"Let's try again, {name}")
        return maxRound + 1
