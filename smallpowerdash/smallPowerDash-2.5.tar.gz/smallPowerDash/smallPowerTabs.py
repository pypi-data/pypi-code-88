import datetime as dt, pickle, time
import os,re,pandas as pd
import dash, dash_core_components as dcc, dash_html_components as html, dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px, plotly.graph_objects as go
import matplotlib.pyplot as plt, matplotlib.colors as mtpcl
from pylab import cm
from dorianUtils.dccExtendedD import DccExtended
from dorianUtils.dashTabsD import TabSelectedTags
from dorianUtils.utilsD import Utils
import smallPowerDash.configFilesSmallPower as cfs

class SmallPowerTab():
    def __init__(self,app,baseId):
        self.baseId=baseId
        self.app = app
        self.utils = Utils()
        self.dccE = DccExtended()
    # ==========================================================================
    #                           SHARED FUNCTIONS CALLBACKS
    # ==========================================================================
    def addWidgets(self,dicWidgets,baseId):
        widgetLayout,dicLayouts = [],{}
        for wid_key,wid_val in dicWidgets.items():
            if 'dd_computation' in wid_key:
                widgetObj = self.dccE.dropDownFromList(baseId+wid_key,self.computationGraphs,
                                                        'what should be computed ?',value = wid_val)


            elif 'dd_expand' in wid_key:
                widgetObj = self.dccE.dropDownFromList(baseId+wid_key,['groups','tags'],'Select the option : ',value = wid_val)

            elif 'dd_modules' in wid_key:
                widgetObj = self.dccE.dropDownFromList(baseId+wid_key,
                            list(self.cfg.modules.keys()),'Select your module: ',value = wid_val)

            elif 'dd_ModuleUnit' in wid_key:
                widgetObj = self.dccE.dropDownFromList(baseId+wid_key,[],
                                'Select the graphs to display: ',value = 0,multi=True)

            for widObj in widgetObj:widgetLayout.append(widObj)

        return widgetLayout

class ComputationTab(SmallPowerTab):
    def __init__(self,folderPkl,app,baseId='ct0_'):
        super().__init__(app,baseId)
        self.cfg = cfs.ConfigFilesSmallPower(folderPkl)
        self.computationGraphs=['power repartition']
        self.tabLayout = self._buildComputeLayout()
        self.tabname = 'computation'
        self._define_callbacks()

    def _define_callbacks(self):
        listInputsGraph = {
            'dd_computation':'value',
            'pdr_timeBtn':'n_clicks',
            'dd_resampleMethod' : 'value',
            'dd_expand' : 'value',
            'dd_cmap':'value',
            'dd_style':'value'
            }
        listStatesGraph = {
            'graph':'figure',
            'in_timeRes' : 'value',
            'pdr_timeStart' : 'value',
            'pdr_timeEnd':'value',
            'pdr_timePdr':'start_date',
                            }

        @self.app.callback(
        Output(self.baseId + 'graph', 'figure'),
        Output(self.baseId + 'pdr_timeBtn', 'n_clicks'),
        [Input(self.baseId + k,v) for k,v in listInputsGraph.items()],
        [State(self.baseId + k,v) for k,v in listStatesGraph.items()],
        State(self.baseId+'pdr_timePdr','end_date'))
        def updateGraph(computation,timeBtn,rsmethod,expand,colmap,style,fig,rs,date0,date1,t0,t1):
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # to ensure that action on graphs only without computation do not
            # trigger computing the dataframe again
            if not timeBtn or trigId in [self.baseId+k for k in ['dd_computation','pdr_timeBtn','dd_typeGraph','dd_expand','dd_resampleMethod']] :
                if not timeBtn : timeBtn=1 # to initialize the first graph
                timeRange = [date0+' '+t0,date1+' '+t1]
                params,params['rs'],params['method'],params['expand']={},rs,rsmethod,expand
                fig   = self.plotGraphComputation(timeRange,computation,params)
                timeBtn = max(timeBtn,1) # to close the initialisation
            else :fig = go.Figure(fig)
            fig = self.utils.updateStyleGraph(fig,style,colmap)
            return fig,timeBtn

        @self.app.callback(Output(self.baseId + 'btn_export','children'),
        Input(self.baseId + 'btn_export', 'n_clicks'),
        State(self.baseId + 'graph','figure'))
        def exportClick(btn,fig):
            fig = go.Figure(fig)
            if btn>0:self.utils.exportDataOnClick(fig,baseName='proof')
            return 'export Data'

    def plotGraphComputation(self,timeRange,computation,params):
        start     = time.time()
        if computation == 'power repartition' :
            fig = self.cfg.plotGraphPowerArea(timeRange,rs=params['rs'],applyMethod=params['method'],expand=params['expand'])
            fig.update_layout(yaxis_title='power in W')
        self.utils.printCTime(start,'computation time : ')
        return fig

    def _buildComputeLayout(self,widthG=80):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                    'in_timeRes':str(60*10)+'s','dd_resampleMethod':'mean',
                    'dd_style':'lines+markers','dd_cmap':'jet','btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_computation':'power repartition','dd_expand':'groups'},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

