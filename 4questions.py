def shiftleft(x):
  y=x[0]
  x=x[1:]
  x.append(y)
  return x

print (shiftleft([6, 2, 5, 3]))

def lasttwo(x):
    y=x[len(x)-2]
    z=x[-1:]
    k=x[:-2]
    k= k+z+y
    return k

print(lasttwo("coding"))

def havethree(x):
    y=0
    if (len(x)>=5):
        for i in x:
            if i == 3:
                if not(x[x.index(i)+1]==3) and not(x[x.index(i)-1]==3):
                    y=y+1
            x.remove(i)
    if y==3:
        return True
    else:
        return False
print(havethree([3,5,3,5,3]))