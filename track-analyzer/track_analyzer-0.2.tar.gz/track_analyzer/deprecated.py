##########################################################################
# Track Analyzer - Quantification and visualization of tracking data     #
# Authors: Arthur Michaut                                                #
# Copyright 2016-2019 Harvard Medical School and Brigham and             #
#                          Women's Hospital                              #
# Copyright 2019-2021 Institut Pasteur and CNRS–UMR3738                  #
# See the COPYRIGHT file for details                                     #
#                                                                        #
# This file is part of Track Analyzer package.                           #
#                                                                        #
# Track Analyzer is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# Track Analyzer is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
# GNU General Public License for more details .                          #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with Track Analyzer (COPYING).                                   #
# If not, see <https://www.gnu.org/licenses/>.                           #
##########################################################################

welcome_message = """

 WELCOME TO TRACK ANALYZER 
 Developed and maintained by Arthur Michaut: arthur.michaut@gmail.com 
 Last release: 11-25-2020

     _''_
    / o  \ 
  <       |
    \    /__
    /       \-----
    /    \    \   \__
    |     \_____\  __>
     \--       ___/  
        \     /
         || ||
         /\ /\   


"""

###############################################
########### IDEAS FOR THE FUTURE ##############
###############################################

def plot_superimposed_traj(df,data_dir,traj_list,center_origin=True,fn_end=''):
    """ Plot a set of trajectories without any background. If center_origin all first points are located in the center"""
    close('all')
    
    track_groups=df.groupby(['track'])

    if center_origin:
        for i,traj_id in enumerate(traj_list):
            traj=get_traj(track_groups,traj_id)
            if i==0:
                minx=traj['x'].min(); maxx=traj['x'].max(); miny=traj['y'].min(); maxy=traj['y'].max()
            else:
                minx=traj['x'].min() if traj['x'].min()<minx else minx
                maxx=traj['x'].max() if traj['x'].max()>maxx else maxx
                miny=traj['y'].min() if traj['y'].min()<miny else miny
                maxy=traj['y'].max() if traj['y'].max()>maxy else maxy
                midx=minx+(maxx-minx)/2.
                midy=miny+(maxy-miny)/2.

    fig,ax=plt.subplots(1,1)
    ax.axis('off')
    for i,traj_id in enumerate(traj_list):
        traj=get_traj(track_groups,traj_id)
        traj_length = traj.shape[0]
        if center_origin:
            traj['x']=traj['x']-midx; traj['y']=traj['y']-midy
        ax.plot(traj['x'],traj['y'],ls='-',color=color_list[i%7])
        ax.plot(traj.loc[traj_length,'x'],traj.loc[traj_length,'y'],ls='none',marker='.',c='k')
    centered='centered' if center_origin else ''
    filename=osp.join(data_dir,'superimposed'+fn_end+centered+'.svg')
    fig.savefig(filename, dpi=300)
    close(fig)

def traj_plot(data_dir):
    df,lengthscale,timescale,columns,dim=get_data(data_dir,refresh=False)
    traj_list=input('give the list of traj you want to plot (sep: comas) if none given they will all be plotted: ')
    traj_list=traj_list.split(',')
    if len(traj_list)==0:
        traj_list=df['track'].values
    else:
        traj_list=[int(t) for t in traj_list]
    plot_superimposed_traj(df,data_dir,traj_list)



###############################################
############### DEPRECATED ####################
###############################################

def get_coord(extents):
    """DEPRECATEDSmall function used by skimage viewer"""
    global viewer,coord_list
    coord_list.append(extents)

def get_ROI_old(image_dir,frame,tool=RectangleTool):
    """DEPRECATED: Interactive function used to get ROIs coordinates of a given image"""
    global viewer,coord_list

    if type(frame) not in [int,float]:
        print("ERROR the given frame is not a number")
        return -1

    filename=osp.join(image_dir,'{:04d}.png'.format(int(frame)))
    if osp.exists(filename) is False:
        print("ERROR the image does not exist for the given frame")
        return -1
    im = io.imread(filename)

    selecting=True
    while selecting:
        viewer = ImageViewer(im)
        coord_list = []
        rect_tool = tool(viewer, on_enter=get_coord) 
        print("Draw your selections, press ENTER to validate one and close the window when you are finished")
        viewer.show()
        print('You have selected {} ROIs'.format(len(coord_list)))
        finished=input('Is the selection correct? [y]/n: ')
        if finished!='n':
            selecting=False
    return coord_list

def compute_XY_flow(df,data_dir,line,orientation,frame,groups,window_size=None,timescale=1.,lengthscale=1.,z_depth=None,reg_dx=1.,plot_steps=False):
    """Compute the flow along the surface defined by a XY line. The first end of the line is x=0 for the plot. The cells crossing the line along the orientation (from first point to second) are counted
    as positive cells, the cells in the other are counted as negative. The count is integrated along a moving window along the line"""

    print('computing XY flow {}'.format(int(frame)),end='\r')

    group=groups.get_group(frame).reset_index(drop=True)

    #find intersection (beware vx is in um and coordinates in px) using formula from https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x1=line[0][0];y1=line[0][1];x2=line[1][0];y2=line[1][1]
    Ox1=orientation[0][0];Oy1=orientation[0][1];Ox2=orientation[1][0];Oy2=orientation[1][1]

    for dim in ['x','y']:
        group['displ_'+dim]=group['v'+dim]*timescale*lengthscale 
        group[dim+'_prev']=group[dim]-group['displ_'+dim] #get previous timestep position
    group = group[(np.isfinite(group['x_prev'])|np.isfinite(group['y_prev']))] #remove nan

    #calculate coordinates of point (I) of intersection between line and displacement vector
    A=x1*y2-y1*x2; B=x1-x2; C=y1-y2
    group['intersec_denom']=B*group['displ_y'] - C*group['displ_x']
    group['intersec_x']=(A*group['displ_x']-B*(group['x']*group['y_prev']-group['y']*group['x_prev']))/group['intersec_denom']#intesection x_coord
    group['intersec_y']=(A*group['displ_y']-C*(group['x']*group['y_prev']-group['y']*group['x_prev']))/group['intersec_denom']#intesection y_coord
    if plot_steps:
        print("all intercepts")
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)
        group.plot.scatter(x='intersec_x',y='intersec_y',ax=ax)
        ax.plot([x1,x2],[y1,y2])
        show(fig)


    # #check if I on line
    ind=((group['intersec_x']>=min(x1,x2)) & (group['intersec_x']<=max(x1,x2)) & (group['intersec_y']>=min(y1,y2))&(group['intersec_y']<=max(y1,y2)))
    group=group[ind]
    if plot_steps:
        print("on line intercepts")
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)
        group.plot.scatter(x='intersec_x',y='intersec_y',ax=ax)
        ax.plot([x1,x2],[y1,y2])
        show(fig)

    #check if crossing line 
    group['intersec_vecx']=group['intersec_x']-group['x_prev']#vector I-x between intersection and previous point
    group['intersec_vecy']=group['intersec_y']-group['y_prev']
    group['converging']=group['intersec_vecx']*group['displ_x']+group['intersec_vecy']*group['displ_y'] #scalar product between (I-x) and displacement vectors.
    if plot_steps:
        print("all I-x")
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)
        ax.quiver(group['x_prev'].values,group['y_prev'].values,group['intersec_vecx'].values,group['intersec_vecy'].values)
        ax.plot([x1,x2],[y1,y2])
        show(fig)

    group=group[group['converging']>0] #if >0 converging towards line. If not discard because crossing is impossible
    if plot_steps:
        print("converging I-x")
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)
        ax.quiver(group['x_prev'].values,group['y_prev'].values,group['intersec_vecx'].values,group['intersec_vecy'].values)
        ax.plot([x1,x2],[y1,y2])
        show(fig)

    group['crossing']=(group['displ_x']**2+group['displ_y']**2)/(group['intersec_vecx']**2+group['intersec_vecy']**2) #|displ|^2/|I-x|^2
    group=group[group['crossing']>=1] #if displacement > distance to surface

    #compute orientation
    group['orientation']=group['displ_x']*(Ox2-Ox1)+group['displ_y']*(Oy2-Oy1) #scalar product between O and displ
    group['orientation']=group['orientation'].apply(lambda x:1 if x>0 else -1)

    #compute distance to line end
    group['line_abscissa']=np.sqrt((group['intersec_x']-x1)**2+(group['intersec_y']-y1)**2)

    #return data
    data=group[['line_abscissa','orientation']].values
    data[:,0]/=lengthscale #rescale data in um
    abs_length = np.sqrt((line[1][0]-line[0][0])**2+(line[1][1]-line[0][1])**2)/lengthscale
    axis_data=arange(0,abs_length,reg_dx)
    data=regularized_rolling_mean(data,axis_data,window_size,reg_dx)
    if window_size is not None:
        window_area=window_size*z_depth if z_depth is not None else window_size
        data[:,1]/=(timescale*window_area)
    else:
        data[:,1]/=timescale
    return data

