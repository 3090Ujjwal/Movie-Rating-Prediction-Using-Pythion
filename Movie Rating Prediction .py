#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


# In[3]:


movies = pd.read_csv('IMDb Movies India.csv', encoding='latin1')
OrgData=movies
movies


# In[4]:


movies.shape


# In[5]:


movies.info


# In[6]:


movies.isnull().sum(axis=0).sort_values(ascending=False)


# In[7]:


movies.isnull().sum(axis=1).sort_values(ascending=False)


# In[8]:


movies.isnull().sum(axis=0).sort_values(ascending=False)/len(movies)*100


# In[9]:


movies


# In[10]:


round(movies.isnull().sum().sort_values(ascending=False)/len(movies)*100,2)


# In[11]:


movies = movies[movies['Actor_1'].notnull()]
movies = movies[movies['Actor_2'].notnull()]


# In[12]:


(movies.isnull().sum(axis=1).sort_values(ascending=False) >5).sum()


# In[13]:


movies=movies[movies.isnull().sum(axis=1).sort_values(ascending=False) <=5]
movies


# In[14]:


round(movies.isnull().sum().sort_values(ascending=False)/len(movies)*100,2)


# In[15]:


movies.groupby('Actor_3').Actor_3.count().sort_values(ascending=False)


# In[16]:


movies.Actor_3.describe()


# In[17]:


movies.Actor_3 = movies.Actor_3.fillna('Pran')


# In[18]:


round(movies.isnull().sum().sort_values(ascending=False)/len(movies)*100,2)


# In[19]:


len(movies)/len(OrgData)*100


# In[20]:


movies.info()


# In[21]:


movies['Actor_3']
movies['Actor_2']


# In[22]:


movies


# In[23]:


movies.sort_values(by='Actor_3',ascending=False)


# In[24]:


top10 = movies.sort_values(by='Actor_3',ascending=False) .head(10)
top10


# In[25]:


movies.drop_duplicates(keep='first',inplace=True)


# In[26]:


movies


# In[27]:


movies['Genre'].str.split('|', expand=True)


# In[28]:


movies=pd.concat([movies,movies['Genre']],axis=1)
movies


# In[30]:


Manmauji=movies[movies['Actor_1']=='Manmauji']
Rasika_Dugal=movies[movies['Actor_1']=='Rasika_Dugal']
Prateik=movies[movies['Actor_1']=='Prateik']


# In[32]:


Manmauji


# In[ ]:




