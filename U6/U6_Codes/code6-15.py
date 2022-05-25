# -*- coding: utf-8 -*-   [   Code 6-15:    RFM  +  Kmeans    +  Quantile  +  Evaluation   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sklearn.cluster import KMeans
from sklearn import metrics


color = sns.color_palette()
data = pd.read_excel('c:/Pyfiles/Online_Retail001.xlsx')

pd.set_option('display.max_columns', None)

testeddate = '2011/12/31'
NOW = datetime.datetime.strptime(testeddate,'%Y/%m/%d')

data['Total_Price'] = data['Quantity']*data['UnitPrice']

data['Order_Date'] = pd.to_datetime(data['InvoiceDate'])

data = data[data.Quantity > 0]
data = data[data.UnitPrice > 0]
data = data[data.iloc[:, :] != '']

# this shows that UK has the hightest number of customers followed by germany and france.
# RFM
# Recency

Cust_UK=data[data['Country']=="United Kingdom"]
# Cust_UK=Cust_UK[['CustomerID','Order_Date']].drop_duplicates()
# print(Cust_UK)          # 5291/10000 rows   

rfmTable = Cust_UK.groupby('CustomerID').agg({'Order_Date': lambda x: (NOW - x.max()), # Recency
                                        'InvoiceNo': lambda x: len(x),               # Frequency
                                        'Total_Price': lambda x: x.sum()})          # Monetary Value
#  print(rfmTable)     #   2130 rows x 3 columns 

rfmTable.rename(columns={'Order_Date': 'recency', 
                         'InvoiceNo': 'frequency', 
                         'Total_Price': 'monetary_value'}, inplace=True)

Cust_country=data[['CustomerID', 'Country']].drop_duplicates()
Cust_country_count=Cust_country.groupby(['Country'])['CustomerID'].aggregate('count').reset_index().sort_values(by='CustomerID', ascending=0)
print(Cust_country_count)


rfmTable['recency'] = rfmTable['recency'].astype('timedelta64[D]')

print(rfmTable)

quantiles = rfmTable.quantile(q=[0.2,0.4,0.6,0.8])
print(quantiles)
quantiles = quantiles.to_dict()
print(quantiles)
rfmSegmentation = rfmTable

# Arguments (x = value, p = recency, d = monetary_value, frequency, k = quartiles dict)

def RClass(x,p,d):
    if x <= d[p][0.2]:
        return 1
    elif x <= d[p][0.4]:
        return 2
    elif x <= d[p][0.6]: 
        return 3
    elif x <= d[p][0.8]:
        return 4
    else:
        return 5
# --------------------------------------------------------------------------------------------------------------------------#    

# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)

def FMClass(x,p,d):
    if x <= d[p][0.2]:
        return 5
    elif x <= d[p][0.4]:
        return 4
    elif x <= d[p][0.6]: 
        return 3
    elif x <= d[p][0.8]: 
        return 2    
    else:
        return 1
 

rfmSegmentation['Recency_Flag'] = rfmSegmentation['recency'].apply(RClass, args=('recency',quantiles,))
rfmSegmentation['Freq_Flag'] = rfmSegmentation['frequency'].apply(FMClass, args=('frequency',quantiles,))
rfmSegmentation['Monetary_Flag'] = rfmSegmentation['monetary_value'].apply(FMClass, args=('monetary_value',quantiles,))

print(rfmSegmentation)


# Show Frequences of RFM
plt.figure(figsize=(12,8))
sns.countplot(x="Recency_Flag", data=rfmSegmentation, color=color[1])
plt.ylabel('Count', fontsize=15)
plt.xlabel('Recency_Flag', fontsize=15)
plt.xticks(rotation='vertical')
plt.title("Frequency of Recency_Flag", fontsize=20)
plt.show()

plt.figure(figsize=(12,8))
sns.countplot(x="Freq_Flag", data=rfmSegmentation, color=color[1])
plt.ylabel('Count', fontsize=15)
plt.xlabel('Freq_Flag', fontsize=15)
plt.xticks(rotation='vertical')
plt.title("Frequency of Freq_Flag", fontsize=20)
plt.show()

plt.figure(figsize=(12,8))
sns.countplot(x="Monetary_Flag", data=rfmSegmentation, color=color[1])
plt.ylabel('Count', fontsize=15)
plt.xlabel('Monetary_flag', fontsize=15)
plt.xticks(rotation='vertical')
plt.title("Frequency of Monetary_flag", fontsize=20)
plt.show()


Cust_UK_All = rfmSegmentation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#finding rfm

#finding finding final score i.e sum of all flags

recency_weight = 5
frequency_weight = 4
monetary_weight = 3

Cust_UK_All['score'] = recency_weight*Cust_UK_All['Recency_Flag'] + frequency_weight*Cust_UK_All['Freq_Flag'] + monetary_weight*Cust_UK_All['Monetary_Flag'];

# Cust_UK_All = Cust_UK_All.sort_values(by='score', ascending=0)
# print(Cust_UK_All)
X = Cust_UK_All.iloc[:, 3:6].values
# X = Cust_UK_All['Recency_Flag', 'Freq_Flag', 'Monetary_Flag'] 


# Silhouette Evaluation with Pictures ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig = plt.figure(figsize=(10,8))
silhouette_avg = []
for i in range(2,11):
    kmeans_fit = KMeans(n_clusters=i, init ='k-means++', max_iter=300,  n_init=10,random_state=0).fit(X)
    silhouette_avg.append(metrics.silhouette_score(X, kmeans_fit.labels_))
       
#   print(silhouette_avg)
plt.plot(range(2, 11), silhouette_avg, 'bx-')
plt.title('silhouette')
plt.xlabel('No of clusters')
plt.ylabel('Avg')
plt.show()


# WCSS Evaluation with Pictures ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig = plt.figure(figsize=(10,8))
wcss =[]
for i in range(2, 11):
  kmeans = KMeans(n_clusters=i, init ='k-means++', max_iter=300,  n_init=10,random_state=0).fit(X)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)


plt.plot(range(2, 11), wcss, 'bx-')
plt.title('Elbow method')
plt.xlabel('No of clusters')
plt.ylabel('WCSS')
plt.show()


# print(X)
kmeans_fit = KMeans(n_clusters=6, init ='k-means++', max_iter=300,  n_init=10,random_state=0).fit(X)
k_labels = kmeans_fit.labels_
print(" Clustering results ：")
# print(k_labels)
Cust_UK_All['Cluster'] = k_labels
Cust_UK_All = Cust_UK_All.sort_values(by='Cluster', ascending=0)
print(Cust_UK_All)
Cust_UK_All.to_excel('c:/Pyfiles/saved_Cust_UK_All.xlsx')  
