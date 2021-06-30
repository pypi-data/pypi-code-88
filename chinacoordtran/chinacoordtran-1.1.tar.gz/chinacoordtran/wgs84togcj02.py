import math
from chinacoordtran.COOR_XY import COOR_XY
from chinacoordtran.utils import transformlat,transformlng,out_of_china
class wgs84togcj02:
    def __init__(self):
        self.x_PI=3.14159265358979324 * 3000.0 / 180.0
        self.PI = 3.1415926535897932384626
        self.a = 6378245.0
        self.ee = 0.00669342162296594323
    def CoordTran(self,dX,dY):
        lat = dY
        lng = dX
        coorxy =COOR_XY()
        if out_of_china(lng, lat):
            coorxy.X=lng
            coorxy.Y=lat
            return coorxy
        else:
            dlat = transformlat(lng - 105.0, lat - 35.0)
            dlng = transformlng(lng - 105.0, lat - 35.0)
            radlat = lat / 180.0 * self.PI
            magic = math.sin(radlat)
            magic = 1 - self.ee * magic * magic
            sqrtmagic = math.sqrt(magic)
            dlat = (dlat * 180.0) / ((self.a * (1 - self.ee)) / (magic * sqrtmagic) * self.PI)
            dlng = (dlng * 180.0) / (self.a / sqrtmagic * math.cos(radlat) * self.PI)
            mglat = lat + dlat
            mglng = lng + dlng
            coorxy.X=mglng
            coorxy.Y=mglat
            return coorxy