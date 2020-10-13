#!/usr/bin/python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ML = "IF"
outlier = "5"
metric = "c"
titulo = 'Isolation Forest - Dataset per day (06/01/20) - '+str(outlier)+'% Outlier'
#titulo = 'Isolation Forest - Dataset per day (06/01/20) - '+str(outlier)+'% Outlier**'
#titulo = ''+str(ML)+' - Dataset per day 06/01/20'
#print(titulo)

data_O10 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O10-"+str(metric)+".csv")
data_O5 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O5-"+str(metric)+".csv")
data_O1 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O1-"+str(metric)+".csv")
data_O0 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O0-"+str(metric)+".csv")

# data_O10 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O10-"+str(metric)+".csv")
# data_O5 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O5-"+str(metric)+".csv")
# data_O1 = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Result_"+str(ML)+"/2020_01_06-O1-"+str(metric)+".csv")

#print(data_O10)

# 2020_01_06-O5-e.csv
# var_recall = [r for r in data_O1.iloc[0,1:]]
var_recall = [r*100 for r in data_O5.iloc[:,1]] #[Fila,Columna]
var_precision = [r*100 for r in data_O5.iloc[:,2]]
var_FAR = [r*100 for r in data_O5.iloc[:,3]]
var_FS = [r*100 for r in data_O5.iloc[:,4]] 

print(var_recall)
print(var_precision)
print(var_FAR)
print(var_FS)

barWidht = 0.15

plt.figure(figsize=(10,5))

r1 = np.arange(len(var_recall))
r2 = [x + barWidht for x in r1]
r3 = [x + barWidht for x in r2]
r4 = [x + barWidht for x in r3]

plt.bar(r1, var_recall, color ='#3366de', width=barWidht, label='Recall')
plt.bar(r2, var_precision, color ='#ff9d00', width=barWidht, label='Precision')
plt.bar(r3, var_FAR, color ='#d43131', width=barWidht, label='False Alarm Rate')
plt.bar(r4, var_FS, color ='#099c0e', width=barWidht, label='F-Score')

# plt.bar(r1, var_recall, color ='#e4eb17', width=barWidht, label='Recall')
# plt.bar(r2, var_precision, color ='#eba417', width=barWidht, label='Precision')
# plt.bar(r3, var_FAR, color ='#177deb', width=barWidht, label='False Alarm Rate')
# plt.bar(r4, var_FS, color ='#eb3317', width=barWidht, label='F-Score')

plt.xlabel('Contamination')
plt.xticks([r + barWidht for r in range(len(var_recall))],['0','0,01','0,02','0,03','0,04','0,05','0,06','0,07','0,08','0,09','0,1','0,2','0,3','0,4','0,5'])
plt.ylabel('Percentage [%]')
plt.title(titulo)
# plt.legend()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), shadow=True, ncol=2)
plt.tight_layout()
plt.savefig("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Figures/"+str(ML)+"-O"+str(outlier)+"-Day.png")
#plt.savefig("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Day/Figures/"+str(ML)+"-OI"+str(outlier)+"-Day.png")

plt.show()