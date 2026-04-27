class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0 #private variable

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks. Marks must be <=100.")

stu= Student("John")
stu.set_marks(90)
print(stu.get_marks())