n=int(raw_input())
a=raw_input()
mas=[]
mas=a.split()
count=0
for i in range(0,n):
    if int(mas[i])%2!=0:
    	count+=1
print count




