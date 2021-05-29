#finding factors of a number
n=int(input('enter number: '))
i=1
print('factors of %d are : '%n)
while i<=n:
    if n%i==0:
        print(i,end="   ")
    i+=1


'''
expected output
enter number: 10
factors of 10 are : 
1   2   5   10
'''
