class Employee:
	def __init__ (self,no,name,leaves):
		self.empno = no
		self.empname = name
		self.leaves = leaves


class Company:
	
	def __init__ (self,name,emp):
		self.cname = name
		self.emps = emp

	def display_leave(self,enum,ltype):
		for emp in self.emps:
			if emp.empno == enum:
				
				for lt,nl in emp.leaves.items():
					if lt == ltype:
						
						print (emp.leaves[lt])


	def leave_application(self,enum,ltype,nday):
		for emp in self.emps:
			if emp.empno == enum:
				for lt,nl in emp.leaves.items():
					if lt == ltype:
						if nday >= emp.leaves[lt]:
							return "Granted"
						else:
							return "Rejected"
	

if __name__ == '__main__':
	n = int(input("Enter number of employee objects"))

	leave = {}

	empl = []

	for i in range(n):

		num = int(input("enter employee number"))
		name = input("enter name")
	
		leave['CL'] = int(input("enter CL"))
		leave['EL'] = int(input("enter EL"))
		leave['SL'] = int(input("enter SL"))
		empl.append(Employee(num,name,leave))

	c = Company("Job Portal",empl)	
	

	search_enum = int(input("Enter search e num"))
	search_type = input("enter search type")
	search_ndays = int(input("enter leave days"))

	c.display_leave(search_enum,search_type)
	message=c.leave_application(search_enum,search_type,search_ndays)

	print (message)





		
		
		


	
	
