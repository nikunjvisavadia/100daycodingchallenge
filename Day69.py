class Isosceles:
    def display1(self):
        print("I am an isosceles triangle")
class Equilateral(Isosceles):
    def display2(self):
        print("I am an equilateral triangle")
class C(Equilateral):
    def display3(self):
        print("I am a triangle")
obj = C()
obj.display2()
obj.display1()
obj.display3()