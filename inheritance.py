class Person:
    def __init__(self,name, age, height):
        self.name= name
        self.age= age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height)
    
    def get_older(years):
        self.age += years


# inherit from Person
class Worker(Person):

    # we added a salary parameter
    def __init__(self, name, age, height, salary):
        # worker is the class, self is the object
        # notice how we don't add salary in the super __init__
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    # notice we override the def __str__(self):, by defining the same method again, if it already exists we override it
    def __str__(self):
        text = super(Worker, self).__str__()
        text += ", Salary {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Henry", 40, 184, 4000)
print(worker1)
print(worker1.calc_yearly_salary())
