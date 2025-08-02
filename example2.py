class Calculator:
        
    def add(self,a,b):
        return(a+b)

    def sub(self,a,b):
        return(a-b)

    def mul(self,a,b):
        return(a*b)

    def div(self,a,b):
        return(a/b)

obj = Calculator()

ADD = obj.add(100,200)
SUB = obj.sub(100,200)
MUL = obj.mul(110,200)
DIV = obj.div(100,200)

print(ADD,SUB,MUL,DIV)