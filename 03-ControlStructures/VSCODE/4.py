# Zadanie 4.4
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' ' # <--- WSTAWIONE

print(university)                       # <--- WSTAWIONE
print(university_expanded.strip())      # <--- WSTAWIONE

# Zadanie 4.5
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char != ' ':                     # <--- WSTAWIONE (obsługa spacji)
        code = ord(char)                # <--- WSTAWIONE
        new_code = code + 1             # <--- WSTAWIONE
        encrypted_text += chr(new_code) # <--- WSTAWIONE
    else:                               # <--- WSTAWIONE
        encrypted_text += ' '           # <--- WSTAWIONE

print(f'Plain text: {plain_text}')      # <--- WSTAWIONE
print(f'Encrypted text: {encrypted_text}') # <--- WSTAWIONE

# Zadanie 4.7
sum_even = 0
for i in range(1, 11):                  # <--- WSTAWIONE
    if i % 2 != 0:                      # <--- WSTAWIONE
        continue
    sum_even += i                       # <--- WSTAWIONE

print(f'Sum of even numbers in the range <1,10> is {sum_even}') # <--- WSTAWIONE

# Zadanie 4.8
for i in range(1, 11):                  # <--- WSTAWIONE
    print(f'1/{i} = {1/i}')             # <--- WSTAWIONE