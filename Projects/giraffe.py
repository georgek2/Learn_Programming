" Working with lists "


''''
"COnverting strings to integers to enable arithmetic functions with variables"

phrase = "I have worked hard to be where i am"
x = list(range(1, 9))

print(x)

for i in range(1, 9):
    print(str(i) + " Time" + ">> " + phrase)


"Calculator on adding numbers"

def numAdd():
    num1 = input("Enter first number: ")
    op = input("Enter Operator: ")
    num2 = input("Enter second number: ")

    result = ""
    if op == "+":
        result = float(num1) + float(num2)
    if op == "-":
        result = float(num1) - float(num2)
    if op == "*":
        result = float(num1) * float(num2)
    if op == "/":
        result = float(num1) / float(num2)

    return float(result)

print(numAdd())


"Madlibz game: Involving concatanating variables and strings"

name = input("Enter you full names: ")
color = input("Enter a color: ")
comment = input("Enter the reason for your choice: ")

print("Hi, My name is " + name + ".")
print(color + " is my favorite color.")
print("I chose it since it " + comment)
'''

fruits = ["Mangoes", "Bananas", "Apples", "Lemons", "Papayas"]

fruits[0] = "Apples"
first = fruits[0] + " : This is the favorite among all."
fruits[4] = "Crackers"

fourth = fruits[4]

'''
fruits.("Oranges")

sixth = fruits[5]

print(first)
print(fruits[0] + ": This is the favorite among all.")
print(second)
print(fruits[1] + ": This is the second favorite.")


print(fruits[0:5])

print(first)
print(fourth)
'''

'''
    Modifying lists, appending (.extend) other lists and items
    Popping them out and back in, replacing them has been covered upfront
'''

ages = [34, 45, 23, 43, 45]
names = ["Lucas", "James", "Paul", "John", "Eve"]

print(names)
names.append("Mike")

names.insert(0, "June")
names.insert(2, "Kamau")

print(names)

guess_word = 'you'
guess = ''
guess_limit = 3
guess_count = 0
out_of_guesses = False

"while guess != guess_word:"
while guess != guess_word and guess_count < guess_limit:
    if guess != guess_word and not out_of_guesses:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        print("Fail!!")




















