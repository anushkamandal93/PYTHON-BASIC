#INPUT AND OUTPUT--------------------------------------------------------------------------------------------------------

#1) Accept numbers from a user
""" num = int(input("enter the no.")) """

#2) Display three string “Name”, “Is”, “James” as “Name**Is**James”
""" name = input("name is james") """

#3) Display float number with 2 decimal places using print()
""" num = 12.34567
print(f"{num:.2f}") """ 

#4) Sum of two integers
""" num1 = int(input("enter the no."))
num2= int(input("enter the no."))
sum=num1+num2
print(f"The sum is {sum}") """

#5) Accept two integers from user and print the sum
""" num1 = int(input("enter the no."))
num2= int(input("enter the no."))
sum=num1+num2
print(f"The sum is {sum}") """

#6) Accept the User's name, age and print in following manner
""" name = input("enter the name.")
age = int(input("enter the age."))
print(f"The name is {name} and age is {age} ") """

#CONDITIONAL STATEMENTS--------------------------------------------------------------------------------------------------
#7) Take 3 int inputs from user and check and print the result.
""" m1 = int(input("enter the no.1."))
m2 = int(input("enter the no.2."))
m3 = int(input("enter the no.3."))
if  m1 == m2 and m2 == m3 :
  print("all are equal")
elif m1 == m2 or m2 == m3 or m1 == m3 :
  print("any two equal")
else:
    print("None are equal") """

#8) Accept two numbers and print the greatest between them
""" m1 = int(input("enter the no.1."))
m2 = int(input("enter the no.2."))
if  m1 > m2 :
  print(f"{m1} is greater")
elif m1 < m2 :
  print(f"{m2} is greater")
else:
    print("equal") """

#9) Accept the gender from the user as char and print the respective greeting message
""" g= input("enter the gender.")
if g == "f" :
    print("Good Morning maam")
elif g == "m"  :
    print("Good Morning sir")
else :
    print("Good Morning")  """  

# 10) Extend the previous program and handle the wrong inputs.
""" g= input("enter the gender.")
if g == "f" or "F" :
    print("Good Morning maam")
elif g == "m" or  "M"  :
    print("Good Morning sir")
else :
    print("wrong input") """

#11) Accept an integer and check whether it is an even number or odd.
""" num = int(input("enter the no."))
if num % 2 == 0 :
 print(f"{num} is even ")
else :
    print(f"{num} is odd ") """

#12) Accept name and age from the user. Check if the user is a valid voter or not.
""" name = input("Enter your name: ")
age = int(input("Enter your age: "))
MIN_VOTING_AGE = 18
print(f"Hello {name}")
if age >= MIN_VOTING_AGE:
    print("You are a valid voter.")
else:
    years_to_wait = MIN_VOTING_AGE - age
    print("You are not eligible to vote yet.")
    print(f"You will be eligible to vote in {years_to_wait} years.") """

#13) Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)
""" import math
principal = float(input("Enter the Principal amount (P): "))
rate = float(input("Enter the Annual Interest Rate in % (r): "))
time = float(input("Enter the Time in years (t): "))
amount = principal * math.pow((1 + rate / 100), time)
compound_interest = amount - principal
print(f"\nTotal Amount after {time} years: {amount:.2f}")
print(f"Compound Interest: {compound_interest:.2f}") """

#14) Accept a year and check if it a leap year or not (google to find out what's a leap year)
""" year = int(input("Enter a year to check: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False
if is_leap:
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.") """

#15) Accept an english alphabet from user and check if it is a consonant or a vowel.
""" L = input("enter the letter.")
if L == "aeiouAEIOU"  :
 print(f"{L} is vowel ")
else :
    print(f"{L} is consonant ") """

#ITERATIVE STATEMENTS---------------------------------------------------------------------------------------------------
#16) Accept an integer and Print hello world n time.
""" n = int(input("Enter how many times to print: "))
for i in range(n):
    print("Hello World") """

#17) Print natural number up to n. 
""" n = int(input("Enter the no.: "))
for i in range(1,n+1):
    print(i) """

#18) Reverse for loop. Print n to 1.
""" n = int(input("Enter the no.: "))
for i in range(n,0,-1):
    print(i) """ 

