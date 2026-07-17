#QUESTIONS-------------------------------------------------------------------------------------------------------------------
#Q1. Ask the user to enter the no. and print the reverse
""" n = int(input("please tell your number :"))
for i in range(n,0,-1):
 print(i) """

#Q2. Ask the user to enter the no. and print it's table
""" n = int(input("please tell your number :"))
for i in range(1,11):
 print(f"{n}x{i}={n*i}") """

#Q3. ask the user to enter the no. and print 
""" n = int(input("please tell your number :"))
a = 0
for i in range(1,n+1):
      a = a + i
print(a) """

# n = int(input("please tell your number :"))
# # a = 1
# for i in range(1,n+1):
#      a = a * i
#      print(a)

# n = int(input("enter a  number :- "))
# a = 1
# for i in range(1,n+1):
#     a = a*i
#     print(a)

# n = int(input("enter a number:- "))
# even_sum = 0
# odd_sum = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#      even_sum = even_sum + i
#     else:
#      odd_sum = odd_sum + i
# print(f"even sum is {even_sum} and odd sum is {odd_sum}")

#factors------------------------------------------
"""print factors of any number 
n = int(input("enter a number :"))
a = 0
for i in range(1,n):
 if n % i == 0:
     a = a + i
if a == n:
    print("number is perfect")
else:
   print("not a perfect number")"""
 
#prime numbers-------------------------------------

""" n = int(input("enter a number :"))
count  = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("prime number")
else:
    print("composite number")  """


""" n = int(input("enter your number: -"))
for i in range(2,(n//2)+1):
    if n%i == 0:
        print("your number is not prime" )
        break
else:
    print("your number is prime") """

#continue , break--------------------------------------

""" n = int(input("enter your number: -"))
for i in range(2,(n//2)+1):
    if n % i == 0:
        print("your number is composite")
        break
else:
    print("your number is prime")"""


#POWER SESSION 1---------------------------------------------------------------------------------------------------------------------------------------------
#Q1. Take a digit input from user reverse it using for loop. 
""" #part 1
n=input("enter the digit.:- ")
   #part 2
digit=""
for i in str(n) [::-1]:
    digit = digit + i
print(digit)"""

#Q2. Fibonacci series upto N term
"""n=input("enter the series no.:- ")
a = 0
b = 1
for i in str(n):
    print(a)
    a,b=b,a+b"""

#Q3. Print the largest digit in a number
"""n= 4289
largest = 0
for i in str(n):
    a = int(i)
    if a > largest:
        largest=a2
print(largest)"""

#Q4. Guessing game (use guesses a no. until correct)
"""import random
akshay  = random.randint(1,50)
for i in range (5):
    tanishq =int(input("enter the no.:- "))
    if tanishq == akshay:
        print("won")
        break
    if tanishq<akshay :
        print("too small")
    if tanishq>akshay :
        print("too high")
else:
    print(f"you lose no.is {akshay}")"""

#Q5. Check if a number is palindrome.
"""num=1221
if str(num)==str(num)[::-1]:
 print(f"{num} is palindrome.")
else : 
   print(f"{num} is not palindrome.")"""

#Q6. Keep taking input until user enters 0, then print sum
"""sum=0
while True:
    n=int(input("enter your no."))
    if n == 0 :
        break
    sum += n
print(sum)"""

#Q7. Reverse the no. using while loop
""" n=int(input("tell your no."))
rev = 0
while n!= 0: 
    rev = rev*10 + n%10
    n = n//10
print(rev) """

#Q8. Check if no. Armstrong no.
""" n = 67
copy = n
length = len(str(n))
sum = 0
while n > 0 :
    digit = n % 10 #3,5,1
    sum += digit**length
    n=n//10
if copy == sum :
    print("Armstrong no.")
else :
    print("not armstrong no.") """

#Q9. print hello world five times with less complexity
"""a = "hello world"
for i in range (6):
    print(a)
print("hello world\n*5")"""

#CLASS QSTS 2 (STRINGS)---------------------------------------------------------------------------------------------------------------------------------------------
#Q1. Negative indexing
""" s="shery"
print(s[::-1]) """

#Q2. print sring in reverse,its length,in uppercase,lowercase and copy into another string
""" s="shery"
print(f"reverse string ->{s[::-1]}")
print(f"length of string ->{len(s)}")
print(f"string in upper format->{s.upper()}")
print(f"string in lower format ->{s.lower()}") """

#Q3. Arrange string charac. such that lowercase letters come first
""" s= "ShEry"
lower = ""
upper = ""
for i in s:
    if i.islower():
        lower=lower + i 
    elif i.isupper():
        upper = upper + i
print(lower + upper) """

#Q4. Count all letters, digits, and special symbols from a given string
""" str1 = "Aifhs298#@$"
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

#Q5. Compare two strings without using inbuilt fun^.
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
    print("both are not same") """

#Q6. Count vowels from given string
""" str1 = "Helloo"
vowels = "AEIOUaeiou"
count =  0

for i in str1 :
    if i in vowels:
        count += 1
print(f"total count of vowels are {count} ") """

""" def countvowels():
    str1 = "Helloo"
    vowels = "AEIOUaeiou"
    count =  0

    for i in str1 :
     if i in vowels:
        count += 1
    print(f"total count of vowels are {count} ") 
countvowels() """

""" def countvowels():
    str1 = "Helloo"
    vowels = "AEIOUaeiou"
    count =  0

    for i in str1 :
     if i in vowels:
        count += 1
    return f"total count of vowels are {count} "
print(countvowels()) """

#Q7. reverse a string
""" z=("hello")
print(z[::-1]) """
 
""" z=("hello")
for i in z:
 print(i) """

""" z=("hello")
for i in z[::-1]:
 print(i) """

""" z=("hello") 
rev = ""
for i in z[::-1]:
     rev = rev + i
print(rev)  """

#Q8. check if the string is pallindrome or not 
""" s = "madam"
if str(s)==str(s)[::-1]:
 print(f"{s} is palindrome.")
else : 
   print(f"{s} is not palindrome.") """

#Q9. count no. of vowel and constants from a string
""" s = "Hello"
vowel =   0
consonant =  0
for i in s:
    if i in "aeiouAEIOU" :
        vowel += 1
    else :
     consonant + 1
print(f"total count of vowels are {vowel} ")
print(f"total count of vowels are {consonant} ")"""

#Q10 count te no. of digit (if return fun^ is there you need to use the print / if we use etuen inside the fun^ it will act as 
# the mini variable and untill unless we didnt print the variable the o/p will not be displayed)
""" def count (n) :
 count = 0
 while n > 0:
      digit = n % 10
      count = count + 1
      n =n//10
 return f"count of digit is  {count} "
print(count (1234) )"""

#Q11. Find the sum of digit of a num 
""" def checksum (num:int) :
 sum  = 0
 while num > 0:
   digit = num % 10
   sum = sum + digit 
   num = num//10
 return f"sum is {sum} " 
print(checksum (123) ) """

#Q12. Armstrong
""" n = 153
copy = n
length = len(str(n))
sum = 0
while n > 0 :
    digit = n % 10 #3,5,1
    sum += digit**length
    n=n//10
if copy == sum :
    print("Armstrong no.")
else :
    print("not armstrong no.") """

