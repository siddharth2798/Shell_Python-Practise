def calculate(num):
	i=0
	while num>0:
		i=i*10 + num%10
		num = num//10
	print (i)

calculate(2030)
