'''To find power of a number 
And to find last digit of the result'''
a=int(input('enter a value '))
b=int(input('enter b value '))
c=a**b
print('%d**%d is %d' %(a,b,c))
last_digit=(c%10)
print('last digit is %d' %(last_digit))

'''Expected output:
enter a value 54
enter b value 3
54**3 is 157464
last digit is 4

'''
