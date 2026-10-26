# Zadanie 3.2
login = 'joe'
password = 'abcd'
entered_login = input('Login: ')
entered_password = input('Password: ')
if login == entered_login and password == entered_password: # <--- WSTAWIONE
    print('You are logged in')
else:
    print('Incorrect login or password!!')

# Zadanie 3.3
age = int(input('Enter your age: '))
if age < 18 or age >= 65:                 # <--- WSTAWIONE
    print('Eligible for discount')        # <--- WSTAWIONE
else:
    print('No discount')                  # <--- WSTAWIONE

# Zadanie 3.4
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))   # <--- WSTAWIONE

if not x < 0 or not y < 0:                # <--- WSTAWIONE
    print(f'At least one of the numbers {x} and {y} is not negative') # <--- WSTAWIONE

# Zadanie 3.5
month = int(input('Enter month number (1..12): '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: # <--- WSTAWIONE
    days = 31 
elif month == 4 or month == 6 or month == 9 or month == 11: # <--- WSTAWIONE
    days = 30                                               # <--- WSTAWIONE
else:                                                       # <--- WSTAWIONE
    days = 28                                               # <--- WSTAWIONE

print(f'Month {month} has {days} days')                     # <--- WSTAWIONE

# Zadanie 3.6
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: # <--- WSTAWIONE
    if day >= 1 and day <= 31:
        day_ok = True
elif month in [4, 6, 9, 11]:                    # <--- WSTAWIONE
    if day >= 1 and day <= 30:                  # <--- WSTAWIONE
        day_ok = True                           # <--- WSTAWIONE
elif month == 2:                                # <--- WSTAWIONE
    if day >= 1 and day <= 28:                  # <--- WSTAWIONE
        day_ok = True                           # <--- WSTAWIONE

message = f'Day {day} for the month {month}'    # <--- WSTAWIONE
if day_ok:
    print(f'{message} is correct')              # <--- WSTAWIONE (dodane formatowanie)
else:
    print(f'{message} is incorrect')            # <--- WSTAWIONE