#!/usr/bin/env python
# coding: utf-8

# In[ ]:


🎯 Learning Objectives

By the end of Day 6, you will confidently use Seaborn to:

Compare distributions across categories

Visualize mean, median, quartiles, variance

Explore KDE (density) across groups

Show data + statistical summary in one plot

Understand when to use each plot


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(8,5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill Distribution per Day")
sns.set_style("dark")
plt.show()


# In[3]:


#2️⃣ Violin Plot
#Shows distribution + density + quartiles.
plt.figure(figsize=(8,5))
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Violin Plot - Total Bill per Day")
plt.show()


# In[4]:


#3️⃣ Boxen Plot (for Large Data)
#Better for datasets with many rows.
plt.figure(figsize=(8,5))
sns.boxenplot(data=tips, x="day", y="total_bill")
plt.title("Boxen Plot - Total Bill per Day")
plt.show()


# In[5]:


#4️⃣ Swarmplot (Exact data points)
#Shows individual points + avoids overlap.
plt.figure(figsize=(8,5))
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Swarm Plot")
plt.show()


# In[6]:


#5️⃣ Stripplot (simpler version of swarmplot)
plt.figure(figsize=(8,5))
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True)
plt.title("Strip Plot with Jitter")
plt.show()


# In[7]:


#6️⃣ Combine Plot (Violin + Swarm)
#Professional analysts use this to show both distribution + actual points:
plt.figure(figsize=(8,5))
sns.violinplot(data=tips, x="day", y="total_bill", inner=None)
sns.swarmplot(data=tips, x="day", y="total_bill", color="black", size=2)
plt.title("Violin + Swarm Combined")
plt.show()


# In[8]:


#7️⃣ KDE Comparison Across Categories
#Compare density between groups.
plt.figure(figsize=(8,5))
sns.kdeplot(data=tips, x="total_bill", hue="sex", fill=True)
plt.title("KDE Distribution by Sex")
plt.show()


# In[9]:


#8️⃣ ECDF Plot (Cumulative Distribution)
#Shows percent of data below a value.
plt.figure(figsize=(8,5))
sns.ecdfplot(data=tips, x="total_bill", hue="day")
plt.title("ECDF Plot - Total Bill Distribution")
plt.show()


# In[ ]:




