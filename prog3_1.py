def score(x,y):
    m=0
    xo=''
    yo=''
    for i in range(min(len(x),len(y))):
        if x[i]==y[i]:
            m=m+1
            xo=xo+x[i]
            yo=yo+y[i]
        else:
            xo=xo+x[i].upper()
            yo=yo+y[i].upper()
    n=max(len(x),len(y))-m
    for i in range(min(len(x),len(y)),max(len(x),len(y))):
        if len(x)>len(y):
            xo=xo+x[i].upper()
            yo=yo+'-'
        else:
            xo=xo+'-'
            yo=yo+y[i].upper()
    print('Matches: {0} Mismatches: {1}'.format(m,n))
    print(xo)
    print(yo)
    print()
    del xo
    del yo
def add(d):
    a=input('Work on which string (1 or 2): ')
    b=input('Before what index: ')
    a=int(a)
    b=int(b)
    temp=d[a]
    temp1=''
    temp1=temp[:b]+'-'+temp[b:]
    d[a]=temp1
def minus(d):
    a=input('Work on which string (1 or 2): ')
    b=input('Delete what index: ')
    a=int(a)
    b=int(b)
    temp=d[a]
    temp1=temp[:b]+temp[b+1:]
    d[a]=temp1
x=input('String 1: ')
y=input('String 2: ')
while True:
    a=input("""What do you want to do:
			        a (add indel)
			        d (delete indel)
	    		        s (score)
			        q (quit) : """)
    if a=='q':
        break
    elif a=='a':
        d={1:x,2:y}
        add(d)
        x=d[1]
        y=d[2]
    elif a=='d':
        d={1:x,2:y}
        minus(d)
        x=d[1]
        y=d[2]
    elif a=='s':
        score(x,y)


