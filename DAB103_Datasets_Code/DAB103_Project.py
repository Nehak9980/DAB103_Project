# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:17:36 2023

@author: nehak
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
#import glob

# use glob to get all the excel files 
# in the folder
path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-3:] == 'xls']
files_xls

#Initialize empty dataframe:
df = pd.DataFrame()

#Loop over list of files to append to empty dataframe:
for f in files_xls:
    data = pd.read_excel(f, 'Data')
    df = df.append(data)
    
df

#Subsetting the dataframe
df1 = df.iloc[2:]
df1.columns = df1.iloc[0]

#Renaming columns
df1.rename(
    columns={"Country Name": "Country_Name", "Country Code": "Country_Code", "Indicator Name": "Indicator_Name", "Indicator Code":"Indicator_Code"},
    inplace=True,
)
df1

#Filtering for countries: US, China, UK, India, Sri Lanka, Germany, 
country_filter = ['USA', 'RUS', 'CHN', 'IND', 'GBR','JPN','DEU']
df2 = df1[df1.Country_Code.isin(country_filter)]

#Final Dataset
df3 = pd.concat([df2.iloc[:,:4],df2.iloc[:,-32:]],axis=1)
dfm = pd.melt(df3, id_vars=['Country_Name','Country_Code','Indicator_Name','Indicator_Code'], 
value_vars= df3[1990:2020], value_name="Values",var_name = "Year")
df4 = dfm.drop('Indicator_Code', axis=1)
df5= df4.pivot(index= ['Country_Name','Country_Code','Year'],columns='Indicator_Name', 
               values='Values')
df6 = df5.reset_index(level=['Country_Name', 'Country_Code','Year'])
df6
df6.dtypes
df6.describe()


sns.countplot(x = df5["GDP (current US$)"],data = df5,hue = df5["Country_Name"])
plt.show()

sns.lineplot( x = df5["Year"] ,y = df5["GDP (current US$)"],
                data = df5, hue =df5["Country_Name"] )
plt.show()

#Plot of GDP
sns.set_style("whitegrid")
sns.set_palette("Purples")
sns.set_context("paper")
g = sns.relplot( x = df6["Year"] ,y = df6["GDP (current US$)"],
                data = df6, hue =df6["Country_Name"], 
                style =df6["Country_Name"]
                ,kind ="line" ,
                markers = True,
                dashes= False
                )
g.fig.suptitle("GDP over years", y = 1.05)()
plt.xticks(rotation = 45)
g.set(xlabel="Year(2007-2020)",ylabel="GDP(US$)")
plt.show()

#Plot of GDP per capita
sns.set_style("whitegrid")
sns.set_palette("Purples")
sns.set_context("paper")
g = sns.relplot( x = df6["Year"] ,y = df6["GDP per capita (current US$)"],
                data = df6, hue =df6["Country_Name"], 
                style =df6["Country_Name"]
                ,kind ="line" ,
                markers = True,
                dashes= False
                )
g.fig.suptitle("GDP per Capita", y = 1.05)()
plt.xticks(rotation = 45)
g.set(xlabel="Year(2007-2020)",ylabel="GDP per capita(US$)")
plt.show()






