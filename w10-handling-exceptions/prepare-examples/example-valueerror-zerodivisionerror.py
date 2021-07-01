# Example 8

"""
Sam, who is the owner of Sam's Sandwich Shop, requested
this program, which computes the number of sandwiches per
employee that were made in his restaurant in one day.
"""


def main():
    try:
        # Get the number of sandwiches made today and the
        # number of employees who worked today from the user.
        sandwiches = int(input("Number of sandwiches that were made today: "))
        employees = int(input("Number of employees who worked today: "))

        # Compute the number of sandwiches per employee
        # that were made today in the restaurant.
        sands_per_emp = sandwiches / employees

        # Print the results for the user to see.
        print(f"{sands_per_emp} sandwiches per employee")

    except ValueError as val_err:
        print()
        print(val_err)
        print("Error: you entered text that is not an integer.")
        print("Please run the program again and enter an integer.")

    except ZeroDivisionError as zero_div_err:
        print()
        print("Error: you entered 0 for the number of employees.")
        print("Please run the program again and enter an integer")
        print("larger than 0 for the number of employees.")


# Call main to start this program.
if __name__ == "__main__":
    main()
