Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Simple code for rules of class:
class Calci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def intdiv(self,a,b):
        return a//b

c=Calci()
c.add(50,30)
80
c.intdiv(50,30)
1
c.mul(50,30)
1500
c.sub(50,30)
20

#Scope of variables:
#1.Class variable
#2.Local variable
#3.Global variable
#4.Instance variable

#Class variable:
#A variable which is located inside the class and outside of all its methods is a class variable

class Loan:
    cv='Gold/House/Personal'
    def p1(self):
        print('p1 is eligible to get:-',Loan.cv)
    def p2(self):
        print('p2 is eligible to get:-',Loan.cv)
    def p3(self):
        print('p3 is eligible to get:-',Loan.cv)

l=Loan()
l.cv
'Gold/House/Personal'
l.p1()
p1 is eligible to get:- Gold/House/Personal
l.p2()
p2 is eligible to get:- Gold/House/Personal
l.p3()
p3 is eligible to get:- Gold/House/Personal

#Local variable:
#A variable which is located inside a method and can be accessed only by that method

class Loan:
    def p1(self):
        lv='Gold loan/House loan/Personal loan'
        print('p1 is eligible to get:-',lv)
    def p2(self):
        print('p2 is eligible to get:-',lv)

l=Loan()
l.p1()
p1 is eligible to get:- Gold loan/House loan/Personal loan
l.p2()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l.p2()
  File "<pyshell#17>", line 6, in p2
    print('p2 is eligible to get:-',lv)
NameError: name 'lv' is not defined

#Global variable:
#A variable which is located outside the class and its methods and can be accessed by global keyword

gv='Parking space'
global gv
class Bank:
    def staffs(self):
        print('Staffs can use the', gv)
    def accountholders(self):
        print('Account holders can use the', gv)
    def depositor(self):
        print('Depositors can use the', gv)

b=Bank()
b.accountholders()
Account holders can use the Parking space
b.depositor()
Depositors can use the Parking space
b.staffs()
Staffs can use the Parking space

#Instance variable:
#Permanently setting up a value to the class during runtime and taking the value from the class by co  nforming and informing the class is a instance variable

class Calci:
    def __init__(self,a,b): #Setting up permanent values to class
        self.a = a
        self.b = b  #Instance variable
    def add(self):
        return self.a + self.b  #confirming and informing to use the values of class
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def mod(self):
        return self.a % self.b
    def intdiv(self):
        return self.a // self.b

c=Calci(50,30)
c.a
50
c.b
30
c.add()
80
c.sub()
20
c.mul()
1500
c.mod()
20
c.intdiv()
1

#Note here c=Calci is Data abstraction because Calci hides in c object
#Calci(50,30) is Data encapsulation as it takes all the values together with it

#Data Abstraction
#Data hiding process
#It shows only the required data for the users and hides the internal complexity of the program

from abc import ABC, abstractmethod
class Rbi(ABC):
    @abstractmethod
    def loanapproval(self):
        pass

    
class Indianbank(Rbi):
    def loanapproval(self):
        print('loan should be approved by RBI')

        
class Statebank(Rbi):
    def loanapproval(self):
        print('loan should be approved by RBI')

        
i=Indianbank()
i.loanapproval()
loan should be approved by RBI
s=Statebank()
s.loanapproval()
loan should be approved by RBI

#Data encapsulation
#It is data wrapping process(Data hiding + Dynamic binding)

class Bankaccount:
    def __init__(self,accountholder,balance):
        self.accountholder = accountholder
        self.__balance = balance
    def getbalance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f'Deposited amount is {amount}. Updated balance is {self.__balance}')
        else:
            print(f'Invalid amount deposited')
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawl amount{amount}. Current balance is {self.__balance}')
        else:
            print(f'insufficient funds')

            
b=Bankaccount('Harish Kumar',10000)
b.accountholder()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b.accountholder()
TypeError: 'str' object is not callable
print('Account Holder:' b.accountholder)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('Account Holder:', b.accountholder)
Account Holder: Harish Kumar
b.getbalance()
10000
b.deposit(5000)
Deposited amount is 5000. Updated balance is 15000
b.withdraw(2000)
Withdrawl amount2000. Current balance is 13000

#Inheritance:
#How a sub class will get access from base class

#Types of inheritance
#1.Single Inheritance
#2.Multiple Inheritance
#3.Multi-level Inheritance
#4.Heirarchical Inheritance
#5.Hybrid Inheritance

#Single Inheritance:
#How a single child will get access from single parent

class Bank:
    def loan(self):
        print('Eligible to get loan')

        
class Person(Bank):
    def loan(self):
        pass

    
p=Person()
p.loan()
class Person(Bank):
    pass

p=Person()
p.loan()
Eligible to get loan

#Multiple Inheritance:
#How a multiple parent give access to a single child

class Indianbank:
    def goldloan(self):
        print('Eligible for gold loan')

        
class Statebank:
    def Carloan(self):
        print('Eligible for car loan')

        
class Hdfcbank:
    def Personalloan(self):
        print('Eligible for personal loan')

        
