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
n = int(input());

for i in range(1, n+1):
	if(i%3 == 0):
		continue;
	print(i,end=' ')
# num 88
[a,d,n] = map(int,input().split());

def get(a,d,n):
	return a+d*(n-1)
print(get(a,d,n));
# num 89
[a,r,n] = map(int,input().split());

def get(a,r,n):
	return a*r**(n-1)
print(get(a,r,n));
# num 90
[a,m,d,n] = map(int,input().split());

total =a
for i in range(0, n-1):
	total = total *m +d
print(total);
# num 91
[a,b,c] = map(int,input().split());

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
# num 92
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

#참고
#- d = []              #어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
#- d.append(값)  #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 
#- d[a[i]] += 1     #2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..
# num 93
a =int(input());
b =list(map(int,input().split()));

for i in range(a-1,-1,-1):
    print(b[i], end=' ' );
# num 94
a =int(input());
b =list(map(int,input().split()));
c = b[0];
for i in range(0,a):
	if(c > b[i]) :
		c = b[i]
print(c);
# num 95
d=[]
for i in range(20):
	d.append([]);
	for j in range(20):
		d[i].append(0);
# d = [[0 for j in range(20)] for i in range(20)]
n = int(input());
for i in range(n):
	x,y = input().split()
	d[int(x)][int(y)] = 1

for i in range(1,20):
	for j in range(1,20):
		print(d[i][j], end=' ')
	print()
# num 96
a = [[]*19 for _ in range(19)]
for i in range(19):
   a[i]=list(map(int,input().split()))

n = int(input())

for i in range(n):
    b,c=map(int,input().split())
    
    for j in range(19):
        if(a[b-1][j]==1):
            a[b-1][j]=0
        else: a[b-1][j]=1
    
    for j in range(19):
        if(a[j][c-1]==1):
            a[j][c-1]=0
        else: a[j][c-1]=1

for i in range(19):
    for j in range(19):
        print(a[i][j],end=' ')
    print()
# num 97
# h : 세로
# w : 가로
# n : 막대 개수
# l : 막대 길이
# d : 0, 1 가로,세로
# x,y : 막대의 가장 왼족 또는 위쪽 위치
# return : 격자판을 채운 막대의 모양을 출력하는 프로그램

[h,w] = map(int,input().split());
n = int(input());

c = [[0]*w for _ in range(h)];

for i in range(n):
	[l,d,x,y] = map(int,input().split());
	
	if(d == 0):
		for j in range(l):
			c[x-1][y-1+j] = 1;
	else:
		for j in range(l):
			c[x-1+j][y-1] = 1;

for i in range(h):
	for j in range(w):
		print(c[i][j], end= ' ');
	print();
# num 98
c = [[]*10 for _ in range(10)]
for i in range(10):
	c[i] = list(map(int,input().split()));
x = 1 
y = 1
c[x][y] = 9

while True:
	if(c[x][y] ==2 ):
		c[x][y] = 9
		break;
	if(c[x][y+1] != 1):
		c[x][y] = 9
		y += 1
	else:
		if(c[x+1][y] != 1):
			c[x][y] = 9
			x += 1
		else:
			c[x][y] = 9
			break;

for i in range(10):
	for j in range(10):
		print(c[i][j], end=' ')
	print()