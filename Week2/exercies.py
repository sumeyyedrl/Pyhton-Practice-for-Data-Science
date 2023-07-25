import seaborn as sns
import pandas as pd

# import titanic dataset from seaborn
df=sns.load_dataset("titanic")

# Find the number of men and women passengers
df["sex"].value_counts()

# Find the number of unique values
df.nunique()

# Find the number of unique values in pclass
df["pclass"].nunique()

# Find the number of unique values in pclass and parch
df[["pclass","parch"]].nunique()

# Check the type of embarked and change it to category
df["embarked"].dtype
df["embarked"]=df["embarked"].astype("category")
df["embarked"].dtype

#Get the data where embarked value is C
df[df["embarked"]=="C"]

#Get the data where embarked value is not S
df[df["embarked"]!="S"]

#Get the data where women that are younger than 30
df[(df["age"]<30) & (df["sex"]=="female")]

#Get the data where Fare greater than 500 or older than 70
df[(df["fare"]>500) | (df["age"]>70)]

#Find the sum of null values element by elemnt
df.isnull().sum()

#Delete who from dataframe
df.drop("who",axis=1,inplace=True)
df.columns

#Fill the null values in deck with mode of deck
df["deck"].fillna(value=(df["deck"].mode()[0]),inplace=True)
df.deck.isnull().any()

#Fill the null values in age with median of age
df["age"].fillna(value=(df["age"].median()),inplace=True)
df.deck.isnull().any()

#Find the sum, count, mean values of the survived variable grouped by pclass and gender
df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})

#Create a new element called age_flag. Give 1 for the people who are younger than 30 and 0 to others
df["age_flag"]=df["age"].apply(lambda x : 1 if x<30 else 0)
df["age_flag"]

# import tips dataset from seaborn
data=sns.load_dataset("tips")
data.head()

#Find the sum, min, max, mean values of the total_bill variable grouped by time
data.groupby("time")["total_bill"].agg(["sum","min","max","mean"])

#Find the sum, min, max, mean values of the total_bill variable grouped by time and day
data.groupby(["time","day"])["total_bill"].agg(["sum","min","max","mean"])

#Find the sum, min, max and average of the total_bill and type values of lunch time and female customers according to day
data.loc[(data["time"]=="Lunch")&(data["sex"]=="Female")].groupby("day")["total_bill","tip"].agg(["sum","min","max","mean"])

#what is the average of orders with size less than 3 and total_bill greater than 10
data.loc[(data["size"]<3)&(data["total_bill"]>10),"total_bill"].mean()

#Create total_bill_tip_sum element that is sum of total_bill and tip
data["total_bill_tip_sum"]=data["total_bill"]+data["tip"]

#Sort total_bill_tip_ by sum variable from largest to smallest and assign the first 30 contacts to a new dataframe
new_data=data.sort_values("total_bill_tip_sum",ascending=False).head(30)
new_data.head()