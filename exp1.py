def product_or_sum(a, b):
    product = a * b
    if product > 1000:
        return a + b
    else:
        return product

# Example usage:
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
result = product_or_sum(num1, num2)
print("Result:", result)
