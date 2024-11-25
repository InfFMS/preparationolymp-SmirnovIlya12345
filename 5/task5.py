from math import sqrt
from math import floor
nummatch=0
breakk=0
LIST=[0]*nummatch
for i in range(nummatch):
    list=[int(input()), int(input())]
    LIST[i]=list
print(LIST)
a=int(input())
print((floor((-1+sqrt(8*a+1))/2))+((a-(floor((-1+sqrt(8*a+1))/2)*floor((-1+sqrt(8*a+1))/2)+floor((-1+sqrt(8*a+1))/2))/2)/floor((1+sqrt(8*a+1))/2)))
