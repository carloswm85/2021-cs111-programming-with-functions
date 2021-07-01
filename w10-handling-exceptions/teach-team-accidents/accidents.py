import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    filename = 'empty_file_location'

    while True: 
        while True:
            # GETTING THE FILE
            # Prompt the user for a filename and open that text file.
            print()
            selection = input("Select file: Default file (0); Enter any file name (1); Protected file (2) →  ")
            print()    
            if selection == '0':
                print("Name of file that contains NHTSA data: ")
                filename = 'E:/GitHub/2021-cs111-programming-with-functions/w10-handling-exceptions/teach-team-accidents/accidents.csv'
                print(filename)
                break
            elif selection == '1':
                filename = input("Name of file that contains NHTSA data: ")
                print(filename)
                break
            elif selection == '2':
                print("Name of file that contains NHTSA data: ")
                filename = 'E:/GitHub/2021-cs111-programming-with-functions/w10-handling-exceptions/teach-team-accidents/accidents_protected.csv'
                print(filename)
                break
            else:
                print(f'{selection} is not a valid option. Try again.')
            
        print()
        # OPENING THE FILE
        try:
            with open(filename, "rt") as text_file:

                # Prompt the user for a percentage.
                perc_reduc = get_float_100("Percent reduction of texting while driving [0, 100]: ")
                print()
                print(f"With a {perc_reduc}% reduction in using a cell phone while",
                        "driving, approximately this number of injuries and",
                        "deaths would have been prevented in the USA.", sep="\n")
                print()
                print("Year, Injuries, Deaths")

                # Use the csv module to create a reader
                # object that will read from the opened file.
                reader = csv.reader(text_file)

                # The first line of the CSV file contains column headings
                # and not a student's I-Number and name, so this statement
                # skips the first line of the CSV file.
                next(reader)

                # Process each row in the CSV file.
                rowNumber = 1
                for row in reader:
                    year = row[YEAR_COLUMN]

                    # Call the estimate_reduction function.
                    injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc, filename, rowNumber)

                    # Print the estimated reductions in injuries and fatalities.
                    if injur != -1 and fatal != -1:
                        print(year, injur, fatal, sep=", ")
                    rowNumber += 1

        except FileNotFoundError as file_not_found_err:
            print(f"Error: Cannot open {filename}, because the file does not exist.")
            print(file_not_found_err)
            print('Please, choose a different file.')
        except PermissionError as perm_err:
            print(f"Error: cannot read from {filename} because you don't have permission.")
            print(perm_err)
            print('Please, choose a different file.')
                    

        print()
        runAgain = input('Do you want to run the program again? NO: 0; YES: Something else →  ')
        if runAgain == '0':
            print()
            print('Program terminated.')
            break

def get_float_100(prompt):
    while True:
        try:
            # In this situation, the computer does not raise an exception, but this situation is still a mistake that the program should alert the user about.
            print()
            floating_number = float(input(prompt))
            if floating_number < 0:
                print(f"{floating_number} is too small. Please enter another number.")
            elif floating_number > 100:
                print(f"{floating_number} is too large. Please enter another number.")
            else:
                break # This line is reached when the user entered a correct number.
        except ValueError as val_err:
            print(
                f"Error: You entered text that is not an integer. Please run the program again and enter an integer.")
            print(val_err)
        
    return floating_number


def estimate_reduction(row, behavior_key, perc_reduc, filename, count):
    """Estimate and return the number of injuries and deaths that would
    not have occurred on U.S. roads and highways if drivers had reduced
    a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been prevented
    """
    try:
        behavior = int(row[behavior_key])
        fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
        ratio = perc_reduc / 100 * behavior / fatal_crashes

        fatalities = int(row[FATALITIES_COLUMN])
        injuries = int(row[INJURIES_COLUMN])

        reduc_fatal = int(round(fatalities * ratio, 0))
        reduc_injur = int(round(injuries * ratio, 0))
    except ZeroDivisionError as zero_div_err:
        print(f'Check row {count}: In {filename}. Cannot divide by 0. Try again.')
        reduc_fatal = -1
        reduc_injur = -1
        print(zero_div_err)

    return reduc_injur, reduc_fatal

# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
