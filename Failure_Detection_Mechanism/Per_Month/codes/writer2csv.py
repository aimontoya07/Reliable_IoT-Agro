#!/usr/bin/python
from csv import writer
from csv import DictWriter
import pandas as pd

def append_list_as_row(file_name, list_of_elem):
	# Open file in append mode
	with open(file_name, 'a+') as write_obj:
		# Create a writer object from csv module
		csv_writer = writer(write_obj)
		# Add contents of list as last row in the csv file
		csv_writer.writerow(list_of_elem)

def append_dict_as_row(file_name, dict_of_elem, field_names):
	# Open file in append mode
	with open(file_name, 'a+') as write_obj:
		# Create a writer object from csv module
		dict_writer = DictWriter(write_obj, fieldnames=field_names)
		# Add dictionary as wor in the csv
		dict_writer.writerow(dict_of_elem)

def main():

	outlier = "10"

#--------------------------------------	
	ML = "DBSCAN"
	metric = "e"
	var = 'e'
	print('Append dictionary as a row to an existing csv file using DictWriter in python')
	header_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
	append_list_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", header_names)	

	cont = ["001","002","003","004","005","006","007","008","009","01","02","03","04","05","06","07","08"]
#	cont = ["0","001","002","003","004","005","006","007","008","009","01","02","03","04","05"]
	# cont = ["001","002","003","004","005","006 ","007","008","009","01"]

	for i in cont :
		print(i)
		cm = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+""+str(i)+"-ms3-cm.csv")
		print(cm)
		TN = float(cm.iloc[0,1])
		FP = float(cm.iloc[0,2])
		FN = float(cm.iloc[1,1])
		TP = float(cm.iloc[1,2])

		try:
		    Accuracy = (TP + TN) / (TP+TN+FP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
		    Recall = TP / (TP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
			FAR = FP / (FP+TN)
		except ZeroDivisionError:
		    FAR = "NA"

		try:
			Precision = TP / (TP+FP)
		except ZeroDivisionError:
		    Precision = "NA"

		try:
			F_Score = (2 * Recall * Precision) / (Recall + Precision)
		except ZeroDivisionError:
		    F_Score = "NA"

		field_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
		row_dict = {var:i,'Accuracy':Accuracy,'Recall':Recall,'Precision':Precision,'False_Alarm_Rate':FAR,'F_Score':F_Score}
		print(row_dict)
		# Append a dict as a row in csv file
		append_dict_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", row_dict, field_names)	

#----------------------------------------
	ML = "IF"
	metric = "c"
	var = 'contamination'
	print('Append dictionary as a row to an existing csv file using DictWriter in python')
	header_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
	append_list_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", header_names)	

	cont = ["0","001","002","003","004","005","006","007","008","009","01","02","03","04","05"]

	for i in cont :
		print(i)
		cm = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+""+str(i)+"-cm.csv")
		print(cm)
		TN = float(cm.iloc[0,1])
		FP = float(cm.iloc[0,2])
		FN = float(cm.iloc[1,1])
		TP = float(cm.iloc[1,2])

		try:
		    Accuracy = (TP + TN) / (TP+TN+FP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
		    Recall = TP / (TP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
			FAR = FP / (FP+TN)
		except ZeroDivisionError:
		    FAR = "NA"

		try:
			Precision = TP / (TP+FP)
		except ZeroDivisionError:
		    Precision = "NA"

		try:
			F_Score = (2 * Recall * Precision) / (Recall + Precision)
		except ZeroDivisionError:
		    F_Score = "NA"

		field_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
		row_dict = {var:i,'Accuracy':Accuracy,'Recall':Recall,'Precision':Precision,'False_Alarm_Rate':FAR,'F_Score':F_Score}
		print(row_dict)
		# Append a dict as a row in csv file
		append_dict_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", row_dict, field_names)	
#-----------------------------------------------
	ML = "SVM"
	metric = "nu"
	var = 'nu'
	print('Append dictionary as a row to an existing csv file using DictWriter in python')
	header_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
	append_list_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", header_names)	

	cont = ["001","002","003","004","005","006 ","007","008","009","01"]

	for i in cont :
		print(i)
		cm = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+""+str(i)+"-cm.csv")
		print(cm)
		TN = float(cm.iloc[0,1])
		FP = float(cm.iloc[0,2])
		FN = float(cm.iloc[1,1])
		TP = float(cm.iloc[1,2])

		try:
		    Accuracy = (TP + TN) / (TP+TN+FP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
		    Recall = TP / (TP+FN)
		except ZeroDivisionError:
		    Recall = "NA"

		try:
			FAR = FP / (FP+TN)
		except ZeroDivisionError:
		    FAR = "NA"

		try:
			Precision = TP / (TP+FP)
		except ZeroDivisionError:
		    Precision = "NA"

		try:
			F_Score = (2 * Recall * Precision) / (Recall + Precision)
		except ZeroDivisionError:
		    F_Score = "NA"

		field_names = [var,'Accuracy','Recall','Precision','False_Alarm_Rate','F_Score']
		row_dict = {var:i,'Accuracy':Accuracy,'Recall':Recall,'Precision':Precision,'False_Alarm_Rate':FAR,'F_Score':F_Score}
		print(row_dict)
		# Append a dict as a row in csv file
		append_dict_as_row("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Month/Result_"+str(ML)+"/2019-11-O"+str(outlier)+"-"+str(metric)+".csv", row_dict, field_names)	


if __name__ == '__main__':
	main()