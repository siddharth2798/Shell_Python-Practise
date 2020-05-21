class Item:
	def __init__(self,iid,name,price,quan):
		self.item_id = iid
		self.item_name = name
		self.item_price = price
		self.quantity_available = quan

	def calculate_price(self,quan):
		if self.quantity_available >= quan:
			total_price = self.item_price *quan
		
			return total_price
		else:
			return 0

class Store:
	
	def __init__(self,ilist):
		self.item_list = ilist

	def generate_bill(self, itemdict):
		price = []
		for item in self.item_list:
			for name in itemdict.keys():
				if name== item.item_name:
					price.append( item.calculate_price(itemdict[name]))

		print (price[0])
		sum =0
		for i in price:
			sum += i
		return sum




if __name__ == '__main__':
	item_list=[]
	inp = {}
	n = int(input("enter number of items"))
	for i in range(n):
		iid = int(input("enter item id"))
		name = input("enter name")
		price = int(input("enter price"))
		quantity = int(input("enter quan"))
		item_list.append(Item(iid,name,price,quantity))


	s = Store(item_list)
	
	num = int(input("enter number of values to be added"))

	for j in range(num):
		nam = input("enter name")
		q = int(input("enter quantity"))
		inp[nam]=q


	result = s.generate_bill(inp)

	print (result)







	
