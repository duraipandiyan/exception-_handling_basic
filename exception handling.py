try:
    num=int(input("enter the limit:"))
    a=0
    b=1
    c=0
    for i in range(1,num+1):

        print(c)
        c=a+b
        a=b
        b=c
except NameError:
    print("woring input:")

except ValueError:
    print("valueError:")
except ZeroDivisionError:
    print('the user enter the zero ' )
else:
    print('the  program was run sucessfully:')
finally:
    print("work done")