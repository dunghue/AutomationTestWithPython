class Employee:
    def __init__ (self, c_id, c_name):
        self.c_id = c_id
        self.c_name = c_name
    def comp_info(self):
        print("The Comp id is", self.c_id)
        print("The compt name is", self.c_name)
        
class Tester(Employee):
    def __init__ (self,c_id,c_name,e_id,department):
        Employee.__init__(self,c_id, c_name)
        self.e_id = e_id
        self.department = department
    def tester_info(self):
        print("The tester's id is", self.e_id)
        print("The tester's department is", self.department)
        
e = Tester(12345,"Amazon",5,"QA Automation")
e.comp_info()
e.tester_info()