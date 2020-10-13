#!/usr/bin/python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams.update({'font.size': 20})
from matplotlib.pyplot import figure

ML = "DBSCAN"
outlier = "10"
metric = "e"
titulo = ''+str(ML)+' - Dataset per month - '+str(outlier)+'% Outlier'

data_O10 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O10-"+str(metric)+".csv")
data_O5 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O5-"+str(metric)+".csv")
data_O1 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O1-"+str(metric)+".csv")
data_O0 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O0-"+str(metric)+".csv")

var_recall = [r*100 for r in data_O10.iloc[:,1]] #[Fila,Columna]
var_precision = [r*100 for r in data_O10.iloc[:,2]]
var_FAR = [r*100 for r in data_O10.iloc[:,3]]
var_FS = [r*100 for r in data_O10.iloc[:,4]]

print(var_recall)
print(var_precision)
print(var_FAR)
print(var_FS)

barWidht = 0.16

#plt.figure() 
#plt.figure(figsize=(9,4)) 
figure(num=None, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

r1 = np.arange(len(var_recall))
r2 = [x + barWidht for x in r1]
r3 = [x + barWidht for x in r2]
r4 = [x + barWidht for x in r3]

plt.bar(r1, var_recall, color ='#3366de', width=barWidht, label='Recall')
plt.bar(r2, var_precision, color ='#ff9d00', width=barWidht, label='Precision')
plt.bar(r3, var_FAR, color ='#d43131', width=barWidht, label='False Alarm Rate')
plt.bar(r4, var_FS, color ='#099c0e', width=barWidht, label='F-Score')

plt.xlabel('eps')
plt.xticks([r + barWidht for r in range(len(var_recall))], ["0,01","0,02","0,03","0,04","0,05","0,06","0,07","0,08","0,09","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,8"])
plt.ylabel('Percentage [%]')
#plt.title(titulo)
#plt.legend(loc='lower center', shadow=True, ncol=2)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=4)
plt.tight_layout()
plt.savefig("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Figures/"+str(ML)+"-O"+str(outlier)+"-Month.png")
plt.show()
