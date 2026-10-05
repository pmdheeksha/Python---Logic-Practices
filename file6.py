# Day2
# a = 15
# b = 10
# c = 20
# if a > b:
#     if a > c:
#         print("A")
#     elif b < c:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")

# # A) A
# # B) B correct
# # C) C
# # D) D

# x = 8
# y = 12
# z = 5
# if x > 5 and y < 10 or z == 5:
#     print("A")
# elif x + y > 25:
#     print("B")
# else:
#     print("C")
# # A) A correct
# # B) B
# # C) C
# # D) Error

# a = 10
# b = 20
# c = 15
# if a < b:
#     if b > c and a + c == 25:
#         print("X")
#     elif a > c or b == 20:
#         print("Y")
#     else:
#         print("Z")
# else:
#     print("W")
# # A) X correct
# # B) Y
# # C) Z
# # D) W

# x = 10
# y = 5
# if x > 5:
#     if y > 10:
#         print("A")
#     else:
#         if x % 2 == 0:
#             print("B")
#         elif x + y > 20:
#             print("C")
#         else:
#             print("D")
# else:
#     print("E")

# # A) A
# # B) B correct
# # C) C
# # D) D


# a = 12
# b = 18
# c = 24
# if a < b and b < c:
#     if a + b > c:
#         print("A")
#     elif a + c == b * 2:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")
# # A) A correct
# # B) B
# # C) C
# # D) D


# x = 15
# y = 10
# z = 20
# if x > y:
#     if x + y > z:
#         print("A")
#     elif z - x == y:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")
# # A) A correct
# # B) B
# # C) C
# # D) D

# a = 20
# b = 15
# c = 25
# if a > b:
#     if b > c:
#         print("A")
#     elif a + b == c:
#         print("B")
#     elif c - a == b:
#         print("C")
#     else:
#         print("D")
# else:
#     print("E")
# # A) A
# # B) B
# # C) C
# # D) D correct
# # E) E

# x = 10
# y = 20
# z = 30
# if x < y:
#     if y < z:
#         if x + z == y * 2:
#             print("A")
#         elif z - y == x:
#             print("B")
#         else:
#             print("C")
#     else:
#         print("D")
# else:
#     print("E")
# # A) A correct
# # B) B
# # C) C
# # D) D
# # E) E


# a = 8
# b = 12
# c = 16
# if a < b:
#     if b < c:
#         if a + b > c:
#             print("A")
#         elif c - a == b:
#             print("B")
#         else:
#             print("C")
#     elif a + c == b * 2:
#         print("D")
#     else:
#         print("E")
# else:
#     print("F")
# # A) A correct
# # B) B
# # C) C
# # D) D
# # E) E
# # F) F

# x = 14
# y = 7
# z = 21
# if x > y:
#     if z > x:
#         if z - x == y:
#             print("A")
#         elif x + y == z:
#             print("B")
#         else:
#             print("C")
#     elif x + y > z:
#         print("D")
#     else:
#         print("E")
# else:
#     print("F")
# # A) A correct
# # B) B
# # C) C
# # D) D
# # E) E
# # F) F

# Write a Python program to check whether a 3-digit number is a palindrome.
# val = int(input("Enter a 3-digit number: "))
# if val>=100 and val<=999:
#     a = val // 100
#     b = val // 10 % 10
#     c = val % 10
#     if a == c:
#         print(val, "is a palindrome")
#     else:
#         print(val, "is not a palindrome")
# else:
#     print("Please enter a valid 3-digit number")

# val =  int(input("Enter a 3-digit number: "))
# if val >=1000 and val<=9999:
#     a = val//1000
#     b = val//100%10
#     c = val//10%10
#     d = val%10
#     if a == d and b == c:
#         print(val, "is a palindrome")
#     else:
#         print(val, "is not a palindrome")




# Write a Python program to find the sum of the digits of a 3-digit number.
# num = int(input("Enter a 3-digit number: "))
# if num >= 100 and num <= 999:
#     a = num //100
#     b = num // 10 % 10

#     c  = num % 10
#     d = a + b + c
#     print("The sum of the digits of", num, "is:", d)
# else:
#     print("Please enter a valid 3-digit number")


# Write a Python program to find the largest digit in a 3-digit number.
# num = int(input("Enter a 3-digit number: "))
# if num >= 100 and num <= 999:
#     a = num // 100
#     b = num // 10 % 10
#     c = num % 10
#     if a > b and a > c:
#         print(f"The largest digit in {num} is: {a}")
#     elif b > a and b > c:
#         print(f"The largest digit in {num} is: {b}")
#     else:
#         print(f"The largest digit in {num} is: {c}")
# else:
#     print("Please enter a valid 3-digit number")


# Write a Python program to count how many even digits and odd digits are present in a 3-digit number.
num = int(input("Enter a 3-digit number: "))
if num >= 100 and num <= 999:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    count_even = 0
    count_odd = 0
    for digit in [a, b, c]:
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"The number of even digits in {num} is: {count_even}")
    print(f"The number of odd digits in {num} is: {count_odd}")