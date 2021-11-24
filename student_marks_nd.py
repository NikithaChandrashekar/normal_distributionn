import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv("student_test_marks.csv")
data = df["math score"].tolist()

mean=sum(data)/len(data)
standard_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

print("mean =" ,mean)
print("standard_deviation =" ,standard_deviation)
print("median =" ,median)
print("mode =" ,mode)

first_std_deviation_start,first_std_deviation_end=mean-standard_deviation,mean+standard_deviation
second_std_deviation_start,second_std_deviation_end=mean-( 2 * standard_deviation),mean+( 2 * standard_deviation)
list_of_data_within_1_sd=[result for result in data if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_2_sd=[result for result in data if result>second_std_deviation_start and result<second_std_deviation_end]

print("{}% of data lies within 1 sd".format(len(list_of_data_within_1_sd)*100.0/len(data)))
print("{}% of data lies within 2 sd".format(len(list_of_data_within_2_sd)*100.0/len(data)))

fig=ff.create_distplot([data],["math scores"],show_hist=False)
fig.show()