def plot_all_avg_ROI(df,data_dir,map_kind,frame_subset=None,selection_frame=None,ROI_list=None,plot_on_map=False,plot_section=True,cumulative_plot=True,avg_plot=True,timescale=1.):

    close('all')

    if selection_frame is None:
        selection_frame=int(input("Give the frame number on which you want to draw your ROIs: "))
    
    [ROI_data_list,ROI_list]=select_map_ROI(data_dir,map_kind,selection_frame,ROI_list)

    frame_list=select_frame_list(df,frame_subset)

    plot_data_list=[]
    for i,frame in enumerate(frame_list):
        [ROI_data_list,ROI_list]=select_map_ROI(data_dir,map_kind,frame,ROI_list)
        if i>0:
            plot_on_map=False #plot it only once
        plot_data_list.append(plot_ROI_avg(df,data_dir,map_kind,frame,ROI_data_list,plot_on_map=plot_on_map,plot_section=plot_section))

    if cumulative_plot:
        time_min=min(frame_list)*timescale; time_max=max(frame_list)*timescale
        #colorbar
        Z = [[0,0],[0,0]]
        levels=array(frame_list)*timescale
        CS3 = plt.contourf(Z, levels, cmap=cm.plasma)
        plt.clf()
        for i,ROI_data in enumerate(ROI_data_list):
            x_data_l=[p[str(i)]['x_data'] for p in plot_data_list]
            y_data_l=[p[str(i)]['y_data'] for p in plot_data_list]
            title=plot_data_list[0][str(i)]['title'];xlab=plot_data_list[0][str(i)]['xlab']
            fig, ax = plt.subplots(1, 1)
            for j in range(len(x_data_l)):
                time=frame_list[j]*timescale
                ax.plot(x_data_l[j],y_data_l[j],color=get_cmap_color(time, cm.plasma, vmin=time_min, vmax=time_max))
            ax.set_title(title)
            ax.set_xlabel(xlab)
            ax.set_ylabel(map_dic[map_kind]['cmap_label'])
            cb=fig.colorbar(CS3)
            cb.set_label(label='time (min)')
            filename=plot_data_list[0][str(i)]['filename_prefix']+'_cumulative.png'
            fig.savefig(filename,dpi=300,bbox_inches='tight')
            plt.close(fig)

    if avg_plot:
        for i,ROI_data in enumerate(ROI_data_list):
            x_data=plot_data_list[0][str(i)]['x_data']
            y_data_l=[p[str(i)]['y_data'] for p in plot_data_list]
            title=plot_data_list[0][str(i)]['title'];xlab=plot_data_list[0][str(i)]['xlab']
            fig, ax = plt.subplots(1, 1)
            sns.tsplot(y_data_l,time=x_data,ax=ax,estimator=np.nanmean,err_style="unit_traces")
            ax.set_title(title)
            ax.set_xlabel(xlab)
            ax.set_ylabel(map_dic[map_kind]['cmap_label'])
            filename=plot_data_list[0][str(i)]['filename_prefix']+'_average.png'
            sns.despine()
            fig.savefig(filename,dpi=300,bbox_inches='tight')
            plt.close(fig)

def plot_all_XY_flow(df,data_dir,line=None,orientation=None,frame_subset=None,window_size=None,selection_frame=None,timescale=1.,lengthscale=1.,z_depth=None):
    """Plot the flow through a vertical surface define by a XY line (the first point of line is the start of the abscissa axis). 
    The orientation of the flow is given by the orientation vector (pointing towards the 2nd point). If line and orientations are not given they are manually drawn with get_ROI"""

    close('all')

    #get parameters
    plot_dir=osp.join(data_dir,'XY_flow')
    safe_mkdir(plot_dir)

    image_dir=osp.join(data_dir,'raw')
    if osp.isdir(image_dir)==False:
        image_dir=osp.join(data_dir,'traj')


    if line is None and orientation is None:
        if selection_frame is None:
            selection_frame=int(input("Give the frame number on which you want to draw your ROIs: "))
        print("Draw two lines (and press ENTER to validate each one of them). \n The first defines your vertical surface (the first point will be the origin of the plot). The second needs to be approximatively perpendicular to the first one. It gives the orientation to the flow (going from the first point to the 2nd)")
        line,orientation=get_ROI(image_dir,selection_frame,tool=LineTool) #lines coordinates are given 2nd point first and 1st point second
        line=line[::-1,:]; orientation=orientation[::-1,:] #flip order of points coordinates 

    #plot data
    frame_list=select_frame_list(df,frame_subset)
    groups=df.groupby('frame')

    plot_data_list=[]
    for i,frame in enumerate(frame_list):
        plot_on_map=True if i==0 else False #plot on map only once
        plot_data_list.append(plot_XY_flow(df,data_dir,line,orientation,frame,groups,window_size=window_size,timescale=timescale,lengthscale=lengthscale,z_depth=z_depth,plot_on_map=plot_on_map))

    #cumulative plot
    abs_length = np.sqrt((line[1][0]-line[0][0])**2+(line[1][1]-line[0][1])**2)/lengthscale
    time_min=min(frame_list)*timescale; time_max=max(frame_list)*timescale
    #colorbar
    Z = [[0,0],[0,0]]
    levels=array(frame_list)*timescale
    CS3 = plt.contourf(Z, levels, cmap=cm.plasma)
    plt.clf()
    x_data_l=[p['x_data'] for p in plot_data_list]
    y_data_l=[p['y_data'] for p in plot_data_list]
    fig, ax = plt.subplots(1, 1)
    for j in range(len(x_data_l)):
        time=frame_list[j]*timescale
        if window_size is None:
            ax.scatter(x_data_l[j],y_data_l[j],color=get_cmap_color(time, cm.plasma, vmin=time_min, vmax=time_max))
        else:
            ax.plot(x_data_l[j],y_data_l[j],color=get_cmap_color(time, cm.plasma, vmin=time_min, vmax=time_max))
    ax.set_title(plot_data_list[0]['title'])
    ax.set_xlabel(plot_data_list[0]['xlab'])
    ax.set_ylabel(plot_data_list[0]['ylab'])
    ax.set_xlim(0,abs_length)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,4))
    cb=fig.colorbar(CS3)
    cb.set_label(label='time (min)')
    filename=plot_data_list[0]['filename_prefix']+'_cumulative.png'
    fig.savefig(filename,dpi=300,bbox_inches='tight')
    plt.close(fig)

    #average plot
    if window_size is not None:
        x_data=plot_data_list[0]['x_data']
        fig, ax = plt.subplots(1, 1)
        sns.tsplot(y_data_l,time=x_data,ax=ax,estimator=np.nanmean,err_style="unit_traces")
        ax.set_title(plot_data_list[0]['title'])
        ax.set_xlabel(plot_data_list[0]['xlab'])
        ax.set_ylabel(plot_data_list[0]['ylab'])
        ax.set_xlim(0,abs_length)
        ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,4))
        filename=plot_data_list[0]['filename_prefix']+'_average.png'
        fig.savefig(filename,dpi=300,bbox_inches='tight')
        plt.close(fig)

    return plot_data_list

def plot_z_flow(df,frame,data_dir,no_bkg=False,vlim=None,axis_on=False):
    """Plot the flow (defined as the net number of cells going through a surface element in the increasing z direction) through the plane of z=z0"""
    
    #Make sure these are 3D data
    if 'z' not in df.columns:
        print("Not a 3D set of data")
        return

    close('all')
    print('plotting z flow {}'.format(int(frame)),end='\r')
    plot_dir=osp.join(data_dir,'z_flow')
    safe_mkdir(plot_dir)
    
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame,no_bkg=no_bkg,axis_on=axis_on)
    X,Y,flow=get_map_data(plot_dir,frame)
    [vmin,vmax]= [flow.min(),flow.max()] if vlim is None else vlim
    cmap=cm.plasma
    C=ax.pcolormesh(X,Y,flow,cmap=cmap,alpha=0.5,vmin=vmin,vmax=vmax)
    ax.axis([xmin,xmax,ymin,ymax])

    if axis_on:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)
    filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
    fig.savefig(filename, dpi=300)
    plt.close(fig)
    
    return flow

def plot_ROI_avg(df,data_dir,map_kind,frame,ROI_data_list,plot_on_map=False,plot_section=True):
    """ Plot average data along the major axis of a map at a given frame"""

    close('all')
    print('plotting ROI average {}'.format(int(frame)),end='\r')

    plot_dir=osp.join(data_dir,map_kind,'ROI_avg')
    safe_mkdir(plot_dir)

    if plot_on_map:
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)

    plot_data={}
    for i,ROI_data in enumerate(ROI_data_list):
        avg=avg_ROI_major_axis(ROI_data)
        if plot_on_map:
            ax.plot(avg['data'][0],avg['data'][1],color=color_list[i])
        fig2, ax2 = plt.subplots(1, 1)
        if avg['major_ax']==0:
            x_data=avg['data'][1]
            title='x = {} px'.format(int(avg['data'][0][0]))
            xlab='y (px)'
        elif avg['major_ax']==1:
            x_data=avg['data'][0]
            title='y = {} px'.format(int(avg['data'][1][0]))
            xlab='x (px)'
        
        filename_prefix=osp.join(plot_dir,'ROI_{}-{}-{}-{}'.format(int(avg['data'][0].min()),int(avg['data'][0].max()),int(avg['data'][1].min()),int(avg['data'][1].max())))
        plot_data[str(i)]={'x_data':x_data,'y_data':avg['data'][2],'title':title,'xlab':xlab,'filename_prefix':filename_prefix}
        
        if plot_section:
            ax2.plot(x_data,avg['data'][2])
            ax2.set_title(title)
            ax2.set_xlabel(xlab)
            ax2.set_ylabel(map_dic[map_kind]['cmap_label'])
            filename=filename_prefix+'_frame_{:04d}.png'.format(int(frame))
            fig2.savefig(filename,dpi=300,bbox_inches='tight')

    if plot_on_map:
        filename=osp.join(plot_dir,'sections_'+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'.png') #filename with the time to get a specific name not to overwrite the different sections files
        fig.savefig(filename,dpi=300,bbox_inches='tight')
        plt.close(fig)

    return plot_data

