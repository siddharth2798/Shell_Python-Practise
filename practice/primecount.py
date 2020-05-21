

def countPrimeNumbers(numbers):
    chk = [False for i in range(len(numbers))]
    c=0
    f=0
    print (chk)
    for num in numbers:
        i=2
        while i<= num//2:
	    
		
            if num%i == 0:
                chk[numbers.index(num)] = True
            i +=1
                
	

    
    for res in chk:
        if res == False:
            c+=1
    
    return c        


if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
        
    print(countPrimeNumbers(numbers))
        

