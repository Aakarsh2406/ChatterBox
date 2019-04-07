a=int(input('temp'))
def fa(t):
    assert t<40,'temp is high'
    return(t-32)*(5/9)
cel=fa(a)
print(cel)

print('value after change=',cel+32)
print('after',cel-43)
