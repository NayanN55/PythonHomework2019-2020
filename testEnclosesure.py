x="2-5*(6+1"
for i in x:
    if i=="(":
        x.replace((x[:(x.index("("))]),"")
    elif i==")":
        x.replace((x[(x.index("(")):]),"")
print(x)
