import sys
f=open(sys.argv[1],'r')
words=f.read()
letter=[]
for i in range(26):
    letter.append(0)
for x in words:
    if x!=' ':
        x=x.lower()
        index=ord(x)-ord('a')
        letter[index]+=1
m=max(letter)
ind=letter.index(m)
d=ind-4
g=open(sys.argv[2],'w')
for i in words:
    if i==' ':
        g.write(' ')
    else:
        a=(ord(i)-d-ord('a'))%26+ord('a')
        g.write(chr(a))


