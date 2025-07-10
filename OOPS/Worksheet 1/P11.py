#Make a Person class and compute age

class person:
    def __init__(self,name,born,today):
        self.name,self.born,self.today=name,born,today

    def compute(self):
        x,y=int(self.today[6:]),int(self.born[6:])
        return x-y

s=person("SUNIL","17-06-2001","03-07-2025")
print(f"{s.name} is {s.compute()} Years Old")