import math
inpu="3x**2+5x+2"
a=int(inpu[inpu.index("x**2")-1])
inpu.strip("x**2")
b=int(inpu[inpu.index("x")-1])
c=int(inpu[9])
print((-b+math.sqrt((b**2) - (4*a*c)))/(2*a))
print((-b-math.sqrt((b**2) - (4*a*c)))/(2*a))