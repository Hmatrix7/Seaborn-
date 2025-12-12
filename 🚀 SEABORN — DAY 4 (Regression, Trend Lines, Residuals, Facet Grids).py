#!/usr/bin/env python
# coding: utf-8

# In[6]:


#🎯 Goal: Understand how variables relate, create regression lines, and analyze trends.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")
sns.set_style("dark")


# In[7]:


#1️⃣ regplot (Simple Regression Plot)
#Shows scatter + regression line + confidence interval.
sns.regplot(data=df, x="total_bill", y="tip")
plt.title("Regression: Total Bill vs Tip")
plt.show()


# In[ ]:


2️⃣ lmplot (The Most Powerful Regression Tool)

lmplot is like regplot but supports:

categories (hue)

multiple plots (col/row)

automatic FacetGrid



# In[9]:


#A) Regression with categories (male vs female)
sns.lmplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Regression by Sex")
plt.show()


# In[11]:


#B) Combine categories (Lunch vs Dinner)
sns.lmplot(data=df, x="total_bill", y="tip", col="time")
plt.show()
#This creates two separate regression plots, one for Lunch and one for Dinner.


# In[12]:


#3️⃣ Residual Plot
#Residuals = actual − predicted
# to check regression quality.
sns.residplot(data=df, x="total_bill", y="tip")
plt.title("Residual Plot")
plt.show()


# In[14]:


#4️⃣ Jointplot With Regression Line
#Kind: 'reg'
sns.jointplot(data=df, x="total_bill", y="tip", kind="reg")
#Shows:
#scatter
#regression
#histograms


# In[15]:


#5️⃣ FacetGrid (Multiple Charts in a Grid)
#FacetGrid allows you to apply a function to multiple subsets of data.
#A) Compare days (Sun, Sat, etc.)
g = sns.FacetGrid(df, col="day")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()


# In[16]:


#B) FacetGrid with regression
g = sns.FacetGrid(df, col="day", hue="sex")
g.map(sns.regplot, "total_bill", "tip")
g.add_legend()
plt.show()


# In[17]:


#6️⃣ Advanced lmplot Examples
#A) Multiple columns (day splits)
sns.lmplot(data=df, x="total_bill", y="tip", col="day")
plt.show()


# In[18]:


#B) Multiple columns + hue (sex)
sns.lmplot(data=df, x="total_bill", y="tip", col="day", hue="sex")
plt.show()


# In[ ]:




