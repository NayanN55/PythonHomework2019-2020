input = open("numtranstesttxt","r")#input
inpu= input.split("\n")
def Enclosesure(x):
    xcopy=x
    for i in x:
        if i == "(":
            x.replace((x[:(x.index("("))]), "")
        elif i == ")":
            x.replace((x[(x.index("(")):]), "")
    print(x)
print(inpu[range(0,5)])