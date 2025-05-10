class Person(object):

    laws = "Protect, Obey and Survive"

    def __init__(self, name, age,job ="Engineer"):
        self.name = name # Attribute
        self.age = age # Attribute
        self.job = job

    def display(self):
        print(f"{self.name}, {self.age}, self.job years old.")

        #Class method
        @Classmethod
        def assemble(cls):
            print("Coming from A Class Method")

age = 8
name = "Cristian"
print(Person.laws)
print(Person.assemble())

employer1 = Person("John", 23)
employer1.display() 