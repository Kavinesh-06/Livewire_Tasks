# if-else

# smallest among two numbers
print("smallest among two numbers")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
if a <= b:
    print(f"Smallest number is {a}")
else:
    print(f"Smallest number is {b}")

# largest among two numbers
print("largest among two numbers")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
if a <= b:
    print(f"Largest number is {a}")
else:
    print(f"Largest number is {b}")

# Absolute Value
print("Absolute Value")
a = int(input("Enter value of a: "))
if a>=0:
    print(f"Absolute Value is {a}")
else:
    print(f"Absolute Value is {-a}")

# whether the number is odd or even
print("the number is odd or even")
a = int(input("Enter a number : "))
if a%2==0:
    print(f"The given number {a} is even")
else:
    print(f"The given number {a} is odd")

# whether the given number is multiple of 5 and 10 or not
print("whether the given number is multiple of 5 and 10 or not")
a = int(input("Enter a number : "))
if a % 5 == 0 :
    print(f"The given number {a} is multiple of 5")
elif a % 10 == 0 :
    print(f"The given number {a} is multiple of 10")
else:
    print(f"The given number {a} is not multiple of 5 and 10")

# Two-digit number or not
print("whether The given Two digit number or not ")
a = int(input("Enter a number : "))
if (a>=10) and (a<=99):
    print(f"The given number {a} is two digit")
else:
    print("Invalid Number")

# Three-digit number or not
print("whether The given three digit number or not ")
a = int(input("Enter a number : "))
if (a>=100) and (a<=999):
    print(f"The given number {a} is two digit")
else:
    print("Invalid Number")

# Ends with 0 or not
print("Ends with zero or not")
a = int(input("Enter a number : "))
if a%10 == 0:
    print(f"The given number {a} is ends with zero")
else:
    print(f"The given number {a} is not ends with zero")

# the given number square is above or below 50
print("the given number square is above or below 50")
a = int(input("Enter a value : "))
if a*a >= 50:
    print(f"The square of the given value {a} is above 50")
else:
    print(f"The square of the given value {a} is below 50")

# Difference the two-digit number
print("Difference the two-digit number")
a = int(input("Enter a two-digit number : "))
if ((a%10) - (a//10)) == 0:
    print(f"The difference of two-digit {a} is 0")
else:
    print(f"The difference of two-digit {a} is not 0")

# Students has pass or fail
print("Students has pass or fail")
Marks = int(input("Enter computer science Marks: "))
if Marks >= 50:
    print("The student has passed")
else:
    print("The student has failed")

# The number is divisible by 10 or not
print("The number is divisible by 10 or not")
a = int(input("Enter a number : "))
if a % 10 == 0 :
    print(f"The given number {a} is divisible by 10")
else:
    print(f"The given number {a} is not divisible by 10")

# The biggest digit from two-digit numbers
print("The biggest digit from two-digit numbers")
a = int(input("Enter a two-digit number : "))
b = a%10
a = a//10
if a > b:
    print(f"The biggest digit is {a}")
else:
    print(f"The biggest digit is {b}")

print("Exam choices")
choice = int(input("Enter your choice, However your choice must be in numeric : "))
if choice == 1:
    print("The will be easy")
else:
    print("The will be difficult")

value = int(input("Enter your value : "))
if value == 1:
    print("You can go out and play")
else:
    print("You can't go out and play")

# using length and breadth to determine the shape
length = int(input("Enter your length : "))
breadth = int(input("Enter your breadth : "))
if length == breadth:
    print("It's a square")
else:
    print("It's a rectangle")

# ASCII Values operations
print("ASCII Values operations")
num = int(input("Enter ASCII value : "))
if 65 <= num <= 90:
    print(f"It is a ASCII value {num} of uppercase alphabet")
elif 97 <= num <= 122:
    print(f"It is a ASCII value {num} of lowercase alphabet")
elif 48 <= num <= 57:
    print(f"It is a ASCII value {num} of numeric character")
else:
    print(f"It is not a ASCII value {num} of uppercase, lower alphabet and numeric character")

# Multiple of both 3 and 5
print ("Check whether the given number is Multiple of both 3 and 5")
a = int(input("Enter a number : "))
if a % 3 == 0 and a % 5 == 0:
    print(f"The given number {a} is Multiple of both 3 and 5")
else:
    print(f"The given number {a} is not Multiple of both 3 and 5")

# whether it's a three-digit number and multiple of 10
num = int(input("Enter a three-digit number : "))
if 100 <= num <= 999:
    if num % 10 == 0:
        print(f"It's an three digit number and multiple of 10 : {num}")
    else:
        print(f"It's an three digit number and not multiple of 10 : {num}")
else:
    print("It isn't a three digit number")

# whether it's a three-digit number and multiple of 2, 5, and 10
num = int(input("Enter a three-digit number : "))
if 100 <= num <= 999:
    if num % 2 == 0 and num % 5 == 0 and num % 10 == 0:
        print(f"It's an three digit number and multiple of 2, 5, 10 : {num}")
    else:
        print(f"It's an three digit number and not multiple of 2, 5, 10 : {num}")
else:
    print("It isn't a three digit number")

# Check the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.
a = int(input("Enter a value 1 : "))
b = int(input("Enter a value 2 : "))
if a%2==0 and b%2==0:
    print(f"Their product is {a*b}")
else:
    print(f"Their sum is {a+b}")

# Buzz number either if ends with 7 or divisible by 7
print("To finding the Buzz number either if ends with 7 or divisible by 7")
number = int(input("Enter a number : "))
if number%10==7 or number%7==0:
    print("It's a Buzz number")
else:
    print("It's not a Buzz number")