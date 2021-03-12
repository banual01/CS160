class Student:
    def __init__(self, name, age, major):
        self._name = name
        self._age = age
        self._major = major

    @property
    def foo(self):
        return self._name
    
    def get_age(self):
        return str(self._age)

    def major(self):
        return self._major

    bar = property(get_age)
    


my_name = Student("Alex", 9, "VisCom")
print(my_name.foo)
print(my_name.bar)
print(my_name.major())
