import math
from chinacoordtran.COOR_XY import COOR_XY
class gcj02tobd09:
    def __init__(self):
        self.x_PI=3.14159265358979324 * 3000.0 / 180.0
        self.PI = 3.1415926535897932384626
        self.a = 6378245.0
        self.ee = 0.00669342162296594323
    def CoordTran(self,dX,dY):
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