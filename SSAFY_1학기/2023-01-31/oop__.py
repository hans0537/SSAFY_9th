
class Car:

    def horn(self):
        print("빵빵")

class Avante(Car):
    pass

class Sonata(Car):
    pass

class Canival(Car):
    pass

avante = Avante()
avante.horn()

s = Sonata()
s.horn()