def plot_XY_flow(df,data_dir,line,orientation,frame,groups,window_size=None,timescale=1.,lengthscale=1.,z_depth=None,plot_on_map=False):
    """Plot the flow along the surface defined by a XY line. The first end of the line is x=0 for the plot. The cells crossing the line along the orientation (from first point to second) are counted
    as positive cells, the cells in the other are counted as negative. The count is integrated along a moving window along the line (line in um)"""
    close('all')

    plot_dir=osp.join(data_dir,'XY_flow')
    safe_mkdir(plot_dir)

    image_dir=osp.join(data_dir,'raw')
    if osp.isdir(image_dir)==False:
        image_dir=osp.join(data_dir,'traj')

    data=compute_XY_flow(df,data_dir,line,orientation,frame,groups,window_size=window_size,timescale=timescale,lengthscale=lengthscale,z_depth=z_depth)

    title='line_{}-{}_{}-{}'.format(int(line[0][0]),int(line[0][1]),int(line[1][0]),int(line[1][1]))
    xlab=r'x ($\mu m$)'
    if window_size is not None:
        ylab=r'flow ($cells.\mu m^{-2}.min^{-1}$)' if z_depth is not None else r'flow ($cells.\mu m^{-1}.min^{-1}$)'
    else:
        ylab=r'flow ($cells.min^{-1}$)'
    filename_prefix=osp.join(plot_dir,title)
    plot_data={'x_data':data[:,0],'y_data':data[:,1],'title':title,'xlab':xlab,'ylab':ylab,'filename_prefix':filename_prefix}
    
    #abscissa length 
    abs_length = np.sqrt((line[1][0]-line[0][0])**2+(line[1][1]-line[0][1])**2)/lengthscale

    fig, ax = plt.subplots(1, 1)
    if window_size is None:
        ax.scatter(data[:,0],data[:,1])
    else:
        ax.plot(data[:,0],data[:,1])
    ax.set_title(title)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.set_xlim(0,abs_length)
    ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,4))
    filename=filename_prefix+'_frame_{:04d}.png'.format(int(frame))
    fig.savefig(filename,dpi=300,bbox_inches='tight')
    plt.close(fig)

    if plot_on_map:
        fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame)
        ax.plot(line[:,0],line[:,1])
        ax.arrow(orientation[0,0],orientation[0,1],orientation[1,0]-orientation[0,0],orientation[1,1]-orientation[0,1],shape='full',length_includes_head=True,width=10,color='k')
        filename=osp.join(plot_dir,filename_prefix+'section.png')
        fig.savefig(filename,dpi=300,bbox_inches='tight')
        plt.close(fig)

    return plot_data

def fit_msd_biased_diff(msd,trajectory,fitrange=[7,60],save_plot=False,data_dir=None,traj=None,second_fit=False):
    '''Fit MSD twice with one-parameter fit. fitrange contains the max boundary of the first range and the max boundary of the second range'''

    if data_dir is not None:
        outdir=osp.join(data_dir,'MSD')
        safe_mkdir(outdir)
    else:
        outdir=None

    msd.dropna(inplace=True)

    #lmfit model
    success=False;best=None;logx=False;logy=False
    v_mean=np.sqrt(trajectory['vx'].mean()**2+trajectory['vy'].mean()**2)
    v_std=np.sqrt(trajectory['vx'].std()**2+trajectory['vy'].std()**2)

    func = lambda t,D:4*D*t+v_mean**2*t**2
    func_model=Model(func)
    p=func_model.make_params(D=1)
    p['D'].set(min=0)

    try:
        if type(fitrange[0]) is int:
            ind = msd['tau']<=fitrange[0]
            msd2 = msd[ind]
        elif type(fitrange[0]) is float:
            m=int(msd.shape[0]*fitrange[0])
            msd2=msd.loc[range(0,m)]

        best=func_model.fit(msd2['msd'],t=msd2['tau'],params=p)
        if best.success==False:
            print("WARNING: fit_msd failed")
        success=best.success
    except:
        best=Dummy_class()
        success=False
    
    if success:
        if second_fit: # Second fit on the second fitrange to get v
            D=best.best_values['D']
            func2 = lambda t,v:4*D*t+v**2*t**2
            func_model2=Model(func2)
            p2=func_model2.make_params(v=v_mean)
            p2['v'].set(min=0)

            try:
                ind = ((msd['tau']>=fitrange[0])&(msd['tau']<=fitrange[1]))
                msd2 = msd[ind]
                best2=func_model2.fit(msd2['msd'],t=msd2['tau'],params=p2)
                if best2.success==False:
                    print("WARNING: fit_msd failed")
                success2=best2.success
            except:
                best2=Dummy_class()
                success2=False
            
            if success2: #add to best the results from best2
                best.best_values['v']=best2.best_values['v']
                if best.covar is not None and best2.covar is not None: 
                    best.covar=array([[best.covar[0][0],0],[0,best2.covar[0][0]]])
                else:
                    best.covar=None
            else:
                success=False
        else: #get v by v_mean
            best.best_values['v']=v_mean
            if best.covar is not None: 
                best.covar=array([[best.covar[0][0],0],[0,v_std]])
            else:
                best.covar=None

    return best,None,success

    def compute_field(df,frame,groups,data_dir,grids=None,dim=3,export_field=False,temporal_average=0):
    """Compute field average by interpolating on a regular grid. 
    Average on a temporal window defined by the list of frames [n-temporal_average:n+temporal_average]"""
    
    print('computing velocity field {}'.format(int(frame)),end='\r')

    plot_dir=osp.join(data_dir,'vfield')
    safe_mkdir(plot_dir)

    coord_list=['x','y','z','x_scaled','y_scaled','z_scaled','vx','vy','vz'] if dim==3 else ['x','y','x_scaled','y_scaled','vx','vy']
    v_coord=['vx','vy','vz'] if dim==3 else ['vx','vy']
        
    group=groups.get_group(frame).reset_index(drop=True)

    if grids is not None:
        node_grid,center_grid = grids
        v_field=interpolate_field(df,groups,node_grid,temporal_average,frame,v_coord)        
    else:
        v_field=[group[v_coord[k]].values for k in range(dim)]
        x=group['x'].values;y=group['y'].values

    #save data in pickle
    data=node_grid+v_field
    save_map_data(plot_dir,data,frame)

    if export_vfield:
        export_dir = osp.join(plot_dir,'export_fields')
        safe_mkdir(export_dir)
        for i,map_ in enumerate(['x','y']+v_coord):
            f_out = osp.join(export_dir,map_+'_t_{:04d}.txt'.format(int(frame)))
            np.savetxt(f_out,data[i],delimiter=',')

    return data

def save_map_data(plot_dir,data,frame):
    datab_dir=osp.join(plot_dir,'data')
    safe_mkdir(datab_dir)
    pickle_fn=osp.join(datab_dir,'{:04d}.p'.format(int(frame)))
    pickle.dump(data,open(pickle_fn,"wb"))

def get_map_data(plot_dir,frame):
    pickle_fn=osp.join(plot_dir,'data','{:04d}.p'.format(int(frame)))
    if osp.exists(pickle_fn):
        data=pickle.load( open( pickle_fn, "rb" ))
    else:
        print('ERROR: database does not exist')
    return data

def get_image_size(data_dir):
    """Get the image size from the image from the raw folder if exists, otherwise from info.txt"""
    raw_dir = osp.join(data_dir,'raw')
    get_from_info=False #get from info.txt
    if osp.isdir(raw_dir): 
        if len(listdir_nohidden(raw_dir))==0: #if raw folder empty
            get_from_info=True
        else: 
            im = io.imread(osp.join(raw_dir,listdir_nohidden(raw_dir)[0]))
            image_size = [im.shape[1],im.shape[0]]
            #check of this take memory and im should be deleted
    else:
        get_from_info=True #if no raw folder

    if get_from_info:
        info=get_info(data_dir)
        if 'image_width' not in info.keys() or 'image_height' not in info.keys():
            raise Exception("ERROR: the image size is not in info.txt. Aborting...")
        image_size=[info['image_width'],info['image_height']]

    return image_size

class Dummy_class:
    """Class used to create an object containing a single attribute success. 
    Used in case of fit failure."""

    def __init__ (self):
        self.success = False

