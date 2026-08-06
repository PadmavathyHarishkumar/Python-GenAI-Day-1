print('****** INVERSE LEFT ANGLE TRIANGLE ******')

print('-------- Row numbers inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

print('-------- Col numbers inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(k+1,end=' ')
    print()

print('-------- Star pattern inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print('*',end=' ')
        
    print()

print('-------- Uppercase row inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

print('-------- Uppercase col inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

print('-------- Lowercase row inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

print('-------- Lowercase col inverse LAT --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()

print('-------- Row names inverse LAT --------')

name='harish'
L=len(name)
for i in range(L,0,-1):
    for j in range(L,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()

print('-------- Col names inverse LAT --------')

name='harish'
L=len(name)
for i in range(L,0,-1):
    for j in range(L,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[k],end=' ')
    print()

print('************ INVERSE PYRAMID ************')

print('-------- Row numbers inverse Pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

print('-------- Col numbers inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(k+1,end=' ')
    print()

print('-------- Star pattern inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

print('-------- Uppercase row inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

print('-------- Uppercase col inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

print('-------- Lowercase row inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

print('-------- Lowercase col inverse pyramid --------')

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()
    
print('-------- Row names inverse pyramid --------')

name='harish'
L=len(name)
for i in range(L,0,-1):
    for j in range(L,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()

print('-------- Col names inverse pyramid --------')

name='harish'
L=len(name)
for i in range(L,0,-1):
    for j in range(L,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(name[k],end=' ')
    print()

print('************ PYRAMID ************')

print('-------- Row numbers Pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

print('-------- Col numbers pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(k+1,end=' ')
    print()

print('-------- Star pattern pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

print('-------- Uppercase row pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

print('-------- Uppercase col pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

print('-------- Lowercase row pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

print('--------Lowercase col pyramid--------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()
    
print('-------- Row names pyramid --------')

name='harish'
L=len(name)
for i in range(L):
    for j in range(L,i+1,-1):
        print('',end=' ')
    for k in range(0,i+1):
        print(name[i],end=' ')
    print()

print('-------- Col names pyramid --------')

name='harish'
L=len(name)
for i in range(L):
    for j in range(L,i+1,-1):
        print('',end=' ')
    for k in range(0,i+1):
        print(name[k],end=' ')
    print()

print('************ DIAMOND ************')

print('-------- Diamond row number pattern --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

for i in range(5-1,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

print('-------- Diamond col number pattern --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(k+1,end=' ')
    print()

for i in range(5-1,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(k+1,end=' ')
    print()

print('-------- Diamond star pattern --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print('*',end=' ')
    print()

print('-------- Uppercase diamond row pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+64),end=' ')
    print()

print('-------- Uppercase diamond col pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+65),end=' ')
    print()

print('-------- Lowercase diamond row pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(i+96),end=' ')
    print()

print('-------- Lowercase diamond col pyramid --------')

for i in range(6):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(chr(k+97),end=' ')
    print()

print('-------- Diamond row names pyramid --------')

name='harish'
L=len(name)
for i in range(L):
    for j in range(L,i+1,-1):
        print('',end=' ')
    for k in range(0,i+1):
        print(name[i],end=' ')
    print()

for i in range(L-1,0,-1):
    for j in range(L,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()

print('-------- Diamond col names pyramid --------')

name='harish'
L=len(name)
for i in range(L):
    for j in range(L,i+1,-1):
        print('',end=' ')
    for k in range(0,i+1):
        print(name[k],end=' ')
    print()

for i in range(L-1,0,-1):
    for j in range(L,i,-1):
        print('',end=' ')
    for k in range(0,i):
        print(name[k],end=' ')
    print()
