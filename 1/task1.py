from time import time
rows=int(input())
columns=int(input())
t1=time()
if rows<1 or columns<1 or rows*columns==1:
    print(0)
else:
    posrows=rows//2
    poscolumns=columns//2
    count=0
    for i in range(rows):
        if i==posrows:
            count+=columns-1
        else:
            for j in range(columns):
                if poscolumns==j or i-posrows==j-poscolumns or i-posrows==-j+poscolumns:
                    count+=1
    print(count)
t2=time()
