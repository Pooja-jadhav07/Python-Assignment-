#1.Even or Odd Function

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4)) 
print(is_even(7)) 


#2.Largest of Two Numbers

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20)) # 20 


#3. Print Numbers

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5) 


#4. Sum of Numbers 

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(5))  


#5. Multiplication Table 

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

table(9) 


#6. Count Even Numbers 

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6])) 


#7. Find Maximum 

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 9, 2, 7])) 


#8. FizzBuzz 

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz() 


#9. Palindrome Checker 

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("madam")) 
print(is_palindrome("hello")) 


#10. Count Vowels 

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Hello World")) 


#11. Second Largest Number.

def second_largest(lst):
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

print(second_largest([10, 20, 4, 45, 99])) 


#12. Guessing Game 

import random

def guessing_game():
    secret = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret:
            print("Correct! You guessed it!")
            break
        elif guess < secret:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game() 


#Grade Function 

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(85)) 
print(grade(95)) 
print(grade(50))  


