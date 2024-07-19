'''for letter in 'word':
    print(letter)

x = 1
for letter in 'word':
    print(x)
    x += 2

count = [1,2,3,4,5]
for i in count:
    print(i,"^2 =",i*i)

#range(2,10,3) where 2 is starting point 10 is ending poinnt and 3 is difference so answer will be(2,5,8)
#range(4,1,-1) returns [4,3,2,1]

numbers = [1,2,3,4,5]
total = 0

for number in numbers:
    total +=number
print(f"total sum: {total}")

person = {"name":"Alice", "age":30, "proffession": "Engineer"}
for key,value in person.items():
    print(f"{key}:{value}")

for i in range(1,6):
    for j in range(1,6):
        print(f"{i} * {j} = {i*j}")
    print()

#numbers = [1,2,3,4,5]
#squares = [numbers ** 2 for number in numbers]
#print(squares)

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)


unique_numbers = {1,2,3,4,5}
for i in unique_numbers:
    print(i)'''


#enter a string: hello world
#number of vowels:3



#write a program that asks the user to input a string and then counts and print the
#number of vowels(a,e,i,o,u) in string



sentence = input("enter the string")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(f"number of vowels:{count}")


                    #WHILE LOOP
total = 0
num = 1
while num<=10:
    total+=num
    num+=1
print("the total sum is ",total)




