def calculate_and_print(num1, opp, num2, text_for_answer):
    print("* = multiply, / = divide")
    if opp == "+":
        total = str(num1 + num2)
    elif opp == "-":
        total = str(num1 - num2)
    elif opp == "*":
        total = str(num1 * num2)
    elif opp == "/":
        total = str(num1 / num2)
    print(text_for_answer + " " + total)
    
def only_calculate_and_save(num1, opp, num2):
    if opp == "+":
        total = str(num1 + num2)
    elif opp == "-":
        total = str(num1 - num2)
    elif opp == "*":
        total = str(num1 * num2)
    elif opp == "/":
        total = str(num1 / num2)
    return total

def only_calculate_and_save_with_the_text_of_the_answer(num1, opp, num2, text_for_answer):
    if opp == "+":
        total = str(num1 + num2)
    elif opp == "-":
        total = str(num1 - num2)
    elif opp == "*":
        total = str(num1 * num2)
    elif opp == "/":
        total = str(num1 / num2)
    return text_for_answer + " " + total

def only_calculate_and_save_in_text_file(num1, opp, num2, filename):
    if opp == "+":
        total = str(num1 + num2)
    elif opp == "-":
        total = str(num1 - num2)
    elif opp == "*":
        total = str(num1 * num2)
    elif opp == "/":
        total = str(num1 / num2)
    if ".txt" not in filename:
        filename = filename + ".txt"
    else:
        filename = filename
    with open(filename, "w") as file:
        file.write(total)
    return total

def only_calculate_and_save_in_text_file_with_text_of_the_answer(num1, opp, num2, filename, text_for_answer):
    if opp == "+":
        total = str(num1 + num2)
    elif opp == "-":
        total = str(num1 - num2)
    elif opp == "*":
        total = str(num1 * num2)
    elif opp == "/":
        total = str(num1 / num2)
    if ".txt" not in filename:
        filename = filename + ".txt"
    else:
        filename = filename
    with open(filename, "w") as file:
        file.write(text_for_answer + " " + total + "\n")
    return total

num1 = float(input("Enter first Number: "))
opp = input("Enter the operation: ")
num2 = float(input("Enter the second number: "))