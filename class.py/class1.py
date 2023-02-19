class Student:
    count=0
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
        Student.count+=1
    def full_space(self):
        return f"{self.name} {self.age} {self.course}" 
    @classmethod
    def count_instances(cls):
        return f'u have creat {Student.count} '  
    @classmethod
    def from_string(cls,x):
        a,b,c=x.split(',')
        return cls(a,b,c)   
print(Student.count_instances())             