#If Else Statements
# Basic Program

# 1.Enter a number and check whether it is positive or negative.
# num = int(input("Enter the value:"))
# if num > 0:
#     print(f"The {num} is positive")
# else:
#     print(f"The {num} is negative" )



# 2.Enter a number and check whether it is even or odd.
# num = int(input("Enter the value:"))
# if num%2==0:
#     print(f"The {num} is even")
# else:
#     print(f"The {num} is odd" )



# 3.Enter a number and check whether it is zero or not.
# num = int(input("Enter the value:"))
# if num ==0:
#     print(f"The {num} is zero")
# else:
#     print(f"The {num} is not zero" )



# 4.Enter your age and check whether you are eligible for voting.
# vote = int(input("Enter your age:"))
# if vote >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")



# 5. Enter a number and check whether it is greater than 100 or not.
# val = int(input("Enter the value:"))
# if val>100:
#     print(f"The {val} is greater than 100")
# else:
#     print(f"The {val} is less than 100")



# 6. Enter a number and check whether it is a multiple of 10 or not.
# num = int(input("Enter the value:"))
# if num%10==0:
#     print(f"The {num} is divisible by 10")
# else:
#     print(f"The {num} is not divisible by 10")



# 7. Enter a student's mark and check whether the student passed or failed. Pass mark = 40.7.
# mark = int(input("Enter your marks:"))
# if mark>=40:
#     print("You are pass in the exam")
# else:
#     print("You are fail in the exam")



# 8. Enter two numbers and print the greater number.
# num_1 = int(input("Enter the first number:"))
# num_2 = int(input("Enter the second number:"))
# if num_1>num_2:
#     print(f"The {num_1} is greater than {num_2}")
# else:
#     print(f"The {num_2} is greater than {num_1}")



# 9. Enter a number and check whether it is divisible by 5 or not.
# num = int(input("Enter the value:"))
# if num%5==0 or num%5==5:
#     print(f"The {num} is divisible by 5")
# else:
#     print(f"The {num} is not divisible by 5")


# # 10. Enter a person's age and check whether they are 18 or above.
# age = int(input("Enter your age:"))
# if age>=18:
#     print(f"The person is 18 or above.")
# else:
#     print(f"You are below 18.")




# Intermediate Program
# 11. Enter three numbers and find the largest number.
# num_1 = int(input("Enter the first number:"))
# num_2 = int(input("Enter the second number:"))  
# num_3 = int(input("Enter the third number:"))
# if num_1>num_2:
#     if num_1>num_3:
#         print(f"The {num_1} is greater than {num_2} and {num_3}")
#     else:
#         print(f"The {num_3} is greater than {num_1} and {num_2}")
# else:
#     if num_2>num_3:
#         print(f"The {num_2} is greater than {num_1} and {num_3}")
#     else:
#         print(f"The {num_3} is greater than {num_1} and {num_2}")   




# val = input("Enter the value: ")
# if 65<=ord(val)<=90 or 97<=ord(val)<=122 or 48<=ord(val)<=57:
# # if (val>='0' and val<='9') or (val>='A' and val>='Z') or (val>='a' and val<='z'):
#     print(f"The {val} is not a special character")
# else:
#     print(f"The {val} is  a special character")


# #12.Enter three numbers and find the smallest number.
# num_1 = int(input("Enter the num1:"))
# num_2 = int(input("Enter the num2:"))
# num_3 = int(input("Enter the num3:"))
# if num_1<num_2:
#     if num_1<num_3:
#         print(f"The {num_1} is smaller than {num_2} and {num_3}")
#     else:
#         print(f"The {num_3} is smaller than {num_1} and {num_2}")
# else:
#     if num_2<num_3:
#         print(f"The {num_2} is smaller than {num_1} and {num_3}")
#     else:
#         print(f"The {num_3} is smaller than {num_1} and {num_2}")


# 13. Enter a number and check whether it is a two-digit number or not.
# num = int(input("Enter the value:"))
# if num in range(10,100) or num in range(-100,-10):
#     print(f"The {num} is a two digit number")
# else:
#     print(f"The {num} is not a two digit number")


# 14. Enter a number and check whether it is a three-digit number or not.
# num = int(input("Enter the value: "))
# if 100<=num<=999 or -999<=num<=-100:
#     print(f"The {num} is a three digit number")
# else:
#     print(f"The {num} is not a three digit number")


# 15. Enter a number and check whether it is divisible by 3 and 5.
# num = int(input("Enter the value: "))
# if num%3==0 and num%5==0:
#     print(f"The {num} is divisible by 3 and 5")
# else:
#     print(f"The {num} is not divisible by 3 and 5")



# 16. Enter a number and check whether it is divisible by 3 or 5.
# num = int(input("Enter the value: "))
# if num%3==0 or num%5==0:
#     print(f"The {num} is divisible by 3 or 5")
# else:
#     print(f"The {num} is not divisible by 3 or 5")



# 17. Enter marks and print Pass/Fail, where the pass mark is 40.
# mark = int(input("Enter your marks: "))
# if mark >= 40:
#     print("You are pass in the exam")
# else:
#     print("You are fail in the exam")



#18. Enter a year and check whether it is a leap year or not.
# year = int(input("Enter the year: "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"The {year} is a leap year")
# else:
#     print(f"The {year} is not a leap year")

#19. Enter a character and check whether it is a vowel or consonant.
# char = input("Enter a character: ")
# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#     print(f"The {char} is a vowel")
# else:
#     print(f"The {char} is a consonant")

# char = input("Enter a character: ")
# if char in ['a','e','i','o','u','A','E','I','O','U']:
#     print(f"The {char} is a vowel")
# else:
#     print(f"The {char} is a consonant")



