
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("C:/Users/HP/Downloads/C110-main (1)/C110-main/C110 whitehat.csv")
data=df["temp"].tolist()
#standard deviation and mean of a 100 data points
dataset=[]
for i in range (0,100):
    randomindex=random.randint(0,len(data)-1)
    value=data[randomindex]
    dataset.append(value)
mean=statistics.mean(dataset)
standarddeviation2=statistics.stdev(dataset)
totalmean=statistics.mean(data)
standarddeviation=statistics.stdev(data)
print("total mean",totalmean)
print("Standard deviation",standarddeviation)
print("mean of sample",mean)
print("standarddeviation of sample",standarddeviation2)


#function to get the mean of given data
def Rmean(counter):
    dataset=[]
    
    for i in range (0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df=meanlist
    mean = statistics.mean(df)
    fig=ff.create_distplot([data],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=Rmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print("mean of sampling distribution",mean)
setup()
totalmean = statistics.mean(data)
print("total mean:- ", totalmean)
#def stnd1():
 #   meanlist=[]
  #  for i in range(0,1000):
   #     setofmeans=Rmean(100)
    #    meanlist.append(setofmeans) 
    #stnd=statistics.stdev(meanlist)
    #print("standard deviation of sampling distribution  ",stnd)
#stnd1()  
def standard_deviation():
    meanlist = []
    for i in range(0,1000):
        set_of_means= Rmean(100)
        meanlist.append(set_of_means)

    std_deviation = statistics.stdev(meanlist)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()  




















 