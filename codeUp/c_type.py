# num 25
a,b = input().split();
c = int(a) + int(b);
print(c);
# num 26
a,b = input().split();
c = int(a) + int(b);
print(c);
# num 27
a = input();
n = int(a);
print('%x'%n);
# num 28
a = input();
n = int(a);
print('%X'%n);
# num 29 16 -> 8
a = input();
n = int(a,16);
print('%o'%n);
# num 30 ord: ordinal position // 문자->정수값 
n = ord(input())
print(n)
# num 31 chr( )는 정수값->문자
c = int(input()); # 65
print(chr(c)); # A
# num 32
n = int(input());
print(-n);
# num 33
n = ord(input());
print(chr(n+1));
# num 34
a,b = input().split();
c = int(a) - int(b);
print(c);
# num 35
a,b = input().split();
c = float(a) * float(b);
print(c);
# num 36
a,b = input().split();
print(a * int(b));
# num 37
n = input();
word = input();
print(int(n) * word);
# num 38, 39
a,b = input().split();
print(int(a)**int(b));
# num 40
a,b = input().split();
print(int(a)//int(b));
# num 41
a,b = input().split();
print(int(a)%int(b));
# num 42
a = float(input());
print(format(a,".2f"));
# num 43
a,b = input().split();
a = float(a);
b = float(b);
print(format(a/b,'.3f'));
# num 44
a,b = input().split();
a = int(a);
b = int(b);
print(a+b);
print(a-b);
print(a*b);
print(a//b);
print(a%b);
print(format(a/b,'.2f'));
# num 45
a,b,c = input().split();
a = int(a);
b = int(b);
c = int(c);
sum = a+b+c;
print(sum, format(sum/3,'.2f'));
