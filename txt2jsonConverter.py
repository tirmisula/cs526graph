import json
import numpy as np

nodeList = []
linkStrList = ''
url = 'BerkStanf_4096_8192.txt'
with open(url,'r') as f:
    tmp = f.read()
    tmp_ = tmp.replace('\n',' ')
    tmp__ = tmp_.split(' ')
    tmp__ = list(map(int, tmp__))
    nodeList = np.unique(tmp__)
def genNodes():
    nodeStrList = ''
    for i in nodeList:
        nodeStr = '{\"id\":\"' + str(i) + '\", \"group\":1}'
        nodeStrList = nodeStrList + ',' + nodeStr
    return nodeStrList
nodeStrList = genNodes().lstrip(',')
with open(url,'r') as f:
    tmp = f.readlines()
    for i in tmp:
        i = i.replace('\n','')
        i = i.split(' ')
        linkStrList = linkStrList + ',' + '{\"source\": \"' + i[0] + '\", \"target\": \"' + i[1] + '\", \"value\": 1}'
linkStrList = linkStrList.lstrip(',')
jsonStrFile = ''
jsonStrFile = '{\"nodes\":[' + nodeStrList + '],\"links\":[' + linkStrList + ']}'
with open(url+'graphFile.json','w') as f:
    f.write(jsonStrFile)
print(tmp__)