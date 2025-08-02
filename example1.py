"""
Change 1 : Create a class

Change 2 : write self in each function inside the brackets
            note : sefl is note an argument 
            sub and add has only two arguments that is a,b

Change 3 : class the class first the using class call the functions

"""
class Math_Func:
    def add(self,a,b):
        return (a+b)

    def sub(self,a,b):
        return(a-b)

obj = Math_Func()
addition = obj.add(10,20)
substraction = obj.sub(20,30)
print('The addition is :',addition)
print('The Substraction :',substraction)



"""
we call run the code in this way also 

"""
addition = Math_Func().add(10,20)
substraction = Math_Func().sub(20,30)
print('The addition is :',addition)
print('The Substraction :',substraction)



-- modification for git hub 