from random import randint

print('Welcome to the Brain Games!')
name = input('May I have your name? ')
print('Answer "yes" if the number is even, otherwise answer "no".')
attempt = 0
while attempt < 3:
    question = randint(1, 100)
    if question % 2 == 0:
        questionStr = 'yes'
    else:
        questionStr = 'no'
    print(f'Question: {question}')
    answer = input('Your answer: ')
    if questionStr == answer:
        print('Correct!')
        attempt += 1
        if attempt == 3:
            print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{questionStr}'.")
        print(f"Let's try again, {name}")
        break
