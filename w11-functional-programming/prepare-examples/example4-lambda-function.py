# Example 4

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    def cels_from_fahr(fahr): return round((fahr - 32) * 5 / 9, 1)

	"""
	Looking at the lambda function in example 4 on line 12, it appears that the lambda function is named cels_from_fahr. However, cels_from_fahr is the name of a variable, not the name of the lambda function. 
	"""

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()

"""
The lambda function has no name. This distinction may seem trivial until we see an example of an inline lambda function. Notice in the next example that the lambda function is defined inside the parentheses for the map function.

Convert each Fahrenheit temperature to Celsius and store
the Celsius temperatures in a list named cels_temps.
	
	cels_temps = list(map(
		lambda fahr: round((fahr - 32) * 5 / 9, 1),
		fahr_temps))

# lambda param1, param2, … paramN: expression

In Python, every lambda function can be written as a regular Python function.
"""
