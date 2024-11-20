a=int(input())
b=int(input())
if b%4==0:
    print(((a+2*b)//4)*((a+2*b+2)//4))
elif b%4==2:
    if a<2:
        print((b+2)*(b-2)//4)
    else:
        print(((a+2*b)//4)*((a+2*b+2)//4))
elif b%4==1:
    if a<2:
        print(((b-1)//2)*(b-1)//2)
    elif a<4:
        print(((b-1)//2)*(((b-1)//2)+2))
    else:
        print(((a+2*b)//4)*((a+2*b+2)//4))
else:
    if a<2:
        print(((b+1)//2)*(b-3)//2)
    elif a<4:
        print(((b+1)//2)*(b+1)//2)
    else:
        print(((a+2*b)//4)*((a+2*b+2)//4))