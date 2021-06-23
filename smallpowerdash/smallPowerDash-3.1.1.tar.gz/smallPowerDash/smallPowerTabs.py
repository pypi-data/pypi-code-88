import datetime as dt, pickle, time, os,re,pandas as pd
import dash, dash_core_components as dcc, dash_html_components as html, dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px, plotly.graph_objects as go
# import matplotlib.pyplot as plt, matplotlib.colors as mtpcl
# from pylab import cm
from dorianUtils.utilsD import Utils
from dorianUtils.dccExtendedD import DccExtended
from dorianUtils.dashTabsD import TabSelectedTags,TabUnitSelector,TabMultiUnits
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

            elif 'dd_moduleGroup' in wid_key:
                widgetObj = self.dccE.dropDownFromList(baseId+wid_key,[],
                                'Select the graphs to display: ',value = 0,multi=True)
            elif 'check_unit' in wid_key:
                widgetObj = [dcc.Checklist(id=baseId+wid_key,options=[{'label': 'unit', 'value':'unit'}],value= wid_val)]

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

    def _buildComputeLayout(self,widthG=85):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                    'in_timeRes':str(60*10)+'s','dd_resampleMethod':'mean',
                    'dd_style':'lines+markers','dd_cmap':'jet','btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_computation':'power repartition','dd_expand':'groups'},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

