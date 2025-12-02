#!/usr/bin/env python
# coding: utf-8

# In[5]:


#🎯 Goal: Understand multi-variable relationships and advanced Seaborn plots.


# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


# In[7]:


df=sns.load_dataset("tips")
sns.set_style("dark")


# In[8]:


#Pairplot (Multi-variable relationships)
#A pairplot shows:
#Histogram of each numeric variable
#Scatter plots for each pair of variables
sns.pairplot(df)
plt.show()


# In[9]:


#Colored pairplot (more useful):
sns.pairplot(df, hue="sex")
plt.show()


# In[10]:


#Correlation Matrix
#A numeric summary of how variables relate (range −1 to 1).
corr = df.corr(numeric_only=True)
corr


# In[11]:


#Heatmap of Correlation Matrix
#This is one of the most important plots in analytics:
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()


# In[12]:


#Jointplot (2-variable deep analysis)
#Shows:
#Scatter
#Histogram
#KDE (density)
#Basic scatter + distribution:
sns.jointplot(data=df, x="total_bill", y="tip", kind="scatter")


# In[13]:


#KDE (smooth density):
sns.jointplot(data=df, x="total_bill", y="tip", kind="kde")


# In[14]:


#Hexbin (good for large datasets):
sns.jointplot(data=df, x="total_bill", y="tip", kind="hex")


# In[16]:


#PairGrid (More control than pairplot)
#If you want full customization:
g = sns.PairGrid(df, hue="sex")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
g.add_legend()
plt.show()


# In[ ]:




