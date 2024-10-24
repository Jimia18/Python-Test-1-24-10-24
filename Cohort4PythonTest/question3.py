# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
def total_sum():
   total_sum = 0

   while True:
    number = float(input("Enter a number(or 0 to stop):\t"))
    if number == 0:
        break
    total_sum += number
    print("The sum of the numbers entered is:{total_sum}")
total_sum()





# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
        27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
        51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70, 71,72,73,74,
        75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101]
for numbers in range(1, 101):
    if numbers % 2 != 0:
        print(numbers)


