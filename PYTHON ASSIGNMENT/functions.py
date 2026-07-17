#1 Write a function to check if a number is prime or not.  
def is_prime(n):
    if n < 2: return "Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return "Not Prime"
    return "Prime"

#2. Write a function to return sum of all numbers from 1 to n. 
def sum_to_n(n):
    return sum(range(1, n + 1))

#3. Write a function to count vowels in a string.  
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 4. Write a function to print Fibonacci series up to n terms. 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 5. Write a function to find second largest element in a list. 
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

# 6. Write a function to remove duplicate elements from a list. 
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

# 7. Write a function to check whether a number is Armstrong or not. 
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    if sum(d**power for d in digits) == n:
        return "Armstrong"
    return "Not Armstrong"

# 8. Write a function to count frequency of each character in a string. 
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        print(f"{char} = {count}")

# 9. Write a function to find common elements between two lists. 
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# 10. Write a function to sort a list without using built-in sort(). 
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst