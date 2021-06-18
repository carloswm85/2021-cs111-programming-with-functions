"""
Your program must do the following:

- Open the provinces.txt file for reading.
- Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
- Print the entire list.
- Remove the first element from the list.
- Remove the last element from the list.
- Replace all occurrences of "AB" in the list with "Alberta".
- Count the number of elements that are "Alberta" and print that number.
"""

def main():
	
	txt_list = read_list(
		"E:/GitHub/2021-cs111-programming-with-functions/w09-text-files/checkpoint-provinces/provinces.txt")
	
	print(txt_list)
	print()

	txt_list.pop(0)
	# print(txt_list)
	# print()

	txt_list.pop(len(txt_list) - 1)
	# print(txt_list)
	# print()

	txt_list = ab_replace(txt_list)

	# print(txt_list)
	# print()

	counted = txt_list.count('Alberta')
	print(f'Alberta occurs {counted} times in the modified list.')

def read_list(file):
	text_list = []

	with open(file, "rt") as text_file:
		for line in text_file:
			clean_line = line.strip()
			text_list.append(clean_line)
	
	return text_list

def ab_replace(list):
	new_list = []
	for item in list:
		if item == 'AB':
			item = 'Alberta'
			new_list.append(item)
		else:
			new_list.append(item)

	return new_list

if __name__ == "__main__":
	main()
