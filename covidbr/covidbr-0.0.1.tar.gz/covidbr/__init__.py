from covidbr.log import logging
from covidbr.io_api import login_io
from covidbr.get_data import data_from_city
from covidbr.plot_data.plotting import plot_media_cases
from covidbr.plot_data.plotting import plot_media_deaths
from covidbr.plot_data.painel import create_painel

#from .logger import logger

all = [data_from_city
       ,login_io,logging,
       plot_media_cases,
       plot_media_deaths,
       create_painel
]