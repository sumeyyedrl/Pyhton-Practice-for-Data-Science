import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("datasets/persona.csv")
df.head()
df.shape
df.info
df.dtypes
df.isnull().sum()

pd.DataFrame({"Source": df["SOURCE"].value_counts(),
              "Ratio": 100*df["SOURCE"].value_counts()/len(df)})

df["PRICE"].nunique()

df["PRICE"].value_counts()

df["COUNTRY"].value_counts()

df.groupby("COUNTRY")["PRICE"].sum()

df["SOURCE"].value_counts()

df.groupby("COUNTRY")["PRICE"].mean()

df.groupby("SOURCE")["PRICE"].mean()

df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean()

agg_df=df.groupby(["COUNTRY","SOURCE","SEX","AGE"])["PRICE"].mean()
agg_df=agg_df.reset_index()
agg_df = agg_df.sort_values("PRICE",ascending=False)
agg_df.head()

agg_df["AGE_CUT"]=pd.cut(agg_df["AGE"],[0,18,23,30,40,70], labels=["0_18","19_23","24_30","31_40","41_70"])
agg_df.head()

agg_df["CUSTOMER_LEVEL_BASED"]=["_".join(i).upper()  for i in agg_df.drop(["AGE","PRICE"], axis=1).values]
agg_df.head()

agg_df["SEGMENT"]= pd.qcut(agg_df["PRICE"],4,labels=["D","C","B","A"])
agg_df.head()

agg_df.groupby("SEGMENT").agg({"PRICE":["mean","max","sum"]})

new_user1="TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["CUSTOMER_LEVEL_BASED"]==new_user1]
new_user2="FRA_IOS_FEMALE_31_40"
agg_df[agg_df["CUSTOMER_LEVEL_BASED"]==new_user2]