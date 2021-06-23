'''TODO:                    
----------------------------------------------
NIVEL TABLA              progr  test comm
----------------------------------------------
missings                 Ok     Ok    
consistencia             Ok     Ok
duplicados llavecruce    Ok     Ok
comparar cruzabilidad    Ok     Ok    pasar un df con llaves-cruce y verificar
duplicados 'reales'      Ok     Ok    duplicados generales en tabla
reporte tabla            Ok     Ok    [tabla, dups, keydups, prof_hist, %joins] 
validacion ultimo mes    pend   pend  prueba unitaria 
reporte variables        Ok     Ok
----------------------------------------------
NIVEL VARIABLE           progr  test comm
----------------------------------------------
missings                 Ok     Ok
consistencia             Ok     Ok
outliers (variable)      Ok     Ok    
PSI (variable)           Ok     Ok    
valores unicos           Ok     Ok 
dict de tipos            Ok     Ok
deciles generales        Ok     Ok
reporte variable         Ok     Ok   [var,tipo,[unicos],%miss,[p10...P90]]
reporte var/fecha        Ok     Ok   [var,fecha,%miss,%outl,mean,std,median,psi]
----------------------------------------------
MISC          
----------------------------------------------
Documentación            Ok
'''
class Qualitor:
    '''Impala/Hive Table Quality Class
    attributes:
    ---------
        connstr:         Connection String, note: could be like "DSN=ODBC"
        conex:           Pyodbc connection Object
        table:           Table to assess quality ie: 'gestor_respuestas'
        zone:            Zone (or schema) where the table is located 
                         ie: 'production_sandbox_intneg'
        datecol:         Date Column
        keycol:          Key column
        cols:            PD Dataframe with column 
                         name and type: ['col_name','type','comment'] 
        months:          ordered list of all months available in the table
        total_regs:      int, count of all rows in the table
        sub_psis:        dictionary with the psi calculation for every month
                         sub_psis[column][month]: Dataframe
        psis:            DataFrame with psi for every month
    methods:
    ---------
        __init__:            constructor method
        _get_columns:        gets all the table columns and types
        _get_months:         gets all the table months
        get_query:           returns a pandas DataFrame of a query
        __key_dupl:          count the pair key-date duplicates in the table
        __tab_dupl:          count the table duplicates
        __tab_missings:      count the table missings
        __tab_consistency:   returns a pandas DataFrame with counts of 
                             rows per date
        tab_join_check:      count how many rows can be joined with a 
                             sample provided
        __var_missings:      count the missing values of a variable
        __var_consistency:   returns a pandas Dataframe with summary 
                             statistics per month
        __outliers:          count the outliers (using IQR method) 
                             of a given variable
        __psi:               return the population stability index 
                             for a variable
        __var_unique:        return the first 1000 distinct values 
                             of a given variable
        __var_percs:         return the estimated percentiles of 
                             a variable using percentile_approx
        table_quality:       assess the table quality
        _column_quality:     asses the quality of a column
        columns_quality:     asses the quality of a list of columns
    '''
    import pyodbc
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    def __init__(self, connstr, table, zone = 'production_sandbox_intneg', 
                 datecol = 'anomes', keycol = 'id_cli'):
        '''constructor method:
        parameters:
        -----------
            connstr: [str] Connection String (if windows 'DSN=Source Name' 
                           if mac/linux please see aux_functions.py)
            table:   [str] Table to make the QA
            zone:    [str] Zone or Scheme of the table 
            datecol: [str] Date Column
            keycol:  [str] Key Column
        
        '''
        self.conex = self.pyodbc.connect(connstr, autocommit = True)
        self.zone = zone
        self.table = table
        self.datecol = datecol
        self.keycol = keycol
        self.numeric_types = ['tinyint','smallint','int','bigint','float',
                              'double','decimal','numeric']
        self.date_types = ['timestamp','date','interval']
        self.string_types = ['string','varchar','char']
        self.misc_types = ['boolean','binary']
        self.sub_psis = {}
        self.psis = {}
        self._get_columns()
        self._get_months()
        self._get_tot_regs()
    

    # General methods
    def _get_columns(self):
        '''get columns and types of a given table:
        returns:
        -----------
            self.cols: [DataFrame] with column 
                       name and type: ['col_name','type','comment'] 
        '''
        query = f'''
                describe
                {self.zone}.{self.table}
                '''

        cols = self.get_query(query)

        fii = cols[cols['col_name']==''].first_valid_index() # first invalid index

        if not fii:
            self.cols = cols
        else:
            self.cols = cols.iloc[0:fii]

        return self.cols
    
    def _get_months(self):
        '''get months of a given table:
        returns:
        -----------
            self.months: [list] sorted list of months 
        '''
        query = f'''
                 select distinct
                 {self.datecol} as month
                 from
                 {self.zone}.{self.table}   
                 '''
        self.months = sorted(self.get_query(query)['month'].tolist())

        return self.months
    
    def _get_tot_regs(self):
        '''get number of rows of a given table:
        returns:
        -----------
            self.total_regs: [int] number of rows of the table 
        '''
        query = f'''
                 select
                    count(*) as `cnt`
                 from 
                 {self.zone}.{self.table}'''
        self.total_regs = self.get_query(query)['cnt'][0]

        return self.total_regs
    
    def get_query(self, query):
        '''get a DataFrame from a query:
        parameters:
        -----------
            query: [string] query to retrieve
        returns:
        -----------
            dataframe: [DataFrame] query  
        '''
        dataframe = self.pd.read_sql(query, self.conex)
        return dataframe
    
    # Table Methods
    def __key_dupl(self):
        '''Get key-date duplicates:
        returns:
        -----------
            df: [DataFrame] dataframe with detail of key-date duplicates 
                            columns:['total_regs','dupl_key-dates']  
        '''
        query = f'''
                 with a as (
                 select
                     {self.datecol} as `date`
                    ,{self.keycol}  as `key`
                    ,count(*)       as `cnt`
                 from 
                 {self.zone}.{self.table}
                 group by {self.datecol}, {self.keycol}
                 )select 
                      count(*) as `cnt`
                  from a
                       where `cnt` > 1'''
        duplicates = self.get_query(query)['cnt'][0]

        df = self.pd.DataFrame(zip([self.total_regs], [duplicates]), 
                               columns = ['total_regs', 'dupl_key-dates'])

        df['%_dupl_key-dates'] = df['dupl_key-dates'] / df['total_regs']

        return df

    def __tab_dupl(self):
        '''Get duplicate row counts:
        returns:
        -----------
            df: [DataFrame] dataframe with detail of duplicates 
                            columns:['total_regs','dupl_regs','%_dupl']  
        '''
        q_a = 'select count(*) as `cnt`' + \
               f' from {self.zone}.{self.table} group by ' + \
               ', '.join(self.cols['col_name'][0:63]) 
               # Hive doesn't support more than 64 cols for group by

        query = f'''
                 with a as({q_a})
                 select count(*) as `cnt`
                 from a
                 where `cnt` > 1
                 '''

        duplicates = self.get_query(query)['cnt'][0]

        df = self.pd.DataFrame(zip([self.total_regs], [duplicates]), 
                               columns = ['total_regs', 'dupl_regs'])

        df['%_dupl'] = df['dupl_regs'] / df['total_regs']

        return df
    
    def __tab_missings(self):
        '''Get missing row counts:
        returns:
        -----------
            df: [DataFrame] dataframe with detail of missings, 
                            columns:['total_regs','miss_regs','%_miss']  
        '''
        head = f'''
                select
                    count(1) as `cnt`
                from 
                {self.zone}.{self.table}
                where
                ''' 
        
        cols = []
        for col in self.cols['col_name']:
            if col not in [self.datecol, self.keycol]:
                cols.append(col)


        bot = ' is null and '.join(cols) + ' is null'

        query = head + bot

        tab_missings = self.get_query(query)['cnt'][0]
        
        df = self.pd.DataFrame(zip([self.total_regs], [tab_missings]), 
                               columns = ['total_regs', 'miss_regs'])

        df['%_miss'] = df['miss_regs'] / df['total_regs']

        return df
    
    def __tab_consistency(self):
        '''Get counts of rews by date:
        returns:
        -----------
            tab_consistency: [DataFrame] dataframe with detail of row counts by 
                                         month, columns:['date','cnt','table']  
        '''
        query = f'''
                 select 
                     {self.datecol}       as `date`
                    ,count({self.keycol}) as `cnt`
                 from {self.zone}.{self.table}
                 group by 1
                 '''
        tab_consistency = self.get_query(query)
        tab_consistency['table'] = self.table
        return tab_consistency
    
    def tab_join_check(self, samp_keys, sandbox_sample = 100000):
        '''Makes a join-check 
        (you can provide some keys of another table and see if you can join):
        parameters:
        -----------
            samp_keys: [pd.Series]: sample of keys from 
                                    another table to check if joins
        returns:
        -----------
            df: [DataFrame] dataframe with detail of row counts by month, 
                            columns:['date','cnt','table']  
        TODO: limit in the key query to accelerate the method
        -----------
        '''

        

        query = f'''select distinct 
                        {self.keycol}  as `key`
                    from {self.zone}.{self.table}
                    limit {sandbox_sample}
                 '''

        keys = self.get_query(query)

        tot_n = len(samp_keys)
        n = samp_keys.isin(keys['key']).sum()
        perc = n/tot_n

        join_check = self.pd.DataFrame(\
                         zip([tot_n], [n],[perc]), \
                         columns = ['samp_keys', 'joined_keys', '%_joined_keys'])
                                     
        return join_check
    
    # var methods
    def _var_date_missings(self, var):
        '''Count missing values per date:
        parameters:
        -----------
            var: [str] variable to analyze
        returns:
        -----------
            var_date_missing: [DataFrame] dataframe with detail of missing row 
                                          counts by month, 
                                          columns:['date','cnt_miss']  
        '''
        query = f'''
                 select
                     {self.datecol}       as `date`
                    ,count({self.keycol}) as `cnt_miss`
                 from 
                 {self.zone}.{self.table}
                 where {var} is null
                 group by {self.datecol}
                 '''
        var_date_missing = self.get_query(query)
        return var_date_missing
    
    def _var_gen_missings(self, var):
        '''Count total missing values:
        parameters:
        -----------
            var: [str] variable to analyze
        returns:
        -----------
            var_missing: [DataFrame] dataframe with detail of missing row 
                                     counts by month, columns:['cnt_miss']  
        '''
        query = f'''
                 select
                     count({self.keycol}) as `cnt_miss`
                 from 
                 {self.zone}.{self.table}
                 where {var} is null
                 '''
        var_missing = self.get_query(query).fillna(0)

        return var_missing

    def _var_consistency(self, var):
        '''Get descriptive statistics per month:
        parameters:
        -----------
            var: [str] variable to analyze
        returns:
        -----------
            var_consistency: [DataFrame] dataframe with statistics by month, 
                                         columns:['date','avg','std','median']  
        '''        
        funcs = {
            'avg' : ['avg', '', ''],
            'stddev_pop' : ['std', '', ''],
            'percentile_approx' : ['median', ', 0.5', ', 100']}

        var_consistency = self.pd.DataFrame()
        for func in list(funcs.keys()):
            par_1, par_2, par_3 = funcs[func]
            query = f'''
                     select
                         {self.datecol}              as `date`
                        ,{func}({var}{par_2}{par_3}) as {par_1}
                     from 
                     {self.zone}.{self.table}
                     group by {self.datecol}
                     '''
            if func == list(funcs.keys())[0]:
                var_consistency = var_consistency.append(self.get_query(query))
            else:
                var_consistency = var_consistency.merge(self.get_query(query), 
                                                        on='date')
        
        return var_consistency
    
    def _outliers(self, var, out_th = 1.5, prec = 1000):
        '''Get outliers:
        parameters:
        -----------
            var:     [str]    variable to analyze
            out_th:  [double] threshold of IQR recommended (1.5 or 3)
            prec:    [int]    precision to estimate quantiles   
        returns:
        -----------
            outls: [DataFrame] dataframe with count of outliers, 
                               columns: ['total_regs','lower_outl','%_low_outl',
                                         'upper_outl','%_upp_outl']
        reference:
        -----------
            Penn state IQR: https://online.stat.psu.edu/stat200/lesson/3/3.2  
        '''  
        q_query = f'''
                   select
                       percentile_approx({var}, 0.25, {prec}) as Q1 
                      ,percentile_approx({var}, 0.75, {prec}) as Q3
                   from 
                   {self.zone}.{self.table}
                   '''
        
        iqr_ds = self.get_query(q_query)
        
        iqr = iqr_ds['q3'][0] - iqr_ds['q1'][0]

        out_up_query = f'''
                        select
                           count(1) as out_up
                        from
                        {self.zone}.{self.table}
                        where
                        {var} > {iqr_ds['q3'][0] + (iqr * out_th)}
                        '''
        
        out_lo_query = f'''
                        select
                           count(1) as out_lo
                        from
                        {self.zone}.{self.table}
                        where
                        {var} < {iqr_ds['q1'][0] - (iqr * out_th)}
                        '''
        
        tot = self.total_regs
        out_up = self.get_query(out_up_query)['out_up'][0]
        out_lo = self.get_query(out_lo_query)['out_lo'][0]
        perc_up = out_up / tot
        perc_lo = out_lo / tot

        outls = self.pd.DataFrame(
            zip([tot],[out_lo],[perc_lo],[out_up],[perc_up]), \
            columns = ['total_regs','lower_outl','%_low_outl',\
                       'upper_outl','%_upp_outl'])

        return outls

    def _psi(self, var, n_ranges = 5, months=None, tqdm=None):
        '''Get population stability index:
        This method is iterative and assumes that the i-1 month is the base, 
        and measure the stability of the i month.
        parameters:
        -----------
            var:       [str]   variable to analyze
            n_ranges:  [int]   number of ranges to estimate distribution   
            months:    [list]  list of consecutive months to estimate
            [tqdm]:    [tqdm]  tqdm object to update postfix_str  
        returns:
        -----------
            psi: [DataFrame] dataframe with count psi per month, 
                             columns: ['month','psi','var']
        reference:
        -----------
            WMU Psi: https://scholarworks.wmich.edu/cgi/viewcontent.cgi?article=4249&context=dissertations  
        '''
        if not months:
            months = self.months
        
        percs = {}
        psis = {}

        for m in range(len(months)): # iterating over months
            if tqdm:
                tqdm.set_postfix_str(f'method: psi - month: {months[m]}')
            if m == range(len(months))[0]:  # continuing if first month
                continue
            
            ## Getting observations of the present month
            n_obs_n_month = self.get_query(f'''  
                                            select 
                                                count(1) as `cnt`
                                            from {self.zone}.{self.table}
                                            where {self.datecol} = {months[m]}
                                            ''')['cnt'][0]
            
            ## Part 1: Calculating percentiles of i-1 month (base)
            mid = []
            for i in range(n_ranges):
                if i == range(n_ranges)[-1]:
                    mid.append(f'max({var}) as `1` ')
                else:
                    perc = round((1/n_ranges)*(i+1),2)
                    mid.append(f'''percentile_approx({var}, {perc}, 500) 
                                   as `{perc}` ''')
            mid = ','.join(mid)

            query = 'select ' + mid + \
                    f''' from {self.zone}.{self.table} 
                         where {self.datecol} == {months[m-1]}'''
            
            perc = self.get_query(query).transpose()\
                       .reset_index() # Getting the values
            perc.columns = ['percentile','var_num']

            ## Part 2: Calculating i month percentages
            counts = self.pd.DataFrame() 
            rng = []                     # ranges 
            cnt_n_month = []             # rows per month

            # Calculating range and counting over range
            for i in range(n_ranges):
                
                if i == range(n_ranges)[0]:
                    perc_max_bkt = round(perc["var_num"][i],0)
                else:
                    perc_min_bkt = round(perc["var_num"][i-1],0)
                    perc_max_bkt = round(perc["var_num"][i],0)
                            
                if i == range(n_ranges)[0]:
                    rng.append(f'<{perc_max_bkt}')
                    cnt_n_month.append(self.get_query(f'''
                                        select
                                           count(1) as `cnt`
                                        from {self.zone}.{self.table}
                                        where {self.datecol} = {months[m]}
                                        and {var} < {perc_max_bkt}
                                        ''')['cnt'][0])
                elif i == range(n_ranges)[-1]:
                    rng.append(f'>{perc_min_bkt}')
                    cnt_n_month.append(self.get_query(f'''
                                    select
                                        count(1) as `cnt`
                                     from {self.zone}.{self.table}
                                     where {self.datecol} = {months[m]}
                                     and {var} > {perc_min_bkt}
                                    ''')['cnt'][0])
                else:
                    rng.append(f'{perc_min_bkt}-{perc_max_bkt}')
                    cnt_n_month.append(self.get_query(f'''
                                       select
                                           count(1) as `cnt`
                                        from {self.zone}.{self.table}
                                        where {self.datecol} = {months[m]}
                                        and {var} between 
                                        {perc_min_bkt} and {perc_max_bkt}
                                       ''')['cnt'][0])
            ## Part 3: calculating psi (summary table and general psi)
            counts['range'] = rng
            counts['perc_p_month'] = round(1/n_ranges,2)
            counts['perc_n_month'] = cnt_n_month/n_obs_n_month
            counts['diff'] = counts['perc_p_month'] - counts['perc_n_month']
            counts['ln'] = self.np.log(counts['perc_p_month']\
                                       / counts['perc_n_month'])
            counts['sub_psi'] = counts['diff'] * counts['ln']
            counts['date'] = months[m]

            percs[months[m]] = counts

            psi = self.np.sum(counts['sub_psi'])
            
            psis[months[m]] = psi
        
        ## Part 4: writing results as attributes
        self.sub_psis[var] = percs
        self.psis[var] = self.pd.DataFrame(zip(psis.keys(),psis.values(),
                                               [var] * len(psis.keys())),
                                           columns = ['date','psi','var'])

        return self.psis[var]

    def _var_unique(self, var):
        '''Get unique variables (only the first 1000 values):
        parameters:
        -----------
            var:     [str]    variable to analyze  
        returns:
        -----------
            unique_values: [list] list of the 1000 unique values
        ''' 
        query = f'''
                 select distinct
                     {var} as `un_values`
                 from {self.zone}.{self.table}
                 limit 1000
                 '''
        unique_values = self.get_query(query)['un_values'].tolist()
        return unique_values

    def _var_percs(self,var, n_bck = 10, samp = 5000000, seed = 69420,
                   precision = 1000, tqdm = None):    
        '''Get percentiles of a variable from a sample:
        parameters:
        -----------
            var:       [str]   variable to analyze
            n_bck:     [int]   number of buckets 
                               (if 10, deciles; if 100, percentiles...)
            samp:      [int]   number of samples
            seed:      [int]   seed for the sample
            precision: [int]   precision to estimate n-tiles
            [tqdm]:    [tqdm]  tqdm object to update postfix_str
        returns:
        -----------
            percs: [DataFrame] DataFrame with the n-tiles as columns 
        ''' 
        delete = f'drop table if exists {self.zone}.perc_{var}_sample purge'
        samp = f'''create table {self.zone}.perc_{var}_sample
                   stored as parquet as
                   select 
                       {var}
                   from {self.zone}.{self.table}
                   distribute by rand({seed}) sort by rand({seed})
                   limit {samp}
                '''
        self.conex.cursor().execute(delete) # deleting the samp table if exists
        self.conex.cursor().execute(samp)   # creating the samp table

        percs = []
        perc = 1/n_bck

        
        for i in range(n_bck):
            if tqdm:
                tqdm.set_postfix_str(f'var: {var} - method: perc - buck: {i}')
            if i == range(n_bck)[0]:
                query = f'''select 
                             min({var}) as min 
                            from {self.zone}.perc_{var}_sample'''
                percs.append(['min', self.get_query(query)['min'][0]])
            elif i == range(n_bck)[-1]:
                query = f'''select 
                             max({var}) as max 
                            from {self.zone}.perc_{var}_sample'''
                percs.append(['max', self.get_query(query)['max'][0]])
            else:
                round_perc = round(i * perc,2)
                query = f'''
                    select 
                     percentile_approx({var}, {round_perc}, {precision}) as p 
                    from {self.zone}.perc_{var}_sample'''
                percs.append([f'p_{int(round_perc * 100)}', 
                                self.get_query(query)['p'][0]])

        self.conex.cursor().execute(delete) # deleting the samp table

        percs = self.pd.DataFrame(percs, columns = ['perc','n']).\
                    set_index('perc').transpose().reset_index(drop = True)
        return percs
      
    
    # Summary 
    def table_quality(self, samp, tqdm = None):
        '''Calls all methods to assess table quality:
        parameters:
        -----------
            samp:    [int]  sample of keys to make join_check
            [tqdm] : [tqdm] if provided, reports the progress
        returns:
        -----------
            tab_report:  [DataFrame] DataFrame with duplicates, key-date 
                                     duplicates, min and max month, number of 
                                     key samples, joined samples               
            cons_report: [DataFrame] DataFrame with counts of rows by month
        ''' 
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'key_dupl'})
        key_dupl = self.__key_dupl()
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'tab_dupl'})
        tab_dupl = self.__tab_dupl()
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'tab_miss'})
        miss = self.__tab_missings()
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'join_check'})
        joinability = self.tab_join_check(samp_keys=samp)
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'tab_cons'})
        cons_report = self.__tab_consistency()
        if tqdm:
            tqdm.set_postfix({'tab': self.table,'mth':'report'})

        tab = zip([self.table], 
                  [tab_dupl['dupl_regs'][0]], [tab_dupl['%_dupl'][0]],
                  [key_dupl['dupl_key-dates'][0]], 
                  [key_dupl['%_dupl_key-dates'][0]],
                  [self.months[0]], [self.months[-1]],
                  [joinability['samp_keys'][0]], 
                  [joinability['joined_keys'][0]], 
                  [joinability['%_joined_keys'][0]],
                  [miss['miss_regs'][0]], [miss['%_miss'][0]])
        
        cols = ['table',
                'dupl_regs', '%_dupl_regs',
                'dupl_key-dates', '%_dupl_key-dates',
                'min_month', 'max_month',
                'samp_keys', 'joined_keys', '%_joined_keys',
                'miss_regs', '%_miss']

        tab_report = self.pd.DataFrame(tab, columns=cols)

        return tab_report, cons_report
    

    def _column_quality(self, var, psi_ranges = 5, tqdm = None, 
                        psi_months = None):
        '''Calls all methods to assess variable quality:
        parameters:
        -----------
            psi_ranges:   [int]  sample of keys to make join_check
            [tqdm] :      [tqdm] if provided, reports the progress
            [psi_months]: [list] list of months to analyse for psi
                                 if None, analyse all self.months
        returns:
        -----------
            gen_report: [DataFrame] DataFrame with %missings, %outliers, 
                                    n-tiles and unique values              
            tim_report: [DataFrame] DataFrame with psi and consistency by month
        ''' 
        if not psi_months:
            psi_months = self.months
        
        # Getting the column type
        cols_df = self.cols
        c_type = cols_df[cols_df['col_name']==var].reset_index()['data_type'][0]

        # Defining methods for numeric or other column types
        if c_type.lower() in self.numeric_types:
            methods = {
                'miss'  : ['_var_gen_missings', var],     
                'outl'  : ['_outliers', var], 
                'uni'   : ['_var_unique', var],       
                'perc'  : ['_var_percs', var],         
                'psi'   : ['_psi', [var, psi_ranges, psi_months]],
                'cons'  : ['_var_consistency', var]
            }
        else:
            methods = {
                'miss' : ['_var_gen_missings', var],
                'uni'  : ['_var_unique', var], 
            }

        if not tqdm:
            tqdm = self.tqdm(list(methods.keys()))

        gen_report = self.pd.DataFrame(zip([var],[c_type]), 
                                       columns=['var','type'])
        tim_report = None

        for mth in methods.keys():
            tqdm.set_postfix_str(f'var: {var} - method: {mth}')
            func = getattr(self, methods[mth][0])
            if mth in ['miss','outl']:
                gen_report = self.pd.concat([gen_report,
                                             func(methods[mth][1])], axis=1)
            if mth == 'perc':
                gen_report = self.pd.concat([gen_report,func(methods[mth][1], 
                                             tqdm = tqdm)], axis=1)
            if mth == 'uni':
                unique = self.pd.Series([func(methods[mth][1])[0:20]],
                                         name= '20_unique_vals')
                gen_report = self.pd.concat([gen_report, unique], axis=1)
            if mth == 'psi':
                psi = func(var = methods[mth][1][0], 
                           n_ranges = methods[mth][1][1], 
                           months = methods[mth][1][2], tqdm = tqdm)
                tim_report = psi
            if mth == 'cons':
                cons = func(var = methods[mth][1])
                tim_report = tim_report.merge(cons, how='left', on='date') 
                
        return gen_report, tim_report

    def columns_quality(self, vars = None, psi_months = None):
        '''Calls the method _column_quality for selected variables:
        parameters:
        -----------
            [vars]:       [list] list of variables analyse, if None, 
                                 the method analyse all the variables 
                                 but self.keycol and self.datecol
            [psi_months]: [list] list of months to analyse for psi
        
        returns:
        -----------
            vars_report: [DataFrame] DataFrame with %missings, %outliers, 
                                     n-tiles and unique values for all vars           
            time_report: [DataFrame] DataFrame with psi and consistency 
                                     by month and var
        ''' 
        if not psi_months:
            psi_months = self.months
        if not vars:
            vars = self.cols[~self.cols['col_name'].\
                       isin([self.keycol,self.datecol])]
        
        p_vars = self.tqdm(vars)

        vars_report = self.pd.DataFrame()
        time_report = self.pd.DataFrame()
        for var in p_vars:
            p_vars.set_postfix_str(f'var: {var}')
            var_rep, time_rep = self._column_quality(var, tqdm = p_vars, 
                                                     psi_months = psi_months)
            vars_report = vars_report.append(var_rep)
            time_report = time_report.append(time_rep)
        
        return vars_report, time_report
