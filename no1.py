def outerfun(a,b):
  square= a**2
  add= innerfun(a,b)
     return add + 5
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
result = outerfun(a,b)
print(result)
