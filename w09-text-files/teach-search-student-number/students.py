import csv
import re

def main():
	run = True
	I_NUMBERS = 0
	STUDENT_NAME = 1

	path = 'E:/GitHub/2021-cs111-programming-with-functions/w09-text-files/teach-/students.csv'
	students = get_dictionary(path, I_NUMBERS, STUDENT_NAME)

	while run:
		print()
		number_student = input('Please enter an I-Number (xx-xxx-xxxx): ')
		undashed_number = number_student.replace('-', '')
		regex_condition = re.match('^[\d_-]*$', undashed_number)

		# if not inumber.isdigit():
		if regex_condition == None:
			print('Invalid I-Number')
		else:
			if len(undashed_number) < 9:
				print('Invalid I-Number: Too few digits')
			elif len(undashed_number) > 9:
				print('Invalid I-Number: Too many digits')
			else:
				# Solution 1
				found = False
				for id, student in students.items():
					if id == undashed_number:
						print(f'Student name is: {student}')
						found = True	
				if not found:
					print('No such student')

				# Solution 2
				# if inumber not in students:
                # 	print("No such student")
            	# else:
                # 	value = students[inumber]
                # 	name = value[NAME]
                # print(name)

		print()
		continue_ = int(input('Continue? Yes: 1, No: Something else → '))
		if continue_ != 1:
			run = False


def get_dictionary(file, key_index, value_index):
	dictionary = {}

	with open(file, 'rt') as csv_file:
		reader = csv.reader(csv_file)
		next(reader)

		for row in reader:
			key = row[key_index]
			value = row[value_index]
			dictionary[key] = value
	
	return dictionary

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == '__main__':
	main()
