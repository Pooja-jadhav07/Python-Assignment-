# 1.Write a Python program to check whether a number is even or odd

n = int(input("Enter the number:"))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


    #2.Write a program to find the largest of three numbers

a = int(input("Enter the 1st no:"))
b = int(input("Enter the 2nd no:"))
c = int(input("Enter the 3rd no:"))
if a >= b and a >= c:
    print("Largest:",a)
elif b>=a and b>=c :
    print("Largest:",b)
else:
    print("Largest:",c)


# 3.Write a program to check whether a given number is prime.

n = int(input("Enter the number:"))
if n < 2:
    print("Not Prime...")
else:
    for i in range(2,n):
        if n% i == 0:
            print("Not prime")
            break 
        else:
            print("Prime") 


# 4.Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter the term:"))
a , b = 0, 1
for i in range (n):
    print(a, end="")
    a,b = b, a+b 


# 5.Write a program to find the factorial of a number using a loop.

n = int(input("Enter the term:"))
fact = 1
for i in range(1,n+1):
    fact = fact*i 
    print("Factorial", fact) 


# 6. Write a program to reverse a string without using [::-1].

s = input("Enter the string:")
rev = ""
for ch in s:
    rev = ch + rev 
    print("Reversed",rev)


# 7. Write a program to check whether a string is a palindrome.

s = input("Enter the string:")
rev = ""
for ch in s:
    rev = ch + rev 
    if s == rev:
        print("It is Palindrome") 
    else:
        print("It is Not Palindrome") 


# 8. Write a program to count the number of vowels and consonants in a string. 

s = input("Enter string: ").lower()
vowels = "aeiou"
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)


# 9.Write a program to find the sum of all elements in a list. 
  
numbers = []
n = int(input("Enter the how many numbers:"))   #the user to enter list elements after running the program
for i in range(n):
    num = int(input("Enter the number:"))
    numbers.append(num)

    total = 0 
    for i in numbers:
        total = total+i 
        print("Sum of all elements:",total )



# 10.Write a program to find the largest and smallest element in a list without using max(). 

lst = [10, 5, 20, 3, 15]
largest = smallest = lst[0]
for x in lst:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
print("Largest:", largest, "Smallest:", smallest)  


# 11.Write a program to remove duplicate elements from a list. 

lst = [1, 2, 2, 3, 4, 4, 5]
new = []
for x in lst:
    if x not in new:
        new.append(x)
print(new)  


               # Write a program to remove duplicate elements from a list.  (the user to enter list elements after running the )

lst = list(map(int, input("Enter numbers with space: ").split()))
new = []

for x in lst:
    if x not in new:
        new.append(x)

print("Original list:", lst)  
print("Without duplicate:", new)


#12. Write a program to count how many times each element appears in a list using a dictionary
   
lst = [1, 2, 2, 3, 1, 4, 2]
count = {}
for i in lst:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    print(count)  



#13.Write a program to find the second-largest number in a list.

lst = [10,20,4,45,99]
largest = max(lst)
second = None 
for i in lst:
    if i != largest:
        if second is None or i > second:
            second = i 
            print("second largeest :", second)  


#14. Write a program to sort a list without using sort() or sorted().

lst = [5, 2, 9, 1, 7]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)


#15. Write a function that accepts a list of numbers and returns a list containing only the even numbers

def get_even(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

print(get_even([1, 2, 3, 4, 5, 6]))


#16. Write a program to find the frequency of each character in a string.

s = "hello"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)


#17. Write a program to check whether two strings are anagrams of each other.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")


#  18.Write a program to find all duplicate values in a list.

my_list = [10, 20, 30, 10, 40, 20, 50, 30]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Original List:", my_list)
print("Duplicate Values:", duplicates) 


#19. Write a program that takes a sentence and finds the longest word.

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word is:", longest)
print("Length:", len(longest)) 



#20. 20. Create a simple student marks program that:
#a. accepts marks for 5 subjects,
#b. calculates the total and percentage,
#c. assigns a grade,and displays whether the student passed or failed

print("Enter marks for 5 subjects (out of 100):")
m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))
m4 = int(input("Subject 4: "))
m5 = int(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 35:
    print("Result: PASSED")
else:
    print("Result: FAILED")