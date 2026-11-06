#Practice Sheet 1 – Lists basics----------------------------------------------------------------------------------------------------------------

#1. Create a list of 5 numbers and print the list.
numbers = [1, 2, 3, 4, 5]
print(numbers)

##2. Create a list of 3 fruits and print each item.
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit, end=" ")
print()

#3. Create a list and print the first element.
my_list_1 = [10, 20, 30]
print(my_list_1[0])

#4. Create a list and print the last element.
my_list_2 = [10, 20, 30]
print(my_list_2[-1])

#5. Create a list and print its length.
my_list_3 = [1, 2, 3, 4]
print("Length =", len(my_list_3))

#6. Create a list and add a new element at the end.
my_list_4 = [1, 2, 3]
my_list_4.append(4)
print(my_list_4)

#7. Create a list and remove an element.
my_list_5 = [1, 2, 3, 4]
my_list_5.remove(2)
print(my_list_5)

#8. Create a list and check if a value exists in it.
my_list_6 = [10, 20, 30]
if 20 in my_list_6:
    print("Present")
else:
    print("Not Present")

#9. Create a list and print all elements using loop.
my_list_7 = [5, 6, 7]
for element in my_list_7:
    print(element, end=" ")
print()

#10. Create a list and print sum of all elements.
my_list_8 = [1, 2, 3]
print("Sum =", sum(my_list_8))

#SHEET 2 LISTS MEDIUM--------------------------------------------------------------------------------------------------------------

#1. Ask the user to enter a list of numbers and print the largest element.
# Ask the user to enter a list of numbers and print the largest element.
user_input = input("Enter a list of numbers (separated by spaces): ")
# Convert the input string into a list of integers
numbers = [int(x) for x in user_input.split()]
# Find and print the largest element
largest = max(numbers)
print(f"Largest = {largest}")

#2. Ask the user to enter a list and print the smallest element.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]
smallest = min(numbers)
print(f"Smallest = {smallest}")

#3. Ask the user to enter a list and print sum of all elements.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]  
print(f"Sum = {sum(numbers)}")

#4. Ask the user to enter a list and count even numbers.
user_input = input("Enter a list of numbers (separated by spaces): ")   
numbers = [int(x) for x in user_input.split()]  
even_count = sum(1 for n in numbers if n % 2 == 0)
print(f"Even numbers = {even_count}")

#5. Ask the user to enter a list and count odd numbers.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]
odd_count = sum(1 for n in numbers if n % 2 != 0)
print(f"Odd numbers = {odd_count}")

#6. Ask the user to enter a list and reverse it.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]
numbers.reverse()
print(f"Reversed = {numbers}")

#7. Ask the user to enter a list and remove duplicates.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]
unique_numbers = list(set(numbers))
print(f"Unique numbers = {unique_numbers}")

#8. Ask the user to enter a list and sort it in ascending order.
user_input = input("Enter a list of numbers (separated by spaces): ")
numbers = [int(x) for x in user_input.split()]
numbers.sort()
print(f"Sorted = {numbers}")
