#!/usr/bin/env python
# coding: utf-8

# In[1]:


#🎯 Goal: Make your visualizations clean, beautiful, and presentation-ready.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")


# In[2]:


#1️⃣ Seaborn Themes (Global Styles)
#Seaborn has 5 default themes:
sns.set_style("whitegrid")   # most popular
sns.set_style("darkgrid")
sns.set_style("white")
sns.set_style("dark")
sns.set_style("ticks")


# In[4]:


#Try switching styles and see how the chart looks.
#Example:
sns.set_style("darkgrid")
sns.boxplot(data=df, x="day", y="tip")
plt.title("Boxplot with Ticks Style")
plt.show()


# In[5]:


#2️⃣ Color Palettes
#Seaborn has hundreds of palettes.
#A) Default qualitative palettes
sns.color_palette("deep")
sns.color_palette("muted")
sns.color_palette("pastel")
sns.color_palette("bright")
sns.color_palette("dark")
sns.color_palette("colorblind")


# In[7]:


#Use like this:
sns.set_palette("deep")
sns.countplot(data=df, x="day")
plt.show()


# In[8]:


#B) Sequential palettes (for numeric data)
#Good for heatmaps:
sns.color_palette("Blues")
sns.color_palette("Greens")
sns.color_palette("Oranges")


# In[9]:


#Use in heatmap:
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.show()


# In[10]:


#C) Diverging palettes (good for +/− values)
sns.color_palette("coolwarm")
sns.color_palette("vlag")
sns.color_palette("icefire")
sns.color_palette("seismic")


# In[11]:


#example
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")


# In[12]:


#D) Fancy modern palettes
sns.color_palette("flare")
sns.color_palette("crest")
sns.color_palette("magma")
sns.color_palette("viridis")
sns.color_palette("rocket")


# In[13]:


#example
sns.set_palette("crest")
sns.histplot(data=df, x="total_bill")
plt.title("Histogram with Crest Palette")
plt.show()


# In[14]:


#3️⃣ Custom Palette
#You can manually define colors:
custom = ["#ff7f0e", "#2ca02c", "#1f77b4"]
sns.set_palette(custom)

sns.countplot(data=df, x="day")
plt.title("Custom Color Palette")
plt.show()


# In[15]:


#4️⃣ Figure Aesthetics (Size, Title, Font, Spines)
#A) Figure size
plt.figure(figsize=(10,6))
sns.barplot(data=df, x="day", y="total_bill")
plt.show()


# In[16]:


#B) Removing top & right spines (clean look)
sns.despine()


# In[17]:


#C) Adjust font scale
sns.set_context("talk")     # bigger fonts
sns.set_context("paper")    # small
sns.set_context("poster")   # very big


# In[18]:


#D) Clean professional style example
sns.set_style("whitegrid")
sns.set_palette("pastel")
sns.set_context("talk")

plt.figure(figsize=(10,6))
sns.barplot(data=df, x="day", y="total_bill")
plt.title("Average Total Bill by Day of Week", fontsize=18)
sns.despine()
plt.show()


# In[19]:


#5️⃣ Combining Everything (Professional Chart Example)
sns.set_style("ticks")
sns.set_palette("flare")
sns.set_context("talk")

plt.figure(figsize=(12,6))
sns.violinplot(data=df, x="time", y="total_bill", hue="sex", split=True)
plt.title("Total Bill Distribution by Time and Sex", fontsize=20)
sns.despine()
plt.show()


# In[ ]:




