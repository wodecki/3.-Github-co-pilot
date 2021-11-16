# import pandas numpy matplotlib and seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

# load 'airbnb_data.csv' into a dataframe
df = pd.read_csv('airbnb_ori.csv')
# make a copy of the dataframe
airbnb = df.copy()

# get airbnb dataframe's info
airbnb.info()
# show airbnb dataframe's dtypes
airbnb.dtypes
# select categorical features from airbnb dataframe
categorical_features = airbnb.select_dtypes(include=['object']).columns
# select numerical features from airbnb dataframe
numerical_features = airbnb.select_dtypes(exclude=['object']).columns
# show categorical features
print(categorical_features)
# show numerical features
print(numerical_features)

# show columns with missing values
airbnb.isnull().sum()
# percentage of missing values
airbnb.isnull().sum()/airbnb.shape[0]
# heatmap of missing values
sns.heatmap(airbnb.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# drop id host_name and last_review
airbnb.drop(['id', 'host_name', 'last_review'], axis=1, inplace=True)

# remove rows with missing values in price
airbnb.dropna(subset=['price'], inplace=True)

# imput price with mean
airbnb['price'].fillna(airbnb['price'].mean(), inplace=True)

# replace null values in review_per_month with 0
airbnb['reviews_per_month'].fillna(0, inplace=True)

# identify spelling issues in neighborhood_group

airbnb['neighbourhood_group'].value_counts()
# convert last_review to datetime
airbnb['last_review'] = pd.to_datetime(airbnb['last_review'])