def select_frame_list(df,frame_subset=None,interactive=True):
    """Make a list of frame list with interactive input if needed. 
    frame_subset can be a number a list [first,last_included] or None for interactive"""
    if interactive:
        if frame_subset is None:
            typing=True
            while typing:
                try:
                    frame_subset=input("Give the frame subset you want to analyze as first,last or unique_frame, if you want them all just press ENTER: ")
                    frame_subset=[int(e) for e in frame_subset.split(",")]

                    if len(frame_subset)==2:
                        if frame_subset[0] in df['frame'].unique() and frame_subset[1] in df['frame'].unique():
                            typing=False
                        else:
                            print("WARNING: the subset is invalid, please try again")
                    elif len(frame_subset)==1:
                        frame_subset=frame_subset[0]
                        if frame_subset in df['frame'].unique():
                            typing=False
                        else:
                            print("WARNING: the subset is invalid, please try again")
                    else:
                        print("WARNING: the subset is invalid, please try again")
                except:
                    typing=False
                    frame_subset=None
     
        elif type(frame_subset) is list:
            if not frame_subset[0] in df['frame'].unique() or not frame_subset[1] in df['frame'].unique():
                return "WARNING: the subset is invalid, please try again"
        elif type(frame_subset) is int:
            if not frame_subset in df['frame'].unique():
                return "WARNING: the subset is invalid, please try again"
        else:
             return "WARNING: the subset is invalid, please try again"

    # select frame_list
    if frame_subset is None: #if no subset
        frame_list=np.sort(df['frame'].unique())
    elif type(frame_subset) is list:
        frame_list = range(frame_subset[0],frame_subset[1]+1)
    elif type(frame_subset) is int:
        frame_list = [frame_subset]
    return frame_list



    # if subtract_vfield is not None:
    #     image_size=get_image_size(data_dir)
    #     grids=make_grid(x_grid_size,image_size=image_size)
    #     subtract_vfield["temporal_average"]=1
    #     subtract_vfield["grid"]=grids[0]

def plot_vel(df,groups,frame,data_dir,grid,no_bkg=False,vlim=None,axis_on=False,save_plot=True,kind='v'):

    close('all')

    print('plotting cells {}'.format(int(frame)),end='\r')

    color_list=plot_param['color_list']

    plot_dir=osp.join(data_dir,kind)
    safe_mkdir(plot_dir)

    #get background using df (with all frames), so the image size is constant if no_bkg
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame,no_bkg=no_bkg,axis_on=axis_on)
    [vmin,vmax]= [df[kind].min(),df[kind].max()] if vlim is None else vlim
    cmap=cm.plasma; cmap.set_bad('w',alpha=0) #set NAN transparent
    
    sub_df=groups.get_group(frame).reset_index(drop=True)
    no_nan=sub_df[np.isfinite(sub_df[kind])]
    
    dont_plot=False
    if no_nan.shape[0]<4:
        dont_plot=True

    if not dont_plot:
        xi,yi=grid
        # Perform linear interpolation of the data (x,y) on a grid defined by (xi,yi)
        triang = tri.Triangulation(no_nan['x'].values, no_nan['y'].values)
        interpolator = tri.LinearTriInterpolator(triang, no_nan[kind].values)
        Xi, Yi = np.meshgrid(xi, yi)
        zi = interpolator(Xi, Yi)

        #plot
        levels=12
        ax.contourf(xi, yi, zi, levels,cmap=cmap,alpha=0.5,vmin=vmin,vmax=vmax)
    
    ax.axis([xmin,xmax,ymin,ymax])

    if axis_on:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)
    if save_plot:
        filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
        fig.savefig(filename, dpi=plot_param['dpi'])

def plot_vel_vs_Y(df,groups,frame,data_dir,origin=None,lengthscale=1.,save_plot=False,kind='v'):

    plot_dir=osp.join(data_dir,kind+'_vs_Y')
    safe_mkdir(plot_dir)
    
    sub_df=groups.get_group(frame).reset_index(drop=True)
    sub_df=sub_df[np.isfinite(sub_df[kind])]

    df_out=pd.DataFrame()
    if origin is not None:
        df_out['y']=abs(sub_df['y']-origin)/lengthscale
        df_out[kind]=sub_df[kind]
    else:
        df_out[['y',kind]]=sub_df[['y',kind]]
    df_out=df_out[np.isfinite(df_out)]

    if save_plot and df_out.shape[0]>0:
        close('all')
        fig,ax=plt.subplots(1,1)
        df_out.plot.scatter(x='y',y=kind,ax=ax)
        ax.set_ylabel(r'$v\ (\mu m.min^{-1})$')
        xlab='position along Y axis (px)' if origin is None else r'distance to anterior ($\mu m$)'
        ax.set_xlabel(xlab)
        filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
        fig.savefig(filename, dpi=plot_param['dpi'])

    return df_out
        # if plot_vs_Y:
    #     plot_MSD_method='along_Y'
    #     if transform_coord is not None:
    #         df_transf,col,col_=get_transf_coord(data_dir,timescale,lengthscale,dim)
    #         if frame_subset is not None:
    #             df_transf = df_transf[((df_transf['frame']>=frame_subset[0]) & (df_transf['frame']<=frame_subset[1]))]
    #         origins=df_transf['y'].mean()
    #     else:
    #         origins=set_origin(data_dir,refresh,dont_set_origin)
    # else:
    #     plot_MSD_method='boxplot'
    #     origins=None

    # if plot_vel is not None:
    #     plot_all_vel(df_list[0],data_dir,no_bkg=no_bkg,force_vlim=None,axis_on=False,kind=plot_vel)
    #     if plot_vs_Y:
    #         plot_all_vel_vs_Y(df_list[0],data_dir,frame_subset,origin=origins,force_vlim=None,save_frame_plot=False,cumulative_plot=False,avg_plot=True,lengthscale=lengthscale,timescale=timescale,kind=plot_vel)

def plot_mean_vel(df,frame,data_dir,no_bkg=False,vlim=None,axis_on=False,save_plot=True,no_stdout=False):
    close('all')
    
    if not no_stdout:
        print('plotting mean velocity {}'.format(int(frame)),end='\r')

    plot_dir=osp.join(data_dir,'mean_vel')
    safe_mkdir(plot_dir)

    #import image
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame,no_bkg=no_bkg,axis_on=axis_on)
    X,Y,mean_vel=get_map_data(plot_dir,frame)
    x_step=X[0,1]-X[0,0]
    y_step=Y[1,0]-Y[0,0]
    x=X-x_step/2
    y=Y-y_step/2
    mean_vel_masked = np.ma.array(mean_vel, mask=np.isnan(mean_vel))
    [vmin,vmax]= [mean_vel_masked.min(),mean_vel_masked.max()] if vlim is None else vlim
    cmap=cm.plasma; cmap.set_bad('w',alpha=0) #set NAN transparent
    C=ax.pcolormesh(x,y,mean_vel_masked,cmap=cmap,alpha=0.5,vmin=vmin,vmax=vmax)
    ax.axis([xmin,xmax,ymin,ymax])

    if axis_on:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)
    if save_plot:
        filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
        fig.savefig(filename, dpi=plot_param['dpi'])

    plot_fig=[fig,ax,xmin,ymin,xmax,ymax]
    data=[x,y,mean_vel,mean_vel_masked]
    return [plot_fig,data]

def plot_v_coord(df,frame,data_dir,no_bkg=False,vlim=None,axis_on=False,save_plot=True,coord='vx',grids=None):
    close('all')
    print('plotting '+coord+' {}'.format(int(frame)),end='\r')
    plot_dir=osp.join(data_dir,coord)
    safe_mkdir(plot_dir)
    coord_={'vx':2,'vy':3,'vz':4}

    #import image
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame,no_bkg=no_bkg,axis_on=axis_on)
    data=get_map_data(osp.join(data_dir,'vfield'),frame)
    data=data[coord_[coord]]
    data_masked = np.ma.array(data, mask=np.isnan(data))
    [vmin,vmax]= [data_masked.min(),data_masked.max()] if vlim is None else vlim
    cmap=cm.plasma; cmap.set_bad('w',alpha=0) #set NAN transparent
    X,Y=grids[0]
    x_step=X[0,1]-X[0,0]
    y_step=Y[1,0]-Y[0,0]
    x=X-x_step/2
    y=Y-y_step/2
    C=ax.pcolormesh(x,y,data_masked,cmap=cmap,alpha=0.5,vmin=vmin,vmax=vmax)
    ax.axis([xmin,xmax,ymin,ymax])

    if axis_on:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)
    if save_plot:
        filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
        fig.savefig(filename, dpi=plot_param['dpi'])

    plot_fig=[fig,ax,xmin,ymin,xmax,ymax]
    data=[x,y,data,data_masked]
    return [plot_fig,data]

def plot_div(df,frame,data_dir,no_bkg=False,vlim=None,axis_on=False):
    """ Plot 2D divergence"""
    close('all')
    print('plotting divergence field {}'.format(int(frame)),end='\r')
    plot_dir=osp.join(data_dir,'div')
    safe_mkdir(plot_dir)

    #import image
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame,no_bkg=no_bkg,axis_on=axis_on)
    X,Y,div=get_map_data(plot_dir,frame)
    div_masked = np.ma.array(div, mask=np.isnan(div))
    [vmin,vmax]= [div_masked.min(),div_masked.max()] if vlim is None else vlim
    cmap=cm.plasma; cmap.set_bad('w',alpha=0) #set NAN transparent
    C=ax.pcolormesh(X[1:-1,1:-1],Y[1:-1,1:-1],div_masked[1:-1,1:-1],cmap=cmap,alpha=0.5,vmin=vmin,vmax=vmax)
    ax.axis([xmin,xmax,ymin,ymax])

    if axis_on:
        ax.grid(False)
        ax.patch.set_visible(False)
        fig.set_tight_layout(True)
    filename=osp.join(plot_dir,'{:04d}.png'.format(int(frame)))
    fig.savefig(filename, dpi=plot_param['dpi'])
    plt.close(fig)

def plot_all_vfield(df,data_dir,grids=None,no_bkg=False,parallelize=False,dim=3,refresh=False,axis_on=False,plot_on_mean=False,black_arrows=False,manual_vlim=False,force_vlim=None,export_vfield=False,temporal_average=0):
    # Maps of all frames are computed through the compute_vlim function
    groups=df.groupby('frame')
    plot_dir=osp.join(data_dir,'vfield')
    safe_mkdir(plot_dir)

    if osp.isdir(osp.join(plot_dir,'data')) is False:
        refresh=True
    if refresh:
        # compute data
        # if parallelize:
        #     num_cores = multiprocessing.cpu_count()
        #     Parallel(n_jobs=num_cores)(delayed(compute_vfield)(df,groups,frame,data_dir,grids) for frame in df['frame'].unique())
        # else:
        #     vlim=compute_vlim(df,compute_vfield,groups,data_dir,grids)
        #     pickle.dump(vlim,open(osp.join(plot_dir,'data','vlim.p'),"wb"))

        #compute data
        vlim=compute_vlim(df,compute_vfield,groups,data_dir,grids,-1,dim=dim,export_vfield=export_vfield,temporal_average=temporal_average)
        pickle.dump(vlim,open(osp.join(plot_dir,'data','vlim.p'),"wb"))

    pickle.dump(grids,open(osp.join(plot_dir,'data','grids.p'),"wb"))
    vlim=pickle.load( open(osp.join(plot_dir,'data','vlim.p'), "rb" ))
    if force_vlim is not None:
        if force_vlim['vfield'] is not None:
            vlim=force_vlim['vfield']
    #plot colorbar
    if dim==3 and not black_arrows:
        plot_cmap(plot_dir,r'$v_z\ (\mu m.min^{-1})$',cm.plasma,vlim[0],vlim[1])

    if plot_on_mean:
        mean_dir=osp.join(data_dir,'mean_vel')
        safe_mkdir(mean_dir)

        if osp.isdir(osp.join(mean_dir,'data')) is False:
            refresh=True
        if refresh:
            #compute data
            if parallelize:
                num_cores = multiprocessing.cpu_count()
                Parallel(n_jobs=num_cores)(delayed(map_dic['mean_vel']['compute_func'])(df,groups,frame,data_dir,grids,lengthscale) for frame in df['frame'].unique())
            else:
                vlim_mean=compute_vlim(df,map_dic['mean_vel']['compute_func'],groups,data_dir,grids,-1,show_hist=manual_vlim,dim=dim)
                pickle.dump(vlim_mean,open(osp.join(mean_dir,'data','vlim.p'),"wb"))

        vlim_mean=pickle.load( open(osp.join(mean_dir,'data','vlim.p'), "rb" ))
        if force_vlim is not None:
            if force_vlim['mean_vel'] is not None:
                vlim_mean=force_vlim['mean_vel']
        #plot colorbar
        plot_cmap(plot_dir,map_dic['mean_vel']['cmap_label'],cm.plasma,vlim_mean[0],vlim_mean[1])
    else:
        vlim_mean=None

    #plot maps
    if parallelize:
        num_cores = multiprocessing.cpu_count()
        Parallel(n_jobs=num_cores)(delayed(plot_vfield)(df,frame,data_dir,no_bkg,vlim,axis_on,plot_on_mean,black_arrows) for frame in df['frame'].unique())
    else:
        for i,frame in enumerate(df['frame'].unique()):
            plot_vfield(df,frame,data_dir,no_bkg=no_bkg,vlim=vlim,axis_on=axis_on,plot_on_mean=plot_on_mean,black_arrows=black_arrows,vlim_mean=vlim_mean)

def plot_all_vel(df,data_dir,no_bkg=False,axis_on=False,force_vlim=None,nxgrid=100,kind='v'):

    plot_dir=osp.join(data_dir,kind)
    safe_mkdir(plot_dir)

    if force_vlim is None:
        vlim=[df[kind].min(),df[kind].max()]
    else:
        vlim=force_vlim

    #create interpolation grid
    fig,ax,xmin,ymin,xmax,ymax,no_bkg=get_background(df,data_dir,frame=df['frame'].unique().min(),no_bkg=no_bkg,axis_on=axis_on) #import background to get the image dimensions
    plt.close(fig)
    gridsize=(xmax-xmin)/nxgrid
    nygrid=int((ymax-ymin)/gridsize)
    grid = [np.linspace(xmin, xmax, nxgrid),np.linspace(ymin, ymax, nygrid)]

    groups=df.groupby('frame')

    plot_cmap(plot_dir,map_dic['mean_vel']['cmap_label'],cm.plasma,vlim[0],vlim[1])

    for frame in df['frame'].unique():
        plot_vel(df,groups,frame,data_dir,grid,no_bkg=no_bkg,vlim=vlim,axis_on=axis_on,kind=kind)

def plot_all_vel_vs_Y(df,data_dir,frame_subset=None,origin=None,force_vlim=None,save_frame_plot=False,cumulative_plot=True,avg_plot=True,lengthscale=1.,timescale=1.,reg_dx=1,window_size=50,kind='v'):

    plot_dir=osp.join(data_dir,kind+'_vs_Y')
    safe_mkdir(plot_dir)

    frame_list=select_frame_list(df,frame_subset,interactive=False)
    groups=df.groupby('frame')

    all_data={}
    reg_data={}

    min_y=None;max_y=None
    for frame in frame_list:
        raw_df=plot_vel_vs_Y(df,groups,frame,data_dir,origin=origin,lengthscale=lengthscale,save_plot=save_frame_plot,kind=kind)
        if raw_df.shape[0]>0:
            all_data[frame]=raw_df
            min_y = int(raw_df['y'].min()) if min_y is None else min(min_y,int(raw_df['y'].min()))
            max_y = int(raw_df['y'].max()) if max_y is None else max(max_y,int(raw_df['y'].max()))
        
    axis_data=arange(min_y,max_y,reg_dx)
    #rolling mean
    for frame in all_data.keys():
        reg_data[frame]=regularized_rolling_mean(all_data[frame].values,axis_data,window_size=window_size,reg_dx=reg_dx)
    
    xlab = 'position along Y axis (px)' if origin is None else r'distance to anterior ($\mu m$)'
    ylab = r'$v\ (\mu m.min^{-1})$'

    if cumulative_plot:
        time_min=min(frame_list)*timescale; time_max=max(frame_list)*timescale
        #colorbar
        Z = [[0,0],[0,0]]
        levels=array(frame_list)*timescale
        CS3 = plt.contourf(Z, levels, cmap=cm.plasma)
        plt.clf()
        #plot
        fig, ax = plt.subplots(1, 1)
        for frame in reg_data.keys():
            time=frame*timescale
            ax.scatter(reg_data[frame][:,0],reg_data[frame][:,1],color=get_cmap_color(time, cm.plasma, vmin=time_min, vmax=time_max))
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
        cb=fig.colorbar(CS3)
        cb.set_label(label='time (min)')
        filename=osp.join(plot_dir,'cumulative.svg')
        fig.savefig(filename,dpi=plot_param['dpi'],bbox_inches='tight')
        plt.close(fig)

    if avg_plot:
        x_data=reg_data[reg_data.keys()[0]][:,0]
        y_data_l=[reg_data[frame][:,1] for frame in reg_data.keys()]
        fig, ax = plt.subplots(1, 1)
        sns.tsplot(y_data_l,time=x_data,ax=ax,estimator=np.nanmean,err_style="unit_traces")
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
        filename=osp.join(plot_dir,'average.svg')
        sns.despine()
        fig.savefig(filename,dpi=plot_param['dpi'],bbox_inches='tight')
        plt.close(fig)

def plot_all_maps(df,data_dir,grids,map_kind,refresh=False,no_bkg=False,parallelize=False,dim=3,manual_vlim=False,axis_on=False,force_vlim=None,**kwargs):

    groups=df.groupby('frame')

    plot_dir=osp.join(data_dir,map_kind)
    safe_mkdir(plot_dir)

    #in the case of velocity coordinate don't recompute the data but get them from the vfield folder
    if map_kind in ['vx','vy','vz'] and osp.isdir(osp.join(data_dir,'vfield','data')):
        get_former_data=True
        plot_dir_=osp.join(data_dir,'vfield')
    else:
        get_former_data=False
        plot_dir_=None

    #force refresh if the data does not exist
    if not osp.isdir(osp.join(plot_dir,'data')):
        safe_mkdir(osp.join(plot_dir,'data'))
        refresh=True
    if refresh:
        #compute data
        if parallelize:
            num_cores = multiprocessing.cpu_count()
            Parallel(n_jobs=num_cores)(delayed(map_dic[map_kind]['compute_func'])(df,groups,frame,data_dir,grids,lengthscale) for frame in df['frame'].unique())
        else:
            if map_kind=='vx':
                data_coord=2
            elif map_kind=='vy':
                data_coord=3
            else:
                data_coord=-1
            vlim=compute_vlim(df,map_dic[map_kind]['compute_func'],groups,data_dir,grids,data_coord,dim,show_hist=manual_vlim,get_former_data=get_former_data,plot_dir=plot_dir_,**kwargs)
            pickle.dump(vlim,open(osp.join(plot_dir,'data','vlim.p'),"wb"))

    pickle.dump(grids,open(osp.join(plot_dir,'data','grids.p'),"wb"))
    vlim=pickle.load( open(osp.join(plot_dir,'data','vlim.p'), "rb" ))
    if force_vlim is not None:
        if force_vlim[map_kind] is not None:
            vlim=force_vlim[map_kind]
    #plot colorbar
    plot_cmap(plot_dir,map_dic[map_kind]['cmap_label'],cm.plasma,vlim[0],vlim[1])

    #plot maps
    if parallelize:
        num_cores = multiprocessing.cpu_count()
        Parallel(n_jobs=num_cores)(delayed(plot_z_flow)(df,frame,data_dir,no_bkg,vlim) for frame in df['frame'].unique())
    else:
        for i,frame in enumerate(df['frame'].unique()):
            if map_kind in ['vx','vy','vz']:
                map_dic[map_kind]['plot_func'](df,frame,data_dir,no_bkg,vlim,axis_on,coord=map_kind,grids=grids)
            else:
                map_dic[map_kind]['plot_func'](df,frame,data_dir,no_bkg,vlim,axis_on)

def avg_ROIs(data_dir,frame_subset=None,selection_frame=None,ROI_list=None,plot_on_map=True,plot_section=True,cumulative_plot=True,avg_plot=True,refresh=False,map_kind=None):
    df,lengthscale,timescale,columns,dim=get_data(data_dir,refresh=refresh)
    if map_kind is None:
        map_kind=input("Give the map wou want to plot your ROIs on (div,mean_vel,z_flow,vx,vy,vz): ")
    plot_all_avg_ROI(df,data_dir,map_kind,frame_subset=frame_subset,selection_frame=selection_frame,ROI_list=ROI_list,plot_on_map=plot_on_map,plot_section=plot_section,cumulative_plot=cumulative_plot,avg_plot=avg_plot,timescale=timescale)

def XY_flow(data_dir,window_size=None,refresh=False,line=None,orientation=None,frame_subset=None,selection_frame=None,z_depth=None):
    df,lengthscale,timescale,columns,dim=get_data(data_dir,refresh=refresh)
    
    if z_depth is None:
        z_lim=[df['z_rel'].min(),df['z_rel'].max()] if dim==3 else []
        z_depth=None if len(z_lim)==0 else z_lim[1]-z_lim[0]

    if window_size is None:
        window_size=int(input("Give the window size you want to calculate the flow on (in um and must be an integer >= 1): "))
    
    plot_all_XY_flow(df,data_dir,line=line,orientation=orientation,frame_subset=frame_subset,window_size=window_size,selection_frame=selection_frame,timescale=timescale,lengthscale=lengthscale,z_depth=z_depth)

def select_traj(data_dir,df=None,frame=1,min_traj_len=1,show_traj=False):
    """Select trajectories within an ROI at a certain frame"""
    if df is None:
        data=get_data(data_dir,refresh=False)
        df=data['df']
    df=filter_by_traj_len(df,min_traj_len=min_traj_len)

    #select cells
    image_dir=osp.join(data_dir,'raw')
    ROI_list=get_ROI(image_dir,frame,tool=RectangleTool)
    groups=df.groupby('frame')
    sub_df=groups.get_group(frame).reset_index(drop=True)
    
    selected_tracks=[]
    for ROI in ROI_list:
        xmin,xmax,ymin,ymax=ROI
        ind = ((sub_df['x']>=xmin)&(sub_df['x']<=xmax)&(sub_df['y']>=ymin)&(sub_df['y']<=ymax))
        selected_tracks = selected_tracks + list(sub_df[ind]['track'].values)

    if show_traj:
        plot_traj([df],[groups],frame,data_dir,plot_traj=True,hide_labels=False,display=True,traj_subset=selected_tracks)
    return selected_tracks

def compute_vlim(df,compute_func,groups,data_dir,grids,data_coord,dim=3,show_hist=False,get_former_data=False,plot_dir=None,**kwargs):
    # compute the max and min over all frames of a map. Compute maps for all frames
    vmin=np.nan;vmax=np.nan #boudaries of colorbar
    for i,frame in enumerate(df['frame'].unique()):
        data=get_map_data(plot_dir,frame) if get_former_data else compute_func(df,frame,groups,data_dir,grids,dim,**kwargs)
        data=data[data_coord]
        if show_hist:
            if i==0:
                r,c=data.shape
                data_hist=data.reshape(r*c,1)
            else:
                r,c=data.shape
                data_hist=vstack((data_hist,data.reshape(r*c,1)))
        if isnan(nanmin(data))==False:
            if isnan(vmin): #if no value computed yet
                vmin=nanmin(data)
            else:
                vmin=nanmin(data) if nanmin(data)<vmin else vmin
        if isnan(nanmax(data))==False:
            if isnan(vmax): #if no value computed yet
                vmax=nanmax(data)
            else:
                vmax=nanmax(data) if nanmax(data)>vmax else vmax

    if show_hist:
        close('all')
        # ion()
        s=pd.Series(data_hist[:,0])
        s.plot.hist()
        show()
        vlim=input('If you want to manually set the colorbar boundaries, enter the values (separated by a coma). Otherwise, press Enter: ')
        vlim=vlim.split(',')
        if len(vlim)==2:
            vmin=float(vlim[0]); vmax=float(vlim[1])
        # ioff()
    return [vmin,vmax]

def get_vlim(data_dir):
    """info.txt gives the lengthscale in um/px, the frame intervalle delta_t in min and the column names of the table"""
    filename=osp.join(data_dir,"vlim.txt")
    if osp.exists(filename):
        with open(filename) as f:
            vlim_dict={'vfield':None,'div':None,'mean_vel':None,'vx':None,'vy':None,'vz':None,'z_flow':None}
            for line in f:
                for key in vlim_dict.keys():
                    if (key in line)==True:
                        if len(line.split())==3:
                            vlim = line.split()[2].split(',')
                            vlim_dict[key] = [float(d) for d in vlim]
    else: 
        vlim_dict=None
    return vlim_dict

def select_map_ROI(data_dir,map_kind,frame,ROI_list=None):
    """Get data from a map in rectangular ROIs. If ROIs not given, manually drawn with get_coordinates."""
    image_dir1=osp.join(data_dir,'raw')

    map_kind_ = 'vfield' if map_kind in ['vx','vy','vz'] else map_kind
    if osp.isdir(image_dir1)==False:
        image_dir1=osp.join(data_dir,map_kind_)

    image_dir=osp.join(data_dir,map_kind_)
    not_found=True
    while not_found:
        if ROI_list is None:
            selection=get_coordinates(image_dir1,frame,tool=RectangleTool)
            ROI_list=selection['rectangle']
        data=get_map_data(image_dir,frame)
        grids=pickle.load( open(osp.join(image_dir,'data','grids.p'), "rb" ))
        node_grid,center_grid=grids
        x_,y_=center_grid
        if map_kind=='vy':
            data=data[3]
        elif map_kind=='vz':
            data=data[4]            
        else:
            data=data[2]
        ROI_data_list=[]
        square_ROI=False
        for ROI in ROI_list:
            x,y,dat,square_ROI=get_subblock_data(x_,y_,data,ROI)
            ROI_data_list.append([x,y,dat])

        if square_ROI:
            re_select=input("WARNING: there is a square ROI. Do you want to select again? [y]/n ")
            if re_select!='n':
                not_found=True
                ROI_list=None #reset ROI to call get_coordinates again
            else:
                not_found=False
        else:
            not_found=False

    return [ROI_data_list,ROI_list]


def plot_pooled_MSD(data_dir,param_list=['D','v'],dt=6,plot_method='along_Y'):
    """Get all the MSD subset in a MSD directory and pooled them on a single plot"""
    outdir=osp.join(data_dir,'MSD')
    if osp.isdir(outdir) is False:
        print("No MSD data")
        return -1

    for data_type in ['all_MSD','binned_MSD']:
        #get all subset files and sort them by increasing first subset boundary a (subset=[a,b]) 
        df_out=pd.DataFrame()
        f_list=[] #file list
        a_list=[] #list of first subset boundaries
        b_list=[] #list of second subset boundaries
        for f in listdir_nohidden(outdir):
            if f.endswith('.csv') and f.find('frame-subset')!=-1 and f.find(data_type)!=-1:
                subset=f[f.find('set_')+4:f.find('.csv')]
                a,b=subset.split('-')
                f_list.append(f)
                a_list.append(a)
                b_list.append(b)

        df_files=pd.DataFrame({'f':f_list,'a':a_list,'b':b_list})
        df_files=df_files.sort_values(by='a').reset_index(drop=True)
        df_files['a']=(df_files['a'].astype(np.float)*dt).astype(np.int)
        df_files['b']=(df_files['b'].astype(np.float)*dt).astype(np.int)

        for k,row in df_files.iterrows():
            f=row['f'];a=row['a'];b=row['b']
            df=pd.read_csv(osp.join(outdir,f),index_col=0)
            df['time_subset']=str(a)+'-'+str(b)+' min'
            df_out=pd.concat([df_out,df])
        df_out.to_csv(osp.join(outdir,data_type+'_pooled.csv'))

        #plot
        lab_dict={'v':r'$\langle v \rangle \ (\mu m/min)$','D':r'$D \ (\mu m^2/min)$'}

        if plot_method=="along_Y":
            df_fit=pd.DataFrame(columns=['gradient','grad_err','mean','std'],index=param_list)
            for param in param_list:
                fig,ax=plt.subplots(1,1)
                for k,time_subset in enumerate(df_out['time_subset'].unique()):
                    df=df_out[df_out['time_subset']==time_subset]
                    if data_type=='all_MSD':
                        df.plot.scatter(x='ymean',y=param,ax=ax,label=time_subset,color=color_list[k])
                    elif data_type=='binned_MSD':
                        df.plot.scatter(x='y',y=param+'_mean',yerr=param+'_std',ax=ax,label=time_subset,color=color_list[k])
                ax.set_ylabel(lab_dict[param])
                xlab=r'position along Y axis ($\mu m$)'
                ax.set_xlabel(xlab)
                sns.despine()
                fig.savefig(osp.join(outdir,param+'_'+data_type+'_along_Y_pooled.svg'),dpi=plot_param['dpi'],bbox_inches='tight')
                plt.close(fig)

                #fit gradient
                if data_type=='all_MSD':
                    data=df_out[['ymean',param]].values
                    parameters,errors,fitted_,Rsq,success=fit_lin(data)
                    df_fit.loc[param,['gradient','grad_err','mean','std']]=[parameters[0],errors[0],df_out[param].mean(),df_out[param].std()]
            if data_type=='all_MSD':
                df_fit.to_csv(osp.join(outdir,'lin-fit_along_Y_pooled.csv'))

        elif plot_method=="boxplot":
            for param in param_list:
                fig,ax=plt.subplots(1,1)
                sns.boxplot(data=df_out,x='time_subset',y=param,ax=ax,width=0.5)
                sns.swarmplot(data=df_out,x='time_subset',y=param,ax=ax,size=8,linewidth=1)   
                ax.set_ylabel(lab_dict[param])
                sns.despine()
                fig.savefig(osp.join(outdir,param+'_boxplot_pooled.svg'),dpi=plot_param['dpi'],bbox_inches='tight')
                plt.close(fig)

    return df_out

    # def plot_mean_param():
        # if plot_method=='along_Y':
    #     # scale Y position and (after shifting of origins is defined)
    #     if origins is not None:
    #         df_out['ymean']=(df_out['ymean']-origins)/lengthscale
    #         if invert_yaxis:
    #             df_out['ymean']=-df_out['ymean']
    #         if set_to_zero: #register everything to the lowest ymean
    #             df_out['ymean']=df_out['ymean']-df_out['ymean'].min()
    #     else: 
    #         df_out['ymean']=df_out['ymean']/lengthscale
    #     #fit gradient
    #     df_fit=pd.DataFrame(columns=['gradient','grad_err','mean','std'],index=param_list)
    #     for param in param_list:
    #         data=df_out[['ymean',param]].values
    #         parameters,errors,fitted_,Rsq,success=fit_lin(data)
    #         df_fit.loc[param,['gradient','grad_err','mean','std']]=[parameters[0],errors[0],df_out[param].mean(),df_out[param].std()]

    #     # average binned data in windows in um of siez given by bin_size
    #     if bin_size is not None:
    #         max_y=data[:,0].max()
    #         win_num=max_y//bin_size
    #         bin_Y=arange(0,(win_num+1)*bin_size+1,bin_size)

    #         cols_=['y']+[p+'_mean' for p in param_list]+[p+'_std' for p in param_list]
    #         df_bin=pd.DataFrame(columns=cols_)
    #         df_bin['y']=bin_Y[:-1]
    #         for i,win in enumerate(bin_Y[:-1]):
    #             ind = ((df_out['ymean']>=win) & ((df_out['ymean']<bin_Y[i+1])))
    #             discard=False
    #             if df_out[ind].shape[0]<1:
    #                 discard=True
    #             mean_ = df_out[ind][param_list].mean()
    #             std_ = df_out[ind][param_list].std()
    #             for param in param_list:
    #                 df_bin.loc[i,param+'_mean']=mean_[param] if discard is False else np.nan
    #                 df_bin.loc[i,param+'_std']=std_[param] if discard is False else np.nan
    #         df_bin.dropna(inplace=True)
    #         df_bin = df_bin.apply(pd.to_numeric)

    #     if to_csv:
    #         df_out.to_csv(osp.join(outdir,'all_MSD'+ext+'.csv'))
    #         try:
    #             df_bin.to_csv(osp.join(outdir,'binned_MSD'+ext+'.csv'))
    #         except NameError:
    #             df_bin = None
    #         df_fit.to_csv(osp.join(outdir,'lin-fit_along_Y'+ext+'.csv'))

    #     for param in param_list:
    #         fig,ax=plt.subplots(1,1)
    #         df_out.plot.scatter(x='ymean',y=param,ax=ax)
    #         ax.set_ylabel(lab_dict[param])
    #         xlab=r'position along Y axis ($\mu m$)' if origins is None else r'distance to origin ($\mu m$)'
    #         ax.set_xlabel(xlab)
    #         sns.despine()
    #         fig.savefig(osp.join(outdir,param+'_along_Y'+ext+'.svg'))

    #         if bin_size is not None:
    #             fig,ax=plt.subplots(1,1)
    #             df_bin.plot.scatter(x='y',y=param+'_mean',yerr=param+'_std',ax=ax)
    #             ax.set_ylabel(lab_dict[param])
    #             xlab=r'position along Y axis ($\mu m$)' if origins is None else r'distance to origin ($\mu m$)'
    #             ax.set_xlabel(xlab)
    #             sns.despine()
    #             fig.savefig(osp.join(outdir,param+'_binned_along_Y'+ext+'.svg'))

    # elif plot_method=='boxplot':
    #     for param in param_list:
    #         fig,ax=subplots(1,1)
    #         sns.boxplot(data=df_out,y=param,ax=ax,width=0.2)
    #         sns.swarmplot(data=df_out,y=param,ax=ax,size=8,linewidth=1,color="0.3")        
    #         ax.set_ylabel(lab_dict[param])
    #         sns.despine()
    #         fig.savefig(osp.join(outdir,param+'_boxplot'+ext+'.svg'))


def centered_first_der(a,dx=1,periodic=True):
    """Calculate the first order centered first derivative of an array a of increment dx.
    If the array is periodic the first and last elements are kept, otherwise they are set to Nan"""
    a_pr=(np.roll(a,-1)-np.roll(a,1))/(2*dx)
    if not periodic:
        a_pr[0]=np.nan
        a_pr[-1]=np.nan
    return a_pr

def centered_sec_der(a,dx=1,periodic=True):
    """Calculate the first order centered second derivative of an array a of increment dx.
    If the array is periodic the first and last elements are kept, otherwise they are set to Nan"""
    a_sec=(np.roll(a,-1)-2*(a)+np.roll(a,1))/(dx**2)
    if not periodic:
        a_sec[0]=np.nan
        a_sec[-1]=np.nan
    return a_sec

def compute_z_flow(df,frame,groups,data_dir,grids,z0,timescale):
    sys.stdout.write('\033[2K\033[1G')
    print('computing z_flow field {}'.format(int(frame)),end='\r')
    #Make sure these are 3D data
    if 'z' not in df.columns:
        print("Not a 3D set of data")
        return

    plot_dir=osp.join(data_dir,'z_flow')
    safe_mkdir(plot_dir)

    group=groups.get_group(frame).reset_index(drop=True)

    df_layer=group[abs(group['vz']*timescale)>=abs(z0-group['z_rel'])] #layer of cells crossing the surface
    df_ascending=df_layer[((df_layer['vz']>=0) & (df_layer['z_rel']<=z0))] #ascending cells below the surface
    df_descending=df_layer[((df_layer['vz']<=0) & (df_layer['z_rel']>=z0))] #descending cells above the surface
    
    #calculate the intersection coordinates (x0,y0) of the vector and the surface (calculate homothety coefficient alpha)
    for df_ in [df_ascending,df_descending]:
        df_.loc[:,'alpha']=abs(z0-df_['z_rel'])/(df_['vz']*timescale)
        df_.loc[:,'x0']=df_['x']+df_['alpha']*df_['vx']*timescale
        df_.loc[:,'y0']=df_['y']+df_['alpha']*df_['vy']*timescale
    
    node_grid,center_grid=grids   
    X,Y=node_grid
    x,y=center_grid
    flow = zeros((x.shape[0],x.shape[1]))
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            ind_asc=((df_ascending['x0']>=X[i,j]) & (df_ascending['x0']<X[i,j+1]) & (df_ascending['y0']>=Y[i,j]) & (df_ascending['y0']<Y[i+1,j]))
            ind_des=((df_descending['x0']>=X[i,j]) & (df_descending['x0']<X[i,j+1]) & (df_descending['y0']>=Y[i,j]) & (df_descending['y0']<Y[i+1,j]))
            flow[i,j]=(df_ascending[ind_asc].shape[0]-df_descending[ind_des].shape[0])/timescale

    #save data in pickle
    data=(x,y,flow)
    save_map_data(plot_dir,data,frame)

    return data

    def compute_msd_non_regular(traj, coords=['x_scaled', 'y_scaled']):
    '''Compute the MSD of a trajectory that potentially misses some steps. By default, it uses scaled data. The trajectory steps MUST be constant'''
    
    dt_array=traj['t'][1:].values - traj['t'][:-1].values
    if dt_array[dt_array==0].size!=0: #if there is an overlap
        print("WARNING: overlap in the traj")
    dt = dt_array[dt_array!=0].min()
    max_shift = np.floor(traj['t'].values.max()/dt).astype(np.int)
    shifts = range(0,max_shift+1)
    tau = np.array(shifts)*dt
    msd = np.zeros(tau.size)
    msd_std = np.zeros(tau.size)
    numpoints = np.zeros(tau.size)
    
    #initialize dictionary of square displacements (displ(t)-displ(t-delta_t))
    sqdists={}
    for delta in tau:
        sqdists[delta]=np.array([])
    
    for shift in shifts:
        #get the displacement if the shift is equal to the right delta
        shifted=traj.shift(-shift)-traj
        delta_set = shifted['t'].unique()
        for delta in delta_set[~np.isnan(delta_set)]:
            indices = shifted['t'] == delta
            sqdists[delta] = np.append(sqdists[delta],np.square(shifted.loc[indices,coords]).sum(axis=1))

    for i,delta in enumerate(tau):
        sqdist=sqdists[delta][~np.isnan(sqdists[delta])]
        msd[i] = sqdist.mean()
        msd_std[i] = sqdist.std()
        numpoints[i] = sqdist.size
    msd = pd.DataFrame({'msd': msd, 'tau': tau, 'msd_std': msd_std, 'numpoints':numpoints})
    return msd

