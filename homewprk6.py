# Home Work 6.2
while True:
    number1 = int(input("Enter first number...: "))
    action1 = input("Enter action (+, -, *, /)...: ")
    number2 = int(input("Enter second number...: "))

    if action1 == "+":
        print("Result:", number1 + number2)
    elif action1 == "-":
        print("Result:", number1 - number2)
    elif action1 == "*":
        print("Result:", number1 * number2)
    elif action1 == "/":
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Error: Division by zero.")
            continue
    else:
        print("Error: Invalid action.")
        continue

    user_input = input("Enter 'yes' If you want to leave the program or 'no' if you want to continue using the program: ")
    if user_input.lower() == "no":
        continue
    if user_input.lower() == "yes":
        print("Exit from program...")
        break

###################################
# home work 6.1

import string
import keyword

test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', '3m', 'm3', 'assert', 'assert_exception', 'some_super_puper__value']

for test_variable in test_data:
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:
            print(f"Error! Found {test_variable} is keyword!")
        elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0:
            is_correct = True
            for symbol in string.punctuation.replace("_", ""):
                if symbol in test_variable:
                    is_correct = False
                    print(f"Error! Found {test_variable} in variable name!")
                    break

            if test_variable.find("__") != -1:
                is_correct = False
                print(f"Error! Found double __ in {test_variable} variable name!")

            if is_correct:
                print(f"Keyword {test_variable} is correct!")
        else:
            print(f"Error! Found {test_variable} in variable name!")
    else:
        print("Incorrect variable length!")


# Home Work 6.3

import string

input_string = "Python Community"
input_string = input_string.translate(str.maketrans("", "", string.punctuation))
input_string = input_string.title().replace(" ", "")
result = "#" + input_string[:140]
print(result)





