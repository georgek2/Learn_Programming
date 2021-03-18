
'''
 Storing items in a list. They have to be in a list and not a tuple since it is immutable

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

earth_metals.sort()

print(earth_metals)

earth_metals.sort(reverse=True)

print(earth_metals)
'''

t = (
    ['jane', 'luke', 'mary'],
['jane', 'luke', 'mary'],
['jane', 'luke', 'mary']
)

guess_word = 'me'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != guess_word and not out_of_guesses:

    if guess_count < guess_limit:
        guess = input('Please Enter Your guess: ')
        guess_count += 1

    else:
        out_of_guesses = True

if guess == guess_word:
    print('Congratulations, You win !!')

else:
    print('Sorry!! out of guesses')


