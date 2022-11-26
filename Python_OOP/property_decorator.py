class Student:

    #init method
    def __init__(self, student_id, student_name):
        self._student_id = student_id
        self._student_name = student_name

    #property decorator
    @property
    def student_id(self):
        return self._student_id

    #setter decorator
    @student_id.setter
    def set_studen_id(self, id):
        if isinstance(id, int) and id > 0:
            self._student_id = id

    #property decorator
    @property
    def student_name(self):
        return self._student_name


student_one = Student(1,"John")
print(student_one.student_id)
print(student_one.student_name)