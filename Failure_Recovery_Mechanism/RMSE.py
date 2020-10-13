#!/usr/bin/python
from csv import writer
from csv import DictWriter
import pandas as pd
import numpy as np 
import sklearn
from sklearn.metrics import mean_squared_error
import math

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

scale = ["Hour","Day","Month"]
file = ["Cubic_Spline","Linear","Nearest_Neighbor"]
outlier = "10"

def main():
	for x in scale :
		for y in file :
			df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Recovery/"+y+"/Per_"+x+"/out-Test_2-O"+outlier+".csv")
			print("/media/Moon/Thesis/DataCollection/Failure_Recovery/"+y+"/Per_"+x+"/out-Test_2-O"+outlier+".csv")

			actual = df['value_temp'].values.tolist()
			#print("Actual data")
			#print(actual)

			predicted = df['recovery']
			#print("Predicted data")
			#print(predicted)

			mse = sklearn.metrics.mean_squared_error(actual, predicted)
			rmse = math.sqrt(mse)

			print("RMSE")
			print(rmse)

			#data = [y,rmse]
			field_names = ['Interpolation','DB','RMSE']
			row_dict = {'Interpolation':y,'DB':x,'RMSE':rmse}
			append_dict_as_row("/media/Moon/Thesis/DataCollection/Failure_Recovery/RMSE-O"+outlier+".csv", row_dict, field_names)	
			#data.to_csv(r"/media/Moon/Thesis/DataCollection/Failure_Recovery/RMSE-01.csv", index = False, header=True)

if __name__ == '__main__':
	main()
#-----------------------------------------------------------------
#a = df['Test_2'].tolist()
#b = df['recovery'].tolist()
#recover = [j if math.isnan(i) == True else i for i,j in zip(a,b)]
#print(recover)