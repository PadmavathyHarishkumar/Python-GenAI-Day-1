print('------------Find Amicable numbers------------')
print()
num1=int(input('Enter your first number:'))
num2=int(input('Enter your Second number:'))

print()
sum1=0
sum2=0

for i in range(1,num1):
    if(num1%i==0):
        sum1+=i
for j in range(1,num2):
    if(num2%j==0):
        sum2+=j
if(sum1==num2)and (sum2==num1):
    print('The number is amicable')
    print()
else:
    print('The number is not amicable')
    print()

print('------------Factors of numbers------------')
print()
num=int(input('Enter your number:'))
print()
for i in range(1,num+1):
    if(num%i==0):
        print(i,end=' ')
print()
print()

print('------------Find Armstrong or not------------')
print()
num=int(input('Enter your number:'))
print()
n=num
digit_count=len(str(num))
addsum=0
while n>0:
    digit=n%10
    addsum+=pow(digit,digit_count)
    n//=10
if(addsum==num):
    print(addsum,('The number is armstrong'))
else:
    print(num,('Not an armstrong number'))
print()
print()

print('------------Find Prime or co-prime------------')
print()
num=int(input('Enter your number:'))
print()
if(num%1==0)and(num%num==0):
    print(num,'is an prime number')
else:
    print(num,'is not an prime number')
print()
