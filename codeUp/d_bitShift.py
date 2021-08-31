# num 46
n = 2
print(n<<1);
# num 47 // a<<b => a*2^b
a,b = input().split();
a = int(a);
b = int(b);
print(a<<b);
# num 48
a,b = input().split();
a = int(a);
b= int(b);
print(a < b);
# num 49
a,b = input().split();
a = int(a);
b= int(b);
print(a == b);
# num 50
a,b = input().split();
a = int(a);
b= int(b);
print(a <= b);
# num 51
a,b = input().split();
a = int(a);
b= int(b);
print(a != b);
# num 52
n = int(input())
print(bool(n))
# num 53
n = int(input())
a = bool(n)
print( not a);
# num 54
a,b = input().split();
a = int(a);
b = int(b);

print(bool(a) and bool(b));
# num 55
a,b = input().split();
a = int(a);
b = int(b);

print(bool(a) or bool(b));
# num 56
a,b = input().split();
a = int(a);
b = int(b);
ba = bool(a);
bb = bool(b);

print((ba and (not bb)) or ((not ba) and bb));
# num 57
a,b = input().split();
ba = bool(int(a));
bb = bool(int(b));
print(bool(ba) == bool(bb));
# num 58
a,b = input().split();
ba = bool(int(a));
bb = bool(int(b));
print(not(ba or bb));
# num 59 (~n = -n - 1 )(-n = ~n + 1)
a = int(input());
print(~a);
# num 60
a,b = input().split();
a = int(a);
b = int(b);
print(a&b);
# num 61
a,b = input().split();
a = int(a);
b = int(b);
print(a|b);
# num 62
a,b = input().split();
a = int(a);
b = int(b);
print(a^b);
# num 63
a,b = input().split();
a = int(a);
b = int(b);
c = (a if(a>=b) else b)
print(int(c))
# num 64
a,b,c = input().split();
a = int(a);
b = int(b);
c = int(c);
min = a if a<b else b;
min = c if c<min else min;
print (min);
# num 65
a,b,c = input().split();
a = int(a);
b = int(b);
c = int(c);
if a%2 == 0:
	print(a)
if b%2 == 0:
	print(b)
if c%2 == 0:
	print(c)
# num 66
a,b,c = input().split();
a = int(a);
b = int(b);
c = int(c);

def checkEven(value):
	if value%2 == 0:
		print("even")
	else:
		print("odd")

checkEven(a)
checkEven(b)
checkEven(c)
# num 67
a = input();
a = int(a);

def check(value):
	if value< 0:
		if value%2 == 0:
			print("A")
		else:
			print("B")
	else:
		if value%2 == 0:
			print("C")
		else:
			print("D")

check(a)
# num 68
a = input();
a = int(a);

def check(value):
	if value >= 90:
		print('A')
	else:
		if value >= 70:
			print('B')
		else:
			if value >= 40:
				print('C')
			else:
				print('D')
				

check(a)
# num 69
a = input();

def check(value):
	if value == 'A':
		print('best!!!')
	elif value == 'B':
		print('good!!');
	elif value == 'C':
		print('run!')
	elif value == 'D':
		print('slowly~')
	else:
		print('what?')

check(a)
# num 70
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
