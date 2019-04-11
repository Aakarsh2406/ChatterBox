q=int(input('Enter the year'))
def is_leap(year):
    if year%4==0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else :
        return False
q=is_leap(q)
if q==True:
    print('You Entered a Leap Year::! congrats')
else :
    print('Sorry,Try again')

