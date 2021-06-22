import pyecharts
from pyecharts.charts import *
import turtle
class Pycharts:
    def __init__(self):
        pass
    def line(self,xais=list,yais=list,name=str,filename=str):
        
        bar = Line()
        bar.add_xaxis(xais)
        bar.add_yaxis(name,yais)
        bar.render(filename+".html")
    def bar(self,xais=list,yais=list,name=str,filename=str):
        
        bar2 = Bar()
        bar2.add_xaxis(xais)
        bar2.add_yaxis(name,yais)
        bar2.render(filename+".html")

    def turtle_init(self,speed,color):
        self.d = turtle.Pen()
        self.speed = speed
        self.d.speed(speed)
        self.d.color(color)
        
    def turtle_draw(self,num):
        
        for i in range(600):
            self.d.speed(self.speed)
            self.d.goto((i-300)*num,i-300)


