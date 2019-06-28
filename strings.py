# strings
name = 'panda'
print(name)

print(name[0])
print(name[1])

# trying something out of range
# print(name[10])

# sliced indexing
x = 'abcdefghij'
print(x)

print(x[:3])

print(x[0:])

print(x[0:10])
# python won't raise error in this case
print(x[0:111])

print(x[::2])

# string methods
x = 'This is a small line of text.'
x = x.split()
print(x)

# string formaters
name = 'Pand'

print('His name is {}'.format(name))

#using new python syntax
print(f'His name is {name}')