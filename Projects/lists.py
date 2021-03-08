# list of names

names = ['Luke', 'Anna', 'Jennifer', 'Mark', 'Harun', 'Erick', 'Loise', 'Brenda']

# print(names)

# print(len(names))

# Bracket Notation
first = names[0]
second = names[1]
third = names[2]

# print(second)

last = names[-1]
second_two = names[-2]

# print(last)

all = names[0:]
excluding_first = names[1:]
excluding_first_n_second = names[2:]

# print(excluding_first_n_second)

first_two = names[0:2]
first_three = names[:3]

# print(first_three)

in_between = names[2:5]

excluding_last = names[:-1]
excluding_last_two = names[:-2]

last_two = names[-2:]
last_three = names[-3:]

# print(in_between)

# Adding Names
# To the end
names.append('Sarah')
print(names)

names.insert(0, 'Oprah')

print(names)

names.pop()
print(names)

names.remove('Jennifer')
print(names)

