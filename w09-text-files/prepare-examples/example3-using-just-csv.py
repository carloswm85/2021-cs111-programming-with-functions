# Example 3

import csv

# Indexes of some of the columns
# in the dentists.csv file.
COMPANY_NAME_INDEX = 0
NUM_EMPLOYEES_INDEX = 6
NUM_PATIENTS_INDEX = 7


def main():
    # Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentists_file.
    with open("E:/GitHub/2021-cs111-programming-with-functions/w09-text-files/prepare-examples/dentists.csv", "rt") as dentists_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(dentists_file)

        # The first line of the CSV file contains column headings
        # and not information about a dental office, so this
        # statement skips the first line of the CSV file.
        next(reader)

        running_max = 0
        most_office = None

        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # For the current row, retrieve the
            # values in columns 0, 9, and 10.
            company = row[COMPANY_NAME_INDEX]
            num_employees = int(row[NUM_EMPLOYEES_INDEX])
            num_patients = int(row[NUM_PATIENTS_INDEX])

            # Compute the number of patients per
            # employee for the current dental office.
            patients_per_employee = num_patients / num_employees

            # If the current dental office has more patients per
            # employee than the running maximum, assign running_max
            # and most_office to be the current dental office.
            if patients_per_employee > running_max:
                running_max = patients_per_employee
                most_office = company

    # Print the results for the user to see.
    print(f"{most_office} has {running_max:.1f} patients per employee")


# Call main to start this program.
if __name__ == "__main__":
    main()
