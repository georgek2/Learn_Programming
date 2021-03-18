

for number in range(4, 30):
    print(number)

'''
women = 250
men = 150


def adding_attendees():

    if men < 200:
        print("The number of men were below 200")

    if women > 300:
        print("The number of women who attended was as expected")

    while men < 200:
        averageNum = (women + men)*2
        return averageNum
    else:
        return men + women

adding_attendees()


def addingAttendees():
    if men < 200:
        print("The number of men were below 200")

    if women > 300:
        print("The number of women who attended was as expected")

    while men < 200:
        averageNum = (women + men)*2
        return averageNum
    else:
        return men + women

print(addingAttendees())

a = ["George", "Marry", "Mike", "John"]

print(a)

for i in a:
    print(i + ". I am a child of God.\n     I love God.")


b = [10, 20, 30, 40, 50]

total = 0
'''
'''for i in b:
    total = total + i
    print(total)
'''

'''Using range to print the elements in the given range. 
Also the list function used to convert the_list into an actual list of the elements"

After that, the list can also be printed using a for loop to make the code more readable

the_list = list(range(1, 11))

print(the_list)

x = str(the_list)

for i in the_list:
    print(i)

--"Remember about converting strings to ints and ints to strings."



x = "The number now is: "

for i in range(1, 6):
    print(i)
    a = str(i)
    print(x + a)



"print(list(range(1, 8)))"

result = 0

for i in range(1, 8):
    result += i

print(result)

" Using the modulo operator gives you the remainder of the nums"
x = 24 % 3

" Adding up the multiples of 3 in the range given above"

total1 = 0
"If the number is divisible by three, that is it has a zero remainder"
for i in range(1, 8):
    if i % 3 == 0:
        total1 += i

print(total1)

num = 0

for i in range(1, 100):
    if i % 5 == 0:
        num += i

print(num)
'''
'''

Employees = ["employee1", "employee2", "employee2"]

for i in Employees:
    print(i)


def employees (self, salary, name, age):
    self.salary = salary
    self.name = name
    self.age = age


print(employees(2000, "george", 15))


myVillage = "Muthiga"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != myVillage and guess_count < guess_limit:
    guess = input("Guess my village: ")
    guess_count += 1
    if guess == myVillage:
        print("Congrats!! You win")
    elif out_of_guesses == True:
        print("Sorry, Out of guesses")


'''
"Edureka- Shay"

count = 1

''' While loops

while count < 11:
    print("Number: ", count)
    count = count + 1

print("Thank You for your cooperation employee nnn")



import random

n = 20
guessed = int(n * random.random()) + 1
guess = 0

while guess != guessed:
    guess = int(input("Enter the new guess: "))
    if guess > 0:
        if guess > guessed:
            print("The Number is too large: ")
        elif guess < guessed:
            print("The number is too small: ")
    else:
        print("Sorry!! YOu LOst")
else:
    print("Yeeeeh!! You won...")


babies = ["Shila", "Shirleen", "Mary", "Junior", "John"]

for baby in babies:
    print(baby)

print("All counted up!!")
"Calculating the factorial of a number"
num = int(input("Enter number: "))
factorial = 1

if num < 0:
    print("Must be a positive number")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1,num + 1):
        factorial = factorial + 1

print(factorial)

'''








































