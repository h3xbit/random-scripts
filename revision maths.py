import math

def s(n,e): return math.pow(n,e)

def effort(e):
    efforts = []
    b = 0
    for n in range(1,10):
        a = s(n,e)
        b += a
    for n in range(1,10):
        a = s(n,e) #current exponetialed number      
        z = (a/b) #current total effort percentage
        efforts.append(z)
    return efforts
#n from 0 to max to for an exponatial sorting
#slice 132 days into 9 sections of exponential increase
#with a exponent of 0.5 (moderate curve) 
#slice(132,0.5)
def slice(n,p):
    y =0
    for e in effort(p):
        x = n * e 
        y+=x
        print(x)
    print(y)

#slice(192,1.25)
n = int(input("number to slice:") )
while True:
    print(slice(n,float(input("e: "))))