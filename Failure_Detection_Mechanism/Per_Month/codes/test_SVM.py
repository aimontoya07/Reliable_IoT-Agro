#!/usr/bin/python
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

percent = "10"
print("Inicio Test: SVM dataset con "+str(percent)+"% outliers")
#df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/DB/month_TAM.csv")
df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/DB/month_TAM-O"+str(percent)+".csv")

value = 'Test_1'
data_init = df[['timestamp','value_temp',value]]
data = data_init.copy()
scaler = StandardScaler()
np_scaled = scaler.fit_transform(data[[value]])
data1 = pd.DataFrame(np_scaled)

cont = ["001","002","003","004","005","006 ","007","008","009","01"]
cont_nu = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]

for w,y in zip(cont,cont_nu) :
    print(w)
    print(y) 
    outliers_fraction = y #(0, 1]. By default 0.5 will be taken.
    model = OneClassSVM(nu=outliers_fraction, kernel="rbf", gamma=0.01)
    model.fit(data1)
    df['anomaly3'] = pd.Series(model.predict(data1))
    data['outlier']=df['anomaly3']
    a = data['value_temp'].tolist()
    b = data[value].tolist()
    comparison = [-1 if i != j else 1 for i,j in zip(a,b)]
    comp = pd.Series(comparison)
    comp_list = comp.tolist()
    clus_list = data['outlier'].tolist()

    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(comp_list, clus_list, labels=[-1,1])
    print(cm)

    data.to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_SVM/2019-11-O"+str(percent)+"-nu"+str(w)+".csv", index = False, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_SVM/2019-11-O"+str(percent)+"-nu"+str(w)+".csv")
    pd.DataFrame(cm).to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_SVM/2019-11-O"+str(percent)+"-nu"+str(w)+"-cm.csv", index = True, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_SVM/2019-11-O"+str(percent)+"-nu"+str(w)+"-cm.csv")
                                                        
print("Fin Test")