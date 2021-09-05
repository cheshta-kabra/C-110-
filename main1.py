import random
import plotly.figure_factory as ff 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import statistics 

df=pd.read_csv('data.csv')
averageList=df['average'].to_list()
mean=sum(averageList)/len(averageList)
std_dev=statistics.stdev(averageList)
print ("Mean",mean)
print ("Std_Dev",std_dev)
fig=ff.create_distplot([averageList],['Result'],show_hist=False)
fig.show()