#HW
#Easy A
# class University:
#     def __init__(self, off_name, location):
#         self.off_name = off_name
#         self.location = location

# class Student(University):
#     def __init__(self, full_name, speciality, off_name, location):
#         super().__init__(off_name, location)
#         self.full_name = full_name
#         self.speciality = speciality

# class Professor(University):
#     def __init__(self, full_name, subject, off_name, location):
#         super().__init__(off_name, location)
#         self.full_name = full_name
#         self.subject = subject

# my_university = University("NU", "Astana")

# my_student = Student("Kasymov Kasym Kasymovich", "Civil Engineering", "NU", "Astana")
# my_professor = Professor("Ermekov Ermek Ermekovich", "Computer Science", "NU", "Astana")

# print(my_university.off_name, my_university.location)

# print(my_student.full_name, my_student.speciality, my_student.off_name, my_student.location)

# print(my_professor.full_name, my_professor.subject, my_professor.off_name, my_professor.location)

#Medium A
# class Table:
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
    
#     def surface_area(self):
#         return self.length * self.width
    
# class DeskTable(Table):
#     def __init__(self, length, width, height):
#         super().__init__(length, width, height)
    
#     def surface_area(self):
#         return super().surface_area()

# my_desk = DeskTable(0.8, 0.6, 0.7)

# print(my_desk.surface_area())

#Hard A
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def square(self):
        return self.length * self.width


class DeskTable(Table):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)


class ComputerTable(DeskTable):
    def __init__(self, length, width, height, monitor_length, monitor_width):
        super().__init__(length, width, height)
        self.monitor_length = monitor_length
        self.monitor_width = monitor_width

    def square(self):
        surface_area = super().square()
        monitor_area = self.monitor_length * self.monitor_width
        return surface_area - monitor_area

dt = DeskTable(0.8, 0.6, 0.7)
ct = ComputerTable(0.8, 0.6, 0.7, 0.3, 0.1)
print(dt.square())
print(ct.square())