#20 Match case Month
# month = int(input("Enter the month number: "))
# match month:
#     case 1|2|12:
#         print("Winter")
#     case 3|4|5:
#         print("Spring")
#     case 6|7|8:
#         print("Summer")
#     case 9|10|11:
#         print("Autumn")
#     case _:
#         print("Invalid month number")


# 21 Boolean checking
# num = int(input("Enter the value: "))
# is_even = num%2==0;
# match is_even:
#     case True:
#         print(f"The {num} is even")
#     case False:
#         print(f"The {num} is odd")


# 22.Withdraw questions
# balance = 90000
# print("1. Withdraw")
# print("2. Deposit")
# print("3. Check Balance")
# print("4. Exit")
# choice = input("Enter your choice: ")
# match choice:
#     case 'Withdraw':
#         withdraw_amount = int(input("Enter the Withdraw Amount: "))
#         if balance<= withdraw_amount:
#             print("Insufficient Balance")
#         else:   
#             balance -= withdraw_amount
#             print(f"Withdraw Amount: {withdraw_amount}")
#             print(f"Remaining Balance: {balance}")
#     case 'Deposit':
#         deposit_amount = int(input("Enter the Deposit Amount:"))
#         balance += deposit_amount
#         print(f"Deposit Amount: {deposit_amount}")
#         print(f"Remaining Balance: {balance}")
#     case 'Check Balaance':
#         print(f"Remaining Balance: {balance}")
#     case 'Exit':
#         print("Thank you for using our services")
#     case _:
#         print("Invalid choice")


# 23
# menu = input("Enter the menu item: \n 1.Electronics \n 2.Clothing \n 3.Groceries \n 4.Exit \n Option: ")
# match menu:
#     case 'Electronics':
#         price = int(input("Enter the price: "))
#         if price>=10000:
#             print("20% discount")
#         else:
#             print("5% discount")
#     case 'Clothing':
#         price = int(input("Enter the price: "))
#         if price>=5000:
#             print("25% discount")
#         else:
#             print("10% discount")
#     case 'Groceries':
#         price = int(input("Enter the price: "))
#         if price>=2000:
#             print("15% discount")
#         else:
#             print("5% discount")
#     case 'Exit':
#         print("Thank you for shopping with us")
#     case _:
#         print("Invalid choice")



# 24
# mark = int(input("Enter your marks: "))
# if mark>=90 and mark<=100:
#     print("A")
# elif mark>=80 and mark<90:
#     print("B")  
# elif 70<=mark<80:
#     print("C")
# elif 60<=mark<70:
#     print("D")
# elif 50<=mark<60:
#     print("E")
# else:
#     print("Fail") 



# 25.Write a Python program to check whether a number is:

# Positive, Negative, or Zero
# If it is positive, also check whether it is Even or Odd.


# val = int(input("Enter the value:"))
# if val>0:
#     print("Positive")
#     if val%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# elif val<0:
#     print("Negative")
# elif val==0:
#     print("Zero")
# else:
#     print("Invalid Number")



# 26. Write a Python program that takes three numbers and finds the largest number.

# num1 = int(input("Enter the num1 "))
# num2 = int(input("Enter the num2 "))
# num3 = int(input("Enter the num3 "))
# if num1>=num2 and num1>=num3:
#     print("num1 is greater")
# elif num2>=num3 and num2>=num1:
#     print("num2 is greater")
# else:
#     print("num3 is greater")


# num1 = int(input("Enter the num1 "))
# num2 = int(input("Enter the num2 "))
# num3 = int(input("Enter the num3 "))
# if num1 == num2 and num1 > num3:
#     print("num1 and num2 are equal and greater")
# elif num1 == num3 and num1 > num2:
#     print("num1 and num3 are equal and greater")
# elif num2 == num3 and num2 > num1:
#     print("num2 and num3 are equal and greater")
# elif num1 > num2 and num1 > num3:
#     print("num1 is greater")
# elif num2 > num1 and num2 > num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater")




# #27. Write a Python program that takes three numbers and checks whether all three numbers are equal.
# num1 = int(input("Enter the num1 "))
# num2 = int(input("Enter the num2 "))
# num3 = int(input("Enter the num3 "))
# if num1 == num2 and num1 == num3 :
#     print("All numbers are equal")
# else:
#     print ("The numbers are not equal")




# #28. Write a Python program that takes three numbers and finds the smallest number.
# num1 = int(input("Enter the num1 "))
# num2 = int(input("Enter the num2 "))
# num3 = int(input("Enter the num3 "))
# if num1==num2 and num1<num3:
#     print(f"The {num1} and {num2} are less than {num3}")
# elif num1==num3 and num1<num2:
#     print(f"The {num1} and {num3} are less than {num2}")
# elif num2==num3 and num2<num1:
#     print(f"The {num2} and {num3} are less than {num1}")
# elif num1<num2 and num1<num3:
#     print(f"The {num1} is less than {num2} and {num3}")
# elif num2<num1 and num2<num3:
#     print(f"The {num2} is less than {num1} and {num3}")
# else:
#     print(f"The {num3} is less than {num1} and {num2}")





# 29. Write a Python program that takes three numbers and checks:
    # If all three are equal → print "All are equal"
    # If only two are equal → print "Two numbers are equal"
    # If all three are different → print "All are different"

# num1 = int(input("Enter the num1 "))
# num2 = int(input("Enter the num2 "))
# num3 = int(input("Enter the num3 "))
# if num1 == num2 and num1 == num3:
#     print("All numbers are equal")
# elif (num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num2 != num1):
#     print("Two numbers are equal ")
# else:
#     print("All numbers are different")