#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix

percent = "10"
hour = "Omicron_12h"
print("Inicio Test: IsolationForest dataset con "+str(percent)+"% outliers")
df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/DB_Hours/"+str(hour)+"-O"+str(percent)+".csv")

value = 'Test_1'
data_init = df[['timestamp','value_temp',value]]
data = data_init.copy()
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data[[value]])
data1 = pd.DataFrame(np_scaled)

cont = ["0","001","002","003","004","005","006","007","008","009","01","02","03","04","05"]
cont_c = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5]

for w,y in zip(cont,cont_c) :
    print(w)
    print(y) 

    outliers_fraction = y # [0, 0.5]
    
    model =  IsolationForest(contamination=outliers_fraction)
    model.fit(data1) 
    df['anomaly2'] = pd.Series(model.predict(data1))
    data['cluster']=df['anomaly2']
    a = data['value_temp'].tolist()
    b = data[value].tolist()
    comparison = [-1 if i != j else 1 for i,j in zip(a,b)]
    comp = pd.Series(comparison)
    comp_list = comp.tolist()
    clus_list = data['cluster'].tolist()
    cm = confusion_matrix(comp_list, clus_list, labels=[-1,1])
    print(cm)
    
    data.to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Result_IF/"+str(hour)+"-O"+str(percent)+"-c"+str(w)+".csv", index = False, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Result_IF/"+str(hour)+"-O"+str(percent)+"-c"+str(w)+".csv")
    pd.DataFrame(cm).to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Result_IF/"+str(hour)+"-O"+str(percent)+"-c"+str(w)+"-cm.csv", index = True, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Result_IF/"+str(hour)+"-O"+str(percent)+"-c"+str(w)+"-cm.csv")
                                                        
print("Fin Test")                                                    