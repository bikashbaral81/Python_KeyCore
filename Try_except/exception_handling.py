try:
    num=int(input("enter the num:"))
    result=10/num

except ZeroDivisionError:
    print("canot divide by 0")

except ValueError:
    print("please enter number")

except Exception as e:
    print("")

else:
    print("\n result",result)

finally:
    print(" program has been complede!!")