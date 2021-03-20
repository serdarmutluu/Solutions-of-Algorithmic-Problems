def mark_pizzeria(l,N):
	c = int(l[2])
	x = int(l[0])-1
	y = int(l[1])-1
	l_res = [[0 for x in range(N)] for y in range(N)]
	for i in range(c+1):
		for j in range(c+1):
			if i+j > c:
				continue
			else:
				if x+i < N and y+j < N:
					l_res[x+i][y+j] = 1
				if x+i < N and y-j>=0:
					l_res[x+i][y-j] = 1
				if x-i >= 0 and y+j < N:
					l_res[x-i][y+j] = 1
				if x-i >= 0 and y-j >= 0:	
					l_res[x-i][y-j] = 1
	return l_res


N,M = input().split()
N = int(N)
M = int(M)
l = [input().split() for _ in range(M)]
res = [[[0 for x in range(N)] for y in range(N)] for i in range(M+1)]

for i in range(M):	
	res[i] = mark_pizzeria(l[i],N)

for i in range(M):
	for j in range(N):
		for k in range(N):
			res[M][j][k] += res[i][j][k]
print(max(max(res[M])))


