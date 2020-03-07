import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
t=float(b*b-4*a*c)
if a==0:
    if b==1:
        print("equation:X+%d=0" %(c))
    else:
        print("equation:%dX+%d=0" %(b,c))
else:
    if a==1:
        print("equation:X²+%dX+%d=0" %(b,c))
    else:
        print("equation:%dX²+%dX+%d=0" %(a,b,c))
if a==0:
    print("%.2f" %(-c/b))
elif t < 0:
    print("无解")
elif t==0:
    x=float(-b/(2*a))
    print("%.2f" % x)
else:
    t1=float(math.sqrt(t))
    x1=float((-b+t1)/(2*a))
    x2=float((-b-t1)/(2*a))
    print("x1=%.2f" % x1)
    print("x2=%.2f" % x2)