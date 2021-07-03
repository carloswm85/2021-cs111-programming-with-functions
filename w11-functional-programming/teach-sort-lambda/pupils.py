import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    path = "E:/GitHub/2021-cs111-programming-with-functions/w11-functional-programming/teach-sort/pupils.csv"

    # Call the read_compound_list function to read the pupils.csv file into a list named students_list.
    students_list = read_compound_list(path)

    # Write a lambda function that will extract the birthdate from a student.
    birthdate_func = lambda birthdate: birthdate[BIRTHDATE_INDEX]
    given_name_func = lambda given_name: given_name[GIVEN_NAME_INDEX]
    birthdate_func_2 = lambda birthdate: birthdate[BIRTHDATE_INDEX]

    # Write a call to the sorted function that will sort the students_list by birthdate from oldest to youngest.
    sorted_students_list_bd = sorted(students_list, key = birthdate_func)    
    sorted_students_list_gn = sorted(students_list, key = given_name_func) 
    sorted_students_list_bd_2 = sorted(students_list, key = birthdate_func_2)    

    print("\nLISTA #1:")
    print_list(students_list)

    # Print the students_list by calling the print_list function.
    print("\nLISTA #2:")
    print_list(sorted_students_list_bd)

    # Within the main function, replace the code that sorts the students_list by birthdate, with code that sorts the students_list by given name.
    print("\nLISTA #3:")
    print_list(sorted_students_list_gn)

    # Within the main function, replace the code that sorts the students_list by birthdate, with code that sorts the students_list by birth month and day. In other words, the code should sort the students_list by birthdate but ignore the year when a student was born.
    print("\nLISTA #4:")
    print_list(sorted_students_list_bd_2)

    

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(lista):
    for element in lista:
        print(element)

if __name__ == "__main__":
    main()
