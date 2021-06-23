import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.dates import DateFormatter
%matplotlib inline

class plot():
    """
    This class is built over matplotlib library in a way to automate and help
    publishers to automate and manipulate their plots to include it into their scientific papers
    """
        
    def scientific(dataframe, x_label, y_label, style = "seaborn-whitegrid", size = (20, 10),
                   zooming = False, x1 = None, x2 = None, y1 = None, y2 = None):
        
        """
        style          : white grid is the default, for more styles please check
                         "https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html"
        size           : size of the figure "for better usage always use the same size in all the plots"
        x_label        : x axis label
        y_label        : y axis label
        zooming        : zoom in the area between the four points chosen (x1, x2, y1, y2)
        x1, x2, y1, y2 : points in the plot where the area of these four points needed to zoom it for better visulization
        """
        # plot using some styling in matplotlib:
        with plt.style.context(style):
            # Initialize the parameters of the plot 
            fig, ax = plt.subplots(figsize=size)
            plt.rcParams["axes.edgecolor"] = "0.15" 
            plt.rcParams["axes.linewidth"]  = 1.25  
            plt.rcParams["font.weight"] = "bold" 
            plt.rcParams["axes.labelweight"] = "bold"
            ax.plot(dataframe)


            if zooming:
                x1 = self.dataframe.iloc[0]
                x2 = self.dataframe.iloc[len(self.dataframe)//3]
                y1 = self.dataframe.index[0]
                y2 = self.dataframe.index[len(self.dataframe)//3]
                axins = ax.inset_axes([0.31, 0.5, 0.47, 0.47])
                # sub region of the original image
                axins.plot(self.dataframe.iloc[:len(self.dataframe)//3])
                axins.set_xlim(x1, x2)
                axins.set_ylim(y1, y2)
                ax.indicate_inset_zoom(axins, edgecolor="black")
                #axins.set_xticklabels('')

            ax.set_xlabel(x_label, fontsize=45, fontweight='bold')
            ax.set_ylabel(y_label, fontsize=45, fontweight='bold')
            ax.tick_params(axis='both', which='both',length=10,direction='in',colors ='black', pad = 10, width = 3)
            ax.xaxis.set_tick_params(labelsize=30)
            ax.yaxis.set_tick_params(labelsize=30)
            ax.locator_params(tight=True, nbins=4)
            ax.margins(x=0)
            #ax.set_xticks(np.arange(0, max(qc1.index)+1, 1000))
            #ax.set_yticks(np.arange(140, 500, 100))
            plt.show()