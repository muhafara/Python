class Employee:

    #class constructor with non-public instance
    def __init__(self,emp_id, emp_name):
        self._emp_id = emp_id
        self._emp_name = emp_name

    #getter for emp_id
    def get_emp_id(self):
        return self._emp_id
    
    #getter for emp_name
    def get_emp_name(self):
        return self._emp_name

    #setter for emp_id    
    def set_emp_id(self, id):
        if isinstance(id, int) and id > 0:
            self.emp_id = id
        else:
            print("Employee id should be greator then zero and positive integer")

    #setter for emp_name
    def set_emp_name(self, name):
        if isinstance(name,str) and name.isalpha():
            self._emp_name = name
        else:
            print("Name should be a string")

#first employee object
emp_one = Employee(1, "John Smith")
print("First Employee Information")
print("Employee id :", emp_one.get_emp_id(),"\nEmployee name :",emp_one.get_emp_name())
#second employee object
emp_two = Employee(2, "Alexander N")
print("Second Employee Information")
print("Employee id :", emp_two.get_emp_id(),"\nEmployee name :",emp_two.get_emp_name())
