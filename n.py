import random
r = random.randint(1, 100)
time = 0
while True:
	time += 1 #time = time +1
	n = input('你估的數字：')
	n = int(n)
	if n > r:
		print('估細d')
	elif n < r:
		print('估大d')
	elif n == r :
		print('你對啦~')
		print ('你用了' , time , '次，就估中了')
		break
	print ('你用了' , time , '次')