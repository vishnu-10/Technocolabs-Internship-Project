#!/usr/bin/env python
# coding: utf-8

# **Run the two cells below before you begin. These will set the notebook to autosave every 10 seconds, import the necessary libraries for this challenge, and set figure appearance.**

# In[1]:


get_ipython().run_line_magic('autosave', '10')


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

mpl.rcParams['figure.dpi'] = 400
mpl.rcParams['font.size'] = 4


# **To begin, import data set `cleaned_data.csv` and create lists of feature names for the remaining financial features: `'BILL_AMT1'`, `'BILL_AMT2'`, `'BILL_AMT3'`, `'BILL_AMT4'`, `'BILL_AMT5'`, `'BILL_AMT6'`,  `'PAY_AMT1'`, `'PAY_AMT2'`, `'PAY_AMT3'`, `'PAY_AMT4'`, `'PAY_AMT5'`, and `'PAY_AMT6'`.**
# 
# **Name the features `bill_feats` and `pay_amt_feats`, respectively.**

# In[5]:


# Import the dataset
data=pd.read_csv(r'C:\Users\Shridhar\Desktop\cleaned_data.csv')
data


# In[8]:


# Create lists `bill_feats` and `pay_amt_feats`
bill_feats=['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']
pay_amt_feats=['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']


# ____________________________________________________________________________________
# **Next, use `.describe()` to examine statistical summaries of the bill amount features**
# 

# In[17]:


data[bill_feats].describe()


# Reflect on what you see. Does it make sense?

# ___________________________________________________________________________________
# **Then you should visualize the bill amount features using a 2 by 3 grid of histogram plots.**
# > Hint: You can use 20 bins for this visualization.

# In[16]:


data[bill_feats].hist(bins=20,layout=(2,3))


# ________________________________________________________________________
# **Next, obtain the `.describe()` summary of the payment amount features.**
# 

# In[18]:


data[pay_amt_feats].describe()


#     Does this make sense?

# _______________________________________________________________________________________
# **Next, plot a histogram of the bill payment features similar to the bill amount features, 
# but also apply some rotation to the x-axis labels with the `xrot` keyword argument 
# so that they don't overlap. In any plotting function, you can include the `xrot=<angle>`
# keyword argument to rotate x-axis labels by a given angle in degrees.**
# 

# In[91]:


pay_1_bins = np.array(range(-2,10))
data[pay_amt_feats].hist(bins=pay_1_bins,layout=(2,3),xrot=15)


#     Consider these results.

# ______________________________________________________________________________________________
# **Then, use a Boolean mask to see how many of the payment amount data are exactly equal to 0. Review the results of the generated mask using `.head()` and `.sum()`.**
# 
# 

# In[54]:


# Create Boolean mask
zero_pmt=data.loc[(data['PAY_AMT1']==0)&(data['PAY_AMT2']==0)&(data['PAY_AMT3']==0)&(data['PAY_AMT4']==0)&(data['PAY_AMT5']==0)&(data['PAY_AMT6']==0),['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']]



# In[55]:


# Use `.head()`
zero_pmt.head()


# In[57]:


# Use `.sum()`
zero_pmt.count().sum()


#      Does this make sense given the histogram in the previous step?

# _______________________________________________________________________________________________________________________________
# **Finally, ignoring the payments of 0 using the mask you created in the previous step, use pandas `.apply()` and NumPy's `np.log10()` to plot histograms of logarithmic transformations of the non-zero payments.**
# > Hint: You can use `.apply()` to apply any function, including `log10`, to all the elements of a DataFrame or a column using the following syntax: `.apply(<function_name>)`.

# In[92]:


import numpy as np
payments=data.loc[:,['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']]
payments.apply(np.log10)
pay_1_bins = np.array(range(-2,10))
payments.hist(bins=pay_1_bins,layout=(2,3),xrot=15)

