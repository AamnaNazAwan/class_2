   #IF ELIF ELSE CONDITIONS
              #NESTED CONDITION

number = 15

if number % 2 == 0:
    print("number is even")
else:
    if number % 3 == 0:
        print("number is divisibl by 3")
    else:
        print("number is odd and not divisible by 3")

fruit = "apple"
fruits = ["apple", "banana", "cherry"]

if fruit in fruits:
    print("fruit is in list")
else:
    print("fruit ia not in list")

#TRY EXCEPT

try:
      value = int(input("enter the number"))
      result = 10/value
except ValueError:
       print("Error : invalid input")
except ZeroDivisionError:
       print("Error : cannot divide by zero")

#RUN this command 3 times using while loop
attempts = 3

while attempts > 0:
    user_input = input("Enter the age of person: ")

    try:
        age = int(user_input)
        if age < 0:
            print("invalid age")
        elif 0 <= age <= 12:
            print("you are a child")
        elif 13 <= age <= 19:
            print("you are a teenager")
        elif 20 <= age <= 64:
            print("you are an adult")
        elif age >= 65:
            print("you are a senior")
    except ValueError:
        print("please enter a valid number")

    attempts -= 1


