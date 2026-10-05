# # Day2 Multiple choice question practiced

# x = 10
# if x > 5:
#     print("A")
# else:
#     print("B")
# # A) A =correct
# # B) B
# # C) Error
# # D) Nothing


# x = 15
# y = 10
# if x > 10 and y < 5:
#     print("A")
# elif x > 10 or y < 5:
#     if y == 10:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")

# # A) A
# # B) B=correct
# # C) C
# # D) D



# a = 20
# b = 15
# c = 10
# if a > b:
#     if b > c:
#         if a > 25:
#             print("A")
#         else:
#             print("B")
#     else:
#         print("C")
# else:
#     print("D")

# # A) A
# # B) B =correct
# # C) C
# # D) D


# x = 12
# y = 8
# z = 20
# if x > 10 and y > 10 or z == 20:
#     print("A")
# else:
#     print("B")

# # A) A = correct
# # B) B
# # C) Error
# # D) Nothing


# x = 5
# y = 10
# if x > 3:
#     if y < 5:
#         print("A")
#     elif x + y == 15:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")

# # A) A
# # B) B =correct
# # C) C
# # D) D


# a = 10
# b = 20
# c = 30
# if a < b:
#     if b < c:
#         print("X")
#     elif a + b == c:
#         print("Y")
#     else:
#         print("Z")
# elif a + c > b:
#     print("P")
# else:
#     print("Q")

# # A) X = correct
# # B) Y
# # C) Z
# # D) P


# x = 10
# if x > 5:
#     print("A")
# if x > 8:
#     print("B")
# else:
#     print("C")

# # A)A
# #   B
# # B)A
# #   C
# # C)B
# # D)A =corect


# x = 20
# y = 10
# if x > 15:
#     if y > 15:
#         print("A")
#     else:
#         if x + y == 30:
#             print("B")
#         else:
#             print("C")
# else:
#     print("D")

# # A) A
# # B) B=correct
# # C) C
# # D) D


# a = 5
# b = 10
# c = 15
# if a < b and b < c or a == c:
#     print("A")
# else:
#     print("B")

# # A) A=correct
# # B) B
# # C) Error
# # D) Nothing


# x = 10
# y = 20
# if x > 5:
#     if y < 15:
#         print("A")
#     elif x + y > 25:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")

# # A) A
# # B) B = correct
# # C) C
# # D) D



# # Programming qusetions
# # Write a Python program that takes three numbers and finds the middle number — the number that is neither the largest nor the smallest.
# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))
# num3 = int(input("Enter the num3:"))
# if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
#     print("num1 is middle")
# elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
#     print("num2 is middle")
# else:
#     print("num3 is middle")


# # Write a Python program that takes three numbers and finds the second largest number.
# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))
# num3 = int(input("Enter the num3:"))
# if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
#     print("num1 is second largest")
# elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
#     print("num2 is second largest")
# elif (num1==num2) and (num1 == num3) and (num2 == num3):
#     print("There is no second largest number")
# elif (num1==num2) and (num1 > num3):
#     print("num1 and num2 are second largest")
# elif (num1==num3) and (num1 > num2):
#     print("num1 and num3 are second largest")
# elif (num2==num3) and (num2 > num1):    
#     print("num2 and num3 are second largest")
# else:
#     print("num3 is second largest")


# # Write a Python program that takes a three-digit number and checks whether it is an Armstrong number.
# num = int(input("Enter a three-digit number: "))
# if num >=100 and num <=999:
#     a = num //100
#     b = num//10 %10
#     c = num % 10
#     if num == a**3 +b ** 3 + c ** 3:
#         print(num, "is an Armstrong number")
#     else:
#         print(num, "is not an Armstrong number")


# # Write a Python program that takes three numbers and finds the largest and smallest number.
# num1 = int(input("Enter the num1:"))
# num2 = int(input("Enter the num2:"))
# num3 = int(input("Enter the num3:"))
# if (num1>num2 and num1>num3):
#     print("Largest number is:", num1)
#     if num2<num3:
#         print("Smallest number is:", num2)
#     else:
#         print("Smallest number is:", num3)
# elif(num2>num1 and num2>num3):
#     print("Largest number is:", num2)
#     if num1<num3:
#         print("Smallest number is:", num1)
#     else:
#         print("Smallest number is:", num3)
# else:
#     print("Largest number is:", num3)
#     if num1<num2:
#         print("Smallest number is:", num1)
#     else:
#         print("Smallest number is:", num2)



# # Write a Python program that takes a three-digit number and finds the:

# # Hundreds digit
# # Tens digit
# # Ones digit

# num = int(input("Enter a three-digit number: "))
# hundreds_digit = num // 100
# tens_digit = num // 10 % 10
# ones_digit = num % 10
# print("Hundreds digit:", hundreds_digit)
# print("Tens digit:", tens_digit)
# print("Ones digit:", ones_digit)



# # Write a Python program that takes a three-digit number and checks whether its first digit and last digit are equal.
# num = int(input("Enter a three-digit number: "))
# first_digit = num // 100
# second_digit = num // 10 % 10
# third_digit = num % 10
# if first_digit == third_digit :
#     print("First and last digits are equal")
# else:
#     print("First and last digits are not equal")



