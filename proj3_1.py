while True:
    c=input('Customer Code ')
    if c=='Q' or c=='q':
        break
    elif c is not 'B' and c is not 'D' and c is not 'W': 
        print('error')
        continue
    n=input('number of days ')
    s=input('start reading ')
    e=input('end reading ')
    n=int(n)
    s=int(s)
    e=int(e)
    if e>s:
        d=e-s
        d=d/10
    else:
        d=999999-s+e+1
        d=d/10
    if c=='B':
        p=40*n+d*0.25
    elif c=='D':
        if d<100*n:
            df=0
        else:
            df=100*n-d
        p=60*n+df*0.25  
    elif c=='W':
        if d<n*900/7:
            p=190*n/7
        elif d>n*900/7 and d<n*1500/7:
            p=n*290/7
        elif d>n*1500/7:
            p=n*390/7+(d-1500*n/7)*0.25        
    
    print("Customer summary:")
    print(" "*10,"classification code:",c)
    print(" "*10,"rental period (days):",n)
    print(" "*10,"odometer reading at start:","{0}".format(s))
    print(" "*10,"odometer reading at end:","{0}".format(e))
    print(" "*10,"number of miles driven::","{0:.1f}".format(d))
    print(" "*10,"amount due: $ ","{0:.2f}".format(p))





