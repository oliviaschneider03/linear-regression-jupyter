#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.

# In[32]:


#pandas is a program used to simply data analysis in python. In this command we are renaming pandas as pd for ease of use
import pandas as pd
#This command allows pandas to read out file with our data and renames it to dataset 
dataset = pd.read_csv("regression_data.csv")


# In[33]:


#This command printed out my spreadsheet proving that the dataset command above worked
print(dataset)


# In[34]:


#matplotlb.pyplot is being shortened to plt. This is renaming the graphing software
import matplotlib.pyplot as plt
#importing numpy which is used for calculating
import numpy as np
#Importing os is used to look for file extension
import os
#importing other packages for statistical analysis
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error
#This should make my scatter plot
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[35]:


#This imports a linear regression model from sklearn and fits it to the data provided
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[36]:


#This then plots the regression line information we just generated and places labels on the graph 
plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
#Added the scatter plot command from before to add the points to the graph
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[37]:


#This is a R-squared analysis
model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# In[38]:


#This is the new addition to the assignment 

#One way to do this assignment is to manually type in your data into arrays as is expemplified below
#x = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.7, 4.0])
#y = np.array([39343.0, 46205.0, 37731.0, 43525.0, 39891.0, 56642.0, 60150.0, 54445.0, 57189.0, 63218.0])

#However, you can also code to allow this system to recognize any data set in csv or xlsx formate and run a regression line on it 

#These steps are used to read the data, define it, and read the specific extension of the document
def load_data(regression_data, YearsExpierence, Salary):
    ext = os.path.splitext(regression_data)[1]
    if ext == '.csv':
        df = pd.read_csv(regression_data)
    if ext in ['.xls', '.xlsx']:
        df = pd.read_excel(regression_data)
    return df

# Now this is defining the data and defining a data frame that can be used later 
regression_data = "regression_data.csv" 
df = load_data(regression_data, 'Years Experience', 'Salaray')

# Printing columns to ensure this command worked
print("Available columns:")
print(df)



# In[39]:


# Split df array into 2 seperate arrays
#.iloc command splits data and the [#,#] represents what rows, columns are being split. : means to include all rows within the indicated column 
x = df.iloc[:, 0].to_numpy()  
y = df.iloc[:, 1].to_numpy()  

#Print arrays to check work
print (x)

print (y)


# Below we calculate the MSE which is the mean squared error. It indicates the average squared difference between the actual and the predicted values on our model. It is used to evalue the fit of the data but it is important to remember that it is scale dependent. 

# In[40]:


# Linear regression - this command uses linregress program to the line of regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

# Plot
#plot command adds the linear regression line calculated above 
#Scatter command copied from earlier to add dots
#Text adds in the equation and the max(y)- number is how you vertically control the placement of the text 
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.text(1.0, max(y) - 3500,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()


# With our graph printed, we are able to analyze the fit. The salary of a working according to our linear model equation seems to increase around 8000 dollats per year of experience with a starting salary of 30000. This is a sanity check and seems to make logical sense. The MSE is really high but we must account for the fact that MSE does include aspects of our y scale which uses quite large values. The r value is also quite high but in a good sense this time. A high r indicates a model that is well fitting. This model seems to fit the data but does have a high amount of error according to our MSE calculation. 

# In[ ]:





# In[ ]:




