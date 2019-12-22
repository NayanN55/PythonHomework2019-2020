def has22(x):
  for i in x:
    if i == 2:
      if x[x.index(i)+1]==2:
        return True
  return False
print(has22([1, 2, 2]))