import numpy as np
import math
import re
import matplotlib.pyplot as plt
import operator
from collections import Counter

nodeList = []
degreeList = []
url = 'Star wars_edges.txt'
with open(url,'r') as f:
    tmp = f.read()
    tmp_ = tmp.replace('\n',' ')
    tmp__ = tmp_.split(' ')
    tmp__ = list(map(int, tmp__))
    nodeList = np.unique(tmp__)
V = len(nodeList)
E = int(len(tmp__) / 2)
graphDensity = V*math.log2(V)
# E < VlogV
print('E:'+str(E)+'\n')
print('V:'+str(V)+'\n')
print('sparsity E < VlogV\n')
for i in nodeList:
    node = str(i)
    node_ = '\\b'+node+'\\b'
    pattern = re.compile(node_)
    degreeList.append(len(pattern.findall(tmp_)))
counts = Counter(degreeList)
counts_sorted = sorted(counts.items(), key=lambda kv: kv[0])
degreeX = list(dict(counts_sorted).keys())
degreeY = list(dict(counts_sorted).values())
plt.figure()
plt.plot(degreeX,degreeY)

print('test')
