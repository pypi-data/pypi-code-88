import random
import datetime
now = datetime.datetime.now()
year = now.year
# from random import seed

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def verify(input) -> bool:
    social = list(map(int, str(input)))
    if len(social) == 12: 
        del social[0:2] 
    if len(social) != 10: 
        return False
    month = int(str(social[2]) + str(social[3])) 
    day = int(str(social[4]) + str(social[5])) 
    if month > 12: 
        return False
    if day > days[month - 1]: 
        return False

    counter = 0 
    Sum = 0
    while counter <= 8: 
        if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter ==8: 
            matrix = 2
        else:
            matrix = 1
        temp = social[counter] * matrix
        if temp > 9:
            double_number = list(map(int,str(temp)))
            Sum += double_number[0] + double_number[1]
        else:
            Sum += temp
        counter += 1
    sum_numbers = list(map(int,str(Sum)))
    last_number = 10 - sum_numbers[1]
    if social[9] == last_number:
        return True
    else:
        return False

def gender(input) -> str:
    social = list(map(int, str(input)))
    if len(social) == 12: 
        del social[0:2] 
    if len(social) != 10: 
        return False
    if social[8] == 1 or social[8] == 3 or social[8] == 5 or social[8] == 7 or social[8] == 9:
        gen = "Male"
    else:
        gen = "Female"
    return gen

def generate(age = 6969, genderstr = 'none') -> str:
    
    if age == 6969:
        output[0] = random.randint(1, 2)
            ##year
        if output[0] == 1: # if it's 1xxx
            output[1] = 9 # 19xx
            output[2] = random.randint(3, 9) # 19rx
            output[3] = random.randint(0, 9) # 10rr
        else: # if it's 2xxx
            output[1] = 0  # 20xx
            output[2] = random.randint(0, 2) # 20rx
        if output[2] == 2: #if its >= 202x
            output[3] = random.randint(0, 1) # 2020 or 2021
        else: # if its 201x
            output[3] = random.randint(0, 9) # 2010 --------> 2019
    else:
        subtract = list(map(int, str(year - age)))
        output[0] = subtract[0]
        output[1] = subtract[1]
        output[2] = subtract[2]
        output[3] = subtract[3]

    output[4] = random.randint(0, 1)

    if output[4] == 0:
        output[5] = random.randint(1, 9)
    else:
        output[5] = random.randint(0, 2)
    
    if output[5] == 2:
        output[6] = random.randint(0, 2)
    else:
        output[6] = random.randint(0, 3)
    
    if output[5] == 2 and output[6] == 0:
        output[7] = random.randint(1,9)
    elif output[5] == 2 and output[6] == 1:
        output[7] = random.randint (0, 9)
    elif output[5] == 2 and output[6] == 2:
        output[7] = random.randint(0, 8)
    elif output[6] == 0:
        output[7] = random.randint(1, 9)
    elif output[6] == 1 or output[6] == 2:
        output[7] = random.randint(0, 9)
    else:
        output[7] = 0

    output[8] = random.randint(0, 9)

    output[9] = random.randint(0, 9)

    if genderstr == 'none':
        print("random active")
        output[10] = random.randint(0, 9)
    elif genderstr == 'male':
        print("male active")
        output[10] = random.choice([1, 3, 5, 7, 9])
    elif genderstr == 'female':
        print("female active")
        output[10] = random.choice([0, 2, 4, 6, 8])

    counter = 0 
    Sum = 0
    while counter <= 10: 
        if counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter == 10: 
            matrix = 2
        elif counter == 0 or counter == 1:
            matrix = 0
        else:
            matrix = 1
        temp = output[counter] * matrix
        if temp > 9:
            double_number = list(map(int,str(temp)))
            Sum += double_number[0] + double_number[1]
        else:
            Sum += temp
        counter += 1
    sum_numbers = list(map(int,str(Sum)))
    last_number = 10 - sum_numbers[1]
    
    output[11] = last_number

    if genderstr == 'male':
        if output[10] == 0:
            output[10] = 1

    strings = [str(integer) for integer in output]
    a_string = "".join(strings)

    numlist = list(map(int, str(a_string)))
    if len(numlist) == 13:
        new = generate(age, genderstr)
        newnumlist = list(map(int, str(new)))
        if len(newnumlist) == 12:
            return new
        else:
            generate(age, genderstr)

    return a_string
