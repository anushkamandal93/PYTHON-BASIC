#FUNCTIONS (reusability)-----------------------------------------------------------------------------
#-->a function is a named block of reusable code designed to perform a specific task. 

#user defined function
""" def hello(): #defining of a fun
    print("hw r u")
hello() #calling of a fun. """

""" def hello():
     return ("hw r u")
a= hello ()
print(a)
print(hello()) # alter way  """

#inbuilt parameter and arguments
""" def adddition(a,b): 
      print(a+b)
adddition(22,11)
adddition(2,11)
adddition(22,1) """

#QST
""" def palindrome(n):
    rev =  0
    copy= n
    while n!= 0:
         rev = rev * 10 + n%10
         n = n//10
    if copy == rev:
          print("palindrome")
    else:
         print("not a palindrome")

palindrome(121)
palindrome(134)
palindrome(198891)
palindrome(451)
palindrome(111) """

#TYPE OF ARGUMENTS========================================================================================================
#1. positional arguments

""" def multiply(a,b): #fixed position
       print(a*b)
multiply(22,11) #fixed positional arguments """

#2. default arguments

""" def info(a,b,c,d): #fixed position
       print(a,b,c,d)
info(a=22,b=11,c=23,d=32)

def info (name,age,id=None):
       print("info recieved")
info("anushka",18) """
#if you give a value using default arguments you always have to give further values using deafult arguments

#QST. check if user can vote====================================================================================
""" def agechecker(n):
     if n >= 18 :
         return True
     else: 
         return False
age = int (input("tell your age"))
if agechecker(age):
     print("vote")
else:
     print("cant vote") """

#STACK(LIFO)===================================================================================================
""" def hello1 () :
    hello2 () 
print("hello1")   

def hello2 () :
    hello3 ()
print("hello2")   

def hello3 () :
     hello4 ()
print("hello3")   

def hello4 () :
    print("hello4")   
hello1() """

#RECURSSION =============================================================================================================
""" def number(n) :
     if n == 101:
         return "done"
     print(n)     #print(n+1)  for reverse
     number(n+1) #number(n) 
number(1) """

#for reverse======================================================================================================
""" def number(n) :
    if n == 101:
        return "done"
    print(n+1)  
    number(n) 
number(1) """

#ARGS*======================================================================================================
#--->Non-Keyword Arguments: Collects extra positional arguments into a tuple.
#How can you create a function that adds up two 

"""def add(a,b,c): #yaha a,b kkya hai parameters
    print(a+b+c)

add(10,20)"""

#Problem is what if hume hi nahi pata ki kitne parameters hone wale hai
#solution -> Using args

#args  -> *variable_name
#denoted by--> *
#variable_name -> chacha,mama,lolo kesa bhi likh skte hai
#args values ko accept krte hai in the form tuple

"""def add(*chacha):
    for i in chacha:
        print(i)
add(10,20,30,40,50)"""

""" def polio(name,age,pin,contact):
     print(name,age,pin,contact)
polio(name="Ramesh",age=22,pin=1222,contact=0000000) """ #inhe hum bolte hai Keyword Arguments

#KWARGS**=============================================================================================================
#-->Keyword Arguments: Collects extra named (key-value) arguments into a dictionary.
#kwargs -> Keyword Arguments
#denote -> **variable_name -> Ramesh,chacha,doremon,bahubali
#kwargs -> accepts krte hai sari values ko in the form of dictionary
#parameters woh -> Keys
#Arguments woh -> Values

""" def polio(**a):
    for i in a:
        print(f"Parameter -> {i} and Argument -> {a[i]}")
        #i-> dict keys , a[i] -> unn keys ki values
polio(name="Suresh",age=21,school="DPs") """

#lambda function -> jan ek function ek line mai aa jaye.
#lambda -> keyword ek variable ko convert kiya function mai.
#a,b: a+b -> agar a and b variable mai kuch value aayegi toh hi a+b chalega werna nahi chalega.

""" add = lambda a,b: a+b
print(add(10,20)) """