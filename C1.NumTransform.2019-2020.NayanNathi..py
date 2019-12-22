# Name: Nayan Nathi
# Grade: 8th
# Division: Junior-5 (Python)
# Contest1 Year: 2019-2020
# Team: Herndon Test Prep
# Program:Junior Division: Number Tranformation

#Data collection
input = open("numtranstesttxt")#input
inpu = input.read()
inpu= inpu.split("\n")
one=inpu[0]
two=inpu[1]
three=inpu[2]
four=inpu[3]
five=inpu[4]

#End of data collection

def numtrans(x):
    a=x.split(" ")
    n = a[0]
    p = int(a[1])
    d = int(a[2])

    num=int(n[len(n)-p])
    inspot=len(str(n))-p  #location of changing num

    if num<=4:
        c=str(d+num)  #d+loctoin number
        b=c[len(c)-1]
        return(str(n).replace(n[inspot:],str(b)+"0"*(p-1))) #output
    elif num>=5:
        c=str(abs(d-num))   #d+locotion Number
        b=c[0]             #first digit
        return(str(n).replace(n[inspot:],str(b)+"0"*(p-1))) #output

print(numtrans(one))
print(numtrans(two))
print(numtrans(three))
print(numtrans(four))
print(numtrans(five))