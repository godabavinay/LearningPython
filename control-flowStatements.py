# conditional statements
loc = 'Bank'

if loc == 'Auto shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
else:
    print('I do not know much')

# looping statements

# for loop
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in my_list:
    print(item)

for item in my_list[::2]:
    print(item)

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for item in my_list:
    print(item)

for a, b in my_list:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for value in d.values():
    print(value)

# while loop
a = 0
while (a < 5):
    print(a)
    a += 1
else:
    print('now a is not less than 5')

while True:
    if a == 100:
        break
    a += 1
print(a)

for i in d.values():
    pass