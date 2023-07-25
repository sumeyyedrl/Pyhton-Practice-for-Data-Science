#Python Exercises
# Convert all letters of the given string expression to uppercase. Replace commas and periods with space, word for word
text = "The goal is to turn data into information, and information into insight."
text = text.split()
[word.upper() for word in text]

# Follow the steps below to the list provided.
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Check the number of elements
len(lst)
# Call the elements in the zero and third index 
print(lst[0],lst[10])
# Create ["D", "A", "T", "A"] list
lst[0:4]
# Delete the element in the eighth index
lst.pop(8)
# Add a new element
lst.append("N")
# Add a new element in eighth index
lst.insert(8,"N")

# Follow the steps below to the dictionary provided.
dict={'Christian': ["America",18],
      'Daisy': ["England",12],
      'Antonio': ["Spain",22],
      'Dante': ["Italy",25]}
# Check the key values
dict.keys()
# Check the values
dict.values()
# Update the Daisy key
dict.update({'Daisy':["England",12]})
# Add a new element
dict['Ahmet']=["Turkey",24]
# Delete Antonio from the dictionary
dict.pop('Antonio')
dict


#Write a function that takes a list as an argument, assigns odd and even numbers in the list to separate lists, and returns those lists.
l={2,13,18,93,22}
def func(list):
    even_list=[]
    odd_list=[]
    [even_list.append(i) if i%2==0 else odd_list.append(i) for i in list]
    return even_list,odd_list

even_list, odd_list=func(l)
print(even_list)
print(odd_list)

# Print student degrees for faculty by using enumerate.
students = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
faculty=["Mühendislik Fakültesi","Tıp Fakültesi"]

for i,ogrenci in enumerate(students,1):
    if i<4:
        print(faculty[0] +" "+ str(i) + " . ogrenci: " + ogrenci)
    else:
        print(faculty[1] +" "+ str(i-len(students)) + " . ogrenci: " + ogrenci)

# Given lists include the code, credit and quota information of a course respectively. Print the course information using zip.
ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]
zipped=list(zip(kredi,ders_kodu,kontenjan))
for a,b,c in zipped:
    print(f"Kredisi {str(a)} olan {b} kodlu dersin kontenjanı {str(c)} kişidir.")

# If set 1 contains set 2, define the function that will print the difference of set 2 from set 1 if it does not include its common elements
kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])
if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2-kume1)


##Comprehension
import seaborn as sns
df=sns.load_dataset("car_crashes")
cols=df.columns
# Convert the numeric elements name to uppercase and add NUM in the beginning.
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in cols]
# Find the elements that doesn't include "no" in the name and add Flag in the end.
[col.upper()+"_FLAG" if "no" not in col else col.upper() for col in cols]
# Find the elements that are different from the given list and create a new dataframe.
og_list=["abbrev","no_previous"]
new_cols=set(cols)-set(og_list)
new_df=df[list(new_cols)]
new_df.head()
