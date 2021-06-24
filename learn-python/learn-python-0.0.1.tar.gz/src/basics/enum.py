from enum import Enum


class Sex(Enum):
    MALE = 1
    FEMALE = 2


if __name__ == '__main__':
    print(Sex.MALE.name)
    print(Sex(2).name)
    if isinstance(Sex.FEMALE, Sex):
        print("Yes")
        print(Sex.FEMALE.value)
