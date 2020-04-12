n = 84

guesses = 1

print ('Numbers of guesses are limited to only 9 times!')

while (guesses<=9):
    guess_number = int(input('Guess the Number. \n'))
    if guess_number < 84:
        print ('your guess is lesser than winning number. \n')
    elif guess_number > 84:
        print ('your guess is greater than winning number. \n')
    else:
        print ('You Win :)')
        print (guesses, 'No. of guesses you took to Win!')
        break
    print (9-guesses, 'No. of guesses are left.')
    guesses = guesses + 1

if guesses > 9:
    print ('G@ME OvEr!!!')