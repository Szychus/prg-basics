###
# Calculates the sum of the digits in a number
#
def sum_digits(number):

    abs(number)  # Ensure the number is positive
    str(number)  # Convert the number to a string to iterate over its digits
    total = 0  # Initialize a variable to hold the sum of the digits

   
    
    ...
    return sum(int(digit) for digit in str(abs(number)))  # Sum the digits and return the result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}            ')