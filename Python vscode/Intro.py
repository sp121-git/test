#variables contains strings, integers, floats, booleans
# these are strings, they are series of text, anything inside "" is a string
food = "panipuri"
first_name = 'max'

# this is integer, they are whole number, it is without ""
age = 23

#floats are integers with decimal
weight = 70.5

# booleans are True or False, make sure to have capital T and F, mostly used in if else statement
is_student = True
is_local_student = False

#typecasting is method to change form of a variable using int(), float(), bool(), str()
#using f string, it is called formatted string with which you can refer to variables, so putting f'something {variable}'
# will give output of something variable, it is space sensitive so if add space inbetween then it will show up in output


print("hello there")
print(f'your name is {first_name}')
print(f'your fav food is {food}')
print(f'your age is {age}')
print(f"your weight is {weight} Kg")
print(f"Are you a student? {is_student}")

if is_local_student:
    print("your are a local student")
# you can also use elif to make else if statement to add more condition
# and to add more condition in if statement you can use logical operators like:
# "and" here if all condition are fulfilled only then the if statement will be executed
# "or" here even if one condition is then also if statement will be executed
# "not" using this operator means that you are accepting the variables opposite value as true or false
else:
    print("you are a international student")
# you can use short version of else if statements in the code by this format..
# x if condition else y, these are called conditional expressions or ternary operators
# exmaple, print("local student" if is_student == True else "international student")
print(type(age)) #this shows the type of variable in output
print(float(age)) #after typing this the age is converted from 23(an integer) to 23.0 (a float)
#similar to that we can change the type, converting a text to boolean can be used to determine if someone has entered
#their name or not, so that if not then it will show up as false.

#input function allows to recieve data

#input is used so you can add answer in the output, you can use this to as variable so that we can interact with the output
print(f'very well, it is good to hear that your are {input('how are you?')}, let us move ahead')
last_name = input('what is your last name?')
print(f'your last name is {last_name}') #so now we get answer your last name is parker as the reply when u answer the question

# len() is used to find length of the string input
# xyz.find("letter") will find first occurrence of the letter
# xyz.rfind("letter") will find last occurrence of the letter
# xyz.capitalize() will capitalize the first letter of the string
# xyz.upper() will capitalize all the letters of the string
# zyx.lower() will convert all letters into lowercase
# xyz.isdigit() will say true or false if the input is digit or not
# xyz.isalpha() will say true or false if the input is alphabets (it is space sensitive)
# xyz.count("") will count whatever u put in the  brackets
# xyz.replace('','') is most useful, it will replace the thing enter before comma to the thing after comma
# print(help(str)) will print the list of helpful strings used in python with bit of description

#indexing is accessing elements of variable using sequence[] with format being [start : end : step]
# like if your variable is number = 12345678 then if u print(number[0] then it will give answer 1 as starting position
# starts with position 0 then 1,3,3.. so at position 0, number is 1, if i do print(number[1:4] then it will give
# 2345 as output and starts with position 1 and end with position 4, if you put empty instead of start the python will
# assume you need it from start like print(number[:4] similarly with end, print(number[3:], putting -1 will give you last element
# step is for counting the element from given number if written [::2] then it will give 2468

#format specifiers are used to format the value based on the flags(codes) inserted
#.(number)f round to that many decimal places (fixed point)
#:(number) means allocate that many spaces
#:03 means allocate and zero pad that many spaces
#:< means left justify
#:> means right justify
#:^ means center align
#:+ means use a plus sign to indicate positive value
#:= means place sign to leftmost position
#: means insert a space before positive numbers
#:, means comma separator


# while loop will execute some codes if some conditions remains true, can be used as just 'while' or 'while not' too

# import time will give us function like pausing code for sometime in between, like using time.sleep(3) will make code sleep
# for 3 seconds then it will continue ahead

#import random gives you access to generate random number
# random.randint(range of number like 1,6) will give you random numbers
# if you have a list of something from which u need to pick randomly than use random,choice() method
# random.shuffle() can be used to shuffle the list 
# list [] - mutable and flexible
# tuple () - immutable and faster
# sets {} - mutable, unordered, no duplicates
