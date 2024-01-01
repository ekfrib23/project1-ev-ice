import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

#cost = 50843
#car='Acura '
#engine='"3.5L 6cyl Turbo 10A"'
year=2023
a = open('edmunds.html').read()
soup = BeautifulSoup(a, features="html.parser")

step=0
location = 1 #1st in list =1
carprices=soup.find_all("div",{"class": "pricing-section"})# model
#carprices=soup.find_all("div",{"class": "col"})# model
for carprice in carprices:
    if step == location-1:
        cost=carprice.text
        cost=cost[-6:]
        cost=cost.replace(",","")
 #       print()
 #       print(cost)
 #   print(carprice)
    step=step+1

tmodels=soup.find_all("h1")# model
for tmodel in tmodels:
 #   print(tmodel)
    car=tmodel.text

car=car[5:-11]
#print(car)

step=0
tmodels=soup.find_all("h2")# model
for tmodel in tmodels:
#    print(tmodel)
    if step == location:
        model=tmodel.text
    step=step+1

model =model.replace("{year} ","")
model=model.split(' (')
#print(f"{model}\n")
car='"'+car+model[0]+'"'
engine = model[1]
engine='"'+engine[:-1]+'"'

#print(car)
tds = soup.find_all('td')
csv_data = []
strings= []

#location=int(location/2)

if location == 1:
    i=-1
else:
    i=location-2
j=i+2
#print((j-1)*48-1)
#print(j*49)
for td in tds:
    if i>(j-1)*49-2:
        if i<j*49:
            inner_text = td.text
#            print(inner_text)

            strings = inner_text.split("\n")
    i=i+1
    if i == 49*j-1: break
    csv_data.extend([string for string in strings if  string])
#    csv_data.extend([string for string in strings if  string])

#print(" ".join(csv_data))

num = np.array(csv_data)
#print(num.size)
reshaped = num.reshape(8,6)
#reshaped = num.reshape(64,6)
new_df=pd.DataFrame(reshaped)
#new_df.drop(new_df.iloc[-1],inplace=True)
new_df.drop(new_df.tail(1).index,inplace=True)
#print(new_df)
index=['Insurance','Maintenance','Repairs','Taxes & Fees','Financing',
       'Depreciation','Fuel']
cost_col = [cost,cost,cost,cost,cost,cost,cost]
year_col = [year,year,year,year,year,year,year]
car_col = [car,car,car,car,car,car,car]
engine_col = [engine,engine,engine,engine,engine,engine,engine]
new_df.insert(loc=0,column='index',value=index)
new_df.insert(loc=7,column='cost',value=cost_col)
new_df.insert(loc=7,column='engine',value=engine_col)
new_df.insert(loc=7,column='car',value=car_col)
new_df.insert(loc=7,column='year',value=year_col)

new_df = new_df.drop(5,axis=1)
print(new_df.to_string(index=False,header=False))
