#This additional text includes what we executed before as well as some new commands 
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#My understanding of this command and the one below is that you are telling the system that you should have 4 arguments and that it should check that with the arguments then being listed below 
if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

#The rest of this code is copied from before 
data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()




#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.

# In[4]:


#pandas is a program used to simply data analysis in python. In this command we are renaming pandas as pd for ease of use
import pandas as pd
#This command allows pandas to read out file with our data and renames it to dataset 
dataset = pd.read_csv("regression_data.csv")


# In[5]:


#This command printed out my spreadsheet proving that the dataset command above worked
print(dataset)


# In[7]:


#matplotlb.pyplot is being shortened to plt. This is renaming the graphing software
import matplotlib.pyplot as plt
#This should make my scatter plot
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")


# In[8]:


#This imports a linear regression model from sklearn and fits it to the data provided
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[14]:


#This then plots the regression line information we just generated and places labels on the graph 
plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
#Added the scatter plot command from before to add the points to the graph
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[13]:


#This is a R-squared analysis
model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared


# In[ ]:




