
class Employee:
    def __init__(self,name,eid,age,gender):
        self.name = name    
        self.eid = eid
        self.age = age
        self.gender = gender
        

class Organisation:
    def __init__ (self,name,olist):
        self.oname = name
        self.emp_list = olist


    def addEmployee(self,name,eid,age,gender):
        self.emp_list.append(Employee(name,eid,age,gender))

    def getEmployeeCount(self):
        return len(self.emp_list)

    def findEmployeeAge(self,fid):
        for emp in self.emp_list:
            if emp.eid == fid:
                return emp.age
            else:
                return -1

    def countEmployees(self,age):
        c=0
        for emp in self.emp_list:
            if emp.age >= age:
                c += 1
        
        return c

        

        

if __name__ == '__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name=input()
        id=int(input())
        age=int(input())
        gender=input()
        o.addEmployee(name,id,age,gender)

    id=int(input())
    age=int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))
