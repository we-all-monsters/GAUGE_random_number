import random
r = random.randint(1, 100)

while True:
	n = input('你估的數字：')
	n = int(n)
	if n > r:
		print('估細d')
	elif n < r:
		print('估大d')
	else :
		print('你對啦~')
	
	