import pyecharts
from pyecharts.charts import *

class Line:
    def __init__(self):
        print('there is a line object.')
    def line(self,xais=list,yais=list,name=str,filename=str):
        
        bar = Line()
        bar.add_xaxis(xais)
        bar.add_yaxis(name,yais)
        bar.render(filename+".html")
        
    
