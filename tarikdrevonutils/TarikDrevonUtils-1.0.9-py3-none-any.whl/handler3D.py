from mpl_toolkits.mplot3d import proj3d
import numpy, importlib,sys


def orthogonal_proj(zfront, zback):
    a = (zfront+zback)/(zfront-zback)
    b = -2*(zfront*zback)/(zfront-zback)
    return numpy.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,a,b],
                        [0,0,0,zback]])
# proj3d.persp_transformation = orthogonal_proj
def set_perspective(b=False):
    importlib.reload(proj3d)
    if not b :
        print('setting persp_transformation as orthogonal')
        proj3d.persp_transformation = orthogonal_proj

class handler_3d:
    def __init__(self,fig,e=[1,0,0],persp=False,xm=None):
        self.dazim=5
        self.delev=5
        self.fig = fig
        self.fig.canvas.mpl_connect('key_press_event', self)
        self.e=e
        ax = fig.canvas.figure.axes[0]
        xm0 = round(ax.get_xlim()[1])
        self.xm0 = xm0
        self.xm  = xm0
        self.elev,self.azim = ax.elev,ax.azim
        set_perspective(b=persp)
    def __call__(self,event):
        # print(event.key)
        ax = event.canvas.figure.axes[0];
        # dx,dy,dz = 0,0,0
        if   event.key == '1'     : self.elev,self.azim = 0,0
        elif event.key == '2'     : self.elev,self.azim = 0,90
        elif event.key == '3'     : self.elev,self.azim = 90,90
        elif event.key == '4'     : self.elev,self.azim = 180,0
        elif event.key == '5'     : self.elev,self.azim = 0,-90
        elif event.key == '6'     : self.elev,self.azim = -90,-90
        elif event.key == 'up'    : self.elev-=self.delev
        elif event.key == 'down'  : self.elev+=self.delev
        elif event.key == 'left'  : self.azim-=self.dazim
        elif event.key == 'right' : self.azim+=self.dazim
        elif event.key == 'ctrl+up'   : self.delev+=5
        elif event.key == 'ctrl+down' : self.delev = max(5,self.delev-5)
        elif event.key == 'ctrl+left' : self.dazim = max(5,self.dazim-5)
        elif event.key == 'ctrl+right': self.dazim+=5
        elif event.key == 'ctrl+r'    : self.delev,self.dazim=5,5
        elif event.key == 'pageup'   : self.xm /=2
        elif event.key == 'pagedown' : self.xm *=2
        elif event.key == 'r'        : self.xm = self.xm0
        if 'ctrl' in event.key :
            print('delev=%d,dazim=%d' %(self.delev,self.dazim))
        if event.key in '123456updownleftright':
            print(self.elev,self.azim)
            ax.elev = self.elev
            ax.azim = self.azim
            print('elev=%d,azim=%d' %(ax.elev,ax.azim))
        if event.key in 'rpageuppagedown' :
            xm = self.xm
            ax.set_xlim([-xm,xm])
            ax.set_ylim([-xm,xm])
            ax.set_zlim([-xm,xm])
            print('xm : ',xm)
        event.canvas.draw()
