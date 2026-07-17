##LOOPS--------------------------------------------------------------------------------------------

#For loop=========================================================================================================================

#(for continous counting)
""" for i in range(1,11,1): 
      print(i) """ 

#(for continous -ve counting)
""" for i in range(-1,-11,-1): 
      print(i) """

#(for reverse continous -ve counting)
""" for i in range(-11,-1,1): 
       print(i) """

#(for reverse continous counting)
""" for i in range(11,1,-1): 
   print(i) """

#counting
""" a=range(50,151,1)
for i in range(50,151,1):
      print(i) """

#negative to positive counting
""" for i in range(-12,11,1):
  print(i) """

#table of 5 & 7
""" for i in range(5,51,5):
       print(i) """

""" for i in range(7,71,7):
 print(i) """

#table of any no.
""" a=int(input("enter the no."))
for i in range(a,a*10+1,a):
     print(i) """

#counting upto given no.
""" n=int(input("enter the no."))
for i in range(1,n+1):
     print(i) """

#counting till last given no.
""" n = int(input("tell your stop no :- "))
for i in range(1,n+1):
     print(i) """

#while loop=================================================================================================
#reversing order of the given no. set (VERTICAL)
""" a = 123 
while a > 0: #Jab tak a zero se bada hai, loop chalao.
     print(a%10) 
     a = a //10 """

#SUM OF NO.
""" n=int(input("tell your no."))
sum=0
while n!= 0:
        sum=sum+n%10   
        n = n// 10     
print(sum) """

#COMBINE REVERSE NO. (HORIZONTAL)
"""n=int(input("tell your no."))
rev = 0 #to store the value
while n!= 0: #jb tk n 0 ke equal nhi hota
     rev = rev*10 + n%10 #to access the last digit
     # rev*10= Purane digits ko ek place LEFT shift karna taaki naya digit end me add ho sake 
     n = n//10 #to remove the last digit
print(rev)"""


#PALINDROME
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

#QST. check if no is armstrong===========================================================================
n = 67                                                                                                                                                                                                           
copy = n
length = len(str(n))     
sum = 0
while n > 0 :
    digit = n % 10 #3,5,1
    sum += digit**length #rule is based on len
    n=n//10
if copy == sum :
    print("Armstrong no.")
else :
    print("not armstrong no.")

