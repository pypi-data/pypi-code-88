from __future__ import absolute_import, division, print_function, unicode_literals
from .ml import FunkSVD, BiasSVD, SVDpp, BPR, ALS, AFM, FM
from .dl import PNN
from .graph import DeepWalk

__author__ = ['Li Tang']
__copyright__ = 'Li Tang'
__credits__ = ['Li Tang']
__license__ = 'MIT'
__version__ = '0.2.0'
__maintainer__ = ['Li Tang']
__email__ = 'litang1025@gmail.com'
__status__ = 'Production'

my_dear = "Dear Miss Sui Lin, I love you!"

__api_info_dict = {
    "sui.ALS": ALS.__doc__,
    "sui.BiasSVD": BiasSVD.__doc__,
    "sui.BPR": BPR.__doc__,
    "sui.FunkSVD": FunkSVD.__doc__,
    "sui.GRU4Rec": "GRU4Rec",
    "sui.PNN": PNN.__doc__,
    "sui.SVDpp": SVDpp.__doc__,
    "sui.DeepWalk": DeepWalk.__doc__,
    "sui.toolbox.top_k": "Return a list containing top k data for a specific dimension",
    "sui.toolbox.random_walk": "Generate a list including walking paths based on random walk in the input graph"
}


def api_info(api=None):
    if api is not None:
        if api in __api_info_dict:
            print('API: {}\nInfo: {}\n'.format(api, __api_info_dict[api]))
        else:
            print('{} is not a correct API.'.format(api))
    else:
        for api, info in __api_info_dict.items():
            print('API: {}\nInfo: {}\n'.format(api, info))
