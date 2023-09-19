''' OOPS - Object Oriented Programming Structure
 class & objects
Pillars of oops
-> Encapsulation 
-> Abstraction   
-> Inheritance
-> Polymorphism

Encapsulation and abstraction used for security 
Inheritance and Polymorphism used for Code Shortening


'''

# class student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def func_2(self):
#         print(self.id)
#         print(self.name)
# class department(student):
#     def __init__(self,dept):
#         self.d = dept
#         print('dept', self.d)
# s = department(1,'sss')
# s.func_2()

class college():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def profile(self):
        print(self.name)
        print(self.name)
class university(college):
    def __init__(self, name):
        super().__init__(id, name)
        self.name = name
        print(self.name)
        print(self.id)

newobj = university("Rk college of engineering")
newobj.name()



