x = 3
while x >= 1:
	ques = input('password please: ')
	password = 'a123456'
	if ques != password:
		print('unsuccess, you have', x - 1, 'chances')
		x = x - 1
	elif ques == password:
		print('success')
		break
