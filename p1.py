x = 43
y = 'abcd'
print(type(x))
print(type(y))
x = x + 1
print(x)
#get input and show the type
name = input('Enter any: ')
print('Type of input value - ',type(name))
print('All inout values are strings')

# is it a Valid input
A = input("Enter name in small:")

if 1<= len(A) <= 15 and A.islower():
	print("Hello"+A)
else:
	print("Invalid input")