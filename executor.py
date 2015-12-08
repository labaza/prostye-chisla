import time

beforeTime = time.time()

# K = 1 million
K = 1000000
lst = [2]

for i in range(3, K + 1, 2):
	if (i > 10) and (i % 10 == 5):
		continue
	for j in lst:
		if j*j - 1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)

afterTime = time.time()

print (K)
print (".......\n")
print ((float)(afterTime - beforeTime))
