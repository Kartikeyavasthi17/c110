import csv
from numpy import histogram
import pandas as pd
import plotly.figure_factory as ff
import statistics 
import random 
import plotly.graph_objects 

df =pd.read_csv("medium_data.csv")
data =df["reading_time"].tolist()

population_mean=statistics.mean(data)
Std_Deviation=statistics.stdev(data)

def randomSampleOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    return mean


def showfig(meanList):
    df=meanList
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=randomSampleOfMean(100)
        mean_list.append(setOfMeans)
    showfig(mean_list)    

setup()    