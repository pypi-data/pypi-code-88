# -*- coding: utf-8 -*-

from datetime import datetime,timedelta
import pytz

from odoo import models, api
from odoo.tools.translate import _
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils
from odoo.addons.sm_connect.models.models_sm_carsharing_db_utils import sm_carsharing_db_utils
from odoo.addons.sm_partago_invoicing.models.models_reservation_calculator import reservation_calculator
from odoo.addons.sm_maintenance.models.models_load_data import load_data
from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils


def compute_reservation_params(parent, res):
  initial_mileage = -1
  current_car = -1

  observations = ""
  start_time = datetime.strptime(str(res['startTime']), '%Y%m%d-%H%M%S')
  end_time = datetime.strptime(str(res['endTime']), '%Y%m%d-%H%M%S')
  if 'startStatus' in res:
    if 'fuel_level' in res['startStatus']:
      initial_fl = res['startStatus']['fuel_level']
    else:
      observations += _("Missing fuel level in startStatus\n")
      initial_fl = 0
    if 'mileage' in res['startStatus']:
      initial_mileage = res['startStatus']['mileage']
    else:
      observations += _("Missing mileage in startStatus\n")
  else:
    initial_fl = 0
    initial_mileage = 0
    observations += _("Missing startStatus\n")
  if 'endStatus' in res:
    if 'fuel_level' in res['endStatus']:
      final_fl = res['endStatus']['fuel_level']
    else:
      observations += _("Missing fuel level in endStatus\n")
      final_fl = 0
    if 'mileage' in res['endStatus']:
      final_mileage = res['endStatus']['mileage']
    else:
      final_mileage = 0
      observations += _("Missing mileage in endStatus\n")
  else:
    final_fl = 0
    final_mileage = 0
    observations += _("Missing endStatus\n")

  if 'effectiveStartTime' in res:
    effective_start_time_ts = datetime.fromtimestamp(float(res['effectiveStartTime']) / 1000, tz=pytz.timezone(
      load_data.get_instance().get_config_timezone()))
    effective_start_time = datetime.strptime(str(effective_start_time_ts.strftime("%Y%m%d-%H%M")), "%Y%m%d-%H%M")

  else:
    effective_start_time = start_time

  if 'effectiveEndTime' in res:
    effective_end_time_ts = datetime.fromtimestamp(float(res['effectiveEndTime']) / 1000,
                             tz=pytz.timezone(load_data.get_instance().get_config_timezone()))
    effective_end_time = datetime.strptime(str(effective_end_time_ts.strftime("%Y%m%d-%H%M")), "%Y%m%d-%H%M")
  else:
    effective_end_time = end_time

  duration = (end_time - start_time).total_seconds() / 60.0
  effective_duration = (effective_end_time - effective_start_time).total_seconds() / 60.0

  if res:
    if 'currentCar' in res:
      current_car = res['currentCar']

  return {
    'start_time': start_time,
    'end_time': end_time,
    'effective_start_time': effective_start_time,
    'effective_end_time': effective_end_time,
    'initial_fl': initial_fl,
    'final_fl': final_fl,
    'initial_mileage': initial_mileage,
    'final_mileage': final_mileage,
    'duration': duration,
    'effective_duration': effective_duration,
    'observations': observations,
    'current_car': current_car
  }


def update_reservation_compute(comp, res_params):
  udata = {
    'member_id': res_params['member_id'],
    'related_company': res_params['related_company'],
    'startTime': res_params['start_time'],
    'endTime': res_params['end_time'],
    'effectiveStartTime': res_params['effective_start_time'],
    'effectiveEndTime': res_params['effective_end_time'],
    'duration': res_params['duration'],
    'effectiveDuration': res_params['effective_duration'],
    'initial_fuel_level': res_params['initial_fl'],
    'final_fuel_level': res_params['final_fl'],
    'fuel_consume': res_params['fuel_consume'],
    'fuel_consume_invoiced': res_params['fuel_consume_invoiced'],
    'used_mileage': res_params['used_mileage'],
    'observations': res_params['observations'],
    'usage_mins_invoiced': res_params['usage_mins'],
    'non_usage_mins_invoiced': res_params['non_usage_mins'],
    'extra_usage_mins_invoiced': res_params['extra_usage_mins'],
    'current_car': res_params['current_car']
  }

  if res_params['carconfig_id'] != 0:
    udata['carconfig_id'] = res_params['carconfig_id']

  comp.write(udata)


