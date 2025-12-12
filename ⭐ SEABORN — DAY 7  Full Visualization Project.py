#!/usr/bin/env python
# coding: utf-8

# In[ ]:


🎯 Project Goal

Use Seaborn to produce a clean, professional exploratory data analysis (EDA) notebook containing:

Data loading

Data cleaning

Univariate analysis

Bivariate analysis

Multivariate analysis

Insights summary


# In[2]:


#📊 Dataset: tips (built-in)
#A perfect dataset for EDA practice.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.head()


# In[ ]:


================================
📌 PART 1 — Data Cleaning
================================
1. Check missing values


# In[3]:


df.isnull().sum()


# In[4]:


#2. Summary statistics
df.describe(include="all")


# In[ ]:


================================
📌 PART 2 — Univariate Analysis
================================
1. Distribution of Total Bill


# In[5]:


sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.show()


# In[6]:


#2. Tip distribution
sns.histplot(df['tip'], kde=True, color='green')
plt.title("Tip Distribution")
plt.show()


# In[ ]:


================================
📌 PART 3 — Bivariate Analysis
================================
1. Total Bill vs Tip (scatter plot)


# In[7]:


sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()


# In[8]:


#2. Tip % by Day (boxplot)
df['tip_pct'] = df['tip'] / df['total_bill']

sns.boxplot(data=df, x="day", y="tip_pct")
plt.title("Tip Percentage by Day")
plt.show()


# In[9]:


#3. Sex vs Total Bill (violin plot)
sns.violinplot(data=df, x="sex", y="total_bill")
plt.title("Total Bill by Gender")
plt.show()


# In[ ]:


================================
📌 PART 4 — Multivariate Analysis
================================
1. Scatter plot with hue & size


# In[10]:


sns.scatterplot(
    data=df, x="total_bill", y="tip",
    hue="sex", size="size", sizes=(20, 200)
)
plt.title("Tip vs Total Bill (with Gender & Party Size)")
plt.show()


# In[11]:


#pairplot
sns.pairplot(df, hue="sex")


# In[16]:


#3. Heatmap (correlation)
numeric_df = df.select_dtypes(include=['int64', 'float64'])

sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="Blues")
plt.title("Correlation Heatmap (Numeric Columns Only)")
plt.show()


# In[ ]:




