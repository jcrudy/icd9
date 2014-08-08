import os
from resources import resources
path = os.path.join(resources,'icd9','ICD-9-CM-v32-master-descriptions','CMS32_DESC_SHORT_DX.txt')
infile = open(path, 'r')

d = {}
for x in infile:
    if len(x) < 5:
        continue
    d[x[0:5].strip()] = x[5:].strip()
    
def is_valid(somecode):
    if somecode in d:
        return True
    else:
        return False

if __name__ == '__main__':
    print "Enter ICD-9 code:"
    testcode = raw_input()
    if is_valid(testcode):
        print "Valid code"
    else:
        print "Invalid code"