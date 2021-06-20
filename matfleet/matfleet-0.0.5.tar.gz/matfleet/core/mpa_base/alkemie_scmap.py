#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/04/19 14:55:53'

import datetime
# from pyecharts import Map, Line, Bar, Overlap, WordCloud, Page
import os
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


def test():
    from pyecharts.faker import Faker
    from pyecharts import options as opts
    from pyecharts.charts import Geo
    from pyecharts.globals import ChartType, SymbolType
    import pandas as pd
    import json
    
    def add_adress_json() -> Geo:
        # http://api.map.baidu.com/geocoder?key=f247cdb592eb43ebac6ccd27f796e2d2&output=json&address=
        test_data_ = [("测试点1", 116.512885, 39.847469), ("测试点2", 125.155373, 42.933308), ("测试点3", 87.416029, 43.477086)]
        count = [1000, 2000, 500]
        address_ = []
        json_data = {}
        for ss in range(len(test_data_)):
            json_data[test_data_[ss][0]] = [test_data_[ss][1], test_data_[ss][2]]
            address_.append(test_data_[ss][0])
        
        json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
        with open('test_data.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_str)
        
        c = (
            Geo()
                .add_schema(maptype="world")  # 可以换成 world,或 china
                .add_coordinate_json(json_file='test_data.json')  # 加入自定义的点
                # 为自定义的点添加属性
                .add("", data_pair=[list(z) for z in zip(address_, count)], symbol_size=30, large_threshold=2000,
                     symbol="pin")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=2000),
                                 title_opts=opts.TitleOpts(title="json加入多个坐标"))
                .render('111.html')
        )
        return c
    
    add_adress_json()



def get_plot(data):
    data = [opts.MapItem(name=k,
                         value=v,
                         label_opts=opts.LabelOpts(is_show=False,
                                                   font_size=15,
                                                   font_weight='bold',
                                                   distance=15,
                                                   background_color='white'),
                         is_selected=False,
                         itemstyle_opts=opts.ItemStyleOpts(border_color='k',
                                                           border_width=2)
                         )
            for k, v in data.items()]
    
    map = Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    
    map.add(series_name="",
            data_pair= data,
            maptype="china",
            is_map_symbol_show=True,
            symbol="pin",
            zoom=1.2)
    
    map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    map.set_global_opts(title_opts=opts.TitleOpts(title="ALKEMIE 超算部署情况", item_gap=10,
                                                  title_textstyle_opts=opts.TextStyleOpts(font_size=25),
                                                  subtitle="截止2021年4月份ALKEMIE超算部署情况",),
                        visualmap_opts=opts.VisualMapOpts(min_=1, max_=3, range_color=["#5EA1AC", "lightcoral"]))
    map.render('ttt.html')
    return map


def make_png(dddd):
    from snapshot_selenium import snapshot as driver
    from pyecharts.render import make_snapshot
    make_snapshot(driver, get_plot(dddd).render(), "./bar.png")


if __name__ == '__main__':
    dddd = {"北京": 3,
            "天津": 1,
            "河南": 1,
            "广东": 2,
            "福建": 1,
            "四川": 1,
            }
    # test()
    get_plot(data=dddd)
