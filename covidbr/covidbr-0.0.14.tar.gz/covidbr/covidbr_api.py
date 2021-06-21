from .log import logging
from .io_api import login_io
from .get_data import data_from_city
from .plot_data.plotting import plot_media_cases
from .plot_data.plotting import plot_media_deaths
from .plot_data.painel import create_painel

#from .logger import logger

all = [data_from_city
       ,login_io,logging,
       plot_media_cases,
       plot_media_deaths,
       create_painel
]