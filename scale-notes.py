keys = ["a","a#","b","c","c#","d","d#","e","f","f#","g","g#"]
major = [2,2,1,2,2,2,1]
natrualMinor = [2,1,2,2,1,2,2]
minor = natrualMinor
harmonicMinor = [2,1,2,2,1,3,1]

class Scale:
    def __init__(self,key,name,keys):
        self.key = key
        self.name = name
        self.keys = keys
    def printSelf(self):
        print(self.key,self.name," : ",self.keys)

def getScaleNotes(key,scale):
    keyPos = keys.index(key)
    scaleNotes = [key]
    pointer = keyPos
    for instruction in scale:
        pointer += instruction
        if(pointer >= len(keys)):
            pointer -= len(keys)
        scaleNotes.append(keys[pointer])
    return scaleNotes

def printScale(key,scale):
    for note in getScaleNotes("b",major):
        print(note)
    print("====")

def getScale(knownNotes):
    allScales = []
    for key in keys:
        allScales.append(Scale(key,"minor",getScaleNotes(key,minor)))
        allScales.append(Scale(key,"major",getScaleNotes(key,major)))

    possibleScales = []

    for scale in allScales:
        possible = True
        for key in knownNotes:
            if(key not in scale.keys):
                possible = False
                break
        if(possible): possibleScales.append(scale)
    
    return possibleScales

notes = input("Enter known notes, seperated by comma: ")

for scale in getScale(notes.split(",")):
    scale.printSelf()
