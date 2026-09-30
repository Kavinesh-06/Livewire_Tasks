print("Hello World")

#  Addition Subtraction Multiplication Division Modulo

a = int(input("Enter the value of 'a'"))
b = int(input("Enter the value of 'b'"))
add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
print("addition = ",add, "subtraction = ",sub,"multiplication = ",mul, "Division = ",div, "Modulo = ",mod)

# Square Root

num = int(input("Enter a number for Square root: "))
Sq_root = num**0.5
print("Square Root : ", Sq_root)

# Area of Triangle

base = int(input("Enter a base: "))
height = int(input("Enter a height: "))
result = base * height * 0.5
print("Area of Triangle : ", result)

# Quadratic Equation

print("Quadratic Equation")
x = int(input("Enter 'a' value: "))
y = int(input("Enter 'b' value: "))

result_1 = (x + y)**2
result_2= (x - y)**2
result_3= x**2 - y**2

print("(a+b)^2 is ",result_1)
print("(a-b)^2 is ",result_2)
print("a^2 - b^2 is ",result_3)

# Swap Two variables Using third variable

print("Swapping variables")
a1 = int(input("Enter a number 1 : "))
b1 = int(input("Enter a number 2 : "))
print("Before Swapping ", a1,b1)
temp = a1
a1 = b1
b1 = temp
print("After Swapping Using third variable ", a1,b1)

# Swap Two variables without Using third variable

a1, b1 = b1, a1
print("After Swapping without Using third variable ", a1,b1)

# Kilometers to miles

k = float(input("Enter how many kilometers : "))
miles = k * 0.63
print("Miles: ", miles)

# celsius to fahrenheit

celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Fahrenheit =", fahrenheit)

# Last digit number

number = int(input("Enter a number: "))
last_digit = number % 10
print("Last digit =", last_digit)

# the Last Two Digits

number = int(input("Enter a number: "))
last_two_digits = number % 100
print("Last two digits =", last_two_digits)

# Five-Digit Number – Square the Middle Digit

digit = int(input("Enter a 5-digit number: "))
digit = str(digit)
mid = int(digit[2])
sq_mid = mid ** 2
print(f"Square of {mid} is : {sq_mid}")
