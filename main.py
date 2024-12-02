#importing pandas 
import pandas as pd
#importing numpy
import numpy as np
#importing statistics
#reading the dataframe
df=pd.read_csv('bt.csv')
print(df.info())
#checking for any null values
df.isnull().any()
#bin values of user rating into categories good and excellent
ratings_of_user=[1,2,3,4,5]
df['binuserrate']=pd.cut(df['User Rating'],ratings_of_user)

user_rating_labels=['terrible','bad','fine','good','excellent']
df['binage']=pd.cut(df['User Rating'],ratings_of_user,labels=user_rating_labels)
print(df['binuserrate'])
#i also took some help in this skipna part from the internet as i was not sure on the format.
#i am not sure of the skipna part
df.skew(axis = 1, skipna = True)
#checking the minimum rate
minrate=df.min(df['User Rating'])
print("the minimum user rating is " ,minrate)