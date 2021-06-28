from datetime import datetime
from html.parser import HTMLParser
#from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils
from odoo.addons.sm_connect.models.models_sm_carsharing_api_utils import sm_carsharing_api_utils

class smp_user_utils(object):
  __instance = None
  # __smp_db_utils = None

  @staticmethod
  def get_instance():
    if smp_user_utils.__instance is None:
      smp_user_utils()
    return smp_user_utils.__instance

  def __init__(self):
    if smp_user_utils.__instance is not None:
      raise Exception("This class is a singleton!")
    else:
      smp_user_utils.__instance = self
      # smp_user_utils.__smp_db_utils = smp_db_utils.get_instance()

  def update_members_carsharing_registration_status_cron(self,parent):
    requested_members = parent.env['res.partner'].search([
      ('cs_registration_info_ok','=',False),
      ('cs_state','not in',('no_access','blocked_banned'))
    ])
    if requested_members.exists():
      for member in requested_members:
        member.recompute_cs_registration_info()

  def register_in_carsharing_cron(self, parent):
    registration_requests = parent.env['sm_partago_user.carsharing_registration_request'].search([
      ('completed','=',False), ('related_member_id', '!=', False)
    ])
    if registration_requests.exists():
      for registration_request in registration_requests:
        registration_request.compute_request(True)
