# Zadanie 1.3
speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

if car_speed > speed_limit:                 # <--- WSTAWIONE
    print(f'Your speed is {car_speed}km/h') # <--- WSTAWIONE
    print('Warning: speed limit exceeded!!')

# Zadanie 1.4
account_balance = 500
total_payment = int(input('Podaj kwotę: ')) # <--- WSTAWIONE
if total_payment <= account_balance:        # <--- WSTAWIONE
    print('Payment completed')
else:
    print('No funds')

# Zadanie 1.5
total_tasks = 20
tasks_ok = int(input('Podaj liczbę poprawnych zadań: ')) # <--- WSTAWIONE
test_passed = False
if tasks_ok >= total_tasks / 2:                          # <--- WSTAWIONE
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

# Zadanie 1.6
number = int(input('Enter number: '))
if number % 2 == 0:                          # <--- WSTAWIONE
    print(f'{number} is even')               # <--- WSTAWIONE
else:
    print(f'{number} is odd')                # <--- WSTAWIONE

# Zadanie 1.7
basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus) # <--- WSTAWIONE
else:
    total_salary = basic_salary                          # <--- WSTAWIONE

print(f'Basic salary: {basic_salary}')       # <--- WSTAWIONE
print(f'Bonus included? {is_bonus}')         # <--- WSTAWIONE
print(f'Total salary: {total_salary}')       # <--- WSTAWIONE