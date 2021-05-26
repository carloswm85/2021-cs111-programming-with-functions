from datetime import datetime

current_dt = datetime.now()
week_day = current_dt.isoweekday()

price_str = 'run'
while price_str != 'done':
	price_str = input('Enter price (type "done" for exiting the program): ')
	if price_str == "done":
		break
	else:
		price = float(price_str)
		quantity = int(input('Enter quantity: '))
		subtotal = price * quantity

		if subtotal < 50:
			difference = 50 - subtotal
			print('Additional amount for discount: ' + str(difference))

		if week_day == 2 or week_day == 6 and subtotal >= 50:
			discount = subtotal * 0.1
			print('Discount is: ' + str(discount))
			subtotal = subtotal - discount

		tax = subtotal * 0.06
		print('Applied tax: ' + str(tax))
		subtotal = subtotal + tax
		print('Total is: ' + str(subtotal))
print('Program finished.')