import argparse, random


parser = argparse.ArgumentParser(description='guess game')
parser.add_argument('-a', '--answer', type=int, help='Enter your answer after -a or --answer')
parser.add_argument('-e' ,'--len', type=int, default=100, help='You can change the numeric range')
parser.add_argument('-g', '--Try', type=int, default=5, help='You can change the number of attempts' )
user_answer = parser.parse_args()
answer = random.randint(0,user_answer.len)
print(answer)
for i in range(0,user_answer.len):
    if i != 0:
        if user_answer.answer == answer:
            print('Congratulations, you guessed right')
            break

        elif user_answer.answer > answer:
            print(f'enter lower number \nNumber of chances left: {user_answer.Try-i}')
            user_answer.answer = int(input('new number:'))

        elif user_answer.answer < answer:
            print(f'enter biger number \nNumber of chances left: {user_answer.Try-i}')
            user_answer.answer = int(input('new number:'))

else:
    if user_answer.answer == answer:
        print('Congratulations, you guessed right')

    else:
        print('GAME OVER!!!')