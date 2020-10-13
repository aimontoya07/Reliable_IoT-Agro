from csv import writer
from csv import reader
import time
import datetime
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

header_of_new_col = 'Test_1'
default_text = 'Some Text'

import pandas as pd

#df = pd.read_csv("/home/aimontoya/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/L_00h.csv")
df = pd.read_csv("/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/DB_Hours/Omicron_12h-O0.csv")
data = df['value_temp']
data_list = data.values.tolist()

print("DataSet size: %s" %(len(data_list)))

import random
from random import randrange, choice, randint
import math

def percentage(part, whole):
  return (float(part)*float(whole))/100

percent = 10
times = percentage(percent,len(data))

import math
times = int(math.ceil(times))
print("Numero de outlier: %s" %(times))

max_temp = max(data)
#print max_temp
min_temp = min(data)
#print min_temp

import numpy as np
q1, q3 = np.percentile(data,[25,75])

#print("El q1 es: %s, y el q3 es: %s" %(q1,q3))

iqr = q3 - q1
#print("iqr es: ", iqr)

lower_bound = q1 - (1 * iqr)
upper_bound = q3 + (1 * iqr)


# range(start, stop) returns [start, start+step, ..., stop-1]
list=[] 
print("Hey")

for i in range(1,int(round(times))+1):
    r=randrange(1,len(data)+1)
    list.append(r)

#r=randrange(1,len(data)+1)
#if r not in list: list.append(r)
print("Tamano final:")
print(len(list))

for x in range(1,int(round(times))+1):
#    print(x)
    outlier = choice([randint(0,int(lower_bound)),randint(int(upper_bound),60)])
    data_list[list[x-1]] = outlier


#print(list)
list_of_str = data_list

add_column_in_csv('/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/DB_Hours/Omicron_12h-O0.csv', '/media/Moon/Thesis/DataCollection/Failure_Detection/Tests/Per_Hour/DB_Hours/Omicron_12h-O'+str(percent)+'.csv', lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(list_of_str[line_num-2]))
