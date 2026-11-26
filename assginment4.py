#1. Data Types1. 
#  1.Find data type of every value in a mixed list 

def check_types(lst):
    for x in lst:
        print(x, "->", type(x).__name__)

check_types([1, "hello", 3.5, True, [1,2], None]) 

#2. Convert nested list into tuple of tuples 
nested = [[1, 2], [3, 4], [5, 6]]
result = tuple(tuple(x) for x in nested)
print(result) # ((1, 2), (3, 4), (5, 6)) 

#3. Remove duplicates while preserving order 
def remove_duplicates(lst):
    seen = []
    for x in lst:
        if x not in seen:
            seen.append(x)
    return seen

print(remove_duplicates([1, 2, 2, 3, 1, "a", "a", "b"])) 


#2. Operators 
# 4. Check if number is power of 2 
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_2(16)) 
print(is_power_of_2(18))  

#5. Swap two numbers using bitwise XOR 
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  

#6. Divisible by both 4 and 6 
def divisible_by_4_and_6(n):
    return n % 4 == 0 and n % 6 == 0

print(divisible_by_4_and_6(12)) 
print(divisible_by_4_and_6(8)) 

#7. Electricity bill 

def electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6
    return bill

print(electricity_bill(250))  

#3. Conditional Statements 
# 8. Check if three sides can form a triangle 
def can_form_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(can_form_triangle(3, 4, 5)) 

#9. Type of triangle
def triangle_type(a, b, c):
    if not can_form_triangle(a, b, c):
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(triangle_type(3, 3, 3)) 
print(triangle_type(3, 3, 4)) 
print(triangle_type(3, 4, 5))  

#10. Simple ATM menu 
def atm():
    balance = 1000
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            amt = float(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print("Withdrawn. New balance:", balance)
            else:
                print("Insufficient balance!")
        elif choice == 2:
            amt = float(input("Enter amount to deposit: "))
            balance += amt
            print("Deposited. New balance:", balance)
        elif choice == 3:
            print("Balance:", balance)
        elif choice == 4:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


#11. Income tax based on slabs 
def income_tax(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30
    return tax

print(income_tax(600000)) 

#12. Menu-driven calculator 
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1. Add  2. Subtract  3. Multiply  4. Divide")
    op = int(input("Enter choice: "))
    if op == 1:
        print("Result:", a + b)
    elif op == 2:
        print("Result:", a - b)
    elif op == 3:
        print("Result:", a * b)
    elif op == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid choice!")


#4. Loops
# 13. Prime numbers between 1 and n 
def primes_upto(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

primes_upto(20) 

#14. Factorial using loop
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5)) 

#15. Fibonacci series up to n terms 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10) 

#16. Armstrong number 
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

print(is_armstrong(153)) # True
print(is_armstrong(123)) # False 


#17. Reverse number and check palindromepython 
def reverse_number(n):
    rev = 0
    temp = n
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev

def is_palindrome_number(n):
    return n == reverse_number(n)

print(reverse_number(123)) 
print(is_palindrome_number(121)) 

# 18. GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18)) 
#5. Functions
#19. Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Madam")) 


#20. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

print(count_vowels_consonants("Hello World")) 

#21. Simple and Compound Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t - p

print(simple_interest(1000, 5, 2)) 
print(compound_interest(1000, 5, 2)) 


#22. Return all factors of a number
def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print(factors(12)) 
#23. Second-largest number in a list
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


#6. Lists
#24. Merge two lists without duplicates
def merge_lists(l1, l2):
    result = []
    for x in l1 + l2:
        if x not in result:
            result.append(x)
    return result

print(merge_lists([1, 2, 3], [3, 4, 5])) 



#25. Second-largest and second-smallest
def second_largest_smallest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return "Not enough unique elements"
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    for num in unique:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_largest, second_smallest

print(second_largest_smallest([5, 1, 4, 2, 3]))  


#26. Rotate a list to the left by k position
def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_left([1, 2, 3, 4, 5], 2)) 

#27. Separate even and odd numbers into two lists
def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

print(separate_even_odd([1, 2, 3, 4, 5, 6])) 


#28. Find common elements between two lists
def common_elements(l1, l2):
    result = []
    for x in l1:
        if x in l2 and x not in result:
            result.append(x)
    return result

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6])) 


#7. Tuples & Sets
#29. Count frequency of each element in a tuple
def count_frequency(t):
    freq = {}
    for x in t:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

print(count_frequency((1, 2, 2, 3, 1, 1))) 


#30. Union, intersection, and difference of two sets
def set_operations(s1, s2):
    print("Union:", s1 | s2)
    print("Intersection:", s1 & s2)
    print("Difference (s1 - s2):", s1 - s2)
    print("Difference (s2 - s1):", s2 - s1)

set_operations({1, 2, 3}, {3, 4, 5})


# 31. Check whether one set is a subset of another
def is_subset(s1, s2):
    return s1.issubset(s2)

print(is_subset({1, 2}, {1, 2, 3, 4})) 
print(is_subset({1, 5}, {1, 2, 3, 4})) 

#32. Count frequency of words in a sentence
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(word_frequency("hello world hello python")) 


#33. Create dictionary from two lists (keys and values)
def create_dict(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

print(create_dict(["a", "b", "c"], [1, 2, 3])) 

#34. Sort dictionary by its values
def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

print(sort_by_value({"a": 3, "b": 1, "c": 2})) 


#9. File Handling
#35. Read a text file and count lines, words, characters
def count_file_stats(filename):
    with open(filename, 'r') as f:
        text = f.read()
        lines = text.splitlines()
        words = text.split()
        print("Lines:", len(lines))
        print("Words:", len(words))
        print("Characters:", len(text))

#36. Copy only even-numbered lines from one file to another
def copy_even_lines(source, dest):
    with open(source, 'r') as f1, open(dest, 'w') as f2:
        lines = f1.readlines()
        for i in range(1, len(lines)):
            if (i + 1) % 2 == 0:
                f2.write(lines[i])
    print("Even lines copied!")


#37. Handle invalid integer input using try-except
def get_integer():
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input! Please enter an integer.")

 
# 38. Handle file-not-found errors while reading a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

read_file("no_file.txt")

#11. Modules
#39. Random password generator
import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password(10))
print(generate_password(12))


#40. Days between two dates using datetime
from datetime import date
def days_between(d1, d2):
    
    date1 = date(d1[0], d1[1], d1[2])
    date2 = date(d2[0], d2[1], d2[2])
    return abs((date2 - date1).days)

print(days_between((2025, 1, 1), (2025, 1, 15))) # 14
print(days_between((2026, 11, 26), (2026, 12, 31))) # 35