class ModuleTab(SmallPowerTab):
    def __init__(self,folderPkl,app,baseId='tmo0_',widthGraph=85):
        super().__init__(app,baseId)
        self.cfg = cfs.AnalysisPerModule(folderPkl)
        self.widthGraph = widthGraph
        self.tabLayout = self._buildModuleLayout()
        self.tabname = 'modules'
        self._define_callbacks()

    def _buildModuleLayout(self):
        dicWidgets = {
                    'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                    'in_timeRes':'auto','dd_resampleMethod':'mean',
                    'dd_style':'lines','dd_cmap':'prism',
                    'btn_export':0,
                    'block_multiAxisSettings':None
                    }
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'check_unit':['unit'],'dd_modules':'GV','dd_moduleGroup':None},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=self.widthGraph)

    def _define_callbacks(self):
        @self.app.callback(
        Output(self.baseId + 'dd_moduleGroup', 'options'),
        Input(self.baseId + 'dd_modules','value'),
        Input(self.baseId + 'check_unit','value'),
        )
        def updateGraph(module,unitGroup):
            if not unitGroup : l = self.cfg.listTagsAllModules(module)[1]
            else : l= list(self.cfg._categorizeTagsPerUnit(module).keys())
            options = [{'label':t,'value':t} for t in l]
            return options

        listInputsGraph = {
            'pdr_timeBtn':'n_clicks',
            'dd_resampleMethod' : 'value',
            'dd_cmap':'value',
            'dd_style':'value',
            'in_heightGraph':'value',
            'in_axisSp':'value',
            'in_hspace':'value',
            'in_vspace':'value',
            }
        listStatesGraph = {
            'graph':'figure',
            'dd_modules':'value',
            'check_unit':'value',
            'dd_moduleGroup':'value',
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
        def updateGraph(timeBtn,rsmethod,colmap,style,hg,axsp,hs,vs,fig,module,unitGroup,listGroups,rs,date0,date1,t0,t1):
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # triggerList = ['dd_modules','dd_moduleGroup','pdr_timeBtn','dd_resampleMethod']
            triggerList = ['pdr_timeBtn','dd_resampleMethod']
            if not timeBtn or trigId in [self.baseId+k for k in triggerList] :
                timeRange = [date0+' '+t0,date1+' '+t1]
                if not unitGroup :
                    fig = self.cfg.figureModule(module,timeRange,groupsOfModule=listGroups,rs=rs,applyMethod=rsmethod)
                else :
                    fig = self.cfg.figureModuleUnits(module,timeRange,listUnits=listGroups,rs=rs,applyMethod=rsmethod)
            else :fig = go.Figure(fig)
            if not unitGroup :fig = self.cfg.updateFigureModule(fig,module,listGroups,hg,hs,vs,axsp)
            else : fig = fig.update_layout(height=hg)
            # fig = self.updateLegend(fig,lgd)
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
    def __init__(self,app,connParameters=None,baseId='ts0_'):
        super().__init__(app,baseId)
        self.cfg         = cfs. ConfigFilesSmallPower_RealTime(connParameters=connParameters)
        self.tabname     = 'tag selector'
        self.tabLayout   = self._buildLayout()
        self._define_callbacks()

    def addWidgets(self,dicWidgets,baseId):
        return TabSelectedTags.addWidgets(self,dicWidgets,baseId)

    def _buildLayout(self,widthG=85):
        dicWidgets = {
                        'block_refresh':{'val_window':60*2,'val_refresh':20,'min_refresh':5,'min_window':1},
                        'btn_update':0,
                        'block_resample':{'val_res':'auto','val_method' : 'mean'},
                        'block_graphSettings':{'style':'lines+markers','type':'scatter','colmap':'jet'}
                        }
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        print(self.dccE.parseLayoutIds(basicWidgets))
        specialWidgets = self.addWidgets({'dd_typeTags':'Temperatures du gv1a','btn_legend':0},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

    def _define_callbacks(self):

        @self.app.callback(Output(self.baseId + 'interval', 'interval'),
                            Input(self.baseId + 'in_refreshTime','value'))
        def updateRefreshTime(refreshTime):return refreshTime*1000

        @self.app.callback(Output(self.baseId + 'btn_legend', 'children'),
                            Input(self.baseId + 'btn_legend','n_clicks'))
        def updateLgdBtn(legendType):return self.updateLegendBtnState(legendType)

        listInputsGraph = {
                        'interval':'n_intervals',
                        'btn_update':'n_clicks',
                        'dd_typeTags':'value',
                        'dd_resampleMethod':'value',
                        'dd_typeGraph':'value',
                        'dd_cmap':'value',
                        'btn_legend':'children',
                        'dd_style':'value',
                        }
        listStatesGraph = {
                            'graph':'figure',
                            'in_timeWindow':'value',
                            'in_timeRes':'value'
                            }
        @self.app.callback(
        Output(self.baseId + 'graph', 'figure'),
        Output(self.baseId + 'btn_update', 'n_clicks'),
        [Input(self.baseId + k,v) for k,v in listInputsGraph.items()],
        [State(self.baseId + k,v) for k,v in listStatesGraph.items()],
        )
        def updateGraph(n,updateBtn,preSelGraph,rsMethod,typeGraph,colmap,lgd,style,fig,tw,rs):
            self.utils.printListArgs(n,updateBtn,preSelGraph,rsMethod,typeGraph,colmap,lgd,style,rs)
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # to ensure that action on graphs only without computation do not
            # trigger computing the dataframe again
            # ==============================================================
            #               CHANGE HERE YOUR CODE
            #           better to use decorators in the parent class
            # ==============================================================
            triggerList = [self.baseId+k for k in ['interval','dd_typeTags','btn_update','dd_resampleMethod','dd_typeGraph']]
            # print(trigId)
            if not updateBtn or trigId in triggerList :
                start = time.time()
                # df    = self.cfg.realtimeDF(preSelGraph,rs=rs,applyMethod=rsMethod)
                df    = self.cfg.realtimeDF(preSelGraph,timeWindow=tw*60,rs=rs,applyMethod=rsMethod)
                # print(df)
                self.utils.printCTime(start)
                fig = self.utils.plotGraphType(df,typeGraph)
                unit = self.cfg.getUnitofTag(df.columns[0])
                nameGrandeur = self.cfg.utils.detectUnit(unit)
                fig.update_layout(yaxis_title = nameGrandeur + ' in ' + unit)
            else :fig = go.Figure(fig)
            # ==============================================================
            #               CHANGE HERE YOUR UPDATE FUNCTION
            #           better to use decorators in the parent class
            # ==============================================================
            fig = self.utils.updateStyleGraph(fig,style,colmap)
            fig = self.updateLegend(fig,lgd)
            # return fig
            return fig,updateBtn

class MultiUnitSmallPowerTab(TabMultiUnits):
    def __init__(self,folderPkl,app,baseId='mut0_'):
        self.cfg = cfs.ConfigFilesSmallPower(folderPkl)
        TabMultiUnits.__init__(self,folderPkl,self.cfg,app,baseId)

    def _buildLayout(self,widthG=85):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                        'in_timeRes':'auto','dd_resampleMethod' : 'mean',
                        'dd_style':'lines+markers','dd_typeGraph':'scatter',
                        'dd_cmap':'jet','btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_tag':self.cfg.get_randomListTags(2),'btn_legend':0,'in_axisSp':0.05},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

class TagSelectedSmallPowerTab(TabSelectedTags):
    def __init__(self,folderPkl,app,baseId='tst0_'):
        self.cfg = cfs.ConfigFilesSmallPower(folderPkl)
        TabSelectedTags.__init__(self,folderPkl,self.cfg,app,baseId)

    def _buildLayout(self,widthG=85):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                        'in_timeRes':'auto','dd_resampleMethod' : 'mean',
                        'dd_style':'lines+markers','dd_typeGraph':'scatter',
                        'dd_cmap':'jet','btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_typeTags':'Temperatures du gv1a','btn_legend':0},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)

class UnitSelectorSmallPowerTab(TabUnitSelector):
    def __init__(self,folderPkl,app,baseId='tst0_'):
        self.cfg = cfs.ConfigFilesSmallPower(folderPkl)
        TabUnitSelector.__init__(self,folderPkl,self.cfg,app,baseId)
