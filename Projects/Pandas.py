'''

students = ['Ben', 'Abel', 'Zach', 'Fine', 'Jane', 'Luke', 'Kev', 'Mercy']

indexes = [42, 50, 36, 17, 28]

indexes.insert(-1, 788)

print(indexes)

students.append(indexes)

print(students)

'''

import pandas as pd

'''
web = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [34, 65, 45, 45, 34, 35], 'Bounce': [3, 4, 2, 2, 4, 3]}

df = pd.DataFrame(web)

"Slicing the dataframe by printing the number of required rows using HEAD AND TAIL functions"
print(df.head(4))
print(df.tail(4))
'''

"Merging data frames "

df1 = pd.DataFrame({'HPI': [40, 46, 78, 60, 84], 'INT_rate': [3, 4, 6, 3, 2], 'GDP': [56, 54, 67, 87, 34]},
                   index=[2004, 2005, 2006, 2007, 2008])

df2 = pd.DataFrame({'HPI': [40, 46, 78, 60, 84], 'INT_rate': [3, 4, 6, 3, 2], 'GDP': [56, 54, 67, 87, 34]},
                   index=[2009, 2010, 2011, 2012, 2013])

axe = pd.merge(df1, df2)

print(axe)




