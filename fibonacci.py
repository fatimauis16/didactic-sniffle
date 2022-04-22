a=int(input('enter the number'))
num1=0
num2=1
count=0
if a<=0:
    print('enter positive number')
elif a==1:
    print(a)
    print(num1)
else:
    while count<a:
        print(num1)
        num=num1+num2
        num1=num2
        num2=num
        count+=1
