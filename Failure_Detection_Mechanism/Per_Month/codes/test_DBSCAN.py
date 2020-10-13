#!/usr/bin/python
#TEST DBSCAN Per-Month
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import confusion_matrix

percent = "10"
print("Inicio Test: DBSCAN dataset con "+str(percent)+"% outliers")
#df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/DB/month_TAM.csv")
df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/DB/month_TAM-O"+str(percent)+".csv")

value = 'Test_1'
data_init = df[['timestamp','value_temp',value]]
data = data_init.copy()
stscaler = StandardScaler().fit(data[[value]])
data1 = stscaler.transform(data[[value]])

#cont = ["01","02","03","04","05","06","07","08"]
#cont_eps = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
cont = ["001","002","003","004","005","006","007","008","009"]
cont_eps = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]

#cont = ["08"]
#cont_eps = [0.8]

for w,y in zip(cont,cont_eps) :
    print(w)
    print(y)
    outlier_detection = DBSCAN(
        eps = y, 
        metric="euclidean", 
        min_samples = 3,
        n_jobs = -1)
    clusters = outlier_detection.fit_predict(data1)
    #print(pd.Series(clusters))
    outlier_cluster = [int(-1) if i != 0 else i for i in pd.Series(clusters)]
    data['cluster']=pd.Series(clusters)
    data['outlier']=pd.Series(outlier_cluster)
    a = data['value_temp'].tolist()
    b = data[value].tolist()
    comparison = [-1 if i != j else 0 for i,j in zip(a,b)]
    comp = pd.Series(comparison)
    comp_list = comp.tolist()
    clus_list = outlier_cluster
    cm = confusion_matrix(comp_list, clus_list, labels=[-1,0])
    print(cm)

    #data.to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_DBSCAN/2019-11-O"+str(percent)+"-e"+str(w)+"-ms3.csv", index = False, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_DBSCAN/2019-11-O"+str(percent)+"-e"+str(w)+"-ms3.csv")
    #pd.DataFrame(cm).to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_DBSCAN/2019-11-O"+str(percent)+"-e"+str(w)+"-ms3-cm.csv", index = True, header=True)
    print("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_DBSCAN/2019-11-O"+str(percent)+"-e"+str(w)+"-ms3-cm.csv")
                                                        
print("Fin Test")