import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
print("Python is looking in:", os.getcwd())
df = pd.read_csv(r'E:\Python GenAI Day 1\exercise-hours-daily-steps-30.csv')
print(df)
new_participants = [[3,1000],[2,6000],[7,2000],[9,1000],[5,5000]]
plt.figure(figsize=(10,7))
fit = df[df['Fit (1/0)']==1]
fat = df[df['Fit (1/0)']==0]
plt.scatter(fit['Exercise Hours'],fit['Daily Steps'],c='green',s=50,label='Fit')
plt.scatter(fat['Exercise Hours'],fat['Daily Steps'],c='blue',s=100,label='Fat')
for i, ns in enumerate(new_participants,start =1):
    ns = np.array(ns)
    df['distance'] = np.sqrt((df['Exercise Hours']-ns[0])**2 + (df['Daily Steps']-ns[1])**2)
    for k in(3,5):
        closest_neighbour = df.sort_values('distance').head(k)
        neighbor_fitness_labels = closest_neighbour['Fit (1/0)']
        fitness_prediction = max(set(neighbor_fitness_labels),key = neighbor_fitness_labels.to_list().count)
        print(f'\nNew joiner {i} K={k}')
        print(closest_neighbour[['Exercise Hours','Daily Steps','Fit (1/0)','distance']])
        print('Prediction =', fitness_prediction,'\n')
        if fitness_prediction == 1:
            print('You are fit','\n')
        else:
            print('You are fat','\n')
        plt.scatter(closest_neighbour['Exercise Hours'],closest_neighbour['Daily Steps'],edgecolors='black', 
                    facecolors = 'purple', s=200,label = f'Neighbours (K={k})' if i==1 else'' )
    plt.scatter(ns[0],ns[1],c='gold',marker = '*',s=250)
    plt.text(ns[0]+0.2,ns[1]+5, f'N{i}' , fontsize = 10 , color = 'black')
plt.xlabel('Exercise Hours')
plt.ylabel('Daily Steps')
plt.title('Fat and Fit Prediction')
plt.grid(True)
plt.legend()
plt.show()

while True:
    print('====================================')
    print('   GETTING USER INPUTS TO PREDICT '   )
    print('====================================')
    Exercise_Hours = int(input('How many hours do you exercise? '))
    Daily_Steps = int(input('How many steps do you walk daily? '))
    if input == 'STOP':
        break
    user_fitness_input = np.array([Exercise_Hours,Daily_Steps])
    df['user_distance']=np.sqrt((df['Exercise Hours'] - user_fitness_input[0])**2 + (df['Daily Steps'] - user_fitness_input[1])**2)
    k = 5
    new_user = df.sort_values('user_distance').head(k)
    user_result = new_user['Fit (1/0)']
    user_fitness_prediction = max(set(user_result),key = user_result.to_list().count)
    print('Prediction : ',user_fitness_prediction,'\n')
    if user_fitness_prediction == 1:
        print('You are fit','\n')
    else:
        print('You are fat','\n')
    while True:
        choice = input('Do you want to check again(yes/no):').casefold()
        if choice == 'yes':
            break
        elif choice == 'no':
            print('\n','Exiting the prediction loop goodbye....')
            exit()
        else:
            print('\n','Enter a valid choice(yes/no)')