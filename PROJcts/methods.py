# Instance Methods <> instance variables
# Class Methods <> class variables
# Static Methods <Works alone>


class Student:

    # Static / Class Variable is defined outside the constructor

    school = 'Muthiga' # All the students belong to the same school

    def __init__(self, m1, m2, m3): 
        # Instance Variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method >> it works with the object
    # Thats why the arg self..
    # INstance Variables can be used with 
    # Instance Methods:
    def average(self): # MEthod belongs to the instance of the object

        return (self.m1 + self.m2 + self.m3) / 3


    # School >> Class Variable
    # Works with class Methods
    @classmethod
    def info(cls): # Wow, instead of self >> keyWOrd >> < cls >

        return cls.school # class method and class variable


    # Static Methods works alone
    # Not with instance variables
    @staticmethod
    def studentsinfo():

        return (f'Students from This Secondary School...')

st1 = Student(46, 78, 34)
st2 = Student(66, 84, 74)

# print(st2.average())
# print(st1.info())
print(st2.studentsinfo())

