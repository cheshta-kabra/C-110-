import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random 
import pandas as pd 
import csv

df=pd.read_csv("data.csv")
data=df['average'].tolist()

def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],['average'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='MEAN'))
    fig.show()


def randomSetofMean(counter):
    dataset=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomSetofMean(121)
        meanlist.append(setofmeans)
    """ stddev=statistics.stdef(meanlist)
    print('std dev is:',stddev) """
    showfig(meanlist)
    mean=statistics.mean(meanlist)
    print('mean of sampling distribution is ', mean)
    stddev()

def stddev():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomSetofMean(121)
        meanlist.append(setofmeans)
    stddev=statistics.stdev(meanlist)
    print('std dev is:',stddev) 
setup()