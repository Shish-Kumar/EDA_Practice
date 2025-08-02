class Calculator:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def add(self):
        return(self.a+self.b)

    def sub(self):
        values = self.add()
        print('Addition',values)
        return(self.a-self.b)
    
SUB = Calculator(100,200).sub()
print('sub',SUB)