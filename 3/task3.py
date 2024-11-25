badname=str(input())
a=[0]*len(badname)
for i in range(len(badname)):
    if badname[i]=="a":
        a[i]=1
    elif badname[i]=="b":
        a[i]=2
    elif badname[i]=="c":
        a[i]=3
    elif badname[i]=="d":
        a[i]=4
    elif badname[i]=="e":
        a[i]=5
    elif badname[i]=="f":
        a[i]=6
    elif badname[i]=="g":
        a[i]=7
    elif badname[i]=="h":
        a[i]=8
    elif badname[i]=="i":
        a[i]=9
    elif badname[i]=="j":
        a[i]=10
    elif badname[i]=="k":
        a[i]=11
    elif badname[i]=="l":
        a[i]=12
    elif badname[i]=="m":
        a[i]=13
    elif badname[i]=="n":
        a[i]=14
    elif badname[i]=="o":
        a[i]=15
    elif badname[i]=="p":
        a[i]=16
    elif badname[i]=="q":
        a[i]=17
    elif badname[i]=="r":
        a[i]=18
    elif badname[i]=="s":
        a[i]=19
    elif badname[i]=="t":
        a[i]=20
    elif badname[i]=="u":
        a[i]=21
    elif badname[i]=="v":
        a[i]=22
    elif badname[i]=="w":
        a[i]=23
    elif badname[i]=="x":
        a[i]=24
    elif badname[i]=="y":
        a[i]=25
    elif badname[i]=="z":
        a[i]=26
badi=-1
badj=-1
mini = 0
minj = 0
min = a[0]
maybe=[]
# print(a)
def f(a):
    for i in range(0, len(a)):
        mini=0
        min = a[i]

        for j in range (i+1,len(a)):
            # print(i,j,mini,min,a[j])
            if a[i]>a[j]:
                if mini==0 or(mini!=0 and min>=a[j]):
                    min = a[j]
                    mini = j
                # badi=i
                # badj=j

                # q = a[badi]
                # a[badi] = a[badj]
                # a[badj] = q
                # maybe.append(a)
        if mini!=0:
            a[mini]=a[i]
            a[i]=min
            return


f(a)
goodname=["a"]*len(badname)
for i in range(len(badname)):
    if a[i]==1:
        goodname[i]="a"
    elif a[i]==2:
        goodname[i]="b"
    elif a[i]==3:
        goodname[i]="c"
    elif a[i]==4:
        goodname[i]="d"
    elif a[i]==5:
        goodname[i]="e"
    elif a[i]==6:
        goodname[i]="f"
    elif a[i]==7:
        goodname[i]="g"
    elif a[i]==8:
        goodname[i]="h"
    elif a[i]==9:
        goodname[i]="i"
    elif a[i]==10:
        goodname[i]="j"
    elif a[i]==11:
        goodname[i]="k"
    elif a[i]==12:
        goodname[i]="l"
    elif a[i]==13:
        goodname[i]="m"
    elif a[i]==14:
        goodname[i]="n"
    elif a[i]==15:
        goodname[i]="o"
    elif a[i]==16:
        goodname[i]="p"
    elif a[i]==17:
        goodname[i]="q"
    elif a[i]==18:
        goodname[i]="r"
    elif a[i]==19:
        goodname[i]="s"
    elif a[i]==20:
        goodname[i]="t"
    elif a[i]==21:
        goodname[i]="u"
    elif a[i]==22:
        goodname[i]="v"
    elif a[i]==23:
        goodname[i]="w"
    elif a[i]==24:
        goodname[i]="x"
    elif a[i]==25:
        goodname[i]="y"
    elif a[i]==26:
        goodname[i]="z"
print("".join(goodname))