print('-------Row numbers left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

print('-------Col numbers left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print((k+1),end=' ')
    print()

print('-------Star pattern left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

print('-------Uppercase row left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

print('-------Uppercase col left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

print('-------Lowercase row left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

print('-------Lowercase col left angle triangle-------')

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()

print('-------Names row left angle triangle-------')

name='harish'
L=len(name)
for i in range(0,L):
    for j in range(L,i,-1):
        print(' ',end=' ')
    for k in range(0,i+1):
        print(name[i],end=' ')
    print()

print('-------Names col left angle triangle-------')

name='harish'
L=len(name)
for i in range(0,L):
    for j in range(L,i,-1):
        print(' ',end=' ')
    for k in range(0,i+1):
        print(name[k],end=' ')
    print()
