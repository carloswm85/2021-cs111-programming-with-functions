def cels_from_fahr(fahr):
	"""Convert a temperature in Fahrenheit to
	Celsius and return the Celsius temperature.
	"""
	cels = (fahr - 32) * 5 / 9
	return cels


def main():
	value = -25
	result = cels_from_fahr(value)
	print(result)

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
	main()
