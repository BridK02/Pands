import json
filename="testdict.json"
sample= dict(name='brid', age=43, grades=[90,74,89])

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

#test the function
writeDict(sample)
