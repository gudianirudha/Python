start=[9,20,2,3,4]
end=[10,30,3,4,5]
n=len(start)
vect=[]
for i in range(n):
    vect.append([start[i],end[i]])
vect=sorted(vect,key=lambda x: (x[0]))
print(vect)
print("Time of workers' arrival")
for i in range(n):
    print(vect[i][0],vect[i][1])
ArrivalTime=8
time=vect[0][0]
i=0
ans=-1
print("For arrival at",ArrivalTime,"Need to wait")

while(ArrivalTime>time and i<n):
    i+=1
    time=vect[i][0]
if ArrivalTime>time:
    print(ans,'hours.')
elif vect[i-1][1]>ArrivalTime:
    print(0,'hours.')
else:
    print(time-ArrivalTime,'hours.')
