# class Stu:
#     def __init__(self,physics,mark1,chem,marks2,math,marks3):
#         self.physics=physics
#         self.marks1=mark1
#         self.chem=chem
#         self.marks2=marks2
#         self.math=math
#         self.marks3=marks3
    
    
#     def av(self):
#         avg=(self.marks1+self.marks2+self.marks3)/3
#         print(f"The total average you get is{avg}")
    

        
# s1=Stu("physics",23,"math",34,"chem",50)
# s1.av()
# # print(s1.get_descriptive_name())
# s1 = Stu("physics", 23, "chem", 34, "math", 50)
# s1.av()
# print(s1.get_descriptive_name())

        
class St:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def av(self):
        sum1=0
        for val in self.marks:
            sum1+=val
        av=sum1/3
        print(f"Your average marks is{av}")
s1=St("Dinesh",(34,42,500))
print(s1.name)
print(s1.marks)
s1.av()