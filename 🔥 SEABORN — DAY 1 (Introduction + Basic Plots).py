#!/usr/bin/env python
# coding: utf-8

# In[1]:


#🎯 Goal: Understand Seaborn basics, load a dataset, and create your first visualizations.
get_ipython().system('pip install seaborn')


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


#Load a Sample Dataset
#Seaborn comes with built-in datasets. We’ll use tips.
df = sns.load_dataset("tips")
df.head()


# In[6]:


#Set a Visual Style (Seaborn Advantage)
sns.set_style("dark")


# In[7]:


#Basic Seaborn Plots
#📌 A) Scatter Plot
#Relationship between total bill and tip:
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()


# In[9]:


#📌 B) Histogram / Distribution Plot
#Understanding how bills are distributed:
#kde=True adds a smooth density curve
sns.histplot(data=df, x="total_bill", kde=True)
plt.title("Distribution of Total Bill")
plt.show()


# In[10]:


#📌 C) Boxplot
#View differences in tips based on day:
sns.boxplot(data=df, x="day", y="tip")
plt.title("Boxplot of Tips by Day")
plt.show()


# In[11]:


#📌 D) Countplot
#Count how many customers came each day:
sns.countplot(data=df, x="day")
plt.title("Customer Count by Day")
plt.show()


# In[ ]:




