class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod
    def classMethod(cls):
        return 'class method', cls

    @staticmethod
    def staticMethod():
        return 'static method'

my_class = MyClass()
print(my_class.method())
print(my_class.classMethod())
print(my_class.staticMethod())