from turtle import st


name= "Ayush"
age= 20
age_next_year= age + 1
# print("hello there user thanks for using my file")
# str=input("Enter your name:")
# print("Thanks", str, "for using my file")
# print("This file is created by", name, "and I am", age, "years old")
# print("Next year I will be", age_next_year, "years old")
# str=input("Enter you age here:")
# print("Next year you will be", int(str) + 1, "years old")
#  a= 69
#  b= 69
# print("The sum of a and b is", a + b)
# a = 50
# b = 20
# print(not False)
# print(not (a>b))
# a= 20
# b= 20
# val1= True
# val2= False
# print(val1 and val2)
# print(val1 or val2)
# print(a == b and a == b)
name= input("Enter your name:")
print("Hello there!", name)
print ("thanks for using this file, we really appreciate it :3")
age= input("Enter you age:")
print("Next year you will be", int(age)+1, "years old")
print("thats quite nice")
response = input("is that right:")
if response == "yes":
    print("Great!")
else:
    age= input("oh no! please enter your age again:")
    print("oh so you are", age, "years old"," next year you will be", age + 1, "years old")
print("thanks for using my file")
input("Press Enter to exit...")