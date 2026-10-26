# Zadanie 2.2
size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')      # <--- WSTAWIONE
elif size == 'L':                # <--- WSTAWIONE
    print('L: Large size')       # <--- WSTAWIONE
elif size == 'XL':               # <--- WSTAWIONE
    print('XL: Extra large size')# <--- WSTAWIONE
else:
    print('Incorrect symbol')    # <--- WSTAWIONE

# Zadanie 2.3
driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 
elif driving_mode == 'M':
    fuel_consumption = 9         # <--- WSTAWIONE
elif driving_mode == 'E':        # <--- WSTAWIONE
    fuel_consumption = 6         # <--- WSTAWIONE

total_consumption = (distance / 100) * fuel_consumption # <--- WSTAWIONE
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters') # <--- WSTAWIONE

# Zadanie 2.4
number1 = float(input('Enter first number: '))      # <--- WSTAWIONE
number2 = float(input('Enter second number: '))     # <--- WSTAWIONE
operator = input('Enter operator (+, -, *, /): ')   # <--- WSTAWIONE

if operator == '+':                                 # <--- WSTAWIONE
    result = number1 + number2                      # <--- WSTAWIONE
elif operator == '-':                               # <--- WSTAWIONE
    result = number1 - number2                      # <--- WSTAWIONE
elif operator == '*':                               # <--- WSTAWIONE
    result = number1 * number2                      # <--- WSTAWIONE
elif operator == '/':                               # <--- WSTAWIONE
    result = number1 / number2                      # <--- WSTAWIONE

print(f'{number1} {operator} {number2} = {result}')

# Zadanie 2.5
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:                 # <--- WSTAWIONE
    quarter = 3                  # <--- WSTAWIONE
elif month >= 4:                 # <--- WSTAWIONE
    quarter = 2                  # <--- WSTAWIONE
else:                            # <--- WSTAWIONE
    quarter = 1                  # <--- WSTAWIONE

print(f'Month {month} is in quarter {quarter}') # <--- WSTAWIONE