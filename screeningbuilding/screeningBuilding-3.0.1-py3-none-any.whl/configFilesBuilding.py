import pytz,pandas as pd, numpy as np,datetime as dt,pickle, os, glob,re
from dorianUtils.configFilesD import ConfigDashTagUnitTimestamp
from dorianUtils.configFilesD import ConfigDashRealTime
from multiprocessing import Process, Queue, current_process,Pool
from scipy import integrate
from pandas.tseries.frequencies import to_offset


class ConfigFilesBuilding(ConfigDashTagUnitTimestamp):
    # ==========================================================================
    #                       INIT FUNCTIONS
    # ==========================================================================

    def __init__(self,folderPkl,pklMeteo=None,folderFig=None,folderExport=None,encode='utf-8'):
        self.appDir  = os.path.dirname(os.path.realpath(__file__))
        self.confFolder = self.appDir +'/confFiles/'
        super().__init__(folderPkl,self.confFolder,folderFig=folderFig,folderExport=folderExport)
        self.rsMinDefault   = 15
        self.listCompteurs  = pd.read_csv(self.confFolder+'/compteurs.csv')
        self.listVars       = pd.read_csv(self.confFolder+'/variables.csv')
        self.dfPLCMonitoring = self._buildDescriptionDFplcMonitoring(encode)
        self.dfMeteoPLC     = self._loadPLCMeteo()
        self.dfPLC          = self._mergeMeteoMonitoringPLC()
        self.listUnits      = list(self.dfPLC.UNITE.unique())
        self.listCalculatedVars = None
        self.pklMeteo       = pklMeteo
        self.listFilesMeteo = self.utils.get_listFilesPklV2(self.pklMeteo)

    def exportToxcel(self,df):
        df.index = [t.astimezone(pytz.timezone('Etc/GMT-2')).replace(tzinfo=None) for t in df.index]
        df.to_excel(dt.date.today().strftime('%Y-%m-%d')+'.xlsx')

    def getListVarsFromPLC(self):
        def getListCompteursFromPLC(self,regExpTagCompteur='[a-zA-Z][0-9]+-\w+'):
            return list(np.unique([re.findall(regExpTagCompteur,k)[0] for k in self.dfPLC.TAG]))
        listVars = self.getTagsTU(getListCompteursFromPLC()[0])
        listVars = [re.split('(h-)| ',k)[2] for k in listVars]
        return listVars

    def _loadPLCMeteo(self):
        dfPLC       = pd.read_csv(self.appDir + '/confFiles/configurationMeteo.csv')
        dfPLC.TAG = dfPLC.TAG.apply(lambda x: x.replace('SIS','SIS-02'))
        return dfPLC

    def _buildDescriptionDFplcMonitoring(self,encode):
        dfi = pd.read_csv(self.confFile,encoding=encode)
        print('dfi.index:',dfi.index)
        for k in dfi.index:
            # print('dfi.iloc[' + str(k)+',0] : ',dfi.iloc[k,0])
            for l in self.listCompteurs.index:
                if self.listCompteurs.iloc[l,0] in dfi.iloc[k,0] :
                    compteurName = self.listCompteurs.iloc[l,1]
            for l in self.listVars.index:
                if self.listVars.iloc[l,0] in dfi.iloc[k,0] :
                    varName = self.listVars.iloc[l,1]
            desName = varName + ' ' + compteurName
            dfi.iloc[k,2] = desName
        return dfi

    def _mergeMeteoMonitoringPLC(self):
        tagToday    = self._getListMeteoTags()
        dfMeteoPLC  = self.dfMeteoPLC[self.dfMeteoPLC.TAG.isin(tagToday)]#keep only measured data not predictions
        return pd.concat([self.dfPLCMonitoring,dfMeteoPLC])

    def _getListMeteoTags(self):
        return list(self.dfMeteoPLC[self.dfMeteoPLC.TAG.str.contains('-[A-Z]{2}-01-')].TAG)

    def _getListMeteoTagsDF(self,df):
        return list(df[df.tag.str.contains('-[A-Z]{2}-01-')].tag.unique())

    def getUsefulTags(self,usefulTag,**kwargs):
        category = self.usefulTags.loc[usefulTag]
        return self.getTagsTU(category.Pattern,category.Unit,ds=False)

    # ==============================================================================
    #                   functions filter on dataFrame
    # ==============================================================================
    def loadFileMeteo(self,filename):
        if '*' in filename :
            filenames=self.utils.get_listFilesPklV2(self.pklMeteo,filename)
            if len(filenames)>0 : filename=filenames[0]
            else : return pd.DataFrame()
        df = pickle.load(open(filename, "rb" ))
        df.tag   = df.tag.apply(lambda x:x.replace('@',''))#problem with tag remove @
        df.tag   = df.tag.apply(lambda x:x.replace('_','-'))#
        tagToday = self._getListMeteoTagsDF(df)
        # tagToday = self._getListMeteoTags()
        # print(tagToday)
        # print(df.tag.unique())
        df       = df[df.tag.isin(tagToday)]#keep only measured data not predictions
        df.timestampUTC = pd.to_datetime(df.timestampUTC,utc=True)# convert datetime to utc
        return df

    def loadFileMonitoring(self,filename):
        return self.loadFile(filename)

    def _DF_fromTagList(self,df,tagList,rs):
        df = df.drop_duplicates(subset=['timestampUTC', 'tag'], keep='last')
        if not isinstance(tagList,list):tagList =[tagList]
        df = df[df.tag.isin(tagList)]
        if not rs=='raw':df = df.pivot(index="timestampUTC", columns="tag", values="value")
        else : df = df.sort_values(by=['tag','timestampUTC']).set_index('timestampUTC')
        return df

    def _loadDFTagsDayMeteoBuilding(self,datum,listTags,rs):
        print(datum)
        realDatum = self.utils.datesBetween2Dates([datum,datum],offset=+1)[0][0]
        dfMonitoring  = self.loadFileMonitoring('*'+realDatum+'*')
        dfMeteo       = self.loadFileMeteo('*'+realDatum+'*')
        if not dfMonitoring.empty : dfMonitoring = self._DF_fromTagList(dfMonitoring,listTags,rs)
        if not dfMeteo.empty : dfMeteo = self._DF_fromTagList(dfMeteo,listTags,rs)
        if rs=='raw':
            df = pd.concat([dfMonitoring,dfMeteo],axis=1)
            # tmp = list(df.columns);tmp.sort();df=df[tmp]
        df = pd.concat([dfMonitoring,dfMeteo],axis=0)
        return df
        # return dfMonitoring

    def DF_loadTimeRangeTags(self,timeRange,listTags,rs='auto',applyMethod='mean',timezone='Europe/Paris',pool=True):
        listDates,delta = self.utils.datesBetween2Dates(timeRange,offset=0)
        if rs=='auto':rs = '{:.0f}'.format(max(1,delta.total_seconds()/6400)) + 's'
        dfs=[]
        if pool:
            with Pool() as p:
                dfs=p.starmap(self._loadDFTagsDayMeteoBuilding, [(datum,listTags,rs) for datum in listDates])
        else:
            for datum in listDates:
                dfs.append(self._loadDFTagsDayMeteoBuilding(datum,listTags,rs))
        df = pd.concat(dfs,axis=0)
        print("finish loading")
        if not rs=='raw':
            df = eval('df.resample(rs).apply(np.' + applyMethod + ')')
            rsOffset = str(max(1,int(float(re.findall('\d+',rs)[0])/2)))
            period=re.findall('[a-zA-z]+',rs)[0]
            df.index=df.index+to_offset(rsOffset +period)
        df = self._DF_cutTimeRange(df,timeRange,timezone)
        if rs=='raw' :
            df['timestamp']=df.index
            df=df.sort_values(by=['tag','timestamp'])
            df=df.drop(['timestamp'],axis=1)
        return df

    # ==========================================================================
    #                       COMPUTATIONS FUNCTIONS
    # ==========================================================================
    def computePowerEnveloppe(self,timeRange,tagPat = 'VIRTUAL.+[0-9]-JTW',rs=None):
        if not rs : rs=str(self.rsMinDefault*60)+'s'
        listTags = self.getTagsTU(tagPat,'kW')
        df = self.DF_loadTimeRangeTags(timeRange,listTags,'5s','nanmean')
        L123min = df.min(axis=1)
        L123max = df.max(axis=1)
        L123moy = df.mean(axis=1)
        L123sum = df.sum(axis=1)
        df = pd.concat([df,L123min,L123max,L123moy,L123sum],axis=1)
        df = df.resample(rs).apply(np.nanmean)
        dfmin = L123min.resample(rs).apply(np.nanmin)
        dfmax = L123max.resample(rs).apply(np.nanmax)
        df = pd.concat([df,dfmin,dfmax],axis=1)

        df.columns=['L1_mean','L2_mean','L3_mean','PminL123_mean','PmaxL123_mean',
                    'PmoyL123_mean','PsumL123_mean','PminL123_min','PmaxL123_max']
        return df

    def _integratePowerCol(self,df,tag,pool):
        print(tag)
        x1=df[df.tag==tag]
        if not x1.empty:
            timestamp=x1.index
            x1['totalSecs']=x1.index.to_series().apply(lambda x: (x-x1.index[0]).total_seconds())/3600
            x1=pd.DataFrame(integrate.cumulative_trapezoid(x1.value,x=x1.totalSecs))
            x1.index=timestamp[1:]
            x1.columns=[tag]
        return x1

    def compute_kWh_fromPower(self,timeRange,listTags=None):
        if not listTags : listTags = self.getUsefulTags('Puissances SLS')
        df = self.DF_loadTimeRangeTags(timeRange,listTags,'raw','nanmean',pool=True)
        dfs=[]
        for tag in listTags:
            dftmp = self._integratePowerCol(df,tag,True)
            if not dftmp.empty:dfs.append(dftmp)

        df=pd.concat(dfs,axis=1)
        return df.ffill().bfill()

    def compute_kWhFromCompteur(self,timeRange,listTags=None):
        if not listTags : listTags = self.getUsefulTags('Compteurs SLS')
        df = self.DF_loadTimeRangeTags(timeRange,listTags,'raw','nanmean')
        dfs=[]
        for tag in listTags:
            x1=df[df.tag==tag]
            dfs.append(x1.iloc[:,1].diff().cumsum()[1:])
        df=pd.concat(dfs,axis=1)
        df.columns=listTags
        return df.ffill().bfill()
        # return df

class ConfigFilesBuildingRealTime(ConfigDashRealTime):
    # ==========================================================================
    #                       INIT FUNCTIONS
    # ==========================================================================

    def __init__(self,confFolder=None,timeWindow=2*60*60,connParameters=None,
                    folderFig=None,folderExport=None,encode='utf-8'):
        self.appDir  = os.path.dirname(os.path.realpath(__file__))
        # self.filePLC = glob.glob(self.appDir +'/confFiles/' + '*PLC*')[0]
        if not connParameters : connParameters ={
            'host'     : "192.168.1.44",
            'port'     : "5434",
            'dbname'   : "BigBrother",
            'user'     : "postgres",
            'password' : "SylfenBDD"
        }
        if not confFolder:confFolder=self.appDir +'/confFiles/'
        super().__init__(confFolder,self.connParameters,timeWindow,
                            folderFig=folderFig,folderExport=folderExport)
