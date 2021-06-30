import math
from chinacoordtran.COOR_XY import COOR_XY
from chinacoordtran.utils import transformlat,transformlng,out_of_china
class CoordTran:
     def __init__(self):
        self.x_PI=3.14159265358979324 * 3000.0 / 180.0
        self.PI = 3.1415926535897932384626
        self.a = 6378245.0
        self.ee = 0.00669342162296594323
     def gcj02towgs84(self,dX,dY):
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
            coorxy.X=lng * 2 - mglng
            coorxy.Y=lat * 2 - mglat
            return coorxy
     def wgs84togcj02(self,dX,dY):
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
     def gcj02tobd09(self,dX,dY):
        lat = dY
        lng = dX
        z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * self.x_PI)
        theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * self.x_PI)
        bd_lng = z * math.cos(theta) + 0.0065
        bd_lat = z * math.sin(theta) + 0.006
        coorxy =COOR_XY()
        coorxy.X=bd_lng
        coorxy.Y=bd_lat
        return coorxy
     def bd09togcj02(self,dX,dY):
        bd_lng = dX
        bd_lat = dY
        x = bd_lng - 0.0065
        y = bd_lat - 0.006
        z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * self.x_PI)
        theta = math.atan2(y, x) - 0.000003 * math.cos(x * self.x_PI)
        gg_lng = z * math.cos(theta)
        gg_lat = z * math.sin(theta)
        coorxy =COOR_XY()
        coorxy.X=gg_lng
        coorxy.Y=gg_lat
        return coorxy