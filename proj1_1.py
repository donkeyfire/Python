def con(a):
    b=10**((1.5*a)+4.8)
    c=b/4.184e9
    p=(b,c)
    return p
template="{0:10}{1:25}{2:25}"
head=('Ritcher','Joules','TNT')
print(template.format(*head))
ri=[1,5,9.1,9.2,9.5]
for r in ri:
    x=con(r)
    out=(str(r),str(x[0]),str(x[1]))
    print(template.format(*out))

while True:
    
    a=input('Please enter a Richter scale value: ')
    try:
        a=float(a)
    except ValueError: 
        print("number only!")
        continue  
    if a<0:
        print('positive only')
    else:
         break
    

print('Richter scale value:',a)
p=con(a)
print('Equivalence in joules:',p[0])

print('Equivalence in tons of TNT:',p[1])
