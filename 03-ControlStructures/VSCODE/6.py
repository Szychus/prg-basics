# Zadanie 6.3
light_switch1 = True 
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2           # <--- WSTAWIONE
print(f"Bulbs lit: {bulbs_on}") # <--- WSTAWIONE

# Zadanie 6.4
new_password = input('Enter new password: ')
if len(new_password) < 12:  # <--- WSTAWIONE
   print('Password too short (min. 12 chars)') 

# Zadanie 6.5
temperature = int(input("Enter temperature: "))
if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")      # <--- WSTAWIONE
elif temperature >= 15:     # <--- WSTAWIONE
    print("It is warm")     # <--- WSTAWIONE
elif temperature >= 0:      # <--- WSTAWIONE
    print("It is cold")     # <--- WSTAWIONE
else:                       # <--- WSTAWIONE
    print("Warning, frost") # <--- WSTAWIONE

# Zadanie 6.8
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')   # <--- WSTAWIONE
person2_age = int(input('Enter second person age: '))# <--- WSTAWIONE

if person1_age >= 18 and person2_age >= 18:          # <--- WSTAWIONE
    print(f'Both {person1_name} and {person2_name} are adults') # <--- WSTAWIONE
else:
    print(f'Either {person1_name} or {person2_name} is not an adult') # <--- WSTAWIONE

# Zadanie 6.16 (fragment)
if program == 'j': total_washing_time += 40          # <--- WSTAWIONE
elif program == 'u': total_washing_time += 70        # <--- WSTAWIONE
elif program == 's': total_washing_time += 20        # <--- WSTAWIONE

if extra_rinse: total_washing_time += 15             # <--- WSTAWIONE
if extra_spin: total_washing_time += 9               # <--- WSTAWIONE