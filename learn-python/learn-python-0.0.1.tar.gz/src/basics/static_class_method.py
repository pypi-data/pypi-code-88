from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        """
        - Used generally to create factory method
        - Can access or modify class state
        """
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        """
        - Used as utility class
        - Can't access class state
        """
        return age > 18


if __name__ == '__main__':

    person_1 = Person("test", 21)
    person_2 = Person.from_birth_year("test", 1996)
    print(person_2.age)
    print(Person.is_adult(21))
    print(getattr(person_1, "age"))
    print(dir(person_1))