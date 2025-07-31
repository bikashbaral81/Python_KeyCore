


ui=input("enter the string:")
l=list(map(int,ui.split(",")))
print(l)
f=list(filter(lambda x:x%2==0,l))
print(f)
