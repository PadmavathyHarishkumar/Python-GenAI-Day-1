import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {"study_hours":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],
        "Att":[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350],
        "Pass":[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}
df = pd.DataFrame(data)
print('Testing with different inputs','\n','='*40)
new_stud = [[23,206],[10,305],[2,97],[33,108],[-33,-108]]
plt.figure(figsize=(10,7))


fail = df[df['Pass']==0]
pass_ = df[df['Pass']==1]
plt.scatter(fail['study_hours'], fail['Att'], c='red', label='Fail')
plt.scatter(pass_['study_hours'], pass_['Att'], c='green', label='Pass')


for i, ns in enumerate(new_stud, start=1):
    ns = np.array(ns)
    df['distance'] = np.sqrt((df['study_hours'] - ns[0])**2 + (df['Att'] - ns[1])**2)

    for k in [3,5]:
        nearest_stu = df.sort_values('distance').head(k)
        stu_result = nearest_stu['Pass']
        prediction = max(set(stu_result), key=stu_result.tolist().count)
        print(nearest_stu[['study_hours','Att','Pass','distance']])
        print("Prediction:", prediction)
        if prediction == 1:
            print('Student will pass\n')
        else:
            print('Student will fail\n')

        plt.scatter(nearest_stu['study_hours'], nearest_stu['Att'],
                    edgecolors='black', facecolors='yellow', s=200,
                    label=f'Neighbors (k={k})' if i==1 else "")

   
    plt.scatter(ns[0], ns[1], c='purple', marker='*', s=250)
    plt.text(ns[0]+0.5, ns[1]+5,f"N{i}", fontsize=10, color='black')

plt.xlabel("Study Hours")
plt.ylabel("Attendance")
plt.title("Student Performance - KNN")
plt.legend()
plt.grid(True)
plt.show() 
    
while True:
    print('====================================')
    print('   GETTING USER INPUTS TO PREDICT '   )
    print('====================================')   
    StudyHours = int(input('What is your study hours ?'))
    Attendance = int(input('What is your attendance?'))
    user_data = np.array([StudyHours,Attendance])
    df['user_distance'] = np.sqrt((df['study_hours'] - user_data[0])**2 + (df['Att'] - user_data[1])**2)
    k = 5
    nearest_user = df.sort_values('user_distance').head(k)
    user_result = nearest_user['Pass']
    pred_user = max(set(user_result), key=user_result.tolist().count)
    print('Prediction of your result is ',pred_user)
    if pred_user == 1:
        print('You will pass','\n')
    else:
        print('You will fail','\n')
    
    while True:
            choice = input('Do you want to check again? (yes/no):').casefold()
            if choice == 'yes':
                break
            elif choice == 'no':
                print('\n''Exiting the prediction loop goodbye....''\n')
                exit()
            else:
                print('\n'"Invalid choice. Please type 'yes' or 'no'.",'\n')

    