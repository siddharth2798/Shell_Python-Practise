def check_prime(num):
	chk = False
	for i in range (2,num//2):
		if num%i == 0:
			chk = True
			break
	if chk == True:
		return 1
	elif chk== False:
		return 0

def prime_composite_list(pclist):
	prime_list=[]
	composite_list=[]
	total_list = []
	
	for num in pclist:
		result = check_prime(num)

		

		if result == 0:
			prime_list.append(num)
		else:
			composite_list.append(num)
	

	total_list.append(prime_list)
	
	total_list.append(composite_list)
	return total_list

if __name__ == '__main__':
	count= int(input())
	inp = []
	
	for i in range(count):
		a = int(input())
		inp.append(a)

	result = prime_composite_list(inp)

	print (result)
		

	

	
		
			
		
