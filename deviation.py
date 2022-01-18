import csv
import math
with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

squaredList=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredList.append(a)
sum=0
for number in squaredList:
    sum=sum+number

result=sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)