#19) Take a number as input and print its table
""" n = int(input("Enter the no.: "))
for i in range(1,11):
     print(f"{n}x{i}={n*i}") """

#20) Sum up to n terms.
""" n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += i  
print(f"The sum of numbers from 1 to {n} is: {sum}") """

#21) Factorial of a number
""" n = int(input("Enter the value of n: "))
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i  
print(f"The factorial of {n} is {factorial}") """

#22) Print the sum of all even & odd numbers in a range seperately.
""" n= int(input("Enter the starting number: "))
even = 0
odd = 0
for i in range(n + 1):
    if i % 2 == 0:
        even += i  
    else:
        odd += i   
print(f"Sum of even numbers: {even}")
print(f"Sum of odd numbers: {odd}") """

#23) Print all the numbers which are either divisible by 3 or 5 in a range 
""" start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Numbers between {start} and {end} divisible by 3 or 5:")
for i in range(start, end + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" " """

#24) Print all the factors of a number.
""" n = int(input("Enter a number to find its factors: "))
print(f"The factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ") """

#25) Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43
""" n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
print(f"The sum of factors (excluding {n}) is: {sum}") """

# 26)  Accept a number and check if it a perfect number or not.
""" n = int(input("enter a number :"))
a = 0
for i in range(1,n):
 if n % i == 0:
     a = a + i
if a == n:
    print("number is perfect")
else:
   print("not a perfect number") """

#27) Seprate each digit of a number and print it on the new line
""" n = int(input("Enter a number: "))
print("Digits from right to left:") 
while a > 0:
     print(a%10)
     a = a //10 """
       
# 28) Check if the number is Prime or not.
""" n = int(input("enter a number :"))
count  = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("prime number")
else:
    print("composite number") """ 

# 29) Accept a number and print its reverse
""" num  = int(input("Enter a number: "))
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse*10 + remainder
    num = num // 10
print(f"{reverse}") """

# 30) Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
""" num  = int(input("Enter a number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse*10 + remainder
    num = num // 10
if temp == reverse :
  print("pallindromic number")
else:
 print("not a pallindromic number") """

##STRNGS----------------------------------------------------------------------------------------------------------------
#31) Print string in reverse,its length,in uppercase,lowercase and copy into another string
""" s="shery"
print(f"reverse string ->{s[::-1]}")
print(f"length of string ->{len(s)}")
print(f"string in upper format->{s.upper()}")
print(f"string in lower format ->{s.lower()}") """

#32) Arrange string characters such that lowercase letters should come first
""" s= "ShEry"
lower = ""
upper = ""
for i in s:
    if i.islower():
        lower=lower + i 
    elif i.isupper():
        upper = upper + i
print(lower + upper) """

#33) Count all letters, digits, and special symbols from a given string
""" tr1 = "Aifhs298#@$"
alpha = 0 #alpha,digit,special = 0 ,0, 0 (alter way for less  line)
digit =0
special= 0
for i in str1:
    if i.isalpha():
       alpha = alpha + 1
    elif i.isdigit ():
        digit=digit  + 1
    else :
        special=special+1
print(f"alpha count ->{alpha}")
print(f"digit count ->{digit}")
print(f"special count ->{special}") """

#34) Compare two strings without using inbuilt functions.
""" str1 = "hello"
str2 = "Helloo"
if len(str1)  == len(str2)  :
    for i in range (len(str1)) :
        if str1[i] != str2[i] :
            print("not same")
            break
    else:
        print("same")
else:
    print("both are not same")  """

# 35) Count Vowels from given string
""" str1 = "Helloo"
vowels = "AEIOUaeiou"
count =  0

for i in str1 :
    if i in vowels:
        count += 1
print(f"total count of vowels are {count} ") """

# 36) Reverse a string
""" z=("hello")
print(z[::-1])  """
 
""" z=("hello")
for i in z:
 print(i)  """

""" z=("hello")
for i in z[::-1]:
 print(i)  """

""" z=("hello") 
rev = ""
for i in z[::-1]:
     rev = rev + i
print(rev) """

# 37) Check string is Pallindrome or not**
""" s = "madam"
if str(s)==str(s)[::-1]:
 print(f"{s} is palindrome.")
else : 
   print(f"{s} is not palindrome.") """