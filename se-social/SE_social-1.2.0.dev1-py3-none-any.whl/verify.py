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