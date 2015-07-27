import math

def round2(x):
    return int(x + math.copysign(0.5, x))

#n1 - no. of non recurring digits
#n2 - no. of recurring digits

def printRecurring2Fraction(x,n1,n2):
    m1 = math.pow(10,n1)
    m2 = math.pow(10,(n1+n2))
    a = x*m1
    b = x*m2
    z = b-a
    y = m2-m1
    z = round2(z)
    print(z,"\n---------\n",y)

def printRecurring2Fraction1line(x,n1,n2):
    print(round2(x*math.pow(10,(n1+n2))-x* math.pow(10,n1)),
          "\n-------\n",math.pow(10,(n1+n2))- math.pow(10,n1)) 

printRecurring2Fraction1line(0.29191,3,2)
