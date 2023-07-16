#Python Exercises
# 2
text = "The goal is to turn data into information, and information into insight."
text = text.split()
[word.upper() for word in text]

# 3
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
print(lst[0],lst[10])
lst[0:4]
lst.pop(8)
lst.append("N")
lst.insert(8,"N")

#4
dict={'Christian': ["America",18],
      'Daisy': ["England",12],
      'Antonio': ["Spain",22],
      'Dante': ["Italy",25]}
dict.keys()
dict.values()
dict.update({'Daisy':["England",12]})
dict['Ahmet']=["Turkey",24]
dict.pop('Antonio')
dict


#5
l={2,13,18,93,22}
def func(list):
    even_list=[]
    odd_list=[]
    [even_list.append(i) if i%2==0 else odd_list.append(i) for i in list]
    return even_list,odd_list

even_list, odd_list=func(l)
print(even_list)
print(odd_list)

#6
ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
fakulte=["Mühendislik Fakültesi","Tıp Fakültesi"]

for i,ogrenci in enumerate(ogrenciler,1):
    if i<4:
        print(fakulte[0] +" "+ str(i) + " . ogrenci: " + ogrenci)
    else:
        print(fakulte[1] +" "+ str(i-3) + " . ogrenci: " + ogrenci)

#7
ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]
zipped=list(zip(kredi,ders_kodu,kontenjan))
for a,b,c in zipped:
    print(f"Kredisi {str(a)} olan {b} kodlu dersin kontenjanı {str(c)} kişidir.")

#8
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

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in cols]

[col.upper()+"_FLAG" if "no" not in col else col.upper() for col in cols]

og_list=["abbrev","no_previous"]
new_cols=set(cols)-set(og_list)
new_df=df[list(new_cols)]
new_df.head()
