example=("p","r","o","g","r","a","m")
x="a"
y="z"
if("a" in example):
    print(x,"is present")
else:
    print(x,"is not present")
if("z" in example):
    print(y,"is present")
else:
    print(y,"is not present")
del example
print("Tuple is deleted")