#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[2]:


# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# In[3]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df.head(10)


# In[4]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df.tail(10)


# In[5]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[6]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[7]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[8]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[9]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[10]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[11]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[12]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[13]:


# Determine data types for the school DataFrame.
school_data_df.dtypes


# In[14]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[15]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
student_data_df.head(10)

