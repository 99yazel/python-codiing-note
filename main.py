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