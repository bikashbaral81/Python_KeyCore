

#l=[]
#n=input("enter the string:")
#j=list(map(int,n.split(",")))
#print(j)


n=input("Enter the string:")
j=list(map(lambda x:int(x)*x,n.split(",")))
print(j)