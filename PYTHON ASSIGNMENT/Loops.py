#SHEET 1-----------------------------------------------------------------------------------------------------------------------------------------------------------
#1 Ask the user to enter a number and print numbers from 1 to that number using loop.
""" a=int(input("enter the no."))
for i in range (1,a+1):
              print(i) """

#2 Ask the user to enter a number and print its multiplication table.
""" a=int(input("enter the no."))
for i in range (1,11):
              print(f"{a}*{i}={a*i}") """

#3 Ask the user to enter a number and print sum from 1 to n. 
""" a=int(input("enter the no."))
sum=0
for i in range (1,a+1):
   sum = sum+ i
print(sum) """

#4 Ask the user to enter a number and count digits using loop.
""" n =input("Enter your no.: ") 
count = 0
for  i in n:
    count = count + 1
print(f"Total digits: {count}") """

#5 Ask the user to enter a number and print reverse of number.
""" num = input("Enter a number: ") 
reversed = num[::-1]
print(f"Reversed number: {reversed}")"""


#6 Ask the user to keep taking input until user enters 0 and print total sum.
""" sum=0
while True:
    n=int(input("enter your no."))
    if n == 0 :
        break
    sum += n
print(sum) """

#SHEET 2----------------------------------------------------------------------------------------------------------------------------------------------------------
#1 Print numbers from 1 to 5 using a for loop.
""" for i in range (1,6):
    print(i) """

#2. Print numbers from 1 to 10.
"""  for i in range (1,11,1):
     print(i)"""

#3. Print odd numbers from 1 to 10.
""" for i in range (1,11,2):
    print(i)"""

#4. Print even numbers from 1 to 10.
""" for i in range (2,12,2):
     print(i)"""

#5 Print numbers from 10 to 1 (reverse order).
""" for i in range (11,0,-1):
    print(i) """

#6 Print multiplication table of 2.
""" for i in range (2,21,2):
    print(i) """

#SHEET 3----------------------------------------------------------------------------------------------------------------
#1 Ask the user to enter a number and print sum of first n natural numbers.
""" n =int(input("enter the number.:- "))
sum=0
for i in range (1,n+1):
     sum=sum+i
print(sum)"""

#2 Ask the user to enter a number and print factorial of that number.
""" n=int(input('enter the number:-')) """


#3. Ask the user to enter a number and print all even numbers up to that number.
""" n=int (input("enter your no."))
for i in range (2,n+1,2):
    print(i) """

#4. Ask the user to enter a number and print all odd numbers up to that number.
""" n=int (input("enter your no."))
for i in range (1,n+1,2):
    print(i) """


#5. Ask the user to enter a number and print numbers divisible by 5 up to that number
""" n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 5 == 0:
        print(i, end=" ") """


#6. Ask the user to enter a number and print the sum of even numbers up to that number.
""" n = int(input("Enter the number: "))
sum_even = 0
for i in range(2, n + 1, 2):
    sum_even += i
print(f"Sum = {sum_even}") """

#7. Ask the user to enter a number and print the product of numbers from 1 to n.
""" n = int(input("Enter the number: "))
product = 1
for i in range(1, n + 1):
    product *= i
print(f"Product = {product}") """

# 8. Ask the user to enter a number and print squares of numbers from 1 to n.
""" n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(i**2, end=" ") """

#9. Ask the user to enter a number and print sum of odd numbers up to n.
""" n = int(input("Enter the number: "))
sum_odd = 0
for i in range(1, n + 1, 2):
    sum_odd += i
print(f"Sum = {sum_odd}") """

#10. Ask the user to enter a number and print reverse of that number using loop.
""" n = int(input("Enter the number: "))
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
print(f"Reverse = {rev}")
 """
#SHEET 4-------------------------------------------------------------------------------------------------------------
# 1.Ask the user to enter a number and print all prime numbers up to that number.
""" n = int(input("Enter the number: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ") """

# 2. Ask the user to enter a number and check if it is Armstrong number.
""" num = int(input("Enter the number: "))
temp = num
sum_digits = 0
power = len(str(num))
while temp > 0:
    sum_digits += (temp % 10) ** power
    temp //= 10
if sum_digits == num:
    print("Armstrong")
else:
    print("Not an Armstrong number") """

# 3. Ask the user to enter a number and print the sum of digits using loop.
""" n = int(input("Enter the number: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print(f"Sum = {sum_digits}") """

# 4. Ask the user to enter a number and print reverse of the number.
""" n = int(input("Enter the number: "))
rev = 0
while n > 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
print(f"Reverse = {rev}") """

# 5. Ask the user to enter a number and check if it is palindrome.
""" n=int(input("tell your no."))
copy = n
rev = 0
while n!= 0: 
       rev = rev*10 + n%10
       n = n//10
print(rev)
if rev == copy:
      print("palindrome")
else:
    print("not a palindrome") """

# 6. Ask the user to enter a number and print all numbers between 1 to n that are divisible by both 3 and 5.
""" n = int(input("Enter the number: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ") """

#7. Ask the user to enter a number and print factorial using loop without using built-in functions.
""" n = int(input("Enter the number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial = {factorial}") """