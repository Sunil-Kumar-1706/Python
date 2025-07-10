#Define a Student class where every student has the same school_name

class student:
    school_name="SSV"
    
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"{self.name}: {student.school_name}")

s1=student("SUNIL")
s2=student("AAKASH")

s1.display()
s2.display()