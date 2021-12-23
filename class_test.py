import maya.cmds as cmds
import maya.mel as mel

#global valuable
NAME_TOOL = 'CALCULATOR_VER_1_1'

class Calculator:
    
    def __init__(self):
        #local valuable
        self.nameValSum = 'SUM :'
        self.valA = 3
        self.valB = 5
  
    # added arguments
    def add(self, *args):
        
        valA = self.valA
        valB = self.valB
        
        if len(args) == 2:
            valA = args[0]
            valB = args[1]
        
        valF = valA + valB
        print NAME_TOOL
        return valF
    
    def sub(self, a, b):
        print a - b
        
    def mul(self, a, b):
        print a * b
        
    def div(self, a, b):
        print a/b
        
cal = Calculator()

# it can be changed to new val
cal.valA = 10
cal.valB

cal.add(5,30)
cal.add()

#python command only
round(2.12314123, 2)

# array + array
arrayA = [1,2,3]
arrayB = ['A','B','C']
arrayC = arrayA + arrayB

# reverse command
arrayC.reverse()
reversed.arrayC