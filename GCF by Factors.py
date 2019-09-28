num1=int(input("enter 1st number "))
num2=int(input("enter 2nd number"))

factor1=[]
factor2=[]


for i in range(1,num1+1):
    if num1%i==0:
         factor1.append(i)

for j in range (1,num2+1):
    if num2%j==0:
        factor2.append(j)
result=set(factor1).intersection(factor2)
print(max(result))

