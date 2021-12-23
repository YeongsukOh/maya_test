import maya.cmds as cmds
import maya.mel as mel

class Calculator:
    
    def __init__(self):
        self.attrA = 'YEONGSUK'
        
    def add(self, a, b):
        print a + b
    
    def sub(self, a, b):
        print a - b
        
    def mul(self, a, b):
        print a * b
        
    def div(self, a, b):
        print a/b
        
cal = Calculator()

cal.mul(3,4)

cal.attrA