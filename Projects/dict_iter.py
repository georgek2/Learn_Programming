# Using map() as an iteration tool 

items = {'name':1400, 'two':3400, 'three':7400}

# Multiply value by two

def mult(item):

    return (item[0], item[1] * 2)

new_dict = {k: v for k, v in map(mult, items.items())}

# Increase by 25%

def increase(item):

    return (item[0], item[1] * 1.5)

dict2 = dict(map(increase, items.items()))

# print(items)
# print(new_dict)
# print(dict2)

# USing filter() to iterate through a dict
# $ filter items that evaluate to false

fruits = {'apple':12, 'avocado':8, 'pineapple':5, 'mango':10, 'watermelon':7}

# filter fruits costing more than $10

def the_filter(fruit):

    return fruits[fruit] < 10

# You can return a list of the fruits
# Costing less than $10

buy = list(filter(the_filter, fruits.keys()))

# Or a newdict() for those fruits

buy_these = {k: fruits[k] for k in filter(the_filter, fruits.keys())}


# print(buy)
# print(buy_these)

# collections.ChainMap()
# chain dictionaries and iterate through them as one

veges = {'carrots': 12, 'kales': 10, 'onions': 7, 'tomatoes': 12}
cookware = {'sufuria': 5, 'cups': 23, 'plates': 45, 'rurijas': 4}

from collections import ChainMap

chained_dict = ChainMap(cookware, veges)

for k, v in chained_dict.items():

    print(f"{k} needed are {v} pieces")


