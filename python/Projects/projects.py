
# Sleep in during the weekend and on vacation

def sleep_in(weekday, vacation):

    if weekday or not vacation:

        return False

    else:

        return True 

# print(sleep_in(True, False))

# print(sleep_in(False, True))

# Return a string a given number of times

def string_times(string, number):

    return string*number

# print(string_times('Hi', 5))

# Return greeting to the given name

def sayHello(name):

    return 'Hello ' + str(name) + '!!'

# print(sayHello('George'))
# print(sayHello('Mike'))
# print(sayHello('Alice'))
# print(sayHello('Liz'))

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

# print(double('The'))
# print(double('Halo'))
# print(double('Love You'))

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







