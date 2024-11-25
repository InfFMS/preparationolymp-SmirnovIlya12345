from math import sqrt
from math import floor
numtraps=int(input())
badlist=[0]*numtraps
for i in range(numtraps):
    badlist[i]=int(input())
list=[0]+sorted(badlist)
print(list)
print(list)
timelist=[0]*numtraps
for i in range(numtraps-1):
    t=0
    for j in range(numtraps-1):
        a=list[j+1]-list[j]
        t+=(floor((-1+sqrt(8*a+1))/2))+((a-(floor((-1+sqrt(8*a+1))/2)*floor((-1+sqrt(8*a+1))/2)+floor((-1+sqrt(8*a+1))/2))/2)/floor((1+sqrt(8*a+1))/2))
