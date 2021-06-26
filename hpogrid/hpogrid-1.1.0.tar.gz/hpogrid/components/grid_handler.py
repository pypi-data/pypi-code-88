import os
import sys
import glob
import argparse
import json
import tempfile

import hpogrid

from hpogrid.components.defaults import *
from hpogrid.utils import helper, stylus
from hpogrid.idds_interface.idds_utils import transpose_config
from hpogrid.configuration import ProjectConfiguration

class GridHandler():
    
    @staticmethod
    def submit(config_input:str, n_jobs=1, site=None, time=-1, search_points=None, mode='grid', debug=False, extra=[]):
        config = GridHandler.preprocess_config(config_input)
        if mode == 'grid':
            GridHandler.submit_grid(config, n_jobs=n_jobs, site=site,
                                    time=time, search_points=search_points, debug=debug, extra=extra)
        elif mode == 'idds':
            GridHandler.submit_idds(config, n_jobs=n_jobs, site=site, debug=debug, extra=extra)
        else:
            raise ValueError('Unknown job submission mode: {}'.format(mode))
            
    @staticmethod
    def preprocess_config(config_input):
        config = hpogrid.load_configuration(config_input)
        config = ProjectConfiguration._validate(config)
        project_name = config['project_name']
        if not helper.is_project(project_name):
            print('INFO: Creating project directory for "{}"'.format(project_name))
            hpogrid.create_project(config, 'create')
        elif not helper.is_project(config_input):
            print('INFO: Replacing project directory for "{}"'.format(project_name))
            hpogrid.create_project(config, 'recreate')
        return config
        
    @staticmethod
    def submit_idds(config, n_jobs=1, site=None, debug=False, extra=[]):
        project_path = helper.get_project_path(config['project_name'])
        print('INFO: Submitting {} idds grid job(s)'.format(n_jobs))
        with tempfile.TemporaryDirectory() as tmpdirname:
            idds_config, search_space = transpose_config(config)
            idds_config_path = os.path.join(tmpdirname, 'idds_config.json')
            search_space_path = os.path.join(tmpdirname, 'search_space.json')
            # create temporary files for idds configuration and search space
            with open(idds_config_path, 'w') as idds_config_file:
                json.dump(idds_config, idds_config_file)
            with open(search_space_path, 'w') as search_space_file:
                json.dump(search_space, search_space_file)  
            command = GridHandler.format_idds_command(config, 
                                               tmpdirname,
                                               site=site,
                                               extra=extra)
            with helper.cd(project_path):
                if debug:
                    print('INFO: iDDS configuration is')
                    table = stylus.create_formatted_dict(idds_config, ['Attribute', 'Value'], indexed=False)
                    print(table)
                    # submit jobs
                    print('INFO: The idds command is ')
                    print('{}'.format(command))
                for _ in range(n_jobs):
                    os.system(command)
    @staticmethod
    def submit_grid(config, n_jobs=1, site=None, time=-1, search_points=None, debug=False, extra=[]):
        project_path = helper.get_project_path(config['project_name'])
        print('INFO: Submitting {} grid job(s)'.format(n_jobs))
        command = GridHandler.format_grid_command(config, site=site,
                                                  time=time,
                                                  search_points=search_points,
                                                  extra=extra)
        with helper.cd(project_path):
            # submit jobs
            for _ in range(n_jobs):
                if debug:
                    print('INFO: The prun command is ')
                    print('{}'.format(command))                
                os.system(command)
                
    @staticmethod
    def format_idds_command(config, tmpdirname, site=None, extra=[]):
        idds_config_path = os.path.join(tmpdirname, 'idds_config.json')
        search_space_path = os.path.join(tmpdirname, 'search_space.json')
        options = {'loadJson': idds_config_path,
                   'searchSpaceFile': search_space_path}
        proj_name = config['project_name']
        grid_config = config['grid_config']
        # override site settings if given
        if not site:
            site = grid_config['site']
                
        if site:
            if isinstance(site, str):
                if site != 'ANY':
                    options['site'] = site
            elif isinstance(site, list):
                options['site'] = ','.join(site)
            else:
                raise ValueError('Invalid site settings: {}'.format(site))
            # specify architecture for gpu/cpu site
            if 'GPU' in options['site']:
                options['architecture'] = 'nvidia-gpu'
        # options excluded from idds configuration file due to
        # possible bash variable expansion
        in_ds = config['grid_config']['inDS']
        out_ds = config['grid_config']['outDS']
        
        if in_ds:
            options['trainingDS'] = in_ds
            
        if '{HPO_PROJECT_NAME}' in out_ds:
            out_ds = out_ds.format(HPO_PROJECT_NAME=proj_name)
        options['outDS'] = out_ds
                
        command = 'phpo {} {}'.format(stylus.join_options(options), ' '.join(extra))    
        return command
    
    @staticmethod
    def format_grid_command(config, site=None, time=-1, search_points=None, extra=[]):
        options = {'forceStaged': '',
                   'useSandbox': '',
                   'noBuild': '',
                   'alrb': ''}
        
        grid_config = config['grid_config']
        proj_name = config['project_name']
        
        options['containerImage'] = grid_config['container']
        
        search_points = '' if not search_points else '--search_points {}'.format(search_points)

        options['exec'] = '"pip install --upgrade hpogrid && '+\
                          'hpogrid run {} --mode grid {}"'.format(proj_name, search_points)

        if not grid_config['retry']:
            options['disableAutoRetry'] = ''

        if grid_config['inDS']:
            options['inDS'] = grid_config['inDS']

        if '{HPO_PROJECT_NAME}' in grid_config['outDS']:
            grid_config['outDS'] = grid_config['outDS'].format(HPO_PROJECT_NAME=proj_name)
                
        options['outDS'] = grid_config['outDS']
                
        if time != -1:
            options['maxCpuCount'] = str(time)
        
        # override site settings if given
        if not site:
            site = grid_config['site']
                
        if site:
            if isinstance(site, str):
                if site != 'ANY':
                    options['site'] = site
            elif isinstance(site, list):
                options['site'] = ','.join(site)
            else:
                raise ValueError('Invalid site settings: {}'.format(site))
            # specify architecture for gpu/cpu site
            if 'GPU' in options['site']:
                options['architecture'] = 'nvidia-gpu'
        
        command = 'prun {} {}'.format(stylus.join_options(options), ' '.join(extra))
        return command        
                