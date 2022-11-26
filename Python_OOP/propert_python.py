class Student:

    def __init__(self, student_id, student_name):
        self._student_id= student_id
        self._student_name = student_name

    #getter for student_id
    def get_student_id(self):
        return self._student_id
    #setter for student_id
    def set_student_id(self, id):
        if isinstance(id, int) and id > 0:
            self._student_id = id
        else:
            print("ENter the valid Id")

    #getter for student_name
    def get_student_name(self):
        return self._student_name
    #setter for studen_name
    def set_student_name(self, name):
        if isinstance(name, str):
            self._student_name = name
        else:
            print("Please enter the valid name")

    #property
    student_id = property(get_student_id, set_student_id)
    student_name = property(get_student_name, set_student_name)

std_one = Student(1,"John")
print(std_one.student_id)
print(std_one.get_student_name())

std_one.set_student_name("Alex")
print(std_one.get_student_name())
    