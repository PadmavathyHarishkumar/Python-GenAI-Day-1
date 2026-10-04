import pandas as pd
import numpy as np

#---------------------
#1.Loading the DataSet
#---------------------
df = pd.read_csv(r"E:\Python GenAI Day 1\titanic.csv")

df = df[['Pclass','Sex','Age','Fare','Survived']]

#--------------------------------
#2.Handling missing values in Age
#--------------------------------
df['Age'] = df['Age'].fillna(df['Age'].median())

#-------------------------------
#3.Mapping sex values to 0 and 1
#-------------------------------
df['Sex'] = df['Sex'].map({'female' : 0 , 'male' : 1})

print('='*37)
print('Actual DataSet of first 10 passengers')
print('='*37)
print(df.head(10),'\n')

#------------------------
#4.Creating Decision Tree
#------------------------
def tree1(Sex):
    if Sex == 0:
        return 1
    else:
        return 0
    
def tree2(Pclass):
    if Pclass <=2:
        return 1
    else:
        return 0
    
def tree3(Age):
    if Age > 22:
        return 1
    else:
        return 0
    
def tree4(Fare):
    if Fare > 7:
        return 1
    else:
        return 0
    
#-----------------------------------------------
#5.Combining all trees to create a Random Forest
#-----------------------------------------------
def random_forest(Sex,Pclass,Age,Fare):
    prediction1 = tree1(Sex)
    prediction2 = tree2(Pclass)
    prediction3 = tree3(Age)
    prediction4 = tree4(Fare)
    
    predictions = [prediction1,prediction2,prediction3,prediction4]
    
#-----------------
#6.Majority voting
#-----------------
    Max_Survival_Prediction = max(set(predictions),key = predictions.count)
    return Max_Survival_Prediction
#----------------------------------------------    
#7.Testing Random Forest on first 10 passengers
#----------------------------------------------
print('='*60)
print('Comparing the Prediction with Actual for first 10 passengers')
print('='*60)
results = []
for i in range(10):
    row = df.iloc[i]
    pred = random_forest(row['Sex'],row['Pclass'],row['Age'],row['Fare'])
    results.append(pred == row['Survived'])
    print(f'row{i} | Actual = {row["Survived"]} | Predicted = {pred}')
    
accuracy = np.mean(results)
print('\n''Accuracy of first 10 passengers :',accuracy,'\n')

#----------------------------------------
#8.Checking the survival of new passenger
#----------------------------------------
Passenger_result = random_forest(
    Sex= 1,
    Pclass= 2,
    Age= 25,
    Fare= 36
)
print('='*42)
print('Checking if new passenger survived or not')
print('='*42)
print(f'Sex = {1}, Pclass = {2}, Age = {25}, Fare = {36}')
if Passenger_result == 1:
    print('\nPassenger was survived ✅ ','\n')
else:
    print('\nPassenger was not survived ❌','\n')
    
#--------------------------------
#9.Getting user inputs to predict
#--------------------------------
print('='*33)
print('   GETTING USER INPUTS TO PREDICT '   )
print('='*33)    
while True:
    Gender = int(input('Enter the passenger gender(1 = Male , 0 = Female) : '))
    Passenger_class = int(input('Enter passenger class : '))
    Passenger_Age = int(input('Enter passenger age : '))
    Passenger_Fare = int(input('Enter passenger fare : '))
    
    User_result = random_forest(Gender,Passenger_class,Passenger_Age,Passenger_Fare)
    
    if User_result == 1:
        print('\nPassenger was survived ✅ ','\n')
    else:
        print('\nPassenger was not survived ❌','\n')
        
    while True:
        choice = input('Do you want to check for another passenger(yes/no)?').casefold()
        if choice == 'yes':
            break
        elif choice == 'no':
            print('Exiting the prediction loop goodbye....')
            exit()
        else :
            print('Enter a valid input(yes/no)')