class Calculator1:
        
    def add(self,a,b):
        return(a+b)

    def sub(self,a,b):
        return(a-b)
    
class Calculator2:
    def mul(self,a,b):
        return(a*b)

    def div(self,a,b):
        return(a/b)

obj1 = Calculator1()

obj2 = Calculator2()

ADD = obj1.add(100,200)
SUB = obj1.sub(100,200)
print(ADD,SUB)

MUL = obj2.mul(110,200)
DIV = obj2.div(100,200)

print(MUL,DIV)