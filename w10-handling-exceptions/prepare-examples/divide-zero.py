x = 42
y = 0

# print(x / y)
# This line of code will throw an error. ZeroDivisionError

# Sorround the code with a triy block.
try:
	print(x / y)
except ZeroDivisionError as e:
	print('Error here, bro! → ', e)
else:
	print('Something else went wrong')
finally:
	print('This is the cleanup code')