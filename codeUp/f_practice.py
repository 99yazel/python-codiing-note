# num 77
n = int(input());
s = 0;
for i in range(1,n+1):
	if(i%2 == 0):
		s += i;

print(s);
# num 78
c = input();
def check(value):
	print(value);
	if(value != 'q'):
		c2 = input();
		check(c2)

check(c);
# num 79
n = int(input());
s = 0;
for i in range(n):
	s += i;
	if(s>=n):
		print(i)
		break;
# num 80
[n,m] = map(int,input().split());
for n in range(1, n+1):
	for m in range(1, m+1):
		print(n,m);
# num 81
a = int(input(),16);

for i in range(1,16):
	print('%X*%X=%X' % (a,i,a*i))
# num 82
n = int(input());

for i in range(1, n+1):
	if(i%10 == 3 or i%10 == 6 or i%10 == 9):
		print('X', end=' ')
		continue;
	print(i, end=' ')
# num 83
[r,g,b] = map(int,input().split());
s=0;
for i in range(r):
	for j in range(g):
		for k in range(b):
			print(i,j,k)
			s+=1;
print(s);
# num 84 
[h,b,c,s] = map(int, input().split());
# h : 1초 동안 마이크로 소리강약을 체크하는 횟수
# b : 한 번 체크한 값을 저장할 때 사용하는 비트 수 
# c : 좌우 등 소리를 저장할 트랙 개수 
# s : 녹음할 시간
# 필요한 저장 용량 계산하는 프로그램

def PCM(h,b,c,s):
	print(format(h * b* c * s/8/1024/1024,'.1f'), end=' MB');

PCM(h,b,c,s);
# num 85
[w,h,b] = map(int, input().split());

def PCM(w,h,b):
	print(format(w* h* b / 8 / 1024 / 1024,'.2f'), end=' MB');

PCM(w,h,b);
# num 86
n = int(input());
s = 0;
c = 1;
while True:
	s +=c;
	c += 1;
	if s>=n:
		break;
print(s);
# num 87