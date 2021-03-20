def distance(a,b):
	result = 0
	if len(a) != len(b):
		return
	for i in range(len(a)):
		result +=(float(b[i]) - float(a[i]))**2
	result = result ** 0.5
	return result



dest = (input().split())
N = int(input())
l = [input().split() for _ in range(N)]

sp = ["0.0","0.0","0.0"]
cost = []
l.append(dest)
while sp != dest:
	l1 = l[0]
	min_dist = distance(sp,l1)
	min_index = 0
	for i in range(len(l)):
		if distance(sp,l[i]) < min_dist and distance(l[i],dest) <= distance(l[min_index],dest):
			min_dist = distance(sp,l[i])
			min_index = i
	cost.append(min_dist)
	sp = l[min_index]
	l.remove(l[min_index])

print("{:.2f}".format(max(cost)))
