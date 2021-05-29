#prime number using while loop
n=int(input('enter number: '))
if n==1:
    print('1 is Not prime nor Composite number')
i=2
while i <= (n//2):
        if (n % i) == 0:
            print('Not a prime number')
            break
        else:
            print('Prime number')
            break


'''
expected output
enter number: 1
1 is Not prime nor Composite number
'''
