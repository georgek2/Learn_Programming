
# # Sleep in during the weekend and on vacation

# def sleep_in(weekday, vacation):

#     if weekday or not vacation:

#         return False

#     else:

#         return True

# # print(sleep_in(True, False))

# # print(sleep_in(False, True))

# Return a string a given number of times


def string_times(string, number):

    return string*number

print(string_times('Hi', 5))

# Return greeting to the given name

def sayHello(name):

    return 'Hello ' + str(name) + '!!'

print(sayHello('George'))
print(sayHello('Mike'))
print(sayHello('Alice'))
print(sayHello('Liz'))


def first_last(list):

    if list[0] == 6 or list[-1] == 6:

        return True

    else:

        return False

# print(first_last([5, 3, 6, 7, 5, 6, 1]))

# A Def for doubling string characters


def double(str):
    result = ''
    for char in str:
        result += char * 2

    return result

print(double('The'))
print(double('Halo'))
print(double('Love You'))

# Return the number of even integers


def even_int(list):
    count = 0
    for int in list:
        if int % 2 == 0:
            count += 1
        # else:
        #     count = count

    return count

print(even_int([1, 3, 5, 7, 8]))

# # The Rock, Paper, Scissors Game
import random

choices = ['rock', 'paper', 'scissors']

rounds = 5
count = 0

while rounds > 0:
    player = input('Enter selection: ')
    comp = random.choice(choices)
    new_round = True
    count += 1
    rounds -= 1
    
    print(f"Round >> {count}")
    print(f"Rounds left: {rounds}")
    while new_round:
        if player == 'rock':
            if comp == 'scissors':
                print('The player won..<<')
                print(comp)
                new_round = False
            elif comp == 'paper':
                print('The Comp won..>>')
                print(comp)
                new_round = False
            else:
                print('Its a Tie...<<')
                print(comp)
                new_round = False
        elif player == 'scissors':
            if comp == 'paper':
                print('The player won..<<')
                print(comp)
                new_round = False
            elif comp == 'rock':
                print('The Comp won..>>')
                print(comp)
                new_round = False
            else:
                print('Its a Tie...^^')
                print(comp)
                new_round = False
        elif player == 'paper':
            if comp == 'rock':
                print('Player won..<<')
                print(comp)
                new_round = False
            elif comp == 'scissors':
                print('Comp won..>>')
                print(comp)
                new_round = False
            else:
                print('Its a Tie..^^')
                print(comp)
                new_round = False
        else:
            print('*'*10)
            print('Invalid Choice')
            print(f"Rounds left: {rounds}")
            new_round = False
            

choices_obj = {
    'first': 'rock',
    'second': 'paper',
    'third': 'scissors'
}

values = []
for key in choices_obj:
    values.append(choices_obj[key])

print(values)

player = input('Enter selection: ')
comp = random.choice([value for key, value in choices_obj.items()])
# comp = random.choice([value for value in choices_obj.values()])
print(comp)
if player == comp:
    print(player)
    print(comp)


# The FizzBuzz Problem

for num in range(20):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# Fibonnacci Sequence

a, b = 0, 1

for i in range(0, 10):
    a, b = b, a + b
    print(a, b)



