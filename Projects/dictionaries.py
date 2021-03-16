
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

# # # __iter__ is called automatically and iterates over the keys
for key in a_dict:
    print(key)

# # # using .items() to iterate over key value pairs
d_items = a_dict.items()
print(d_items)

for item in a_dict.items():
    print(item) # Tuples of key value pairs

# # # Unpack key and value separately
for key, value in a_dict.items():
    print('Key > ', key, ': Value > ', value)

# # # # Using .keys()
d_keys = a_dict.keys()
print(d_keys)

# # # Using .values()
d_values = a_dict.values()
print(d_values)

for value in a_dict.values():
    print(value)

# # # Checking for membership using (in)
print('pet' in a_dict.keys())
print('dog' in a_dict.values())


# # # MOdifying values and keys
prices = {'one': 10, 'two': 20}
for k, v in prices.items():
    prices[k] = v * 2

print(prices)

new_dict = {}
# Turning keys into values
for k, v in prices.items():
    new_dict[v] = k

print(new_dict)

# # # Filtering dict items <conditionals>
a_dict = {'one':1, 'two':2, 'three':3, 'four':4,'five':5}
new_dict = {}
for k, v in a_dict.items():
    if v <=2:
        new_dict[k] = v


print(new_dict)

# # # Doing calculations
result = 0
for v in a_dict.values():
    result += v

print(result)

# # # Dictionay Comprehensions

one = ['red', 'choma', 'dog']
two = ['color', 'dish', 'pet']

new_dict = {}
for k, v in zip(two, one):
    new_dict[k] = v 

# # # print(new_dict)

# # # # The above can be simplified using a comprehension
the_dict = {k: v for k, v in zip(two, one)}
print(the_dict)

# # # Also, tuning keys into values revised using compehensions
another = {v: k for k, v in a_dict.items()}
print(another)

# # # Filtering using comprehension
yet = {k:v for k, v in a_dict.items() if v <=3}
print(yet)

# # # Calculations uisng comprehensions
# # # List compre..
items = {'one': 2345, 'two': 50000, 'three': 58093, 'four': 900000}
totals = sum([value for value in items.values()])
print(totals)

# # # For large dictionaries
# # # Using a generator > addresses memory concerns
new_totals = sum(v for v in items.values())
print(new_totals)

# # # Can also pass the iterable to sum()
new_totals_2 = sum(items.values())
print(new_totals_2)

# # Removing certain K: V pairs from a dict
# # USing set operations
again = {k: items[k] for k in items.keys() - {'one'}}

# # print(again)

# # Sorting Dictionaries $$ > This depands on the data types of the keys and values
# # Using < Sorted()> and comprehensions
# # Sorting using keys
names = {'paul':75, 'victor':12, 'josh':63, 'andrew':23, "charlie":34}
sort_names = {k: names[k] for k in sorted(names)} # Alphabetically

# print(names)
# print(sort_names)

# Sorting using keys
# Using < SOrted()> with a second arg >> key = 'This tells 
# Key >> a def that returns the value in each iteration

def by_value(item):

    return item[1]

sort_names_2 = {k: names[k] for k, v in sorted(names.items(), key=by_value)}
# Default is ascending order
print(names)
print(sort_names_2)

print('SOrted by KEys: ')
for k, v in sorted(names.items()):
    print(">> ", k, v)

names_asc = {k: names[k] for k in sorted(names)}
print(names_asc)
print('SOrted by KEys RVD: ')

# for k, v in sorted(names.items(), reverse=True):
#     print(">> ", k, v)

names_desc = {k: names[k] for k in sorted(names, reverse=True)}
print(names_desc)
print('Sorted by VALues: ')

for k, v in sorted(names.items(), key=by_value):
    print(">> ", k, v)
names_val = {k: names[k] for k, v in sorted(names.items(), key=by_value, reverse=True)}
print(names_val)
print('Sorted by VALues RVD: ')
for k, v in sorted(names.items(), key=by_value, reverse=True):
    print(">> ", k, v)
print(names)
print(names_val)

# Iterating and deleting dict items >> .popitem()
# calling .popitem() on a empty dict raises a KeyError

item = names.popitem()
print(item)
item = names.popitem()
print(item)
item = names.popitem()
print(item)
item = names.popitem()
print(item)
item = names.popitem() # LAst Item
print(item)
item = names.popitem() # So this will raise a KeyError
print(item)

# Above is pretty verbose
# Use a while loop and error handling to prevent the error after
# Last item is popped

while True: # Runs until the logic below is exhausted
    print(f'Dictionary length: {len(names)}')

    try: # Delete an item if it exists in the dict
        item = names.popitem() # Deletes an item and returns it
        # print(f'>> {item} deleted')

    except KeyError: # If the above raises an error do this..
        print('**The dictionary is empty')
        break # Exit the loop 

# Using Builtin functions for iteration
# >> map()
# > takes a function and an iterable 
# map(function, iterable, ......)

prices = {'one': 100, 'two': 234, 'three': 546, 'four': 890}

# Increase prices by 25%
# def to do that
def increase(price):

    return (price[0], price[1] * 1.25)

new_prices = dict(map(increase, prices.items())) # dict def to tell python its a dict

print('Old prices')
for k, v in prices.items():
    print('>> ', k, v)
print('New prices')
for k, v in new_prices.items():
    print('>> ', k, v)






