"""
Program: dpowell_personality_ml_v1.05.py
Last Edit Date: 3/18/20

-------------------------------------------------------------------------------
Objective: Create a machine learning algorithm that can with at least 85% accuracy
to predict a personality trait of person using spending habits.

-------------------------------------------------------------------------------
Data set notes:
- The data was created in 2013 of people ages 15 - 30 years old
- Survey covers 150 questions ranging from tastes in music to demographics
- The data set used for the program is focused around people from Slovakia

-------------------------------------------------------------------------------
Program Algorithm:
1. Read CSV Files
2. Split data into training and validation sets
3. Train estimators on training data
4. Validate training models accuracy
5. Calculate the average accuracy of number of models tested
6. Repeat steps 1 - 5 till all models are created
6. Graph results from models

-------------------------------------------------------------------------------
Acknowledgment Notes:

Survey Data set:
https://www.kaggle.com/miroslavsabo/young-people-survey#responses.csv

Machine learning models and example code from:
https://scikit-learn.org/stable/index.html

Sample machine learning code provided by Dr. Nichols

Sample machine learning code
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

Matplot Guide
https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional
  -plotting.html

Time function
https://www.programiz.com/python-programming/time

-------------------------------------------------------------------------------
Change Log:
-v1.00
 -first version of program

-v1.01

 -Added LinearSVC to compare overall accuracy scores and classification scores
  compared to the MLPClassifier

 -Added a way to test the algorithm using the iris data set

-v1.02

  -refocused purpose of algorithm to compare models based on an average overall
   accuracy score, time, and number of features used.

  -added multiple scripts to carry out training and validating models based on
   the input number of instances

  -added a visual tool to show the relationship between the three variables
   being observed.

-v1.03
  -Set average accuracy of 10 models per set of features per different 
   estimator parameters

  -reduced to only needing one python file and the sames CSV files to train
   models

  -Setup code where more estimators and models can be added for training

-v1.04
  - Fixed issue with convergence warnings by changing to higher number of
    iterations for all models equally

-v1.05
  - Added more detailed comments to the code to flow with the project paper
  - Adjusted output labels of 3D scatter plot

-------------------------------------------------------------------------------
Know Bugs In Program:
None

-------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 dpowell_personality_ml_v1.05.py
-------------------------------------------------------------------------------
Output v1.05:

-See Diagram that appears after running code

-------------------------------------------------------------------------------
"""

#Libraries---------------------------------------------------------------------

#Used in Section: Data Handling
from pandas import read_csv
from sklearn.model_selection import train_test_split

#Used in Section: Model Creation and Prediction
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
import time as tm

