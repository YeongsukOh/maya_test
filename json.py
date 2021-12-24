# json

dictData = {'A':123, 'B':456}
dictData['A']

import json
import os

json.dumps({'A': 345, 'B':678})

json.dumps({'A': 587, 'B':678}, sort_keys = True, indent=4)

jsonData = json.dumps({'A': 587, 'B':678}, sort_keys = True, indent=4)

#it is impossible
jsonData['A']

readJsonData = json.loads(jsonData)
readJsonData.keys()
readJsonData['A']
readJsonData.values()
readJsonData.items()

### FILE I/O

filePath = r'C:\Users\Designer\Dropbox\³» PC (Designer-PC)\Desktop\maya_test'
newP = filePath + '\\' + 'fileIO'
fileName = 'json_test.json'
newF = newP + '\\' + fileName
os.path.exists(newP) # True

jsonDatas = json.dumps({'A': 587, 'B':678}, sort_keys = True, indent=4)

jsonTest = open(newF, 'w')
jsonTest.write(jsonDatas)
jsonTest.close()

os.path.exists(newF) # True

if os.path.exists(newF):
    jsonDataRead = open(newF, 'r').read()
    jsonDataConverted = json.loads(jsonDataRead)
else:
    pass

jsonDataConverted['A']
keys = jsonDataConverted.keys()
vals = jsonDataConverted.values()
items = jsonDataConverted.items()