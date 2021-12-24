import maya.cmds as cmds
import maya.mel as mel
import class_test as cl
reload(cl)

cal = cl.Calculator()
cal.add()

# to use partial, this step is necessary
from functools import partial

# partial / lambda

# without "*args" it can't use in command of UI
def cmdButtonPushGeneral(*args):
    print "general button was pushed"

# in this case, *args should be located in last.
def cmdButtonPushPartial(buttonName, *args):
    print "%s button was pushed"%buttonName

# in tems of lambda, it doesn't need to use "*args" 
def cmdButtonPushLambda(buttonName):
    print "%s button was pushed"%buttonName

# example of button

def loadUI():
    
    buttonNameP = 'partial'
    buttonNameL = 'lambda'
    
    # this is for partial to use val from class
    cal.valA = 10
    cal.valB = 23
        
    cmds.window(t = 'example', w = 150, h = 150)
    cmds.columnLayout(adj = True)
    cmds.button(l = 'general', c = cmdButtonPushGeneral)
    
    # this is different between partial and lambda
    cmds.button(l = 'partial', c = partial(cmdButtonPushPartial, buttonNameP))
    
    # in case of lambda, it doesn't need to "*args"
    cmds.button(l = 'lambda', c = lambda x:cmdButtonPushLambda(buttonNameL))
    cmds.button(l = 'partial_test', c = partial(cal.add))
    cmds.button(l = 'lambda_test', c = lambda x:cal.add(10,15))
    cmds.showWindow()
    
loadUI()