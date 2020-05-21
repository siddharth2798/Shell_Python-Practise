class Employee:

	def __init__ (self,eid,name,role,salary):
		self.emp_id = eid
		self.emp_name = name
		self.emp_role = role
		self.emp_salary = salary

	def increase_salary (self, percentage):
		self.emp_salary += (percentage/100) * self.emp_salary
		return self.emp_salary
		
class Organisation:
	def __init__ (self, name, elist):
		self.org_name = name
		self.emp_list = elist 
	
	def calculate_increment(self,erole,inc):
		nlist = []
		for emp in self.emp_list:
			if emp.emp_role == erole:

				increment = emp.increase_salary(inc)
				nlist.append(emp)
		return nlist

if __name__ == '__main__':
	n = int(input("Enter number of objects\n"))
	emplist = []
	result = []
	for i in range (0,n):
		emp_id = int(input("Enter employee id\n"))
		emp_name = input("Enter employee name\n")
		emp_role = input("Enter employee role\n")
		emp_salary = int(input("Enter employee salary\n"))
		
		emplist.append(Employee(emp_id,emp_name,emp_role,emp_salary))
	search_role = input("Enter the role to search \n")
	inc_per = int(input("enter the percentage to inc\n"))
	
	o = Organisation("JobPortal",emplist)
	
	result = o.calculate_increment(search_role,inc_per)
	for emp in result:
		print(emp.emp_name,end=" ")
		print(emp.emp_salary)
	
	
	
	
	


				
				
		
		