class Person(Indianbank,Statebank,Hdfcbank):
    pass

p=Person()
p.Carloan()
Eligible for car loan
p.Personalloan()
Eligible for personal loan
p.goldloan()
Eligible for gold loan

#Multi-level Inheritance:
#Child class depending on properties of another inherited child

class Gpay:
    def gpay(self):
        print('Used to send money, Book tickets, Order food')

        
class Swiggy(Gpay):
    def swiggy(self):
        print('Used to order food from favourite hotel')

        
class Buhari(Swiggy):
    def buhari(self):
        print('Used to order the meal')

        
b=Buhari()
b.gpay()
Used to send money, Book tickets, Order food
b.swiggy()
Used to order food from favourite hotel
b.buhari()
Used to order the meal

#Heirarchical Inheritance:
#Multiple child inherits on a single parent

class Bank:
    def hdfcbank(self):
        print('Can provide loan amount of 10lakhs')

        
class Person1(Bank):
    def marriage(self):
        print('Current income is 50k savings is 5lakhs')

        
class person2(Bank):
    def startup(self):
        print('Current income is 1lakh savings is 15lakhs')

        
p1=Person1()
p1.marriage()
Current income is 50k savings is 5lakhs
p1.hdfcbank()
Can provide loan amount of 10lakhs
p2=Person2()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    p2=Person2()
NameError: name 'Person2' is not defined. Did you mean: 'person2'?
p2=person2()
p2.startup()
Current income is 1lakh savings is 15lakhs
p2.hdfcbank()
Can provide loan amount of 10lakhs

#Hybrid Inheritance:
#It is a combination of two or all inheritance

class Bank:
    def loan(self):
        print('CIBIL score is good so eligible for loan')

        
class Parent(Bank):
    pass
#------------------------ Single Inheritance ----------------------#

class Child(Bank,Parent):
    pass

Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    class Child(Bank,Parent):
TypeError: Cannot create a consistent method resolution order (MRO) for bases Bank, Parent
class Bank:
    def loan(self):
        print('CIBIL score is good so eligible for loan')

        
class Parent(Bank):
    def savings(self):
        print('10Lakhs saved for child marriage')

        
#-------------------------- Single Inheritance -------------------------#
        
class Salary:
    def dependson(self):
        print('Parent salary is 40k')

        
class Child(Parent,Salary):
    pass

pa=Parent()
pa.loan()
CIBIL score is good so eligible for loan
pa.savings()
10Lakhs saved for child marriage
ch=Child()
ch.dependson()
Parent salary is 40k
ch.loan()
CIBIL score is good so eligible for loan
ch.savings()
10Lakhs saved for child marriage

#--------------------------- Hybrid Inheritance ---------------------------#

#Polymorphism:
#Poly means MANY and Morphism means FORMS
#A function with same name performs different activities is called as polymorphism

class Bank:
    def loan(self):
        print('Eligible to get loan')

        
class Customer1(Bank):
    def loan(self):
        print('Eligible for car loan')

        
class Customer2(Bank):
    def loan(self):
        print('Eligible for personal loan')

        
class Customer3(Bank):
    def loan(self):
        print('Eligible for gold loan')

        
customers = (Customer1,Customer2,Customer3)
customers = [Customer1(),Customer2(),Customer3()]
for customer in customers:
    customer.loan()

    
Eligible for car loan
Eligible for personal loan
Eligible for gold loan

#All properties of OOPS in a single code:

class Bankdetails:
    def __init__(self,Holder_name,Account_number,Mobile):
        self.Holder_name = Holder_name
        self.Account_number = Account_number
        self.Mobile = Mobile
    def details(self):
        print(f'Account holder name is {self.Holder_name}\n Account number is {self.Account_number}')
        print(f'Mobile number is {self.Mobile}')

        
class Mandatedetails(Bankdetails):
    def__init__(self,Holder_name,Account_number,Mobile,Branch,IFSC):
        
SyntaxError: invalid syntax
>>> class Mandatedetails(Bankdetails):
...     def __init__(self,Holder_name,Account_number,Mobile,Branch,IFSC):
...         Bankdetails.__init__(self,Holder_name,Account_number,Mobile)
...         self.Branch = Branch
...         self.IFSC = IFSC
... 
...         
>>> class Passbook(Mandatedetails):
...     def details(self):
...         print(f'Account holder name: {self.Holder_name}\n Account number: {self.Account_number}')
...         print(f'Mobile number: {self.Mobile}\n IFSC CODE: {self.IFSC}\n Branch: {self.Branch}')
... 
...         
>>> bankdetails = Bankdetails('HarishKumar','145564962655','5414845584')
>>> bankdetails.details()
Account holder name is HarishKumar
 Account number is 145564962655
Mobile number is 5414845584
>>> 
>>> passbook = Passbook('HarishKumar','145564962655','5414845584','Chennai','IOB15484658')
>>> passbook.details()
Account holder name: HarishKumar
 Account number: 145564962655
Mobile number: 5414845584
 IFSC CODE: IOB15484658
 Branch: Chennai
