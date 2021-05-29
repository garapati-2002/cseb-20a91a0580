a=int(input('total bill amount: '))
if a in range(1000,2000) :
    dis=a*0.1
    print('discount :%.2f'%dis)
    paid=a-dis
    print('paid amount is:%d'%paid)
elif a in range(2000,3000) :
    dis=a*0.2
    print('discount :%.2f'%dis)
    paid=a-dis
    print('paid amount is:%d'%paid)
elif a in range(3000,5000) :
    dis=a*0.3
    print('discount :%.2f'%dis)
    paid=a-dis
    print('paid amount is:%d'%paid)
elif a > 5000 :
    dis=a*0.4
    print('discount :%.2f'%dis)
    paid=a-dis
    print('paid amount is:%d'%paid)
else :
    print('no discount')
    print('paid amount is:%d'%a)


'''
 expexted output
 total bill amount: 8000
discount :3200.00
paid amount is:4800
'''
    
