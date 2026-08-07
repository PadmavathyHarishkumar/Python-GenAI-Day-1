#Functions:-
#---------
#Functions are organized set of meaningful instructions used to do a specific task whenever the function gets called
#Functions are reusable code template
#Functions are reusable code instructions template
#Functions are named code containers
#Functions are sub routine
#Functions are code container modules

#Function components:-
#--------------------
#Parameter =====> Place holder(promoted variable)
#Arguments =====> value given by user during runtime

def add(a,b):
    print(a+b)

add(60,30)
print()
add(540,650)
print()
#Here (a,b) are paramaetrs and (60,30) are arguments

#Types of functions:-
#--------------------
#1.) User defined function(customized function)
#2.) Math function
#3.) Builtin function
#4.) Recursive function
#5.) Lambda function(anonymous function)

#User defined fuction:
#---------------------
#A function where the paramaters and arguments are defined by the user is called as user defined function(UDF)

def bike(brand,model,price):
    print(f'bike brand is {brand} model is {model} price is {price}')
bike('honda','xblade',110000)
print()
#Patterns using UDF:-
#--------------------
while True:
    name = input('enter name:')

    def namerat():
        for i in range(len(name)):
            for j in range(len(name),i-1):
                print(' ',end=' ')
            for k in range(0,i+1):
                print(name[i],end=' ')
            print()


    def invnamerat():
        for i in range(len(name),0,-1):
            for j in range(len(name),i-1):
                print(' ',end=' ')
            for k in range(0,i):
                print(name[i-1],end=' ')
            print()

    def pyramid():
        for i in range(len(name)):
            for j in range(len(name),i,-1):
                print('',end=' ')
            for k in range(0,i+1):
                print(name[i],end=' ')
            print()
    def invpyramid():
        for i in range(len(name),0,-1):
            for j in range(len(name),i,-1):
                print('',end=' ')
            for k in range(0,i):
                print(name[i-1],end=' ')
            print()

    def diamond():
        for i in range(len(name)):
            for j in range(len(name),i+1,-1):
                print('',end=' ')
            for k in range(0,i+1):
                print(name[i],end=' ')
            print()

        for i in range(len(name)-1,0,-1):
            for j in range(len(name),i,-1):
                print('',end=' ')
            for k in range(0,i):
                print(name[i-1],end=' ')
            print()

    def namelat():
        for i in range(len(name)):
            for j in range(len(name)-1,i,-1):
                print(' ',end=' ')
            for k in range(0,i+1):
                print(name[i],end=' ')
            print()

    def invnamelat():
        for i in range(len(name),0,-1):
            for j in range(len(name),i,-1):
                print(' ',end=' ')
            for k in range(0,i):
                print(name[i-1],end=' ')
            print()

        print('available choices')
    print('-----------------')
    print('1. namerat')
    print('2. invnamerat')
    print('3. pyramid')
    print('4. invpyramid')
    print('5. diamond')
    print('6. namelat')
    print('7. invnamelat')
    choice = int(input('enter your choice:'))

    if choice==1:
        namerat()
    elif choice==2:
        invnamerat()
    elif choice==3:
        pyramid()
    elif choice==4:
        invpyramid()
    elif choice==5:
        diamond()
    elif choice==6:
        namelat()
    elif choice==7:
        invnamelat()
    else:
        print('enter valid choice:')
