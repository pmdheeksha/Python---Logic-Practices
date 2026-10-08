# Day 3

# numbers = [2, 5, 8, 11, 14]
# total = 0
# for num in numbers:
#     if num % 2 == 0:
#         total += num
#     else:
#         total -= num
# print(total)
# # A) 8 correct
# # B) 10
# # C) -2
# # D) 0


# numbers = [3, 6, 9, 12]
# for i in range(len(numbers)):
#     if numbers[i] % 3 == 0:
#         numbers[i] = numbers[i] // 3
# print(numbers)
# # A) [1, 2, 3, 4]
# # B) [3, 6, 9, 12]
# # C) [0, 1, 2, 3]
# # D) [9, 18, 27, 36]


# numbers = [2, 4, 6, 8, 10]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
# print(total)
# # A) 18  correct
# # B) 30
# # C) 12
# # D) 20 


# numbers = [5, 10, 15, 20, 25]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] > 10 and i % 2 == 0:
#         count += 1
# print(count)
# # A) 1 correct
# # B) 2
# # C) 3
# # D) 4


# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = numbers[i] * 2
# print(numbers)
# # A) [1, 4, 3, 8, 5] correct
# # B) [2, 4, 6, 8, 10] 
# # C) [1, 2, 3, 4, 5]
# # D) [2, 2, 6, 4, 10]


# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in range(len(numbers) - 1, -1, -1):
#     total += numbers[i]
# print(total)
# # A) 100
# # B) 150 
# # C) 120
# # D) 140


# numbers = [3, 5, 7, 9]
# for i in range(len(numbers)):
#     if i == 2:
#         break
#     print(numbers[i], end=" ")
# # A) 3 5
# # B) 3 5 7
# # C) 5 7
# # D) 3 5 7 9


# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         continue
#     print(num, end=" ")
# # A) 1 2 3 4 5
# # B) 1 2 4 5  correct
# # C) 3
# # D) 1 2


# numbers = [2, 4, 6, 8]
# for i in range(len(numbers)):
#     if numbers[i] > 4:
#         print(numbers[i], end=" ")
#     else:
#         print(i, end=" ")
# # A) 0 1 6 8 correct
# # B) 2 4 6 8
# # C) 0 4 6 8
# # D) 0 1 2 3


# numbers = [1, 2, 3, 4, 5]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
#     else:
#         total -= numbers[i]
# print(total)
# # A) 3 correct
# # B) 5
# # C) 15
# # D) -3

# numbers = [2, 5, 8, 11, 14]
# total = 0
# for num in numbers:
#     if num % 2 == 0:
#         total += num
#     else:
#         total -= num
# print(total)

# # **Answer:** `8`

# numbers = [3, 6, 9, 12]
# for i in range(len(numbers)):
#     if numbers[i] % 3 == 0:
#         numbers[i] = numbers[i] // 3
# print(numbers)


# # **Answer:** `[1, 2, 3, 4]`

# numbers = [2, 4, 6, 8, 10]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
# print(total)


# # **Answer:** `18`

# numbers = [5, 10, 15, 20, 25]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] > 10 and i % 2 == 0:
#         count += 1
# print(count)


# # **Answer:** `2`

# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = numbers[i] * 2
# print(numbers)

# # **Answer:** `[1, 4, 3, 8, 5]`

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in range(len(numbers) - 1, -1, -1):
#     total += numbers[i]
# print(total)


# # **Answer:** `150`

# numbers = [3, 5, 7, 9]
# for i in range(len(numbers)):
#     if i == 2:
#         break
#     print(numbers[i], end=" ")


# # **Answer:** `3 5`


# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         continue
#     print(num, end=" ")


# # **Answer:** `1 2 4 5`

# numbers = [2, 4, 6, 8]
# for i in range(len(numbers)):
#     if numbers[i] > 4:
#         print(numbers[i], end=" ")
#     else:
#         print(i, end=" ")


# # **Answer:** `0 1 6 8`


# numbers = [1, 2, 3, 4, 5]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
#     else:
#         total -= numbers[i]
# print(total)

# # **Answer:** `3`

# numbers = [10, 20, 30, 40, 50]
# for i in range(len(numbers)):
#     print(i, numbers[i])

# # **Answer:**
# # 0 10
# # 1 20
# # 2 30
# # 3 40
# # 4 50

# numbers = [5, 10, 15, 20]
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         print(numbers[i])


# # **Answer:**
# # 5
# # 15

# numbers = [4, 8, 12, 16, 20]
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         print(numbers[i])

# # **Answer:**
# # 8
# # 16

# numbers = [5, 10, 15, 20, 25]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
# print(total)


# # **Answer:** `45`

# numbers = [4, 7, 10, 13, 16, 19]
# total = 0
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0 and i % 2 == 0:
#         total += numbers[i]
# print(total)


# # **Answer:** `30`
# numbers = [3, 6, 9, 12, 15]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] > 8 and i % 2 != 0:
#         count += 1
# print(count)


# # **Answer:** `1`

# numbers = [2, 5, 8, 11, 14, 17]
# total = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         total += numbers[i]
#     elif numbers[i] > 10:
#         total += 1
# print(total)


# # **Answer:** `26`

# numbers = [10, 15, 20, 25, 30]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] % 5 == 0:
#         if i % 2 == 0:
#             count += 1
# print(count)

# # **Answer:** `3`


# numbers = [5, 12, 7, 20, 9, 30]
# total = 0
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         if i % 2 != 0:
#             total += numbers[i]
# print(total)


# # **Answer:** `62`


# # Find the sum of all even numbers using a for loop.
# numbers = [12, 5, 18, 7, 20, 3, 15]
# sum = 0
# for n in range(len(numbers)):
#     if numbers[n]%2==0:
#         sum+=numbers[n]
# print(sum)

# # **Answer:** `50`


# # Count the positive, negative, and zero values using a for loop.
# numbers = [10, -5, 20, -8, 0, 15, -3]
# count_positive = 0
# count_negative = 0
# count_zero = 0
# for i in range(len(numbers)):
#     if numbers[i]>0:
#         count_positive+=1
#     elif numbers[i]<0:
#         count_negative+=1
#     else:
#         count_zero+=1
# print("Positive numbers:", count_positive)
# print("Negative numbers:", count_negative)
# print("Zero numbers:", count_zero)

# **Answer:**
# Positive numbers: 3
# Negative numbers: 3
# Zero numbers: 1


# # Print only the numbers that are greater than 10 and even.
# numbers = [4, 7, 12, 9, 20, 15, 6]
# for i in numbers:
#     if i>10 and i%2==0:
#         print(i)

# **Answer:**
# 12
# 20


# # Find the sum of values at even indexes.
# numbers = [5, 10, 15, 20, 25, 30]
# sum = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         sum += numbers[i]
# print(sum)

# **Answer:** `45`

# # Count how many numbers are even and greater than 10.
# numbers = [3, 8, 12, 5, 18, 7, 20]
# count = 0
# for i in numbers:
#     if i > 10 and i % 2 == 0:
#         count += 1
# print(count)

# **Answer:** `3`



# # Print the values at odd indexes.
# numbers = [2, 5, 8, 11, 14, 17]
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         print(numbers[i], end=" ")

# **Answer:** `5 11 17`


# # Calculate the sum by alternately adding and subtracting values:
# numbers = [10, 20, 30, 40, 50]
# sum = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         sum += numbers[i]
#     else:
#         sum -= numbers[i]
# print(sum)


# **Answer:** `-30`