def max1(list2):
    max_no=list2[0]
    for i in list2:
        if i>max_no:
            max_no=i
    return max_no    
    
def calc_BMI(height, weight):
    # 計算 BMI
    # 判斷 體重是否過重
    BMI = float(weight)/((float(height)/100)**2)

    if BMI<18.5:
        message = "注意：您的體重太輕，要注意攝取營養。"
    elif 18.5<=BMI<25:
        message = "恭喜您！您的體重正常，請保持。"
    elif 25<=BMI<30:
        message = "注意：您的體重過重，請保持好的生活習慣來維持健康。"
    else:
        message = "注意：您體重已達肥胖，請保持好的生活習慣來維持健康。"
    
    return BMI, message
    
def print_9x9(x, y):
    out = ''
    for i in range(1, x+1):
        for j in range(1, y+1):
            out += f'{i}*{j}={i*j}\t'
        out += '\n'
    return out
    
def check_prime(x):
    is_prime = True # 是質數
    for i in range(2, x):
        if x%i == 0:
            is_prime = False
            break
        
    return is_prime
    
    
if __name__ == '__main__':
    print(check_prime(10))
    assert check_prime(10) == True
    print(check_prime(11))
    print(calc_BMI(170,70))
    print(calc_BMI(180,70))
    print(calc_BMI(190,90))
    

def sum_list(list1):
    total=0
    for i in list1:
        total+=i
    return total

def sort_list(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-1):
            if list1[j]> list1[j+1]:
                list1[j], list1[j+1] = list1[j+1],list1[j]
    return list1

def isPalindrome(s):
    return s[::-1]
    
    
if __name__=='__main__':
    print(palindrome('1234'))

