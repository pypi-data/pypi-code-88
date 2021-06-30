import math
from chinacoordtran.COOR_XY import COOR_XY
class bd09togcj02:
    def __init__(self):
        self.x_PI=3.14159265358979324 * 3000.0 / 180.0
        self.PI = 3.1415926535897932384626
        self.a = 6378245.0
        self.ee = 0.00669342162296594323
    def CoordTran(self,dX,dY):
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