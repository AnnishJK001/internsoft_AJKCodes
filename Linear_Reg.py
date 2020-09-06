# -*- coding: utf-8 -*-
"""


@author: AnnishJK
"""
#importing thr libraries

import pandas as pd
import matplotlib.pyplot as plt


#Reading the dataset
data = pd.read_csv('advertising.csv')


#visualize

fig , axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x= 'TV',y='Sales',ax=axs[0],figsize=(14,7))
data.plot(kind='scatter',x= 'Radio',y='Sales',ax=axs[1],figsize=(14,7))
data.plot(kind='scatter',x= 'Newspaper',y='Sales',ax=axs[2],figsize=(14,7))

#create X and Y for linear regression

feature_cols = ['TV']
X=data [feature_cols]
y=data.Sales


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, y)


print(lr.intercept_) 
print(lr.coef_)



print(lr.predict([[50]]))

#create a dataframe with min and max values

x_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
#print(x_new.head())
print(x_new)


preds  = lr.predict(x_new)
print(preds)

data.plot(kind = 'scatter',x = 'TV',y = 'Sales')
plt.plot(x_new,preds,c='red',linewidth=2)

#stats model
import  statsmodels.formula.api as smf
lm = smf.ols(formula = 'Sales ~ TV',data=data).fit()
print(lm.conf_int())



#finding th probability
print(lm.pvalues)

#finding the rsquare value
print(lm.rsquared)

#multi linear regression
feature_cols = ['TV','Radio','Newspaper']
x=data[feature_cols]
y= data.Sales

lr = LinearRegression()
lr.fit(x,y)

print(lr.intercept_)
print(lr.coef_)

#statsmodel
lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
print(lm.conf_int())
print(lm.summary())

lm = smf.ols(formula='Sales ~ TV+Radio',data=data).fit()
print(lm.conf_int())
print(lm.summary())