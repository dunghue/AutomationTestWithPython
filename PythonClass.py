class Employee:
    def __init__ (self,id_num, name, age, address, salary):
        self.id_num = id_num
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def validation(self):
        if (str(self.id_num) == "123" and self.name == "John"):
            print("This is Jonh and his age is", self.age,
            ",his address is", self.address,
            "and this salary is", self.salary)
        
        else:
            print("Not John")
            
e = Employee(123,"John",25,"Texas",1000)
e.validation()
    
        
            

            