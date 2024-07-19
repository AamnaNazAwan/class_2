              #IF ELIF ELSE CONDITIONS
              #NESTED CONDITION

'''number = 15

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
    print("fruit ia not in list")'''

#RUN this command 3 times using while loop

user_input = input("Enter the age of person")

while user_input<=3:
 try:
     age = int(user_input)
if age < 0:
      print("invalid age")
elif  0 <= age <= 12:
    print("you are a child")
elif age  > 13 and age < 19:
    print("you are a teenager")
elif age >20 and age < 64:
    print("you are a adult")
elif age > 65:
    print("you are senior")
 except ValueError:
      print("Error : invalid age")
   user_input +=1


enter your age = 25
you are an adult
              
              
enter your age: -5
invalid age
              
enter your age: seventeen
please enter a valid number


             #TRY EXCEPT

try:
      value = int(input("enter the number"))
      result = 10/value
except ValueError:
       print("Error : invalid input")
except ZeroDivisionError:
       print("Error : cannot divide by zero")