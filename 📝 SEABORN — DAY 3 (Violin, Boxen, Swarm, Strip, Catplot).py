#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#🎯 Goal: Master categorical visualizations and compare groups effectively.


# In[1]:


import seaborn as sns
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df=sns.load_dataset("tips")
sns.set_style("dark")


# In[5]:


print(df)


# In[6]:


#Violin Plot
#Shows distribution + density for each category.
sns.violinplot(data=df, x="day", y="total_bill")
plt.title("Violin Plot: Total Bill by Day")
plt.show()


# In[7]:


#With split categories (Male vs Female):
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot: Total Bill by Day & Sex")
plt.show()


# In[8]:


#Boxen Plot (Advanced Box Plot)
#Good for large datasets — it shows distribution more clearly than a boxplot.
sns.boxenplot(data=df, x="day", y="tip")
plt.title("Boxen Plot: Tips by Day")
plt.show()


# In[9]:


#Swarm Plot
#Shows every data point — great for small datasets.
sns.swarmplot(data=df, x="day", y="tip")
plt.title("Swarm Plot: Tips by Day")
plt.show()


# In[10]:


#Strip Plot
#Similar to swarmplot, but points overlap.
sns.stripplot(data=df, x="day", y="total_bill")
plt.title("Strip Plot: Total Bill by Day")
plt.show()


# In[11]:


#catplot (Universal Categorical API)
#catplot can draw almost any categorical plot.
#A) Bar plot
sns.catplot(data=df, x="day", y="total_bill", kind="bar")


# In[12]:


#B) Box plot
sns.catplot(data=df, x="day", y="total_bill", kind="box")


# In[13]:


#C) Violin plot
sns.catplot(data=df, x="day", y="total_bill", kind="violin")


# In[14]:


#D) Countplot using catplot
sns.catplot(data=df, x="day", kind="count")


# In[15]:


#⭐ Comparison Example: Violin vs Boxen vs Box
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(data=df, x="day", y="total_bill", ax=axes[0])
axes[0].set_title("Boxplot")

sns.violinplot(data=df, x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Violin Plot")

sns.boxenplot(data=df, x="day", y="total_bill", ax=axes[2])
axes[2].set_title("Boxen Plot")

plt.tight_layout()
plt.show()


# In[ ]:




