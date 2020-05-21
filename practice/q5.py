def count_words (word):
	result = {}
	word_list = []
	throw_list = []
	

	word_list = word.split()
	

	#word_list.remove('hello')
	#print (word_list)
	i=0
	j=0
	c=0
	
	for x in word_list:
		c= word_list.count(x)
		result[x] =c

	
	return result


	

def max_occurence (word):
	result = count_words(word)
	values = result.values()
	maximum = max(values)
	for a,x in result.items():
		if maximum == x:
			return a
	

if __name__ == '__main__':

	sent = input("Enter the sentence to be checked")
	
	dict = count_words(sent)
	
	
	st = max_occurence (sent)
	
	print (st)

	
