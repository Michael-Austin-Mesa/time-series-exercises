#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import timedelta, datetime #, strptime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
#from env import user, password, host
#import requests

#import env
import os

from acquire import wrangle_store_data

import warnings
warnings.filterwarnings("ignore")

# plotting defaults
plt.rc('figure', figsize=(13, 7))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)


# In[2]:


def index_time_data(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col).sort_index()
    
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['day of the week'] = df.index.strftime('%A')

    return df


# In[ ]:




