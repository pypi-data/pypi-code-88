from re import X
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio


class Plotter():
    """Create a plot object to visualize the data.

    Create a plotly plot given a plot type choice, a dataframe, and input parameters to set up the plot layout.
    Function to show the plot is create_plot().
    
    Args:
        choice (str): "1", "2", or "3" for the different plot types
        df (DataFrame): df (future: vaex) dataframe containing the data for the plot
        gui_input (dict): dictionary with parameters to set up the plot:
            - list of x, y, z (color coded) columns
            - list of the slider columns (e.g. one col for each time step)
            - optional: a title, x,y or z limits (as tuple)
        fig_size (tuple): witdth and height of plot; Default: (900,700)

    Examples:
        >>> import slot
        # create a plot object to display the data
        # specifying the plot type and columns to plot & slide over
        >>> plot = slot.Plotter("2", gui_input={"xyz_cols":["x", "y", "z"],
                                                "slider_cols":[""y1", "y2"]})

    """
    def __init__(self, choice, df, gui_input=None, fig_size=(900,700)):
        
        self.choice = choice
        self.df = df
        self.fig_size = fig_size

        # gui_input contains: colums to plot, axis limits, title etc..
        self.xyz_cols = gui_input["xyz_cols"]
        if self.choice == "2":
            if gui_input == None:
                raise Exception("For type2 plot, need to provide gui_input dict.")
            try: 
                self.slider_cols = gui_input["slider_cols"]
            except:
                raise Exception("For type1 plot, need to specify list of " + 
                                "y-columns used for the slider.")
        try:
            self.title = gui_input["title"]
        except:
            self.title = None
        try:
            self.xlim = gui_input["xlim"]
        except:
            self.xlim = None
        try:
            self.ylim = gui_input["ylim"]
        except:
            self.ylim = None
        try:
            self.zlim = gui_input["zlim"]
        except:
            self.zlim = None

    def plottype(self):
        if self.choice == '1':
            msg = 'You chose plot type 1: dummy plot.'
            self.plot_type_dummy()
        elif self.choice == '2':
            msg = 'You chose plot type 2'
        elif self.choice == '3':
            msg = 'You chose plot type 3'
        return msg

    def plot_type_dummy(self):
        '''
        Just a dummy function
        '''
        pass

    def create_plot(self):
        if self.choice == "1":
            pass
        if self.choice == "2":
            self.plot_type1()
        if self.choice == "3":
            pass

    def set_xlim(self, x_lower, x_upper):
        """Set limits of the x-axis."""
        self.xlim = (x_lower, x_upper)
        raise NotImplementedError("Not implemented.")

    def set_ylim(self, y_lower, y_upper):
        """Set limits of the y-axis."""
        self.ylim = (y_lower, y_upper)
        raise NotImplementedError("Not implemented.")

    def set_zlim(self, z_lower, z_upper):
        """Set limits of the z-axis."""
        self.zlim = (z_lower, z_upper)
        raise NotImplementedError("Not implemented.")

    def set_xyz_cols(self, xcol, ycol, zcol):
        """Set the x-, y- and z-column names to plot.
        FUTURE: could split this up into 3 functions
        """ 
        self.xyz_cols = [xcol, ycol, zcol]
        raise NotImplementedError("Not implemented.")

    def set_slider_cols(self, slider_cols):
        """Set the columns to slide over (for plot type 1). 
        Input is a list of column names (str)."""
        self.slider_cols = slider_cols
        raise NotImplementedError("Not implemented.")

    def plot_type1(self):
        """Generate the interactive plotly plot.
        
        Scatter plot of y as a fct. of x, with z colorcoded,
        plus slider to shift over provided y columns (e.g. y at diff. times)
        NOTE: x, y and z are all plotted in log10

        Returns:
            plot

        """
        # get the data for the specified columns
        x_axis = self.df[self.xyz_cols[0]]
        y_axis = self.df[self.xyz_cols[1]]
        z_axis = self.df[self.xyz_cols[2]]
        
        # create plot layout
        if self.xlim == None:
            self.xlim = (np.min(x_axis), np.max(x_axis))
        if self.ylim == None:
            self.ylim = (np.min(y_axis), np.max(y_axis))
        if self.zlim == None:
            self.zlim = (np.min(z_axis), np.max(z_axis))
        if self.title == None:
            self.title = "title"

        layout = go.Layout(
                        width=self.fig_size[0],
                        height=self.fig_size[1],
                        title=self.title,
                        xaxis=go.layout.XAxis(title=self.xyz_cols[0],
                                                range=[self.xlim[0], self.ylim[1]]),
                        yaxis=go.layout.YAxis(title=self.xyz_cols[1],
                                                range=[self.ylim[0], self.ylim[1]]),
                        ) #title=str(y_axis.expression) for vaex df
        
        # Create Figure or FirgureWidget (couldn't really figure out the difference)
        fig = go.Figure(layout=layout)
        #fig = go.FigureWidget(layout=layout)
        #fig = go.FigureWidget(data=[self.scatter], layout=self.layout)

        # Add traces, one for each slider step
        # in my test data, the y-values for each time are in a seperate column,
        # with column names given by self.slider_cols
        for step in self.slider_cols:
            fig.add_trace(go.Scatter( 
                    visible=False,
                    name="𝜈 = " + str(step),
                    x=x_axis.values,
                    y=self.df[step].values,
                    marker=dict(
                        size=15,
                        cmax=np.log10(self.zlim[1]),
                        cmin=np.log10(self.zlim[0]),
                        color=np.log10(z_axis),
                        colorbar=dict(
                            title=str(self.xyz_cols[2])
                        ),
                        colorscale="turbo"
                    ),
                    mode="markers",
                    ))

        # Make 0th trace visible at the start
        fig.data[0].visible = True

        # Create and add slider
        steps = []
        for i in range(len(fig.data)):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(fig.data)},
                    {"title": "Slider switched to step: " + \
                    self.slider_cols[i] + ' Myr'}],  # layout attribute
            )
            step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
            steps.append(step)

        # configure the sliders
        sliders = [dict(
            active=0,
            currentvalue={"prefix": "Age [Myr]: "},
            pad={"t": 50},
            steps=steps
        )]

        fig.update_layout(
            sliders=sliders,
        )

        fig.update_xaxes(title_text=self.xyz_cols[0], type="log",
                         range=[np.log10(self.xlim[0]), np.log10(self.xlim[1])])
        fig.update_yaxes(title_text=self.xyz_cols[1], type="log",
                         range=[np.log10(self.ylim[0]), np.log10(self.ylim[1])])
        
        fig.update_traces(mode='markers', opacity=0.75, 
                    marker=dict(
                    #    color="rgba(152, 0, 0, .8)",##00CED1
                        size=5,
                        line=dict(
                            color='Black',
                            width=0.5
                        )
                    ),
        )

        fig.update_layout(template="ggplot2") #"simple_white"

        fig.show()
