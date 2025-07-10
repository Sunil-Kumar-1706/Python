'''
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.
'''

class note:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    def display(self):
        print(f"{self.title} = {self.content}")

note1=note("Tamil Movies","Leo,Master")
note2=note("Telugu Movies","RRR")

note1.display()
note2.display()
        