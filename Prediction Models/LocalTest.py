#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


import numpy as np


# In[3]:


model1 = pickle.load(open('model.pkl', 'rb'))


# In[7]:


pip install scikit-learn==1.0.2


# In[4]:


features = np.array([[46.56,0,0,0,0.0,0.0,0,0,12,0,1,2,8.0,0,0,0]])
pred = model1.predict(features)
print(pred)


# In[5]:


features = np.array([[28.07,0,1,0,0.0,0.0,0,1,11,0,1,4,8.0,0,0,1]])
pred1 = model1.predict(features)
print(pred1)


# In[6]:


features = np.array([[23.38,0,0,0,0.0,0.0,0,0,8,0,1,4,6.0,0,0,0]])
pred12 = model1.predict(features)
print(pred12)


# In[ ]:




