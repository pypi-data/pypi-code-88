import datetime as dt, pickle, time
import os,re,pandas as pd
import dash, dash_core_components as dcc, dash_html_components as html, dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.express as px, plotly.graph_objects as go
# import matplotlib.pyplot as plt, matplotlib.colors as mtpcl
# from pylab import cm
from dorianUtils.dccExtendedD import DccExtended
from dorianUtils.utilsD import Utils
import screeningBuilding.configFilesBuilding as cfb
from dorianUtils.dashTabsD import TabSelectedTags,TabMultiUnits

class ComputationTab():
    ''' computation tab '''

    def __init__(self,cfg,sbd):
        self.sbd = sbd
        self.cfg = cfg
        self.utils = Utils()
        self.dccE = DccExtended()
        self.computationGraphs=['power enveloppe','kWh from power','kWh from compteur']
    # ==========================================================================
    #                           SHARED FUNCTIONS CALLBACKS
    # ==========================================================================
    def buildLayoutLocal(self,dicWidgets,baseId,widthG=80,nbGraphs=1,nbCaches=0):
        widgetLayout,dicLayouts = [],{}
        for widgetId in dicWidgets.items():
            if 'dd_computation' in widgetId[0]:
                widgetObj = self.dccE.dropDownFromList(baseId+widgetId[0],self.computationGraphs,
                                                        'what should be computed ?',value = widgetId[1])
            elif 'dd_cmap' in widgetId[0]:
                widgetObj = self.dccE.dropDownFromList(baseId+widgetId[0],self.utils.cmapNames[0],
                                                'select the colormap : ',value=widgetId[1])

            elif 'dd_typeGraph' in widgetId[0]:
                widgetObj = self.dccE.dropDownFromList(baseId+widgetId[0],self.sbd.graphTypes,
                            'Select type graph : ',defaultIdx=widgetId[1],
                            style={'fontsize':'20 px','height': '40px','min-height': '1px',},optionHeight=20)


            elif 'dd_resampleMethod' in widgetId[0]:
                widgetObj = self.dccE.dropDownFromList(baseId+widgetId[0],['mean','max','min','median'],
                'Select the resampling method: ',value=widgetId[1],multi=False)

            elif 'dd_style' in widgetId[0]:
                widgetObj = self.dccE.dropDownFromList(baseId+widgetId[0],self.sbd.graphStyles,'Select the style : ',value = widgetId[1])

            elif 'btn_export' in widgetId[0]:
                widgetObj = [html.Button('export .txt',id=baseId+widgetId[0], n_clicks=widgetId[1])]

            elif 'in_timeRes' in widgetId[0]:
                widgetObj = [html.P('time resolution : '),
                dcc.Input(id=baseId+widgetId[0],placeholder='time resolution : ',type='text',value=widgetId[1])]

            elif 'pdr_time' in widgetId[0] :
                tmax=widgetId[1]
                # if not tmax : tmax = dt.datetime.now()
                if not tmax :
                    tmax = self.utils.findDateInFilename(self.cfg.listFilesPkl[-1])
                t1 = tmax - dt.timedelta(hours=tmax.hour+1)
                t0 = t1 - dt.timedelta(days=3)

                widgetObj = [
                html.Div([
                    dbc.Row([dbc.Col(html.P('select start and end time : ')),
                        dbc.Col(html.Button(id  = baseId + widgetId[0] + 'Btn',children='update Time'))]),

                    dbc.Row([dbc.Col(dcc.DatePickerRange( id = baseId + widgetId[0] + 'Pdr',
                                max_date_allowed = tmax, initial_visible_month = t0.date(),
                                display_format = 'MMM D, YY',minimum_nights=0,
                                start_date = t0.date(), end_date   = t1.date()))]),

                    dbc.Row([dbc.Col(dcc.Input(id = baseId + widgetId[0] + 'Start',type='text',value = '07:00',size='13',style={'font-size' : 13})),
                            dbc.Col(dcc.Input(id = baseId + widgetId[0] + 'End',type='text',value = '21:00',size='13',style={'font-size' : 13}))])
                ])]

            for widObj in widgetObj:widgetLayout.append(widObj)

        dicLayouts['widgetLayout'] = html.Div(widgetLayout,
                                    style={"width": str(100-widthG) + "%", "float": "left"})

        dicLayouts['graphLayout']= html.Div([dcc.Graph(id=baseId+'graph' + str(k)) for k in range(1,nbGraphs+1)],
                                    style={"width": str(widthG) + "%", "display": "inline-block"})

        layout = html.Div(list(dicLayouts.values()))
        return layout

    # ==========================================================================
    #                           TABS
    # ==========================================================================
    def computation_pdr_resample(self,baseId,widthG=80,heightGraph=900):
        dicWidgets = {'pdr_time' : None,'in_timeRes':str(60*10)+'s','dd_computation':'power enveloppe',
                    'dd_style':'lines+markers','dd_cmap':'jet','btn_export':0}
        TUinPDRrs_html = self.buildLayoutLocal(dicWidgets,baseId,widthG=widthG,nbCaches=1,nbGraphs=1)
        listIds = self.dccE.parseLayoutIds(TUinPDRrs_html)

        # ==========================================================================
        #                           COMPUTE AND GRAPHICS CALLBACKS
        # ==========================================================================

        def computeDataFrame(timeRange,computation,rs):
            start     = time.time()
            if computation == 'power enveloppe' :
                df = self.cfg.computePowerEnveloppe(timeRange,rs=rs)
                unit = 'kW'
            elif computation == 'kWh from power' :
                df   = self.cfg.compute_kWh_fromPower(timeRange)
                df = df.resample(rs).ffill()
                unit = 'kWh'
            elif computation == 'kWh from compteur' :
                df   = self.cfg.compute_kWhFromCompteur(timeRange)
                df = df.resample(rs).ffill()
                # df = df.resample(rs).sum()
                unit = 'kWh'
            self.utils.printCTime(start,'computation time : ')
            return df,unit

        listInputsGraph = {
                        'dd_computation':'value',
                        'pdr_timeBtn':'n_clicks',
                        'dd_cmap':'value',
                        'dd_style':'value'}
        listStatesGraph = {
                            'graph1':'figure',
                            'in_timeRes' : 'value',
                            'pdr_timeStart' : 'value',
                            'pdr_timeEnd':'value',
                            'pdr_timePdr':'start_date',
                            }
        @self.sbd.app.callback(
        Output(baseId + 'graph1', 'figure'),
        Output(baseId + 'pdr_timeBtn', 'n_clicks'),
        [Input(baseId + k,v) for k,v in listInputsGraph.items()],
        [State(baseId + k,v) for k,v in listStatesGraph.items()],
        State(baseId+'pdr_timePdr','end_date'))
        def updateGraph(computation,timeBtn,colmap,style,fig,rs,date0,date1,t0,t1):
            ctx = dash.callback_context
            trigId = ctx.triggered[0]['prop_id'].split('.')[0]
            # to ensure that action on graphs only without computation do not
            # trigger computing the dataframe again
            if not timeBtn or trigId in [baseId+k for k in ['dd_computation','pdr_timeBtn','dd_typeGraph']] :
                # print('===============here===============')
                if not timeBtn : timeBtn=1 # to initialize the first graph
                timeRange = [date0+' '+t0,date1+' '+t1]
                df,unit   = computeDataFrame(timeRange,computation,rs)
                fig       = self.sbd.drawGraph(df,'scatter')
                nameGrandeur = self.cfg.utils.detectUnit(unit)
                fig.update_layout(yaxis_title = nameGrandeur + ' in ' + unit)
                timeBtn = max(timeBtn,1) # to close the initialisation
            else :fig = go.Figure(fig)
            fig = self.sbd.updateStyleGraph(fig,style,colmap)
            return fig,timeBtn

        # ==========================================================================
        #                           EXPORT CALLBACK
        # ==========================================================================
        @self.sbd.app.callback(Output(baseId + 'btn_export','children'),
        Input(baseId + 'btn_export', 'n_clicks'),
        State(baseId + 'graph1','figure'))
        def exportClick(btn,fig):
            fig = go.Figure(fig)
            if btn>0:self.utils.exportDataOnClick(fig,baseName='proof')
            return 'export Data'

        return TUinPDRrs_html

class TagSelectedScreeningBuilding(TabSelectedTags):
    def __init__(self,folderPkl,app,pklMeteo=None,baseId='tst0_'):
        self.cfg = cfb.ConfigFilesBuilding(folderPkl,pklMeteo=pklMeteo)
        TabSelectedTags.__init__(self,folderPkl,self.cfg,app,baseId)

    def _buildLayout(self,widthG=85):
        dicWidgets = {'pdr_time' : {'tmin':self.cfg.listFilesPkl[0],'tmax':self.cfg.listFilesPkl[-1]},
                        'in_timeRes':'auto','dd_resampleMethod' : 'mean',
                        'dd_style':'lines+markers','dd_typeGraph':'scatter',
                        'dd_cmap':'jet','btn_export':0}
        basicWidgets = self.dccE.basicComponents(dicWidgets,self.baseId)
        specialWidgets = self.addWidgets({'dd_typeTags':'Puissances sls','btn_legend':0},self.baseId)
        # reodrer widgets
        widgetLayout = basicWidgets + specialWidgets
        return self.dccE.buildGraphLayout(widgetLayout,self.baseId,widthG=widthG)
