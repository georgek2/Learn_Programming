
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# __iter__ is called automatically and iterates over the keys
for key in a_dict:
    print(key)

# using .items() to iterate over key value pairs
d_items = a_dict.items()
# print(d_items)

for item in a_dict.items():
    print(item) # Tuples of key value pairs

# Unpack key and value separately
for key, value in a_dict.items():
    print('Key > ', key, ': Value > ', value)

# # Using .keys()
d_keys = a_dict.keys()
# print(d_keys)

# Using .values()
d_values = a_dict.values()
# print(d_values)

for value in a_dict.values():
    print(value)

# Checking for membership using (in)
print('pet' in a_dict.keys())
print('dog' in a_dict.values())


# MOdifying values and keys
prices = {'one': 10, 'two': 20}
for k, v in prices.items():
    prices[k] = v * 2

# print(prices)

new_dict = {}
# Turning keys into values
for k, v in prices.items():
    new_dict[v] = k

# print(new_dict)

# Filtering dict items <conditionals>
a_dict = {'one':1, 'two':2, 'three':3, 'four':4,'five':5}
new_dict = {}
for k, v in a_dict.items():
    if v <=2:
        new_dict[k] = v


# print(new_dict)

# Doing calculations
result = 0
for v in a_dict.values():
    result += v

# print(result)

# Dictionay Comprehensions

one = ['red', 'choma', 'dog']
two = ['color', 'dish', 'pet']

new_dict = {}
for k, v in zip(two, one):
    new_dict[k] = v 

# print(new_dict)

# # The above can be simplified using a comprehension
the_dict = {k: v for k, v in zip(two, one)}
# print(the_dict)

# Also, tuning keys into values revised using compehensions
another = {v: k for k, v in a_dict.items()}
# print(another)

# Filtering using comprehension
yet = {k:v for k, v in a_dict.items() if v <=3}
# print(yet)

# Calculations uisng comprehensions
# List compre..
items = {'one': 2345, 'two': 50000, 'three': 58093, 'four': 900000}
totals = sum([value for value in items.values()])
print(totals)

# For large dictionaries
# Using a generator > addresses memory concerns
new_totals = sum(v for v in items.values())
print(new_totals)

# Can also pass the iterable to sum()
new_totals_2 = sum(items.values())
print(new_totals_2)




























