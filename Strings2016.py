input = open("Stringstxt")#input
inpu = input.read()
inpu= inpu.split("\n")
inpu1=inpu[0]
inpu.remove(inpu1)
for i in inpu:
    inp=i.split(", ")
    x=int(inp[0])
    y=int(inp[1])
    print(inpu1[x:y])
