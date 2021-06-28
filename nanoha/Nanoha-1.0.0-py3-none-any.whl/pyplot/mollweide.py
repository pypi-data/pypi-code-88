import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm
class Mollweide:
	def __init__(self, rowcol=(1,1), cmap='rainbow', locator=ticker.MaxNLocator(), supertitle='', ticksfontdict={}, supertitlefontdict={}, titlefontdict={}, colorbardict={}):
		self.supertitle  = supertitle
		self.colorbardict = colorbardict
		self.data        = {}
		self.figsize     = (rowcol[1]*6.4,rowcol[0]*3.6)
		self.plotdict    = [dict(cmap=cmap, locator=locator) for i in range(rowcol[0]*rowcol[1])]
		self.ticksfontdict = {'size': 10}   #{'family': 'serif', 'style': 'normal', 'weight': 'normal', 'color':  'black', 'size': 10}
		self.titlefontdict = {'size': 14}   #{'family': 'serif', 'style': 'italic', 'weight': 'normal', 'color':  'black', 'size': 14}
		self.supertitlefontdict = {'size': 35}   #{'family': 'calibri', 'style': 'italic', 'weight': 'normal', 'color':  'black', 'size': 20}
		self.ticksfontdict.update(ticksfontdict)
		self.titlefontdict.update(titlefontdict)
		self.supertitlefontdict.update(supertitlefontdict)

	def subplots(self, i, j, k, theta, phi, value, title=None, **dic):
		self.data[(i, j, k)] = {'x':phi, 'y':theta, 'z':value, 'title':title}
		# print(k, dic )
		self.plotdict[k-1].update(dic)

	def show(self, usetex=False, savefile=None, dpi=None):
		fig = plt.figure(figsize=self.figsize)
		if usetex:
			plt.rc('text', usetex=True)
			plt.rc('font', family='calibri')
		if self.supertitle:
			fig.suptitle(self.supertitle, **self.supertitlefontdict)
		R   = 10
		for i, j, k in self.data.keys():
			phis, thetas = self.data[(i, j, k)]['x'], self.data[(i, j, k)]['y']
			phis, thetas = np.meshgrid(phis, thetas)
			x = R * phis * np.sin(thetas)/np.pi
			y = R * 0.75 * np.cos(thetas)	
			z = self.data[(i,j,k)]['z']
			edgex = R*np.sin(np.linspace(0, np.pi, 100))
			edgey = R*0.75*np.cos(np.linspace(0, np.pi, 100))

			ax = plt.subplot(i, j, k, alpha=0)
			# print(self.plotdict[k-1])
			fmt=self.plotdict[k-1].get('fmt', ticker.ScalarFormatter())
			# print(fmt)
			self.plotdict[k-1].pop('fmt', None)
			bar=ax.contourf(x, y, z, 8, alpha=0.75, **self.plotdict[k-1])
			cbar = plt.colorbar(bar, ax=ax, format=fmt)
			cbar.ax.tick_params(**self.colorbardict) 
			cbar.ax.minorticks_off()
			# c=plt.contour(x,y,z,8,colors='k')
			# ax.set_title(title) 			
			# ax.clabel(c,inline=True,fontsize=10)

			plt.xlim(-R-0.5, R+0.5)
			plt.ylim(-R, R)
			plt.axis('off')
			plt.plot( edgex, edgey, 'k')
			plt.plot(-edgex, edgey, 'k')

			for ps in range(-5,6): 
				if ps<0:
					tick = r'-%d$^\circ$'% (-30*ps)
				else:
					tick = r'%d$^\circ$'% (30*ps)
				plt.text(R/6*ps, 0, tick, fontdict=self.ticksfontdict, ha='center', va='center_baseline')
			# poffset = [0.02, 0.02, 0.06, 0.1, 0.13]
			# offset = np.array(poffset+[0]+poffset[::-1])*R
			for ps in range(-5, 6):
				if ps<0:
					tick = r'-%d$^\circ$'% (-15*ps)
					plt.text(-R*np.cos(np.pi/12*ps) + 0.24*R*(np.cos(np.pi/15*ps - 0.15*np.pi)-1), R*0.75*np.sin(np.pi/12*ps), tick, fontdict=self.ticksfontdict, ha='right', va='center_baseline')
				elif ps>0:
					tick = r'%d$^\circ$'% (15*ps)
					plt.text(-R*np.cos(np.pi/12*ps) + 0.24*R*(np.cos(np.pi/15*ps + 0.15*np.pi)-1), R*0.75*np.sin(np.pi/12*ps), tick, fontdict=self.ticksfontdict, ha='right', va='center_baseline')
				else:
					plt.text(-1.05*R, 0, r'$0^\circ$', fontdict=self.ticksfontdict, ha='right', va='center_baseline')
			plt.text(0, R*0.8, self.data[(i,j,k)]['title'], fontdict=self.titlefontdict, ha='center', va='bottom')
		fig.patch.set_alpha(0)
		# fig.tight_layout()
		if not savefile:
			plt.show()
		else:
			plt.savefig(savefile, dpi=dpi)