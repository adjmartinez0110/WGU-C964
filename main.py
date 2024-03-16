#The dataset used in this model has been modified. The original is found on Kaggle.
#Link is https://www.kaggle.com/datasets/thedevastator/uncovering-state-by-state-car-theft-trends-in-20
#Credit goes to Joe Boutros for providing this dataset.

import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from lists import states_lister
from lists import mm_lister
from visuals import bar_graph_thefts
from visuals import bar_graphs_states
from visuals import pie_chart_years
import warnings
import time


# Creating the dataframes
state_df = pd.read_csv(r'2015_State_Top10Report_forStateDF.csv')
mm_df = pd.read_csv(r'2015_State_Top10Report_forMakeModelDF.csv')

#defining x and y
state_features = state_df[['State']]
state_X = state_features
state_y = state_df['Likelihood of Theft']

mm_features = mm_df[['Make/Model']]
mm_X = mm_features
mm_y = mm_df['Likelihood of Theft']

# Allocating test and training data
X_trainS, X_testS, y_trainS, y_testS = model_selection.train_test_split(state_X, state_y, test_size=0.3)
X_trainMM, X_testMM, y_trainMM, y_testMM = model_selection.train_test_split(mm_X, mm_y, test_size=0.3)

# Creating the model
model_state = DecisionTreeClassifier()
model_mm = DecisionTreeClassifier()

# Suppress specific warning
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Training the model
model_state.fit(X_trainS, y_trainS)
model_mm.fit(X_trainMM, y_trainMM)

#Model prediction for accuracy
y_state_pred = model_state.predict(X_testS)
y_mm_pred = model_mm.predict(X_testMM)

#accuracy for validation
state_model_accuracy = accuracy_score(y_testS, y_state_pred)
#print('State model accuracy: ', state_model_accuracy)

mm_model_accuracy = accuracy_score(y_testMM, y_mm_pred)
#print('M/M model accuracy: ', mm_model_accuracy)





print("Welcome to the Valley Kestrel Vehicle Theft Predicting App!")

print("This app is used to predict the likelihood of vehicle theft depending on the state the vehicle is located in or the make and model of your vehicle.")

selection = int(input("Would you like to enter your state or your vehicle for the prediction? Enter 1 for state, 2 for vehicle: "))

numbers1 = []
numbers2 = []

if selection == 1:
    print("Carefully observe the following list of states: ")
    time.sleep(2)
    states_lister()

    state_user_input = int(input('Please enter the number associated with your state: '))
    for i in range(1, 51):
        numbers1.append(i)

    #Specified prediction
    state_prediction = model_state.predict([[state_user_input]])

    # Output prediction
    if state_user_input not in numbers1:
        print("Invalid input. Please try again.")
    elif state_prediction[0] == 1:
        print("The vehicle in this state has a higher likelihood to be stolen. Please take the necessary precautions.")
    else:
        print("The vehicle in this state has a lower likelihood to be stolen. We still recommend taking the necessary precautions.")



elif selection == 2:
    print("Please carefully observe the following list of vehicles: ")
    time.sleep(2)
    mm_lister()
    mm_user_input = int(input("Please enter the number associated with your vehicle: "))
    for i in range(1, 48):
        numbers2.append(i)

    state_prediction = model_state.predict([[mm_user_input]])

    # Output prediction
    if mm_user_input not in numbers2:
        print("Invalid input. Please try again.")
    elif state_prediction[0] == 1:
        print("This vehicle has a higher likelihood to be stolen. Please take the necessary precautions.")
    else:
        print("This vehicle has a lower likelihood to be stolen. We still recommend taking the necessary precautions.")



else:
    print('An unknown error occurred. Please try again.')

bar_graph_thefts()

bar_graphs_states()

pie_chart_years()


