import os
path = os.path.join("/home","hidhe","Documents","git","version 39","short_dx.txt")
infile = open(path, 'r')
d = {}

for x in infile:
    if len(x) < 5:
        continue
    code = x[0:5]
    while code[-1] == " ":
        code = code[:-1]
    k = code
    v = x[5:]
    d[k] = v.strip()
print d
