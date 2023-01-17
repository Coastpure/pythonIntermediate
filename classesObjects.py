class Person:
    # object of a class, self is the object
    # __init__ constructor name
    amount = 0
    def __init__(self,name, age, height):
        self.name= name
        self.age= age
        self.height = height
        Person.amount += 1
# self parameter has to be in every function that we define
# self.name= name, we are accepting some parameters name age & height, and we are then assigning the values of
# these parameters to the actual attributes of our class
#     what happens when you delete a person
    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height)


# person 1 is an object here
person1 = Person("Mike",30,180)
print(person1.name)
print(person1.age)
print(person1.height)

person2 = Person("Sara", 40, 186)
# del person2

# print(person1)
print(Person.amount)

