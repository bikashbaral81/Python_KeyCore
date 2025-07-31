


#  TUPLE

#n=int(input("Enter the number :"))
#t=tuple(range(1,n+1))
#print(t)
#print(t[0])
#mid=t[len(t)//2]
#print(mid)
#print(t[-1])


#t=()
#n=int(input("Enter the number:"))

#for i in range(1,n+1):
#    t.update(i)


#d={}
#n=int(input("enter the num:"))
#for i in range (1,n+1):
#    l=[]
#    for j in range (1,n+1):
#        l.append(i*j)
#    d[i]=l
#    print(d)



#def fun1(*args,**kwargs):
#    print(args,kwargs)
#     return *args,**kwargs
#print(fun1(1,2,3,4,5,1,a="apple",b="ball"))


#def fun(sum):
#    sum=0
#    n=int(input("Enter the number : "))
#    for i in range (1,n+1):
#        sum+=i
#    return sum
#print(fun(sum))


#def fun(*args):
#    s=0
#    for i in args:
#        s+=i
#    return s
#print(fun(1,2,3,4,5))


#def fun(a,b):
#    a={1:1,2:4}
#    b={}
#    for i in a:
#        b[a[i]]=i
#        b[3]=9
#    return b
#a={1:1,2:4}
#b={}
#print(fun(a,b))


#def fun(a,d=None):
#    if d is None: 
#        d={}
#    d[a]=a*a
#    return d
#a=3
#d={1:1,2:4}
#print(fun(a,d))


#def fun(**kwargs):
#    res={}
#    for key,value in kwargs.items():
#        if  isinstance (value,int) :
#            res[key]=value
#    return res
#print(fun(a=1,b="python",c=2,d=8))




#def fun(a,t=None):
#    if t is None:
#        t=[]
#    t.append(a)
#    return t
#a=3
#t=[1,2]
#print(fun(a,t))


#def fun(l1,l2):
#    d={}
#    for i in range (len(l1)):
#        d[l1[i]]=l2[i]
#    return d
#l1=["a","b"]
#l2=[1,2,3]
#print(fun(l1,l2))

#def fun(l1,l2):
#    d={}
#    for i in range (min(len(l1),len(l2))):
#        d[l1[i]]=l2[i]
#    return d
#l1=["a","b","c"]
#l2=[1,2]
#print(fun(l1,l2))


#DATE-04/06/2025

#def fun(item):
#    return item[0]
#e={"alice":87,"bob":92,"charlie":78,"david":95,"eva":88}
#si=sorted(e.items(),key=fun)
#print=(dict(si))


# MIN_PROJECT_01  
def stud_details():
    student={}
    studs=int(input("enter the number: "))
    for i in (1,studs+1):
        stud_name=input("enter thr name : ")
        stud_grade=int(input("enter the grade:"))

    student[stud_name]=stud_grade
    return stud_details

0
def cal_avg(student):
    t=student.values()
    avg=t/len(student)
    return avg 


def  stud_pass(student):
    l=[]
    for stud_name,stud_grade in student.items():
        if stud_grade>=50:
            l.append(stud_name)
    return l


def main():
    stud_details()
    cal_avg(student)
    stud_pass(student)
print(main())