def compute_mean_vel(df,frame,groups,data_dir,grids,dim=3):
    """Uses the vfield data to compute the modulus of the vfield on center_grid (x,y)"""
    sys.stdout.write('\033[2K\033[1G')
    print('computing mean velocity field {}'.format(int(frame)),end='\r')

    plot_dir=osp.join(data_dir,'mean_vel')
    safe_mkdir(plot_dir)

    #get avg_vfield
    node_grid,center_grid=grids
    X,Y=node_grid
    data=get_map_data(osp.join(data_dir,'vfield'),frame)
    avg_vfield=data[2:]

    #compute avg
    V=0
    for k in range(dim):
        V+=avg_vfield[k]**2
    mean_vel=sqrt(V)

    #save data in pickle
    data=(X,Y,mean_vel)
    save_map_data(plot_dir,data,frame)

    return data    

def get_subblock_data(X,Y,data,ROI):
    square_ROI=False
    xmin,xmax,ymin,ymax=ROI
    ind=((X>=xmin) & (X<=xmax) & (Y>=ymin) & (Y<=ymax))
    x,y=meshgrid(np.unique(X[ind]),np.unique(Y[ind])) #sublock (x,y)
    if x.shape[0]==x.shape[1]:
        square_ROI=True
    dat=data[ind].reshape(*x.shape)
    return [x,y,dat,square_ROI]

def avg_ROI_major_axis(ROI_data):
    """average data along the major axis of the ROI"""

    #get principal axis
    r,c=ROI_data[0].shape
    if r==c:
        print('ERROR: square ROI')
        return
    elif r>c:
        major_ax,minor_ax=0,1
    elif r<c:
        major_ax,minor_ax=1,0

    #average
    avg_data=[]
    for d in ROI_data:
        avg_data.append(np.nanmean(d,axis=minor_ax))

    return {'data':avg_data,'major_ax':major_ax}

def exclude_traj(data_dir,frame=1,show_traj=False):
    """Select trajectories to exclude from analysis within an ROI at a certain frame and save them in the exclude file"""
    selected_traj=select_traj(data_dir,frame=frame,min_traj_len=1,show_traj=show_traj)

    exclude_fn = osp.join(data_dir,'exclude_traj.txt')
    with open(exclude_fn,'a') as f:
        for traj in selected_traj:
            f.write('{}\n'.format(int(traj)))

def regularized_rolling_mean(data,axis_data,window_size=None,reg_dx=1.):
    """Compute the rolling sum of a discrete set of data (2D array: x,y) along a regularized axis (axis_data: 1D array) with a step of reg_dx"""
    if window_size is None:
        return data

    #regularize data (fill with zeros missing data)
    reg_data=array([axis_data,np.zeros(axis_data.shape[0])]).T
    for i in range(data.shape[0]):
        ind=((reg_data[:,0]>=data[i,0]) & (reg_data[:,0]<data[i,0]+reg_dx)) #find index in new
        reg_data[ind,1]+=data[i,1]

    #rolling
    reg_data=pd.DataFrame(reg_data,columns=list('xy'))
    reg_data['y']=reg_data['y'].rolling(window_size,min_periods=1).mean()

    return reg_data.values

def show_usage():
    """Print usage (outdated)"""
    usage_message = """Usage: \n- plot cells analysis using cell_analysis(data_dir,refresh,parallelize,plot_traj,hide_labels,transform_coord,no_bkg,linewidth,plot3D,min_traj_len,frame_subset,redchi_th) \t data_dir: data directory, refresh (default False) to refresh the table values, parallelize (default False) to run analyses in parallel, 
    plot_traj (default true) to print the cell trajectories, hide_labels (default True) to hide the cell label, no_bkg (default False) to remove the image background, linewidth being the trajectories width (default=1.0), frame_subset: to plot only on a subset of frames [first,last], transform_coord: transform coordinates using coord_transformation.csv file (default: False),split_MSD_analysis: wraper function to split analysis of MSD in 30 frames chunks (default=True)\n
    - plot maps using map_analysis(data_dir,refresh,parallelize,x_grid_size,no_bkg,z0,dimensions,axis_on,plot_on_mean,black_arrows,export_field) \t data_dir: data directory, refresh (default False) to refresh the table values, parallelize (default False) to run analyses in parallel, 
    x_grid_size: number of columns in the grid (default 10), no_bkg (default False) to remove the image background, z0: altitude of the z_flow surface (default None => center of z axis), dimensions ([row,column] default None) to give the image dimension in case of no_bkg, axis_on: display axes along maps (default False),plot_on_mean: plot vfield on mean_vel map (default=True),
    black_arrows: don't use vz to color code vfield arrows (default=True), export_field: export velocity fields as txt files (default False) \n
    - plot average ROIs using avg_ROIs(data_dir,frame_subset=None,selection_frame=None,ROI_list=None,plot_on_map=True,plot_section=True,cumulative_plot=True,avg_plot=True) \t data_dir: data directory, frame_subset is a list [first,last], default None: open interactive choice \n
    - plot XY flow through a vertical surface defined by a XY line using XY_flow(data_dir,window_size=None,refresh=False,line=None,orientation=None,frame_subset=None,selection_frame=None,z_depth=None) \t data_dir: data directory, frame_subset is a list [first,last], default None: open interactive choice, window_size = rolling average window in um, default None => interactive choice \n
    - plot_centered_traj(data_dir,selection_frame=1,min_traj_len=1,frame_subset=None,force_max_frame=None,dont_center=False,hide_labels=False,transform_coord=False,refresh=False,set_axis_lim=None) \n
    - plot_vx_vs_vy(data_dir,transform_coord=False,refresh=False,select_ROI=True,set_axis_lim=None)"""
    print(usage_message)

def filter_by_ROI(df, image, filter_all_frames=False, return_ROIs=False):
    """Function used to choose subsets of trajectories which are within ROIs eiher: at a given frame (if filter_all_frames is False), or at all frame (if filter_all_frames is True).
    The selection is made by means of a rectangle tool on the image. It can be a 2D, 3D, or 4D image.
    t_dim and z_dim give the dimension index of time and z of the nd-image. If None, this dimension doesn't exist """

    if image is None:
        raise Exception("ERROR: no image provided. Aborting...")

    tracks = df.groupby('track')
    df_out = pd.DataFrame()

    selection = get_coordinates(image)
    ROI_list = selection['rectangle']

    for i, ROI in enumerate(ROI_list):
        xmin, xmax, ymin, ymax = ROI['coord']
        frame = ROI['frame']

        subdf = pd.DataFrame()
        if filter_all_frames:
            for fr in df['frame'].unique():
                # the subset at the given frame
                ind = ((df['frame'] == fr) & (df['x'] >= xmin) & (df['x'] <= xmax) & (df['y'] >= ymin) & (
                        df['y'] <= ymax))
                subdf = pd.concat([subdf, df[ind]])
        else:
            # the subset at the given frame
            ind = ((df['frame'] == frame) & (df['x'] >= xmin) & (df['x'] <= xmax) & (df['y'] >= ymin) & (
                    df['y'] <= ymax))
            subdf_frame = df[ind]

            # get the subset in the whole dataset
            for t in subdf_frame['track'].unique():
                track = tracks.get_group(t)
                subdf = pd.concat([subdf, track])

        # remove empty ROI
        if subdf.shape[0] == 0:
            print("Warning: ROI #{} doesn't contain any trajectory. ROI skipped...".format(i))
        else:
            subdf['group'] = i
            df_out = pd.concat([df_out, subdf])

    if return_ROIs:
        return df_out, ROI_list
    else:
        return df_out

    