import pandas as pd
import geopandas as gpd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from . import helper_funcs
from . import diagnostics

def crosswalk(source_shape_or_filepath, source_shape_id, target_shape_or_filepath, target_shape_id, 
				source_population_col_id = None, source_col_id_to_weigh_by_population = None,
				tolerance_percent = 10, tolerance_units = None, 
				export = False, export_filename = None):
		# ------------------------------------additional error handling for columns required

	# ---------------------- read in files
	# rudimentary handling of arguments but suffices for now
	if type(source_shape_or_filepath) == 'str':
		source_shape = gpd.GeoDataFrame.from_file(source_shape_or_filepath)
	else:
		source_shape = source_shape_or_filepath
	if type(target_shape_or_filepath) == 'str':
		target_shape = gpd.GeoDataFrame.from_file(target_shape_or_filepath)
	else:
		target_shape = target_shape_or_filepath
	source_shape['area_base_source'] = source_shape.area
	target_shape = target_shape.to_crs(source_shape.crs) # kinda important this one 
	target_shape['area_base_target'] = target_shape.area

	# ---------------------------------intersect
	intersect = gpd.overlay(source_shape, target_shape, how='intersection', keep_geom_type=False)
	intersect['intersect_area'] = intersect.area
	# intersect['geom_type'] = intersect['geometry'].geom_type
	intersect['INTERSECT_ID'] = intersect[source_shape_id].astype(str) + '_' + intersect[target_shape_id].astype(str)	

	intersect_unedited = intersect.copy() # preserving just in case - used for user stats below

	# ----------------------------filter intersection based on tolerance
	intersect_smallest_area_from_source_and_target = min(min(intersect['area_base_source']), min(intersect['area_base_target']))

	if tolerance_units is not None and not(np.isnan(tolerance_units)):
		tolerance_percent = (tolerance_units / intersect_smallest_area_from_source_and_target)*100
	elif not(np.isnan(tolerance_percent)):
		tolerance_units = intersect_smallest_area_from_source_and_target*(tolerance_percent/100)
	else:
		raise ToleranceException("Tolerance could not be calculated.")

	intersect_smallest_area_postfilter = tolerance_units
	
	intersect = intersect[intersect['intersect_area'] > intersect_smallest_area_postfilter]

	# ----------------------------add weights and adjust the desired variable by population, if provided
	intersect['weight'] = intersect['intersect_area'] / intersect['area_base_source']
	if source_population_col_id is not None:
		# calculate population by target
		intersect['intersect_population'] = intersect['weight'] * intersect[source_population_col_id]
		intersect['target_shape_population'] = intersect.groupby(target_shape_id)['intersect_population'].transform('sum')

		if source_col_id_to_weigh_by_population is not None:
			intersect['intersect_'+source_col_id_to_weigh_by_population] = (intersect['weight'] * intersect[source_col_id_to_weigh_by_population]) * (intersect['intersect_population'] / intersect['target_shape_population'])
			intersect['target_shape_'+source_col_id_to_weigh_by_population] = intersect.groupby(target_shape_id)['intersect_'+source_col_id_to_weigh_by_population].transform('sum')
	
	# ------------------------------get diagnostics
	tolerance_values_sim_prop = [0.00001, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 0.9, 1, 1.5]
	if tolerance_percent/100 not in tolerance_values_sim_prop:
		tolerance_values_sim_prop.append(tolerance_percent/100)

	diagnostics_obj = diagnostics.get_diagnostics_obj(source_shape, source_shape_id, target_shape, target_shape_id, intersect_unedited, intersect, tolerance_percent, tolerance_units, tolerance_values_sim_prop)
	
	#-------------------------------------------------------------------------------EXPORT--------------------------
	if export:
		if export_filename is None:
			time_now = datetime.now().strftime('%H%M%S-%Y%m%d')
			filename = 'crosswalk_'+time_now+'.csv'
		else:
			filename = export_filename

		if not(filename.endswith('.csv')):
			filename = filename+'.csv'

		# dropping geometry to save space and time
		intersect.drop('geometry', axis='columns', inplace=False).to_csv(filename, index=False)

	return intersect, diagnostics_obj