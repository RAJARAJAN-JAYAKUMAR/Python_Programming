class calc:
  detail = 'its a calculator'
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def add(self):
    return self.a+self.b
    
  @staticmethod  
  def help(): #here i didn't pass any argument
    return "this class acts as a calculator"

  @classmethod
  def classmethod(calc,q,w):
    return q+w

print(calc.help()) #calling static method

obj = calc(10,20) #calling instance method
print(obj.add()) 

print(calc.classmethod(10,20)) #calling class method
