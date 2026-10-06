# # Day 3
# # for loop

# for i in range(2, 8, 2):
#     print(i, end=" ")

"""A) 2 4 6 8
B) 2 4 6 correct
C) 1 3 5 7
D) 2 3 4 5 6 7"""

# name = "PYTHON"
# for ch in name:
#     if ch == "T":
#         print("Found")
#     else:
#         print(ch)

"""A)P
Y
Found
H
O
N   correct
B)P
Y
T
H
O
N
C)Found
D)P
Y
Found"""


# for i in range(1, 8):
#     if i % 2 == 0:
#         print(i, end=" ")

"""A) 1 3 5 7
B) 2 4 6 correct
C) 1 2 3 4 5 6 7 
D) 2 4 6 8"""

# numbers = [10, 20, 30, 40]
# for i in numbers:
#     print(i // 10, end=" ")

"""A) 1 2 3 4 correct
B) 10 20 30 40
C) 0 1 2 3
D) 100 200 300 400"""

# for i in range(10, 2, -2):
#     print(i, end=" ")

"""A) 10 8 6 4 2
B) 10 8 6 4 correct
C) 8 6 4 2
D) 10 9 8 7 6 5 4 3"""

# numbers = [3, 7, 9, 12, 15]
# for num in numbers:
#     if num > 10:
#         break
#     print(num, end=" ")

"""A) 3 7 9 correct
B) 3 7 9 12
C) 12 15
D) 3 7 9 12 15"""

# for i in range(1, 7):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

"""A) 1 2 3 4 5 6
B) 2 4 6
C) 1 3 5 correct
D) 1 2 3 5"""

# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i, j)

"""A)1 1
1 2
2 1
2 2
3 1
3 2  correct
B)1 1
2 2
3 3
C)1 2
2 3
3 4
D)1 1
2 1
3 1"""

# for i in range(1, 4):
#     for j in range(1, 4):
#         if i == j:
#             print(i, end=" ")

"""A) 1 2 3 correct
B) 1 1 2 2 3 3
C) 2 3
D) 1 2 3 4"""

# for i in range(1, 5):
#     if i == 3:
#         continue
#     for j in range(1, 3):
#         print(i + j, end=" ")

"""A) 2 3 4 5 6
B) 2 3 3 4 5 6 correct
C) 2 3 4 5
D) 2 3 4 5 5 6"""


# Print numbers from 1 to 10
# for i in range (1,11):
#     print(i,end=" ")


# Print even numbers from 1 to 20
# for i in range (1,21):
#     if i%2==0:
#         print(i, end=" ")

# Print odd numbers from 1 to 20
# for i in range (1,21):
#     if i%2!=0:
#         print(i, end=" ")

# # Print numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i, end=" ")

# Print the multiplication table of 5
# for i in range(1, 11):
#     print(f"5 x {i} = {5*i}")


# Find the sum of numbers from 1 to 10
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(f"Sum of first {i} numbers is: {sum}")

# # Print each character of a string
# val = 'PYTHON'
# for ch in val:
#     print(ch)

# Write a Python program to print the numbers from 1 to 20 using a for loop.

# for i in range (1,21):
#     if i%3==0:
#         print(i, end=" ")


# # Find the sum of all numbers in a list
# numbers = [10, 20, 30, 40, 50]
# sum = 0
# for num in numbers:
#     sum += num
# print("Sum of numbers:", sum)


# # Print only positive numbers
# numbers = [-5, 10, -2, 8, 0, 15, -7]
# for num in numbers:
#     if num > 0:
#         print(num, end=" ")


# # Write a program using a for loop to count how many numbers are greater than 10.
# numbers = [12,7,25,4,18,9]
# count = 0
# for num in numbers:
#     if num > 10:
#         count+=1
# print("Count:",count)

# Write a program to find the sum of all even numbers in the list.
# numbers = [15, 8, 22, 7, 30, 11]
# even_sum = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_sum += num
# print("Sum of even numbers:", even_sum)



# # Write a Python program using a for loop to find the largest number in the list.
# numbers = [12, 7, 25, 4, 18, 9, 30]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print("Largest number:", largest)



# # Write a program to find the smallest number in the list.
# numbers = [12, 7, 25, 4, 18, 9, 30]
# smallest = numbers[0]
# for num in numbers:
#     if num< smallest:
#         smallest = num 
# print("Smallest number:", smallest)



# # Using a for loop, count:Positive numbers,Negative numbers,Zeros
# numbers = [10, -5, 0, 8, -2, 0, 15, -7]
# pos_count = 0
# neg_count = 0
# zero_count = 0
# for num in numbers:
#     if num > 0:
#         pos_count += 1
#     elif num < 0:
#         neg_count += 1
#     else:
#         zero_count += 1
# print("Positive numbers:", pos_count)
# print("Negative numbers:", neg_count)
# print("Zero numbers:", zero_count)



# Find the second largest number using a for loop.
# numbers = [12, 7, 25, 4, 18, 30, 9]
# largest = numbers[0]
# second_largest = largest-1
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest:
#         second_largest = num
# print("Second largest number:", second_largest)



# # Find the second smallest number using a for loop.
# numbers = [12, 7, 25, 4, 18, 30, 9]
# smallest = numbers[0]
# second_smallest = smallest +1 
# for num in numbers:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest:
#         second_smallest = num
# print("Second smallest number:", second_smallest)




# # Find the second smallest distinct number using a for loop.
# numbers = [15, 3, 22, 8, 3, 17, 5]
# smallest = numbers[0]
# second_smallest = smallest - 1  
# for num in numbers:
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num
# print("Second smallest distinct number:", second_smallest)