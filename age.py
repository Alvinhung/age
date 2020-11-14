#age.py
driving = input('Have you ever driven a car')
if driving != 'yes' and driving != 'no':
	print('Can only input yes/no')
	raise SystemExit

age = input('Your age?')
age = int(age)


if driving == 'yes':

	if age >= 18:
		print('You pass the exam')
	else:
		print('Why have you driven the car before??')
elif driving == 'no':
	if age >= 18:
		print('Maybe you can take the exam then get the license')
	else:
		print('A few years to wait, bro')



