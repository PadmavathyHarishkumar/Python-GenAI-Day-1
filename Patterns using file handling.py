access_file = 'Patterns using file handling.txt'
def patterns(access_file):
    f = open(access_file,'w')
    f.write('Left angle triangle\n--------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write(' ' ' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Right angle triangle\n--------------------\n')
    f = open(access_file,'a')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write('' '')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Pyramid pattern\n---------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write('' ' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Inverse Pyramid pattern\n----------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write('' ' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Inverse Left angle triangle\n----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write(' ' ' ')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Inverse Right angle triangle\n----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
            f.write('' '')
        for k in range(0,i):
            f.write(str(i))
            f.write(' ')
        f.write('\n')
    f.write('Star pattern\n------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write('' ' ')
        for k in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.write('Diamond pattern\n---------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
            f.write('' ' ')
        for k in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    for i in range(4,0,-1):
        for j in range(5,i,-1):
            f.write('' ' ')
        for k in range(0,i):
            f.write('*')
            f.write(' ')
        f.write('\n')
    f.close()
def display_patterns(access_file):
    f = open(access_file,'r')
    for i in f.readlines():
        print(i)

if __name__=='__main__':
    patterns(access_file)
    display_patterns(access_file)
