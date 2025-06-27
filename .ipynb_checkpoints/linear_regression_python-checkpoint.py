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




