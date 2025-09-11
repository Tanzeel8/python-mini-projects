print("Simple Python Calculator")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, %%, %/-): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == '%':
    result = num1 % num2                     # modulus
elif operator == '%%':
    result = (num1 * num2) / 100             # percentage
elif operator == '%/-':
    result = num1 - (num1 * num2 / 100)      # subtract % of num1
else:
    result = "Invalid operator."

print("Result:", result)