class ModuleTab(SmallPowerTab):
    def __init__(self,folderPkl,app,baseId='tmo0_'):
        super().__init__(app,baseId)
        self.cfg = cfs.AnalysisPerModule(folderPkl)
        self.tabLayout = self._buildModuleLayout()
        self.tabname = 'modules'
        self._define_callbacks()

    def _buildModuleLayout(self,widthG=85):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                    'in_timeRes':str(60*10)+'s','dd_resampleMethod':'mean',
                    'dd_style':'lines','dd_cmap':'prism','in_heightGraph':900,'btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_modules':'GV','dd_ModuleUnit':None},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

    def _define_callbacks(self):
        @self.app.callback(
        Output(self.baseId + 'dd_ModuleUnit', 'options'),
        Input(self.baseId + 'dd_modules','value'),
        )
        def updateGraph(module):
            # list(self.cfg.modules[module].keys())
            l= list(self.cfg._categorizeTagsPerUnit(module).keys())
            options = [{'label':t,'value':t} for t in l]
            return options

        listInputsGraph = {
            'dd_modules':'value',
            'pdr_timeBtn':'n_clicks',
            'dd_resampleMethod' : 'value',
            'dd_cmap':'value',
            'dd_style':'value',
            'in_heightGraph':'value',
            }
        listStatesGraph = {
            'graph':'figure',
            'in_timeRes' : 'value',
            'pdr_timeStart' : 'value',
            'pdr_timeEnd':'value',
            'pdr_timePdr':'start_date',
        }
        @self.app.callback(
        Output(self.baseId + 'graph', 'figure'),
        Output(self.baseId + 'pdr_timeBtn', 'n_clicks'),
        [Input(self.baseId + k,v) for k,v in listInputsGraph.items()],
        [State(self.baseId + k,v) for k,v in listStatesGraph.items()],
        State(self.baseId+'pdr_timePdr','end_date'))
        def updateGraph(module,timeBtn,rsmethod,colmap,style,hg,fig,rs,date0,date1,t0,t1):
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # to ensure that action on graphs only without computation do not
            # trigger computing the dataframe again
            if not timeBtn or trigId in [self.baseId+k for k in ['dd_modules','pdr_timeBtn','dd_resampleMethod']] :
                # print('===============here===============')
                if not timeBtn : timeBtn=1 # to initialize the first graph
                timeRange = [date0+' '+t0,date1+' '+t1]
                fig = self.cfg.figureModuleUnits(module,timeRange,rs=rs,applyMethod=rsmethod)
                timeBtn = max(timeBtn,1) # to close the initialisation
            else :fig = go.Figure(fig)
            fig = self.utils.updateStyleGraph(fig,style,colmap,heightGraph=hg)
            return fig,timeBtn

        @self.app.callback(
        Output(self.baseId + 'btn_export','children'),
        Input(self.baseId + 'btn_export', 'n_clicks'),
        State(self.baseId + 'graph','figure'))
        def exportClick(btn,fig):
            fig = go.Figure(fig)
            if btn>0:self.utils.exportDataOnClick(fig,baseName='proof')
            return 'export Data'

class RealTimeTagSelectorTab(SmallPowerTab,TabSelectedTags):
    def __init__(self,app,timeWindow=2*60*60,connParameters=None,baseId='ts0_'):
        super().__init__(app,baseId)
        self.cfg = cfs. ConfigFilesSmallPower_RealTime(timeWindow=timeWindow,connParameters=connParameters)
        self.tabLayout = self._buildLayout()
        self.tabname = 'graph selector'
        self._define_callbacks()

    def addWidgets(self,dicWidgets,baseId):
        return TabSelectedTags.addWidgets(self,dicWidgets,baseId)

    def _buildLayout(self,widthG=80):
        dicWidgets = {  'btn_update':None,
                        'in_timeRes':str(60*10)+'s','dd_resampleMethod' : 'mean',
                        'dd_style':'lines+markers','dd_typeGraph':'scatter',
                        'dd_cmap':'jet'}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_typeTags':'Temperatures du gv1a','btn_legend':0},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

    def _define_callbacks(self):

        @self.app.callback(Output(self.baseId + 'btn_legend', 'children'),
                            Input(self.baseId + 'btn_legend','n_clicks'))
        def updateLgdBtn(legendType):return self.updateLegendBtnState(legendType)

        listInputsGraph = {
                        'btn_update':'n_clicks',
                        'dd_typeTags':'value',
                        'dd_resampleMethod':'value',
                        'dd_typeGraph':'value',
                        'dd_cmap':'value',
                        'btn_legend':'children',
                        'dd_style':'value'}
        listStatesGraph = {
                            'graph':'figure',
                            'in_timeRes':'value'
                            }
        @self.app.callback(
        Output(self.baseId + 'graph', 'figure'),
        Output(self.baseId + 'btn_update', 'children'),
        [Input(self.baseId + k,v) for k,v in listInputsGraph.items()],
        [State(self.baseId + k,v) for k,v in listStatesGraph.items()],
        )
        def updateGraph(updateBtn,preSelGraph,rsMethod,typeGraph,colmap,lgd,style,fig,rs):
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # to ensure that action on graphs only without computation do not
            # trigger computing the dataframe again
            triggerList = [self.baseId+k for k in ['dd_typeTags','btn_update','dd_resampleMethod','dd_typeGraph']]
            if not updateBtn or trigId in  triggerList:
                start       = time.time()
                df          = self.cfg.realtimeDF(preSelGraph,rs=rs,applyMethod=rsMethod)
                self.utils.printCTime(start)
                # print(df)
                fig     = self.drawGraph(df,typeGraph)
                unit = self.cfg.getUnitofTag(df.columns[0])
                nameGrandeur = self.cfg.utils.detectUnit(unit)
                fig.update_layout(yaxis_title = nameGrandeur + ' in ' + unit)
            else :fig = go.Figure(fig)
            fig = self.utils.updateStyleGraph(fig,style,colmap)
            fig = self.updateLegend(fig,lgd)
            return fig,updateBtn
