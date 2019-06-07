num1,num2=map(int,input().split())
l1=list(map(int,input().split()))
for i1 in range(num2):
	u1,v1=map(int,input().split())
	num3=l1[u1-1:v1]
	num1=num3[0]
	for j in range(1,len(num3)):
		num1=num1^num3[j]
	print(num1)
