from typing import Tuple, List
import pandas as pd
import numpy as np
from .raw import RawDataApi
from .basic import BasicDataApi
from .derived import DerivedDataApi
from ...util.singleton import Singleton
from ...util.calculator_item import *


class ResearchToolApi(metaclass=Singleton):
    
    def get_asset_info_by_key_words(self, key_words: Tuple[str] = ()):
        def get_info_list(dic):
            res = []
            for k,v in dic.items():
                res.append({
                    'asset_id':k,
                    'asset_name':v,
                })
            return res

        try:
            max_num = 20
            stock_info = RawDataApi().get_em_stock_info_by_key_words(key_words)
            stock_info = stock_info.head(min(max_num, stock_info.shape[0]))
            stock_dic = stock_info.set_index('stock_id')['name'].to_dict()

            index_info = BasicDataApi().get_index_info_by_key_words(key_words)
            index_info = index_info.head(min(max_num, index_info.shape[0]))
            index_dic = index_info.set_index('index_id')['desc_name'].to_dict()

            fund_info = BasicDataApi().get_fund_info_by_key_words(key_words=key_words)
            fund_info = fund_info.head(min(max_num, fund_info.shape[0]))
            fund_dic = fund_info.set_index('fund_id')['desc_name'].to_dict()

            fof_info = BasicDataApi().get_fof_info_by_key_words(manager_id='1',key_words=key_words)
            fof_info = fof_info.head(min(max_num, fof_info.shape[0]))
            fof_dic = fof_info.set_index('fof_id')['fof_name'].to_dict()

            stg_info = BasicDataApi().get_asset_info_by_type_by_key_words(asset_type=['策略指数'],key_words=key_words)
            stg_info = stg_info.head(min(max_num, stg_info.shape[0]))
            stg_dic = stg_info.set_index('real_id')['real_name'].to_dict()

            result = []
            res_i = get_info_list(stock_dic)
            if len(res_i) > 0:
                result.append({'asset_type':'股票','asset_list':res_i})
            res_i = get_info_list(index_dic)
            if len(res_i) > 0:
                result.append({'asset_type':'指数','asset_list':res_i})
            res_i = get_info_list(fund_dic)
            if len(res_i) > 0:
                result.append({'asset_type':'公募基金','asset_list':res_i})
            res_i = get_info_list(fof_dic)
            if len(res_i) > 0:
                result.append({'asset_type':'私募基金','asset_list':res_i})
            res_i = get_info_list(stg_dic)
            if len(res_i) > 0:
                result.append({'asset_type':'策略指数','asset_list':res_i})
            return result

        except Exception as e:
            print(f'failed to asset price <err_msg> {e} from ResearchToolApi.get_asset_info_by_key_words')
            return []

    def get_stats_df(self, df):
        stats_name = {
                'start_date':'成立日',
                'annual_ret':'年化收益',
                'annual_vol':'年化波动',
                'sharpe':'夏普',
                'mdd':'最大回撤',
                'mdd_date1':'最大回撤开始日',
                'mdd_date2':'最大回撤结束日',
            }
        res = []
        for asset in df:
            _df = df[[asset]].copy().dropna()
            stats_dic = CalculatorBase.get_stat_result(dates=_df.index, values=_df[asset], risk_free_rate=0.025)
            stats_dic['资产名'] = asset
            res.append(stats_dic)
        stats_df = pd.DataFrame(res).set_index('资产名')[stats_name.keys()].rename(columns=stats_name)
        stats_df['成立日'] = stats_df['成立日'].astype(str)
        stats_df['最大回撤开始日'] = stats_df['最大回撤开始日'].astype(str)
        stats_df['最大回撤结束日'] = stats_df['最大回撤结束日'].astype(str)
        stats_df.columns.name = '价格比指标'
        return stats_df

    def get_all_asset_price(self, stock_info, index_info, fund_info, hf_fund_info, hf_index_info, asset_id):
        raw = RawDataApi()
        basic = BasicDataApi()
        id_list_1 = stock_info[stock_info.stock_id.isin(asset_id)].stock_id.tolist()
        id_list_2 = index_info[index_info.index_id.isin(asset_id)].index_id.tolist()
        id_list_3 = fund_info[fund_info.fund_id.isin(asset_id)].fund_id.tolist()
        id_list_4 = hf_fund_info[hf_fund_info.fof_id.isin(asset_id)].fof_id.tolist()
        id_list_5 = hf_index_info[hf_index_info.real_id.isin(asset_id)].real_id.tolist()
        result = []
        if len(id_list_1) > 0 :
            # stock price
            dic = stock_info.set_index('stock_id')['name'].to_dict()
            df = raw.get_em_stock_post_price(stock_list=id_list_1)
            df = df.pivot_table(index='datetime',columns='stock_id',values='close')
            #df = df.rename(columns=dic)
            if not df.empty:
                result.append(df)
        if len(id_list_2) > 0:        
            # index price
            dic = index_info.set_index('index_id')['desc_name'].to_dict()
            df = basic.get_index_price(index_list=id_list_2)
            df = df.pivot_table(index='datetime',columns='index_id',values='close')
            #df = df.rename(columns=dic)
            if not df.empty:
                result.append(df)
        if len(id_list_3) > 0:
            # fund nav
            dic = fund_info.set_index('fund_id')['desc_name'].to_dict()
            df = basic.get_fund_nav(fund_list=id_list_3)
            df = df.pivot_table(index='datetime',columns='fund_id',values='adjusted_net_value')
            #df = df.rename(columns=dic)
            if not df.empty:
                result.append(df)
        if len(id_list_4) > 0:
            # hf fund nav
            dic = hf_fund_info.set_index('fof_id')['fof_name'].to_dict()
            default_manager_id = 'py1'
            fund_nav1 = DerivedDataApi().get_fof_nav(fof_id_list=id_list_4,manager_id=default_manager_id)
            col1 = []
            col2 = []
            _result = []
            if not fund_nav1.empty:
                fund_nav1 = fund_nav1.pivot_table(index='datetime',columns='fof_id',values='adjusted_nav')
                col1 = fund_nav1.columns.tolist()
                _result.append(fund_nav1[col1])
            fund_nav2 = DerivedDataApi().get_fof_nav_public(fof_id_list=id_list_4)
            if fund_nav2 is not None and not fund_nav2.empty:
                fund_nav2 = fund_nav2.pivot_table(index='datetime',columns='fof_id',values='adjusted_nav')
                col2 = fund_nav2.columns.tolist()
                col2 = [_ for _ in col2 if _ not in col1]
                _result.append(fund_nav2[col2])
            if len(_result) > 0:
                df = pd.concat(_result, axis=1).sort_index()
                #df = df.rename(columns=dic)
                df = df.set_axis(pd.to_datetime(df.index), inplace=False).resample('W-FRI').last()
                df.index = [i.date() for i in df.index]
                if not df.empty:
                    result.append(df)
        if len(id_list_5) > 0:
            # hf_index_price
            dic = hf_index_info.set_index('real_id')['real_name'].to_dict()
            df = raw.get_hf_index_price(index_ids=id_list_5)
            df = df.pivot_table(index='index_date', columns='index_id', values='close')
            #df = df.rename(columns=dic)
            if not df.empty:
                result.append(df)
        return pd.concat(result,axis=1).sort_index()

    def get_data_dict_of_list(self, df):
        dic = {}
        for col in df:
            dic[col] = df[col].values.tolist()
        return dic

    def get_asset_info_with_begin_date(self, key_words):
        max_num = 20
        stock_info = RawDataApi().get_em_stock_info_by_key_words(key_words)
        stock_info = stock_info.head(min(max_num, stock_info.shape[0]))
        stock_dic = stock_info.set_index('stock_id')['name'].to_dict()

        index_info = BasicDataApi().get_index_info_by_key_words(key_words)
        index_info = index_info.head(min(max_num, index_info.shape[0]))
        index_dic = index_info.set_index('index_id')['desc_name'].to_dict()

        fund_info = BasicDataApi().get_fund_info_by_key_words(key_words=key_words)
        fund_info = fund_info.head(min(max_num, fund_info.shape[0]))
        fund_dic = fund_info.set_index('fund_id')['desc_name'].to_dict()

        fof_info = BasicDataApi().get_fof_info_by_key_words(manager_id='1',key_words=key_words)
        fof_info = fof_info.head(min(max_num, fof_info.shape[0]))
        fof_dic = fof_info.set_index('fof_id')['fof_name'].to_dict()

        stg_info = BasicDataApi().get_asset_info_by_type_by_key_words(asset_type=['策略指数'],key_words=key_words)
        stg_info = stg_info.head(min(max_num, stg_info.shape[0]))
        stg_dic = stg_info.set_index('real_id')['real_name'].to_dict()

        stock_dic.update(index_dic)
        stock_dic.update(fund_dic)
        stock_dic.update(fof_dic)
        stock_dic.update(stg_dic)
        price_df = self.get_all_asset_price(stock_info, index_info, fund_info, fof_info, stg_info, stock_dic.keys())
        _stock_dic = stock_info.set_index('stock_id')['name'].to_dict()
        res = []
        for col in price_df:
            if col in _stock_dic:
                asset_type = '股票'
            elif col in index_dic:
                asset_type = '指数'
            elif col in fund_dic:
                asset_type = '公募基金'
            elif col in fof_dic:
                asset_type = '私募基金'
            elif col in stg_dic:
                asset_type =  '私募基金'
            dic = {
                'id':col,
                'name':stock_dic[col],
                'begin_date':price_df[col].dropna().index[0],
                'asset_type':asset_type,
            }
            res.append(dic)
        df = pd.DataFrame(res)
        return df
    
    def super_price_ratio(self, asset_ids: Tuple[str]=(), bmk_id: str='', start_date=None, end_date=None):
        try:
            all_asset_ids = asset_ids if bmk_id in asset_ids else asset_ids + [bmk_id]
            stock_info = RawDataApi().get_em_stock_info(stock_list=all_asset_ids)
            index_info = BasicDataApi().get_index_info(index_list=all_asset_ids)
            fund_info = BasicDataApi().get_fund_info(fund_list=all_asset_ids)
            hf_fund_info = BasicDataApi().get_fof_info(manager_id='1', fof_id_list=all_asset_ids)
            hf_index_info = BasicDataApi().get_asset_info_by_real_id_and_asset_type(real_id_list=all_asset_ids,asset_type='策略指数')

            # id 和名字对照
            dic = stock_info.set_index('stock_id')['name'].to_dict()
            dic1 = index_info.set_index('index_id')['desc_name'].to_dict()
            dic2 = fund_info.set_index('fund_id')['desc_name'].to_dict()
            dic3 = hf_fund_info.set_index('fof_id')['fof_name'].to_dict()
            dic4 = hf_index_info.set_index('real_id')['real_name'].to_dict()
            dic.update(dic1)
            dic.update(dic2)
            dic.update(dic3)
            dic.update(dic4)
            name_dic = [{'asset_id':k,'asset_name':v} for k,v in dic.items()]

            price_df = self.get_all_asset_price(stock_info, index_info, fund_info, hf_fund_info, hf_index_info, asset_ids).loc[start_date:end_date]
            benchmark_df = self.get_all_asset_price(stock_info, index_info, fund_info, hf_fund_info, hf_index_info, [bmk_id]).loc[start_date:end_date]
            price_df = price_df.join(benchmark_df).sort_index()
            price_df = price_df/price_df.bfill().iloc[0]
            price_df = price_df.dropna()
            benchmark_name = benchmark_df.columns[0]
            
            # 把资产价格起点设置在同期指数点位，形成散开方式
            _price_df = price_df.copy()
            asset_names = _price_df.columns.tolist()
            for asset_i in asset_names:
                b_d = _price_df[asset_i].dropna().index[0]
                ratio = price_df[benchmark_name].loc[b_d]
                _price_df[asset_i] = _price_df[asset_i] * ratio
            
            # 各资产求价格比
            result = []
            for col in price_df:
                if col == benchmark_name:
                    continue
                _df = price_df[[col]].join(benchmark_df.rename(columns={benchmark_name:'benchmark'})).dropna()
                _df = _df / _df.iloc[0]
                _df = (_df[col] / _df['benchmark']).to_frame()
                _df.columns = [col]
                result.append(_df)
            df = pd.concat(result,axis=1).sort_index()
            cols = df.columns.tolist()
            cols = [f'{_}/{benchmark_name}' for _ in cols]
            df.columns= cols

            calculate_result = self.get_stats_df(df)
            result = {'mv':self.get_data_dict_of_list(_price_df),
                    'mv_diff':self.get_data_dict_of_list(df),
                    'table':calculate_result.T.to_dict(),
                    'name_dic':name_dic,
                    'datetime':df.index.astype(str).tolist(),
            }
        except Exception as e:
            print(f'Failed to get data <err_msg> {e} from ResearchToolApi.super_price_ratio')
            result = {'mv':{},
                    'mv_diff':{},
                    'table':{},
                    'name_dic':[],
                    'datetime':[],
            }
        return result

if __name__ == '__main__':
    
    # 搜关键字返回资产名
    keys_words = ['茅台','贵州']
    result = ResearchToolApi().get_asset_info_by_key_words(key_words=keys_words)

    # 价格比计算
    asset_ids = ['600519.SH']
    bmk_id = 'hs300'
    start_date = datetime.date(2021,1,1)
    end_date = datetime.date(2022,1,1)
    result = ResearchToolApi().super_price_ratio(asset_ids=asset_ids,
                                                bmk_id=bmk_id,
                                                start_date=start_date,
                                                end_date=end_date,
                                                )