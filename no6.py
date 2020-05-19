def add(x,y):
  return(x+y)
def sub(x,y):
  return(x-y)
def mul(x,y):
  return(x*y)
def div(x,y):
  return(x/y)

print("1.Add, 2.Subtract,3.Multiply, 4.Division")
while(True):
 choice = input(" Enter Choice:1/2/3/4:")
 if choice in ('1','2','3','4'):
    n1= float(input("First no <=4:"))
    n2= float(input("Second no <=4:"))
    if choice == '1':
      print(n1,"+",n2,"=",add(n1,n2))
    elif choice == '2':
      print(n1,"-",n2,"=",sub(n1,n2))
    elif choice == '3':
      print(n1,"*",n2,"=",mul(n1,n2))
    elif choice == '4':
      print(n1,"/",n2,"=",div(n1,n2))
    break
 else:
     print("INVALID")
