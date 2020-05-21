class Book:
	
	def __init__(self,bid,name):
		self.book_id = bid
		self.book_name = name


class Library:

	def __init__(self,lid,add,blist):
		self.library_id = lid
		self.address = add
		self.book_list = blist


	def count_books(self,nc):
		c=0
		for book in self.book_list:
			if book.book_name.startswith(nc):
				c = c+1
		return c

	def remove_books(self,bookl):
		for book in self.book_list:
			for issue in bookl:
				if book.book_name == issue:
					self.book_list.remove(book)
		return self.book_list


if __name__ == '__main__':

	l = []
	del_list =[]
	n = int(input("Enter number of objects"))
	for i in range(n):
		bid = int(input("enter book id"))
		bname = input("enter book name")
		l.append(Book(bid,bname))

	lib = Library(141,"London",l)

	ch = input("enter character to be searched")

	num = int(input("enter number of books to be del"))
	
	for i in range(num):
		name = input("enter name")
		del_list.append(name)

	count = lib.count_books(ch)
	result = lib.remove_books(del_list)
	print(count,end=" ")

	for book in result:
		print (book.book_name,end=" ")

	

		
		
	


