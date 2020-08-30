### EDA - EXPLORATORY DATA ANALYSIS ###
## Importing necessary Libraries ##

import pandas as pd
import matplotlib.pyplot as plt

## Importing and Studying Dataset ##

dataset = pd.read_csv('transaction_data.csv') #Dataset Imported

# Viewing Details about Dataset
dataset.head()#returns few top rows(by default 5)  
dataset.columns#returns column names
dataset.describe()#describe the numerical things of staticial data

## Data Cleaning ##

dataset.isna().any()#it returns a boolean value for missing field
dataset.isna().sum()
#drop()- it deletes the column 
dataset = dataset.drop(columns = ['ItemDescription'])
dataset.isna().any()
dataset.isna().sum()

## Data Visualization ##

#Visualization of dataset[country=all]
dataset_country=dataset[['Country']]
dataset_country_list= list(map(str,dataset_country['Country']))
dataset_country_dict= {}
for i1 in dataset_country_list:
    if i1 in dataset_country_dict: dataset_country_dict[i1]+=1
    else: dataset_country_dict[i1]=1
plt.figure(figsize=(10, 10))
plt.pie(dataset_country_dict.values(), labels=dataset_country_dict.keys(),autopct='%1.1f%%')
plt.title("Pie Chart Showing frequency of customers in different Countries")
plt.axis('equal')
plt.show()

#Visualization of dataset[country!=UK]
dataset_country_rest = dataset[dataset.Country != 'United Kingdom'][['Country']]
dataset_country_rest_list= list(map(str,dataset_country_rest['Country']))
dataset_country_rest_dict= {}
for i1 in dataset_country_rest_list:
    if i1 in dataset_country_rest_dict: dataset_country_rest_dict[i1]+=1
    else: dataset_country_rest_dict[i1]=1
plt.figure(figsize=(10, 10))
plt.pie(dataset_country_rest_dict.values(), labels=dataset_country_rest_dict.keys(),autopct='%1.1f%%')
plt.title("Pie Chart Showing frequency of customers in different Countries (excluding United Kingdom")
plt.axis('equal')
plt.show()



dataset2 = dataset[dataset.Country == 'United Kingdom']

#Visualization of dataset of UK with UserId#
dataset2_user = dataset2[['UserId']]
dataset2_user_list= list(map(int,dataset2_user['UserId']))
dataset2_user_dict={}
for i2 in dataset2_user_list:
    if i2 in dataset2_user_dict: dataset2_user_dict[i2]+=1
    else: dataset2_user_dict[i2]=1
dataset2_user_segment_Type = []
dataset2_user_segment_Name = ['Active Customers','Decent Customers','Least Active Customers']
temp=list(dataset2_user_dict.values())
sum1_user=0
sum2_user=0
sum3_user=0
for i3 in temp:
    if(i3>=400):sum1_user+=i3
    if(i3<400 and i3>=100):sum2_user+=i3
    if(i3<100):sum3_user+=i3
dataset2_user_segment_Type.append(sum1_user)
dataset2_user_segment_Type.append(sum2_user)
dataset2_user_segment_Type.append(sum3_user)
plt.figure(figsize=(10, 10))
plt.pie(dataset2_user_segment_Type, labels=dataset2_user_segment_Name,autopct='%1.1f%%')
plt.title("Frequency of customers actively purchasing items in United Kingdom")
plt.axis('equal')
plt.show()
    
#Visualization of dataset of UK with ItemCode#

dataset2_item = dataset2[['ItemCode']]
dataset2_item_list= list(map(int,dataset2_item['ItemCode']))
dataset2_item_dict={}
for i4 in dataset2_item_list:
    if i4 in dataset2_item_dict: dataset2_item_dict[i4]+=1
    else: dataset2_item_dict[i4]=1
dataset2_item_segment_Type = []
dataset2_item_segment_Name = ['Mostly in Demand','Average in Demand','Least in Demand']
temp1=list(dataset2_item_dict.values())
sum1_item=0
sum2_item=0
sum3_item=0
for i5 in temp1:
    if(i5>=400):sum1_item+=i5
    if(i5<400 and i5>=100):sum2_item+=i5
    if(i5<100):sum3_item+=i5
dataset2_item_segment_Type.append(sum1_item)
dataset2_item_segment_Type.append(sum2_item)
dataset2_item_segment_Type.append(sum3_item)
plt.figure(figsize=(10, 10))
plt.pie(dataset2_item_segment_Type, labels=dataset2_item_segment_Name,autopct='%1.1f%%')
plt.title("FFrequency of items in demand in United Kingdom")
plt.axis('equal')
plt.show()

#Visualization of both simultaneously#
data = {"Items in Demand":dataset2_item_segment_Type,        
        "Active User":dataset2_user_segment_Type        
        };
index = ["High", "Average", "Low"];
compare = pd.DataFrame(data=data, index=index);
compare.plot.bar(rot=15, title="Visualization Based on Items in Demand and Active User");
plt.show(block=True);

##Result Calculation##

dataset_result1_1= dataset[dataset['Country'] =='Germany']
dataset_result1_2= dataset[dataset['Country'] =='France']
dataset_result1_3= dataset[dataset['Country'] =='EIRE']
dataset_result1 = pd.concat([dataset_result1_1, dataset_result1_2, dataset_result1_3])
result1=dataset_result1[['UserId']]

dataset_result2_1= dataset[dataset['Country'] == 'Spain']
dataset_result2_2= dataset[dataset['Country'] == 'Belgium']
dataset_result2_3= dataset[dataset['Country'] == 'Netherlands']
dataset_result2_4= dataset[dataset['Country'] == 'Switzerland']
dataset_result2_5= dataset[dataset['Country'] == 'Portugal']
dataset_result2_6= dataset[dataset['Country'] == 'Australia']
dataset_result2 = pd.concat([dataset_result2_1, dataset_result2_2, dataset_result2_3, 
                             dataset_result2_4, dataset_result2_5, dataset_result2_6])
result2=dataset_result2[['UserId']]
result_final=pd.concat([result1,result2],keys=['A(above 10%)','B(Below 10%)'])
result_final=result_final[result_final['UserId']!=-1]
result_final.to_csv('Final_result.csv', index = False)


