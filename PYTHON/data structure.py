#DATA STRUCTURE----------------------------------------------------------------------------------------------------------------------------------------------------------

#1. List ==========================================================================================
#--->(store value at once)
#list-->to use list you need to use sq. bracket"
""" a= 12
b= 13
c= 14
d=12
e=34
l=[12,13,14,12,34] """

#SPECIAL POWERS

#a. HETROGENEOUS NATURE(can store any type of data at once) eg.:- l=[12,"hello",14.89,True,print()] 
#b. ORDERED (every element on the list has a deginated position )
#c. MUTABLE NATURE(Can change anythng inside the list at any point of time)
#d. DUPLICATE NATURE(can store duplicate element inside list)

#reading a list
""" a=[12,13,14,15,16]
print(a)  
print(a[4],a[-1]) """

#udating a list
""" a=[12,13,14,15,16]
a[-1]=56
print(a) """ 

#deleting a list
""" a=[12,13,14,15,16]
del a[-1]
print(a) """

#CREATING LOOP ON LIST

a=[12,13,14,15,16]
#based on values(accessing direct no.)
for i in a : #(IF RANGE IS UNKNOWN)
   print(i) 
#alter way
for i in range (0,5): #(IF RANGE IS KNOWN)
      print(a[i]) 

#based on index(accessing index/position)

for i in range (0,5): #(TO KNOW THE NO. INDEX VALUE)
    print(i)
for i in range (0,len(a)):
    print(a[i]) 

"METHODS"
"""append"""
# a=[12,13,14,15]
# a.append(5)   "to add any other value from last"
# print(a)

# l=[]
# for i in range(10,51,10):
#     l.append(i)
# print(l)

""" INSERT """
# a=[12,13,14,15]
# a.insert(2,5)   "to add value at exact position"
# print(a)

""" CLEAR """
# a=[12,13,14,15]
# a.clear()   "to add value at exact position"
# print(a)

"""POP"""
# a=[12,13,14,15]
# a.pop()   #to remove exact index value and if nthg mention last value is removed
# print(a)

'''REMOVE'''
# a=[12,13,14,15]
# a.remove(14)   #to remove value
# print(a)

#2. Tuple=======================================================================================================
"""
Ordered (indexing)
Can have duplicacy
Heterogeneous
Immutable """

#t=() #empty tuple
""" t=(1,2,3,4,5)
t[2]=10 
print(t) """

#DIRECT LOOP
""" t=(1,2,3,4,5)
for i in t:
    print(i) """

#INDIRECT LOOP
""" t=(1,2,3,4,5)
for i in range (len(t)):
    print(i,t[i]) """

#ENUMERATE --->tells the indexing of the elements
t=(1,2,3,4,5)
for index,value in enumerate (t):
   print(index,value)

#INDEXING/SLICING
""" t=(1,2,3,4,5)
print(t[2])
print(t[1:4]) """

#METHODS IN TUPLE
#1. count()
""" t=(1,2,2,2,3,4,5,3,4)
print(t.count(2))
print(t.count(3)) """

#2. index()
""" t=(1,2,2,2,3,4,5,3,4)
print(t.index(1))
print(t.index(2)) """

#MEMBERSHIP OPERATORS
""" t=(1,2,2,2,3,4,5,3,4)
print(3 in t)
print(9 in t) """

#TUPLE UNPACKING
""" t=(1,2,3,4,5)
a,b,c,d,e=t #unpacking should be equal to value inside variable
print(a)
print(b)
print(c)
print(d)
print(e)
a = 1,2 #this is packed """

#STAR EXPRESSION (*)
""" t=(1,2,3,4,5)
a,*b =t
print(a)
print(b)

t=(1,2,3,4,5) 
a,*b,c=t
print(a)
print(b) # middle value extraction 
print(c)

(1,2,3,4,5) #last value
a,*b,c=t
print(a)
print(c) """ 

#MERGING TWO TUPLES
""" t1=(1,2,3)
t2=(4,5,6)
print(t1+t2) """

#3. Set=====================================================================================================================
""" Sets are unordered (no indexing)
Semi mutable (can add but cannot change or remove
Unique elements(no duplicates)
Heterogeneous(can contain d/f data types)
a=dict{}
b=set()
c=list[ ]"""

#creating a set()
""" s={1,2,3,4,5}
print(type(s)) """

#duplicacy test
""" s={1,2,3,4,4,5,5}
print(type(s)) """

### Methods in set
""" 
1. Add
2. Update 
3. Remove
4. Discard
5. Pop
6. Clear"""

#add(for adding single value)
""" s={1,2,3,4,5}
s.add(6) """
#update (for adding multiple value)
""" s.update([7,8,9])
print(s) """
#remove (error if value is not present)
""" s.remove(10)
print(s) """
#discard(run even if the value is unavailable)
""" s.discard(10)
print(s) """
#pop(remove 1st element or smallest)) 
""" print(s.pop()) """
#clear(remove all value)
""" s.clear()
print(s) """

### Functions
""" 
1. Intersection (common value)
2. Union(no duplicates value)
3. Difference (value different from 1st one)
4. Symmetric Difference (rare value jo value 1 me h but 2 me nhi aur 2 me h toh 1 me nhi)  """

#Intersection (common value)
""" s1={1,2,3,4}
s2={2,3,4,6}
print(f"intersection:{s1.intersectio(s2)}") """

#Union
""" s1={1,2,3,4}
s2={2,3,4,6}
print(f"union:{s1.union(s2)}") """

#Differnce
""" s1={1,2,3,4}
s2={2,3,4,6}
print(f"difference s1:{s1.difference(s2)}")
print(f"difference s2:{s2.difference(s1)}") """

#Symmetric difference 
""" s1={1,2,3,4}
s2={2,3,4,6}
print(f"symmetric difference:{s1.symmetric_difference(s2)}") """

### Frozen sets(make immutable)
""" fs={10,20,30,40,50}
fs=frozen(fs)
fs.add(60)
fs.remove(10)
print(fs) """

#4. Dict=================================================================================================

"""To count the fq of same elements in a list"""

""" l={1,1,1,2,3,3,3,4,4,4,5,5,5,6,6,7,7,7,7}
d={}

for i in l:
     if i in d.keys():
         d[i]=d[i]+1
     else:
         d[i]-1
print(f"fq of elements are {d}")

 """