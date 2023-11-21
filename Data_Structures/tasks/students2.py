from toolbox.structure.linked_list import SLL, SNode


class Students(SLL):
    pass
    # def add_student(self, student):
    #     if type(student) is not Student:
    #         raise f"<{student}> is not Student"
    #     self.students.add_first(student)

    # def search(self, stu_code):
    #     for stu_node in self.students.traverse():
    #         if stu_code == stu_node.element.stu_code:
    #             return stu_node
    
    # def get_stu_gpa(self, stu_code):
    #     target = self.search(stu_code)
    #     if target is not None:
    #         return target.element.gpa()
    #     else:
    #         print(f"{stu_code} is not found")

class StuNode(SNode):
    def __init__(self, stu_code, name):
        self.stu_code = stu_code
        self.name = name
        self.lessons = None

class Lessons(SLL):
    def __init__(self):
        pass
    
# class Student:
#     def __init__(self, stu_code, name):
#         self.stu_code = stu_code
#         self.name = name
#         self.lessons = SLL()

#     def add_lesson(self, lesson):
#         if type(lesson) is not Lesson:
#             raise f"<{lesson} is not Lesson object>"
#         self.lessons.add_first(lesson)
        
#     def gpa(self):
#         sum = 0
#         units = 0
#         for node in self.lessons.traverse():
#             unit = node.element.unit
#             sum += node.element.grade * unit
#             units += unit
#         if units != 0:
#             return sum / units



class LesNode(SNode):
    def __init__(self, lesson_code):
        super().__init__(self, lesson_code)
        self.code = lesson_code
        self._unit = 0
        self._grade = 0
    
    @property
    def unit(self):
        return self._unit
    @unit.setter
    def unit(self, value):
        if type(value) == int:
            self._unit = value
        else:
            print(f"<{value}> is not integer")
            
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        try:
            if value > 20:
                raise Exception(value, "Bigger then 20")
        except TypeError as err:
            raise Exception(f"value: {value}", err)
        self._grade = value


# def test_students():
#     students = Students()
#     moeini = Student(4003111050, "mohammad moeini")
#     ds = Lesson(1214614)
#     ds.grade = 15
#     ds.unit = 3
#     dg2 = Lesson(1214229)
#     dg2.grade = 20
#     dg2.unit = 3
#     moeini.add_lesson(ds)
#     moeini.add_lesson(dg2)
#     students.add_student(moeini)
#     print(students.get_stu_gpa(400311105))
#     print(students.get_stu_gpa(4003111050))

