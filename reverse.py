#reverse of a number
n=int(input('enter number: '))
sum=0
temp=n
#stemp = 0
#n=temp
while n!=0:
    r=n%10
    sum = sum*10+r
    n//=10
print('reverse of %d is %d '%(temp,sum))

'''
expected output
enter number: 1234
reverse of 1234 is 4321
'''
