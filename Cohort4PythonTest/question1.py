# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
# x1 = float(input("Enter x1:\t" ))
# x2 = float(input("Enter x2:\t" ))
# y1 = float(input("Enter y1:\t" )) 
# y2 = float(input("Enter y2:\t" ))

# import math
# sqrt = math.sqrt()
# distance = sqrt(*((x1-x2)**2) +((y2-y2)**2))
# print(len(distance))




# Question 1(ii)
# Write a Python program to find maximum between three numbers.
def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 <= num3:
        print(num1)
    elif num2 >= num1 and num2 <= num3:
        print(num2)
    else:
        print(num3)

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    maximum = find_maximum(num1, num2, num3)
    print(f"The maximum number is: {maximum}")




