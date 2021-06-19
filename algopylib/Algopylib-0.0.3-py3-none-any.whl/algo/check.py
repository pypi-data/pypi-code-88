import math

def is_power_of_2(num : int) -> bool:
    """
    Finds whether a number is a power of 2.

    Parameters:
        num: the number to be checked

    Returns:
        True if number is a power of 2, otherwise False
    """
    if num <= 0:
        raise ValueError
    else:
        if  num & (num - 1) == 0:
            return True
        else:
            return False
        

def is_power_of_n(num:int,n :int) ->bool:
    """
    Check whether a number is a power of n.
    Parameters:
        num: the number to be checked
        n: the number those power num is checked
    Returns:
        True if number is a power of n, otherwise False
    """
    
    if num <= 0:
        raise ValueError
    else:
        
        if(math.ceil(math.log10(num)/math.log10(n))==math.floor(math.log10(num)/math.log10(n))):
            return True
        else:
            return False

    

def is_square(num : int) -> bool:
     """
    Check if a number is perfect square number or not.

    Parameters:
         num: the number to be checked

    Returns:
        True if number is square number, otherwise False
    """
     if num < 0:
         raise ValueError("math domain error")
     if math.sqrt(num) * math.sqrt(num) == num:
        return True
     else:
         return False
    


def is_palindrome(s : str) -> bool:
    """
    Checks if a given string is palindrome or not.
    A string is said to be palindrome if the reverse of the string is the same as string.

    Parameters:
        s: The string to be checked.

    Returns:
        True if string is palindrome, otherwise False.

    """
    if s == s[::-1]:
        return True
    else:
        return False

    

def is_subsequence(str1 : str, str2 : str) -> bool:
    """
    Given two strings string1 and string2, finds if string1 is a subsequence of string2.
    
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
    
    Parameters:
        string1: string being checked to be a subsequence
        string2: original string

    Returns:
        True if subsequence, else False
    """
    len_str1 : int = len(str1)
    len_str2 : int = len(str2)
    i : int = 0  
    j : int = 0  
    # Traverse both str1 and str2
    while i < len_str1 and j < len_str2:
        # Compare current character of str2 with str1
        if str1[i] == str2[j]:
            # If matched, then move to next character in str1
            i = i + 1
        j = j + 1
    return i == len_str1
    


def is_even(num : int) -> bool:
    """
    Check if a number is even or not.

    Parameters:
         num: the number to be checked

    Returns:
        True if number is even, otherwise False
    """
    if (num%2) == 0:
        return True
    else:
        return False
    

def is_odd(num : int) ->bool:
    """
    Checks if a number is odd or not.

    Parameters:
         num: the number to be checked

    Returns:
        True if number is odd, otherwise False
    """
    if (num%2) != 0:
        return True
    else:
         return False
    
def is_prime(num : int) -> bool:
    """
    Checks if a number is prime or not.

    Parameters:
         num: the number to be checked

    Returns:
        True if number is prime, otherwise False
    """
    flag : bool = True

    if num <= 0:
        raise ValueError("Input argument should be a natural number")
    elif num == 1:
        flag = False 
    else:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag

