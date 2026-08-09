circle=[(2,8), (2, 7), (2, 9),(3, 5),(3,11), (4, 4), (5, 3), (7, 2), (8, 2),(11, 3),(12, 12), (11, 13), (8, 14), (7, 14), (5, 13), (4, 12),(12,4),(13,5),(14,7),(14,8),(14,9),(13,11),(9,2),(9,14)]
def circle_():
    for i in range(1,16):
        for j in range(1,16):
            if(i,j)in circle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
            

semi_circle =[(2,8), (2, 7), (2, 9),(3, 5),(3,11), (4, 4), (5, 3), (7, 2), (8, 2),(8, 14),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(7, 14), (5, 13), (4, 12)]
def semi_circle_():
    for i in range(1,9):
        for j in range(1,19):
            if(i,j)in semi_circle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

Oval=[(2,8), (2, 7), (2, 9),(3, 5),(3,11), (4, 4), (5, 3), (7, 2), (8, 2),(11, 3),(12, 12), (11, 13), (8, 14), (7, 14), (5, 13), (4, 12),(12,4),(13,5),(14,7),(14,8),(14,9),(13,11),(9,2),(9,14)]
def oval_():
    for i in range(1,16):
        for j in range(1,16):
            if(i,j)in Oval:
                print('*',end=' ')
            else:
                print('',end=' ')
        print()

Heart=[(1,4),(2,2),(1,3),(1,9),(1,5),(1,7),(1,8),(2,6),(3,2),(3,10),(2,10),(4,2),(4,10),(5,3),(5,9),(6,4),(6,8),(7,5),(7,7),(8,6)]
def heart_():
    for i in range(1,9):
        for j in range(1,19):
            if(i,j)in Heart:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

Rhombus=[(1,4),(2,3),(2,5),(3,2),(3,6),(4,1),(4,7),(5,2),(5,6),(6,3),(6,5),(7,4)]
def rhombus_():
    for i in range(1,8):
        for j in range(1,8):
            if(i,j)in Rhombus:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

Triangle=[(1,4),(2,3),(2,5),(3,2),(3,6),(4,1),(4,7),(4,2),(4,3),(4,4),(4,5),(4,6)]
def Triangle_():
    for i in range(1,5):
        for j in range(1,8):
            if(i,j)in Triangle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        
Square=[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,6),(3,1),(3,6),(4,1),(4,6),(5,1),(5,6),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]
def Square_():
    for i in range(1,7):
        for j in range(1,7):
            if(i,j)in Square:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

Rectangle=[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,1),(2,9),(3,1),(3,9),(4,1),(4,9),(5,1),(5,9),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9)]
def Rectangle_():
    for i in range(1,7):
        for j in range(1,10):
            if(i,j)in Rectangle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

Trapezium=[(1,6),(1,7),(1,8),(1,9),(2,5),(2,12),(3,4),(3,13),(4,3),(4,14),(5,2),(5,15),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9)]
def Trapezium_():
    for i in range(1,7):
        for j in range(1,16):
            if(i,j)in Trapezium:
                print('*',end=' ')
            else:
                print('',end=' ')
        print()
        
while True:
    print('enter available choices:')
    print('1.) Circle')
    print('2.) Semi_circle')
    print('3.) Oval')
    print('4.) Heart')
    print('5.) Rhombus')
    print('6.) Triangle')
    print('7.) Square')
    print('8.) Rectangle')
    print('9.) Trapezium')

    choice = int(input('enter your choice:'))
    if choice==1:
        circle_()
    elif choice==2:
        semi_circle_()
    elif choice==3:
        oval_()
    elif choice==4:
        heart_()
    elif choice==5:
        rhombus_()
    elif choice==6:
        Triangle_()
    elif choice==7:
        Square_()
    elif choice==8:
        Rectangle_()
    elif choice==9:
        Trapezium_()
    else:
        print('enter a valid choice')
