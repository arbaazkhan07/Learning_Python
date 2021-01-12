"""class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Arbaaz khan', 7)
s2 = Student('Naveed', 8)

s1.show()
s1.lap.show()
s2.show()
s2.lap.show()"""


# or

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Arbaaz khan', 7)
s2 = Student('Naveed', 8)

s1.show()
s2.show()
