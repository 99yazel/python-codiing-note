a = input();
a = int(a);
def check(value):
	if value//3 == 1:
		print('spring');
	elif value//3 == 2:
		print('summer');
	elif value//3 == 3:
		print('fall');
	else:
		print('winter');

check(a)