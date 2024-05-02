class Employee:
    def __init__(self,name , last) -> None:
        self.name = name
        self.last = last


class Supervisor(Employee):
    def __init__(self, name, last , password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employee):
    def leave_request(self , day):
        return "May i Take a Leave for "+ str(day) + "days"


saqlain = Employee("saqlain" , "A" , )
abbass = Supervisor("abbass" , "A" , "bananan")
kiran = Chefs("kiran" , "k")


print(kiran.leave_request(2))