class sm_reservation_wizard(models.TransientModel):
  _name = "smp.sm_reservation_wizard"

  @api.multi
  def create_request(self):
    self.ensure_one()
    parent = self
    self.compute_reservations(parent)
    return True

  @staticmethod
  def compute_reservations_new(parent):
    print("COMPUTING RESERVATIONS")
    app_db_utils = smp_db_utils.get_instance()
    now_date = datetime.now()
    till_q = now_date.strftime('%Y-%m-%d') + "T00:00:00.00"
    yesterday_date = datetime.now()+ timedelta(days=-1)
    from_q = yesterday_date.strftime('%Y-%m-%d') + "T00:00:00.00"
    reservations_data = app_db_utils.get_app_reservations(from_q,till_q)
    if reservations_data is not False:
      for reservation_data in reservations_data:
        print("RESERVATION DATAS")
        print(reservation_data['resourceId'])
        if reservation_data['car'] is not None:
          print(reservation_data['car'])
        print(reservation_data['personId'])
    return True

  @staticmethod
  def compute_reservations(parent):
    n_context = dict(parent.env.context).copy()
    n_context.update({'batch_db_update': True})
    parent.env.context = n_context

    db_utils = sm_carsharing_db_utils.get_instance()

    rbp_vals = db_utils.firebase_get(endpoint='indexes', key='reservationsByPerson')

    if rbp_vals is not None:
      for rperson in rbp_vals:
        member = parent.env['res.partner'].search([
          ('cs_person_index', '=', rperson)])
        if member.exists():
          for res_index in sorted(rbp_vals[rperson], reverse=True):
            res_id = rbp_vals[rperson][res_index]

            res_data = res_id.split('/', 1)
            car = res_data[0]
            timestamp = res_data[1]

            endpoint_computed = "reservations/" + car
            res = db_utils.firebase_get(endpoint=endpoint_computed, key=timestamp)

            if res:
              now = datetime.now()
              res_params = compute_reservation_params(parent, res)
              res_params['member_id'] = member.id
              res_params['related_company'] = member.parent_id.name
              carconfig = parent.env['smp.sm_car_config'].search([('name', '=', res_data[0])])
              res_params['carconfig_id'] = carconfig.id

              # TODO query reservations in a better way so it takes less.

              if res_params['start_time'] < now:
                comp = sm_utils.get_create_existing_model(parent.env['smp.sm_reservation_compute'],
                  [('name', '=', res_id)],{'name': res_id, 'compute_invoiced': False,
                  'compute_forgiven': False, 'ignore_update': False})

                if not comp.ignore_update and not comp.compute_invoiced and not comp.compute_forgiven:

                  res_params['fuel_consume'] = res_params['final_fl'] - res_params['initial_fl']
                  res_params['fuel_consume_invoiced'] = 0
                  
                  res_params['used_mileage'] = res_params['final_mileage'] - res_params['initial_mileage']
                  if res_params['used_mileage'] < 0:
                    res_params['used_mileage'] = 0

                  new_calculated_attributes = reservation_calculator.get_general_values(res_params,'list')

                  res_params['usage_mins'] = new_calculated_attributes['usage_mins']
                  res_params['non_usage_mins'] = new_calculated_attributes['non_usage_mins']
                  res_params['extra_usage_mins'] = new_calculated_attributes['extra_usage_mins']

                  update_reservation_compute(comp, res_params)

                # TODO: check if reservations by user
                # are really sorted and break once we arrive to the already computed ones.
                else:
                  if comp.compute_invoiced:
                    break
    return True
