#1. Check if a number is positive, negative, or zero. 

num = int(input("Enter Number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")


 #2. Check whether a number is even or odd. 

num = int(input("Enter Number:"))
if num % 2 == 0:
     print("Even")
else: 
     print("Odd")


 #3. Find the greater of two numbers. 
 
a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))
if a > b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than", a)

#4. Find the greatest of three numbers. 

a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))
c = int(input("Enter the third no:"))
if a >= b and a >= c:
    print(a, "is greater than ",b,c)
elif b >= a and b >= c:
    print(b,"is graeter than",a,c)
else:
    print(c,"is gearter than",a,b)

#5. Check if a person is eligible to vote (age ≥ 18). 

age = int(input("Enter your age:"))
if age >=18:
    print("You are eligible for  vote ")
else:
    print("You are not eligible for vote")

#6. Check whether a year is a leap year

year = int(input("Enter the year:"))
if year % 400 == 0:
    print("This is the Leap year")
else:
    print("This is Not Leap year")

#7.Check if a character is a vowel or consonant. 

ch = input("Enter character: ").lower()
if ch in "aeiou" :
    print("VOWELS")
else:
    print("CONSONANTS")


#8.Check whether a number is divisible by 5 and 11. 

num = int(input("Enter the number:"))
if num % 5==0  and num % 11==0 :
    print("Dibisible by 5 and 11")
else:
    print("Not divisible ")

#9.Check if a number is a multiple of both 3 and 7. 

num = int(input("Enter the number:"))
if num % 3==0 and num % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("No multiple")

#10.10. Assign grades based on marks:
#  a. 90–100: A 
# b. 80–89: B 
# c. 70–79: C 
# d. 60–69: D 
# e. Below 60: F 
marks = int(input("Enter the marks"))
if marks >= 90:
    print("Grade A ")
elif marks >=80:
    print("Grade B ")
elif marks >=70:
    print("Grade C ")
elif marks >=60:
    print("Grade  D ")
else:
    print("Grade F ")


#11. Check if a character is uppercase or lowercase. 

ch = input("Enter Character:")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not alphabet")


#12. Find whether the entered alphabet is a vowel using if-elif. 

ch = input("Enter alphabet:").lower()
if ch == 'a'or ch == 'e'or ch == 'i'or ch =='o'or ch == 'u':
  print("Vowels")
else:
  print("Not vowels")


#13.Check if three sides can form a triangle. 

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b > c and b + c > a and a + c > b:
    print("Can form triangle")
else:
    print("Cannot form triangle")

#14.Determine the type of triangle (Equilateral, Isosceles, Scalene). 

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

#15.Find the largest among four numbers. 

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))
print("Largest is:", max(a, b, c, d))

#16. Check whether a number is a three-digit number. 

num = int(input("Enter number: "))
if 100 <= num <= 999 or -999 <= num <= -100:
    print("Three-digit number")
else:
    print("Not three-digit")

#17. Calculate electricity bill using slab rates. 
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100*3 + (units-100)*5
else:
    bill = 100*3 + 100*5 + (units-200)*7
print("Bill:", bill)


#18.Calculate income tax based on income slabs. 

income = int(input("Enter income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30
print("Tax:", tax)

#19.Check if a student passes (minimum 35 marks in each subject). 

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")

 #20.Find whether a number is within a given range. 

num = int(input("Enter number: "))
low = int(input("Enter low: "))
high = int(input("Enter high: "))
if low <= num <= high:
    print("Within range")
else:
    print("Out of range")

#21.Build a simple calculator using if-elif-else (+, -, *, /).

a = float(input("Enter first: "))
b = float(input("Enter second: "))
op = input("Enter + - * / : ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")


#22.Check if a year is a century leap year. 

year = int(input("Enter year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Century Leap Year")
    else:
        print("Century but Not Leap Year")
else:
    print("Not Century Year")


#23. Determine the season based on the month number. 

month = int(input("Enter month 1-12: "))
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Summer")
elif month in [6, 7, 8, 9]:
    print("Monsoon / Rainy")
else:
    print("Autumn")


#24. Find the number of days in a month. 

month = int(input("Enter month 1-12: "))
if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")


#25.Check whether a password meets minimum conditions (length, digits, etc.). 

pwd = input("Enter password: ")
if len(pwd) >= 8 and any(c.isdigit() for c in pwd):
    print("Strong password")
else:
    print("Weak password - min 8 chars and 1 digit needed")


#26. Determine ticket price based on age category. 

age = int(input("Enter age: "))
if age < 5:
    print("Free")
elif age < 18:
    print("Price: 50")
elif age < 60:
    print("Price: 100")
else:
    print("Price: 60 - Senior discount")


#27.Calculate discount based on purchase amount. 

amount = float(input("Enter amount: "))
if amount >= 5000:
    print("Discount 20%, Pay:", amount * 0.8)
elif amount >= 1000:
    print("Discount 10%, Pay:", amount * 0.9)
else:
    print("No discount, Pay:", amount)


#28.Check if a person is eligible for a driving license (age and eyesight condition). 

age = int(input("Enter age: "))
eyesight = input("Eyesight ok? yes/no: ").lower()
if age >= 18 and eyesight == "yes":
    print("Eligible for license")
else:
    print("Not eligible")



# 29.Create a login system with username and password validation. 

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid username or password")


#30.Create a menu-driven program using if-elif-else with options like: 
# a. Addition 
# b. Subtraction 
# c. Multiplication 
# d. Division
#  e. Exit 

print("1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
choice = int(input("Enter choice: "))
if choice == 5:
    print("Exit")
else:
    a = float(input("Enter first: "))
    b = float(input("Enter second: "))
    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4:
        print(a / b)
    else:
        print("Invalid choice")


