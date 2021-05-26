from datetime import datetime, timedelta
now = datetime.now()
print('Today is: ' + str(now))

one_day = timedelta(days=1)
yesterday = now - one_day
print('Yesterday was: ' + str(yesterday))

print('D: ' + str(now.day))
print('M: ' + str(now.month))
print('Y: ' + str(now.year))

birthday = input('When is ypu birthday? (dd/mm/yyyy)')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