#Used in Section: Display Results
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#Main Function ----------------------------------------------------------------
def main():

    #Local Declarations -----------------------------------

    #Initialization of variables
    average = 10              #Number of times to make a model to determine
                              # overall average accuracy score

    feature = [1,2,3,4,5,6,7] #List of the amount of features used per model

    MLPdata1 = []             #List to store overall average accuracy
                              # of MLPClassifier

    MLPdata2 = []             #List to store overall average accuracy
                              # of MLPClassifier

    MLPdata3 = []             #List to store overall average accuracy
                              # of MLPClassifier

    final_time1 = []          #List to store time taken to analyze both models
                              # with n features

    final_time2 = []          #List to store time taken to analyze both models
                              # with n features

    final_time3 = []          #List to store time taken to analyze both models
                              # with n features
    
    #Local Statements -------------------------------------

    #SECTION: Data Handling----------------------------------------------------

    print("        MLPClassifier Model Comparison         ")
    print("-----------------------------------------------")
    print("Please wait until the 3D scatter plot displays ")

    #For loop to iterate through all models being observed
    for iter_selection in range(3):
  
        #For loop to iterate through data sets used by the models and estimators
        for i in range(7):

            #If statements to that determine which set of data is being used
            if i == 0:
                #Load data set values from CSV file
                csvData = "responses-1feature-finances.csv"
                
                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances']

                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two NumPy X and y arrays
                X1 = array[:,0:2]
                y1 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X1, y1, test_size=0.20)

            if i == 1:
                #Load data set values from CSV file
                csvData = "responses-2features.csv"    

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two NumPy X and y arrays
                X2 = array[:,0:3]
                y2 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X2, y2, test_size=0.20)

            if i == 2:
                #Load data set values from CSV file
                csvData = "responses-3features.csv"    

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres', 'Branded clothing']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two numpy X and y arrays
                X3 = array[:,0:4]
                y3 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X3, y3, test_size=0.20)

            if i == 3:

                #Load data set values from CSV file
                csvData = "responses-4features.csv"

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres', 'Branded clothing','Entertainment spending']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two numpy X and y arrays
                X4 = array[:,0:5]
                y4 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X4, y4, test_size=0.20)

            if i == 4:

                #Load data set values from CSV file
                csvData = "responses-5features.csv"    

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres', 'Branded clothing',
                         'Entertainment spending', 'Spending on looks']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two numpy X and y arrays
                X5 = array[:,0:6]
                y5 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X5, y5, test_size=0.20)

            if i == 5:

                #Load data set values from CSV file
                csvData = "responses-6features.csv"    

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres', 'Branded clothing',
                        'Entertainment spending', 'Spending on looks', 'Spending on gadgets']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two numpy X and y arrays
                X6 = array[:,0:7]
                y6 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X6, y6, test_size=0.20)

            if i == 6:

                #Load data set values from CSV file
                csvData = "responses-7features.csv"    

                #Array to store names of feature(s) and target feature
                names = ['Getting angry', 'Finances','Shopping centres', 'Branded clothing',
                         'Entertainment spending', 'Spending on looks', 'Spending on gadgets',
                         'Spending on healthy eating']
    
                #Stores the data values with names of questions
                dataset = read_csv(csvData, names=names)

                #Stores array values into an array
                array = dataset.values

                #Initialization of two numpy X and y arrays
                X7 = array[:,0:8]
                y7 = array[:,0]

                #Function to split the question values into a training set where 20 percent of the 
                # data set is used for validation
                (X_train, X_validation, Y_train, Y_validation) = train_test_split(X7, y7, test_size=0.20)

    #Section: Model Creation and Prediction------------------------------------

            #Sets the overall average accuracy to zero before each test
            # extra information is not used is the next test's results
            MLPavg = 0

            #https://scikit-learn.org/stable/index.html
            #Initialization of the model to be used along with parameters to use

            #Time function to begin timer
            start_time = tm.time()

            for i in range(average):

                if iter_selection == 0:

                    #Default MLPClassifier
                    estimator_MLP = MLPClassifier(max_iter=1400)

                if iter_selection == 1:

                    #MLPClassifier with tangent activation function
                    estimator_MLP = MLPClassifier(activation='tanh', max_iter=1400)

                if iter_selection == 2:

                    #MLP Classifier with logistic activation function
                    estimator_MLP = MLPClassifier(activation='logistic', max_iter=1400)

                #Function to train the model with the data set
                estimator_MLP.fit(X_train, Y_train)

                #Prediction function for MLPClassifer
                prediction_MLP = estimator_MLP.predict(X_validation)
               
                #Determine the accuracy score of the model
                MLPavg = accuracy_score(Y_validation, prediction_MLP) * 100 + MLPavg

            #Takes and stores the stop time of determining the model average
            stop_time = tm.time() - start_time
            
            #Determines the average overall accuracy
            MLPavg = MLPavg / average

            #Stores the information of the first model
            if iter_selection == 0:   
                
                #Stores accuracy results of test into an array
                MLPdata1.append(float(MLPavg))

                #Stores time results of test in an array
                final_time1.append(float(stop_time))

            #Stores the information of the second model
            if iter_selection == 1:

                #Stores accuracy results of test into an array
                MLPdata2.append(float(MLPavg))

                #Stores time results of test in an array
                final_time2.append(float(stop_time))

            #Stores the information of the third model
            if iter_selection == 2:

                #Stores accuracy results of test into an array
                MLPdata3.append(float(MLPavg))

                #Stores time results of test in an array
                final_time3.append(float(stop_time))

    #Section: Displaying Results-----------------------------------------------

    #Initialization of MatPlotLib model
    ax = plt.axes(projection='3d')

    #Plots MLPClassifier data
    ax.scatter3D(feature, MLPdata1, final_time1)
    ax.scatter3D(feature, MLPdata2, final_time2)
    ax.scatter3D(feature, MLPdata3, final_time3)
    ax.legend(['Default','Tangent','Logistic'])

    #Axis labels and figure title
    ax.set_xlabel('Number Of Features')
    ax.set_ylabel('Average Accuracy Score')
    ax.set_zlabel('Time Taken (Seconds)')
    title = 'MLPClassifier Average of ' + str(average) + ' Model(s)'
    ax.set_title(title)

    #Shows graph to screen
    plt.show()
    
#Main function call------------------------------------------------------------
main()


