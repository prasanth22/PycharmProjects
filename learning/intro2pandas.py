import pandas as pd
XYZ_web = {'day':[1,2,3,4,5,6],
           "visitors":[1000,700,6000,1000,400,35],
           "Bounce_rate":[20,20,23,15,10,34]}
df = pd.DataFrame(XYZ_web)
print(df)
#slicing
print(df.head(2))
print(df.tail(2))
#merging
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Ind_rate":[2,1,2,3],"Ind_gdp":[50,45,45,67]},index=[2001,2002,2003,2004])
df2 = pd.DataFrame({"HPI":[80,90,70,60],"Ind_rate":[2,1,2,3],"Ind_gdp":[50,45,45,67]},index=[2005,2006,2007,2008])
print(pd.merge(df1,df2,on="HPI"))
#concatnate
print(pd.concat(df1,df2))
#joining
df3 = pd.DataFrame({"Ind_rate":[2,1,2,3],"Ind_gdp":[50,45,45,67]},index=[2001,2002,2003,2004])
df4 = pd.DataFrame({"low_tier_HPI":[50,45,45,67],"unemployment":[1,3,5,6]},index=[2001,2003,2004,2005])
join= df3.join(df4)
print(join)
