# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def main():
	run = True

	while run:
		user_input = input('\nDo you want to accept user input? If not, sample data will be loaded (Y/N) ').upper()
		if user_input == 'Y':
			gender = input("Please enter your gender (M or F): ").upper()
			birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
			weight = int(input("Enter your weight in US pounds: "))
			weight_stones = int(input("Enter your weight in UK stones: "))
			height = int(input("Enter your height in US inches: "))
			height_fi = input("Enter your height in US feet and inches (decimal): ")
		else:
			select_sample = input('Do you want sample data for male (M) or female (F)?').upper()
			if select_sample == "F":
				gender = "F"
				birthdate = "2001-03-21"
				weight = 125
				weight_stones = 9
				height = 54
				height_fi = "4 6"
				print('\nSample data for FEMALE.')
				print('\tBirthdate: 2001-03-21')
				print('\tWeight in US pounds: 125')
				print('\tWeight in US inches: 54')
			else:
				gender = "M"
				birthdate = "2003-11-26"
				weight = 145
				weight_stones = 10.3571
				height = 58
				height_fi = "4 10"
				print('\nSample data for MALE.')
				print('\tBirthdate: 2003-11-26')
				print('\tWeight in US pounds: 145')
				print('\tWeight in US inches: 58')

		# Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
		# and basal_metabolic_rate functions as needed.
		age = compute_age(birthdate)
		weight_kg = kg_from_lb(weight)
		weight_kg_stones = kg_from_stones(weight_stones)
		height_cm = cm_from_in(height)
		height_cm_fi = cm_from_fi(height_fi)
		height_m = m_from_in(height)
		bmi = body_mass_index(weight_kg, height_cm)
		bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

		weight_kg = round(weight_kg, 2)
		weight_kg_stones = round(weight_kg_stones, 2)
		height_cm = round(height_cm, 2)
		height_m = round(height_m, 2)
		height_cm_fi = round(height_cm_fi, 2)

		# Print the results for the user to see.
		print('Core operations:')
		print(f"\tAge (years): {age}")
		print(f"\tWeight (kg): {weight_kg}")
		print(f"\tHeight (cm): {height_cm}")
		print(f"\tBody mass index: {bmi}")
		print(f"\tBasal metabolic rate (kcal/day): {bmr}")

		# Stretch Challenges
		print('Additional operations:')
		print(f"\tHeight (m): {height_m}")
		print(f"\tWeight (stones): {weight_stones}")
		print(f"\tWeight (kg from stones): {weight_kg_stones}")
		print(f"\tHeight (cm from fi): {height_cm_fi}")

		exit_program = input('\nDo you want to run the program again? (Y/N) ').upper()
		if exit_program == "N":
			run = False
			print('Program terminated.')

def compute_age(birth):
	"""Compute and return a person's age in years.

	Parameter birth: a person's birthdate stored as
	a string in this format: YYYY-MM-DD
	Return: a person's age in years.
	"""
	birthday = datetime.strptime(birth, "%Y-%m-%d")
	today = datetime.now()

	# Compute the difference between today and the birthday in years.
	years = today.year - birthday.year

	# If necessary, subtract one from the difference.
	if birthday.month > today.month or \
		(birthday.month == today.month and birthday.day > today.day):
		years -= 1

	return years

def kg_from_lb(lb):
	"""Convert a mass in pounds to kilograms.
	Parameter lb: a mass in US pounds.
	Return: the mass in kilograms.
	"""
	kg = lb * 0.45359237
	return kg


def cm_from_in(inch):
	"""Convert a length in inches to centimeters.
	Parameter inch: a length in inches.
	Return: the length in centimeters.
	"""
	cm = inch * 2.54
	return cm

def body_mass_index(weight, height):
	"""Calculate and return a person's body mass index (bmi).
	Parameters:
	weight must be in kilograms.
	height must be in centimeters.
	Return: a person's body mass index.
	"""
	bmi = (10000 * weight) / (height ** 2)
	return round(bmi, 1)

def basal_metabolic_rate(gender, weight, height, age):
	"""Calculate and return a person's basal metabolic rate (bmr).
	Parameters:
	weight must be in kilograms.
	height must be in centimeters.
	age must be in years.
	Return: a person's basal metabolic rate in kcal per day.
	"""
	if gender == "M":
		bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
	elif gender == "F":
		bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
	else:
		bmr = -1
	return round(bmr, 0)

# Stretch Challenges
def m_from_in(inch):
	m = inch * 0.0254
	return m

def kg_from_stones(weight_stones):
	kg = weight_stones * 6.35029
	return kg

def cm_from_fi(feet_inches_str):
	list_fi = [int(i) for i in feet_inches_str.split() if i.isdigit()]
	cm = 0 + cm_from_ft(list_fi[0]) + cm_from_in(list_fi[1])
	return cm

def cm_from_ft(feet):
	cm = int(feet) * 30.48
	return cm

# Call the main function so that
# this program will start executing.
main()

