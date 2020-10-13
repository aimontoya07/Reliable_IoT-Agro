#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({'font.size': 16})
from matplotlib.pyplot import figure

#outlier = "10"
titulo = 'Comparison - Dataset per hour'

data = pd.read_csv('/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Omicron_12h-comparison.csv')

print(data)

var_recall = [r*100 for r in data.iloc[:,1]] #[Fila,Columna]
var_precision = [r*100 for r in data.iloc[:,2]]
var_FAR = [r*100 for r in data.iloc[:,3]]
var_FS = [r*100 for r in data.iloc[:,4]]

print(var_recall)
print(var_precision)
print(var_FAR)
print(var_FS)

barWidht = 0.15

#plt.figure(figsize=(10,5))
figure(num=None, figsize=(20, 8), dpi=80, facecolor='w', edgecolor='k')
r1 = np.arange(len(var_recall))
r2 = [x + barWidht for x in r1]
r3 = [x + barWidht for x in r2]
r4 = [x + barWidht for x in r3]

plt.bar(r1, var_recall, color ='#3366de', width=barWidht, label='Recall')
plt.bar(r2, var_precision, color ='#ff9d00', width=barWidht, label='Precision')
plt.bar(r3, var_FAR, color ='#d43131', width=barWidht, label='False Alarm Rate')
plt.bar(r4, var_FS, color ='#099c0e', width=barWidht, label='F-Score')

plt.xlabel('')

plt.xticks([r + barWidht for r in range(len(var_recall))],['DBSCAN (e=0,3-0.8)','IF (c=0-0,04)','SVM (nu=0,01-0,1)','DBSCAN (e=0,3-0,8)','IF (c=0,05-0,08)','SVM (nu=0,09-0,1)','DBSCAN (e=0,2)','IF (c=0,09-0,1)','SVM (nu=0,09-0,1)'])
plt.ylabel('Percentage [%]')
#plt.title(titulo)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06), shadow=True, ncol=4)
# plt.savefig("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/Figures/comparison-O"+str(outlier)+"-Hour.png")
plt.show()