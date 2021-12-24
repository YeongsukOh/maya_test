# file I/O

import os
filePath = 'C:/Users/Designer/Dropbox/내 PC (Designer-PC)/Desktop/maya_test/test_scene.ma'

# or
# put 'r' for slash
filePath = r'C:\Users\Designer\Dropbox\내 PC (Designer-PC)\Desktop\maya_test\test_scene.ma'

os.path.exists(filePath)

# file location
dir = os.path.dirname(filePath)


newDir = r'C:\Users\Designer\Dropbox\내 PC (Designer-PC)\Desktop\maya_test\fileIO'

# create dir
try:
    os.mkdir(newDir)    
except:
    pass


fileNameNew = 'test_txt_file.txt'
newf = newDir + '\\' + fileNameNew

os.path.exists(newf)

# writing a file
fileName = open(newf, 'w')
fileName.write('This is the 1st line\n')
fileName.write('This is the 2nd line\n')
fileName.close()

fileName = open(newf, 'r')
firstLine = fileName.readline()
fileName.close()

print firstLine

fileName = open(newf, 'r')
allLines = fileName.read()
fileName.close()

print allLines

lines = allLines.split('\n')
print lines[0]
print lines[1]

mayaFile = r'C:\Users\Designer\Dropbox\내 PC (Designer-PC)\Desktop\maya_test\test_scene_1.ma'
os.path.exists(mayaFile)
file = open(mayaFile, 'r')
allLineRead = file.read()
file.close()

print allLineRead

lines = allLineRead.split('\n')

transfomrNode = []
for line in lines:
    if 'transform' in line:
        print line
        transfomrNode.append(line)
        
print transfomrNode[0]