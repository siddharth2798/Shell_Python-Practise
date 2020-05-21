class Account:
	def __init__(self,accno,accname,accbal):
		self.account_no = accno
		self.account_name = accname
		self.account_balance = accbal
	
	def depositAmnt(self,deptAmnt):
		self.account_balance += deptAmnt
		print ( self.account_balance)
	
	def withdrawAmnt(self, withAmnt):
		if ((self.account_balance - withAmnt) >= 1000):
			self.account_balance -= withAmnt
			print ( self.account_balance)
			return 1
		else:
			return 0

if __name__ == '__main__':
	no = int(input("Enter the acc number"))
	name = input("Enter the name")
	balance = int(input("Enter the balance"))
	
	a = Account(no,name,balance)

	depAm = int(input("Deposit amnt"))
	
	
	withAm = int(input("Withdraw amnt"))
	a.depositAmnt(depAm)
	b = a.withdrawAmnt(withAm)

	
	if b == 1:
		print ("pani nadannu")
	else:
		print("Pani paali")
	 

