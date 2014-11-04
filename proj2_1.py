print ('='*27,'RESTART','='*27)
print ("Guess a six-digit number SLAYER so that following equation is true, where each letter stands for the digit in the position shown:")
print()
print('SLAYER + SLAYER + SLAYER = LAYERS')

def breaks(a):
    x=list();
    for i in range(6):
        x.append(a//(10**(5-i)))
        a=a-x[i]*(10**(5-i))
    return x



for i in range(100000,333333):     
    x=breaks(i)
    y=breaks(3*i)
    z=x[1:]
    z.append(x[0])
    if y==z:
        print(i)
    


    


