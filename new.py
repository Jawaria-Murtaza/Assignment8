hours=input('enter hours:')
rate=input('enter rate:')
try:
    hours=int(hours)
    rate=int(rate)
    pay=hours*rate
    print (pay)
except:
    rate=-1
    print ('Error,please enter numeric input')