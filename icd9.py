import os
path = os.path.join("/home","hidhe","Documents","git","version 39","short_dx.txt")
infile = open(path, 'r')
d = {}

for x in infile:
    if len(x) < 5:
        continue
    d[x[0:5].strip()] = x[5:].strip()
print d
