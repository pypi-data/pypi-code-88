# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from html.parser import HTMLParser
from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils
from odoo.addons.sm_maintenance.models.models_sm_resources import sm_resources
from odoo.addons.sm_connect.models.models_sm_wordpress_db_utils import sm_wordpress_db_utils
from odoo.addons.sm_partago_usage.models.models_smp_usage_utils import smp_usage_utils

class sm_reward(models.Model):
  _name = 'sm_rewards.sm_reward'
  _inherit = ['mail.thread']
  _description = "CS Reward"

  name = fields.Char(string=_("Name"))

  # REWARD DATA
  reward_type = fields.Selection([
    ('promocode', 'Promo codes'),
    ('fleet_maintenance', 'Fleet maintenance')], string=_("Type"),required=True)
  promo_code = fields.Char(string=_("Promo code"))
  related_analytic_account_id = fields.Many2one(
    'account.analytic.account', string=_("Reward analytic account"))
  reward_date = fields.Date(string=_("Date"))
  reward_addtime = fields.Integer(string=_("Reward (time/minutes)"))
  reward_addmoney = fields.Float(string=_("Reward (money)"))
  reward_info = fields.Char(string=_("Info"))
  force_register_cs = fields.Boolean(string=_("Force registration"))
  force_dedicated_ba = fields.Boolean(string=_("Force dedicated billingAccount"))
  coupon_group = fields.Char(string=_("Group (index)"))
  coupon_group_secondary = fields.Char(string=_("Secondary Group (index)"))
  group_config = fields.Char(string=_("Group config")) # TODO: To be removed

  # REWARD TARIFF DATA
  tariff_name = fields.Char(string=_("Tariff Name"))
  tariff_related_model = fields.Char(string=_("Related model"))
  tariff_type = fields.Char(string=_("Type"))
  tariff_quantity = fields.Char(string=_("Quantity"))

  # STATUS INDICATORS
  completed = fields.Date(string=_("Completed Date"))
  state = fields.Selection([
    ('new', 'New'),
    ('member','Member computed'),
    ('follower','Follower added'),
    ('complete', 'Completed'),
    ('cancelled','Cancelled')
  ], default='new')
  final_state = fields.Selection([
    ('not_completed', 'Not completed'),
    ('soci_not_found', 'Member not found'),
    ('reward_completed', 'Completed'),
    ('cancelled','Cancelled')
  ], default='not_completed')

  # MAINTENANCE FIELDS
  maintenance_reservation_type = fields.Selection([
    ('maintenace', 'Reservation only for maintenance task'),
    ('reservation_and_maintenance', 'Reservation and maintenance task'),
  ],string=_("Maintenance reservation type"))
  maintenance_forgive_reservation = fields.Boolean(string=_("Forgive related reservation"))
  maintenance_type = fields.Selection([
    ('clean_inside', 'Clean inside vehicle'),
    ('clean_outside', 'Clean outside vehicle'),
    ('clean_inside_outside', 'Clean inside and outside vehicle'),
    ('car_to_mechanic', 'Bring car to mechanic'),
    ('swap_car', 'Swap car'),
    ('wheel_pressure', 'Adjust wheel pressure'),
    ('charge_car', 'Charge vehicle'),
    ('member_tutorial', 'Teach another member'),
    ('representation_act', 'Representation act'),
    ('other', 'Other'),
  ],string=_("Maintenance type"))
  maintenance_duration = fields.Char(string=_("Maintenance duration"))
  maintenance_observations = fields.Text(string=_("Observations"))
  maintenance_carconfig_index = fields.Char(string=_("carConfig index"))
  maintenance_carconfig_id = fields.Many2one('smp.sm_car_config',string=_("carConfig DB"),
    compute="_get_maintenance_carconfig_id",store=True)
  maintenance_carconfig_home = fields.Char(string=_("carConfig Home"))
  maintenance_cs_person_index = fields.Char(string=_("Carsharing person index"))
  maintenance_reservation_start = fields.Char(string=_("Reservation start"))
  maintenance_reservation_id = fields.Many2one('smp.sm_reservation_compute',string=_("Reservation DB"))
  maintenance_car_plate = fields.Char(string=_("Car plate (from form)"))
  maintenance_car_id = fields.Many2one('fleet.vehicle',string=_("car DB"),
    compute="_get_maintenance_car_id",store=True)
  maintenance_car_id_plate = fields.Char(string="car License plate",compute="_get_maintenance_car_id_plate")
  maintenance_create_car_service = fields.Boolean(string=_("Create car service"))
  maintenance_car_service_id = fields.Many2one('fleet.service.type',string=_("car service DB"))
  maintenance_discount_reservation = fields.Boolean(string=_("Discount minutes from reservation"))

  # COMPLETED COMPUTATION FIELDS
  related_member_id = fields.Many2one('res.partner', string=_("Partner"))
  maintenance_car_service_log_ids = fields.One2many(
    comodel_name='fleet.vehicle.log.services',
    inverse_name='related_reward_id',
    string=_("CS car services"))
  
  cs_registration_request_ids = fields.One2many(
    comodel_name='sm_partago_user.carsharing_registration_request',
    inverse_name='related_reward_id',
    string=_("CS registration requests"))

  pb_record_ids= fields.One2many(
    comodel_name='pocketbook.pocketbook_record',
    inverse_name='related_reward_id',
    string=_("CS pocketbook records"))

  tariffs_ids = fields.One2many(
    comodel_name='smp.sm_carsharing_tariff',
    inverse_name='related_reward_id',
    string=_("CS tariffs"))

  # EXTERNAL DATA
  data_partner_creation_type = fields.Selection([
    ("none", "Nothing to do"),
    ("new", "Create new partner"),
    ("existing", "Find existing partner")],
    string=_("Partner creation type"),
    default="none",
    required=True
  )
  data_partner_cs_user_type = fields.Selection([
    ('user', 'Regular user'),
    ('promo', 'Promo user')
  ], default='promo', string=_("Carsharing user type"))
  data_partner_firstname = fields.Char(string=_("Firstname"))
  data_partner_lastname = fields.Char(string=_("Lastname"))
  data_partner_vat = fields.Char(string=_("VAT"))
  data_partner_email = fields.Char(string=_("Email"))
  data_partner_mobile = fields.Char(string=_("Mobile"))
  data_partner_phone = fields.Char(string=_("Phone"))
  data_partner_gender = fields.Selection(
    [("male", "Male"), ("female", "Female"), ("other", "Other")],
    string=_("Gender"),
  )
  data_partner_birthdate_date = fields.Date(string=_("Birthdate"))
  data_partner_street = fields.Char(string=_("Street"))
  data_partner_zip = fields.Char(string=_("ZIP"))
  data_partner_state_id = fields.Many2one('res.country.state', string=_("State"))
  data_partner_city = fields.Char(string=_("City"))
  data_partner_iban = fields.Char(string=_("IBAN"))
  data_partner_driving_license_expiration_date = fields.Char(string=_("Driving license expiration date"))
  data_partner_image_dni = fields.Char(string=_("DNI image"))
  data_partner_image_driving_license = fields.Char(string=_("Driving license image"))

  # EXTERNAL REFERENCES
  external_obj_id = fields.Integer(string=_("External obj id"))
  external_promo_obj_id = fields.Integer(string=_("External promo obj id"))

  wp_member_coupon_id = fields.Char(string=_("Member coupon wp ID")) # Deprecated
  wp_coupon_id = fields.Char(string=_("Coupon wp ID")) # Deprecated
  maintenance_wp_entry_id = fields.Char("Maintenance wp ID") # Deprecated
  wp_member_id = fields.Char(string=_("Member wp ID")) # Deprecated

  cron_executed = fields.Boolean(string=_("Cron executed"))
  _order = "reward_date desc"
  
  # COMPUTED FIELDS
  @api.depends('maintenance_carconfig_index')
  def _get_maintenance_carconfig_id(self):
    for record in self:
      if record.maintenance_carconfig_index:
        existing_cc = self.env['smp.sm_car_config'].search([('name','=',record.maintenance_carconfig_index)])
        if existing_cc.exists():
          record.maintenance_carconfig_id = existing_cc[0].id

  @api.depends('maintenance_carconfig_id','maintenance_car_plate')
  def _get_maintenance_car_id(self):
    for record in self:
      lp = False
      if record.maintenance_carconfig_id:
        lp = record.maintenance_carconfig_id.rel_car_id_license_plate
      else:
        if record.maintenance_car_plate:
          lp = record.maintenance_car_plate
      if lp:
        existing_c = self.env['fleet.vehicle'].search([('license_plate','=',lp)])
        if existing_c.exists():
          record.maintenance_car_id = existing_c[0].id

  @api.depends('maintenance_car_id')
  def _get_maintenance_car_id_plate(self):
    for record in self:
      if record.maintenance_car_id:
        record.maintenance_car_id_plate = record.maintenance_car_id.license_plate

  # STATUS
  def set_status(self,status):
    self.write({
      'state': status
    })

  # VIEW
  @api.multi
  def get_reward_form_view(self):
    view_ref = self.env['ir.ui.view'].search(
      [('name', '=', 'view_reward_form')])
    reward_id = self.env.context.get('active_id', False)
    return {
      'name': 'Reward',
      'view_type': 'form',
      'view_mode': 'form',
      'res_model': 'sm_rewards.sm_reward',
      'type': 'ir.actions.act_window',
      'view_id': view_ref.id,
      'target': 'current',
      'res_id': reward_id,
      'context': self.env.context
    }

  # ACTIONS - RESET
  def reset_state_action(self):
    if self.env.context:
      rwds = self.env['sm_rewards.sm_reward'].browse(
        self.env.context['active_ids'])
      if rwds.exists():
        for rwd in rwds:
          rwd.write({
            'state': 'new',
            'final_state': 'not_completed',
            'completed': False
          })

  # ACTIONS - CANCEL
  @api.multi
  def cancel_reward_progressbar_action(self):
    if self.state != 'complete':
      self.set_cancelled_status()
    else:
      resources = sm_resources.getInstance()
      return resources.get_successful_action_message(self,_("Can't cancel a completed reward"), self._name)

  def set_cancelled_status(self):
    self.write({
      'state': 'cancelled',
      'final_state': 'cancelled',
      'completed': datetime.now()
    })

  # ACTIONS - REL RESERVATION
  def find_related_reservation_action(self):
    if self.env.context:
      rwds = self.env['sm_rewards.sm_reward'].browse(
        self.env.context['active_ids'])
      if rwds.exists():
        _usage_utils = smp_usage_utils.get_instance()
        for rwd in rwds:
          if self.maintenance_reservation_start:
            date_obj = datetime.strptime(str(self.maintenance_reservation_start), "%Y-%m-%d %H:%M:%S")
            rel_reservation = _usage_utils.get_reservation_from_cc_and_start(self,self.maintenance_carconfig_index,date_obj)
            if rel_reservation:
              self.write({
                'maintenance_reservation_id': rel_reservation.id
              })

  # CRON
  def process_reward_from_cron(self):
    # Member
    if self.state == 'new':
      try:
        validation = self.compute_member()
      except Exception as error:
        sm_utils.create_system_task(self,"CS Rerwards error on create subscription", str(error))
      if validation['valid'] == False:
        if self.data_partner_creation_type == 'existing' and not self._get_existing_related_partner():
          self.fetch_user_error_incron()
        else:
          error_msg = _("""CS Reward memebrship validation error. %s Reward id: %s""") % (validation['error'],str(self.id))
          sm_utils.create_system_task(self,"CS Rerwards error.",error_msg)
          return False
    # Follower
    follower_success = self.add_follower()
    if not follower_success:
      error_msg = _("""CS Reward follower error. Couldn't add follower.No related member defined. Reward id: %s""") % (str(self.id))
      sm_utils.create_system_task(self,"CS Reward error.",error_msg)
      return False
    # Compute
    validation = self._validate_completion()
    if validation['valid']:
      self.complete_reward()
    else:
      error_msg = _("""CS Reward completion validation error. %s Reward id: %s""") % (validation['error'],str(self.id))
      sm_utils.create_system_task(self,"CS Rerwards error.",error_msg)
      return False
    return True

  # ACTIONS - MEMBER
  def _validate_membership(self):
    if self.data_partner_creation_type == 'none':
      return {
        'error': _('Error: Reward must have "Partner creation type" defined.'),
        'valid': False
      }
    if self.data_partner_creation_type == 'new' or self.data_partner_creation_type == 'subscription':
      # Maintenance rewards cannot be type new
      if self.reward_type == 'fleet_maintenance':
        return {
        'error': _("Error: Misconfiguration. Cannot create a member on maintenance reward."),
        'valid': False
      }
      # Required fields
      if not self.data_partner_cs_user_type or \
        not self.data_partner_firstname or \
        not self.data_partner_lastname or \
        not self.data_partner_vat or \
        not self.data_partner_email or \
        not self.data_partner_mobile or \
        not self.data_partner_iban:
        return {
          'error': _("Error: Missing fields on member creation."),
          'valid': False
        }
      # IBAN validation
      if not sm_utils.validate_iban(self,self.data_partner_iban):
        return {
          'error': _("Error: IBAN not valid."),
          'valid': False
        }
      # Existing member validation
      if self._get_existing_related_partner():
        return {
          'error': _("Error: Trying to create a new member but it already exists one."),
          'valid': False
        }
    # Member not found
    if self.data_partner_creation_type == 'existing' and not self._get_existing_related_partner():
      return {
        'error': _("Error: Member not found."),
        'valid': False
      }
    # 200 OK
    return {
      'valid': True
    }

  def compute_member(self):
    # member can be manually setup (for maintenance rewards)
    if self.related_member_id:
      self.set_status('member')
      return {
        'valid': True
      }
    validation = self._validate_membership()
    if validation['valid']:
      if self.data_partner_creation_type == 'existing':
        self.fetch_user()
        self.set_status('member')
      elif self.data_partner_creation_type == 'new':
        self.fetch_user()
        self.set_status('member')
      return {
        'valid': True
      }
    else:
      return {
        'valid': False,
        'error': validation['error']
      }

  @api.multi
  def compute_member_progressbar_action(self):
    if self.state == 'new':
      validation = self.compute_member()
      if validation['valid'] == False:
        resources = sm_resources.getInstance()
        return resources.get_successful_action_message(self,validation['error'], self._name)

  def compute_member_action(self):
    if self.env.context:
      rwds = self.env['sm_rewards.sm_reward'].browse(
        self.env.context['active_ids'])
      if rwds.exists():
        for rwd in rwds:
          if rwd.state == 'new':
            self.compute_member()

  # ACTIONS - FOLLOWER
  def add_follower(self):
    if self.related_member_id:
      self.message_subscribe([self.related_member_id.id])
      self.set_status('follower')
      return True
    return False

  @api.multi
  def add_follower_progressbar_action(self):
    if self.state == 'member':
      follower_success = self.add_follower()
      if not follower_success:
        resources = sm_resources.getInstance()
        return resources.get_successful_action_message(self,
        _("Error: Couldn't add follower to reward. No related member defined."), self._name)

  def add_follower_action(self):
    if self.env.context:
      rwds = self.env['sm_rewards.sm_reward'].browse(
        self.env.context['active_ids'])
      if rwds.exists():
        for rwd in rwds:
          if rwd.state == 'member':
            rwd.add_follower()


  # MEMBER COMPUTE
  def _get_existing_related_partner(self):
    h = HTMLParser()
    if self.maintenance_cs_person_index:
      rel_member_q = self.env['res.partner'].sudo().search([('cs_person_index', '=', self.maintenance_cs_person_index)])
      if rel_member_q.exists():
        return rel_member_q[0]
    else:
      if self.data_partner_vat:
        q = str(self.data_partner_vat).replace("-", "").replace(" ", "").upper()
        rel_member_q = self.env['res.partner'].sudo().search([('vat', '=', q)])
        if rel_member_q.exists():
          email_r_member_found = False
          for rmember in rel_member_q:
            if rmember.email == self.data_partner_email:
              return rmember
          return rel_member_q[0]
    return False

  def fetch_user_error_incron(self):
    db_utils = sm_wordpress_db_utils.get_instance()
    if self.external_promo_obj_id:
      db_utils.reactivate_coupon(self)
    self.set_complete_status('soci_not_found')
    sm_utils.send_email_from_template(
      self, 'cs_reward_soci_not_found_email_template_id')


  def fetch_user(self):
    rel_member = self._get_existing_related_partner()
    if rel_member:
      if rel_member.parent_id:
        self.write({
          'related_member_id': rel_member.parent_id.id
        })
      else:
        self.write({
          'related_member_id': rel_member.id
        })
      return True
    return False

  def create_user(self):
    partner_creation_data = {
      'cs_user_type': self.data_partner_cs_user_type,
      'firstname' : self.data_partner_firstname,
      'lastname' : self.data_partner_lastname,
      'vat' : self.data_partner_vat,
      'email' : self.data_partner_email,
      'mobile' : self.data_partner_mobile,
      'phone' : self.data_partner_phone,
      'gender' : self.data_partner_gender,
      'birthdate_date' : self.data_partner_birthdate_date,
      'street' : self.data_partner_street,
      'zip' : self.data_partner_zip,
      'state_id' : self.data_partner_state_id.id,
      'city' : self.data_partner_city,
      'driving_license_expiration_date' : self.data_partner_driving_license_expiration_date,
      'image_dni' : self.data_partner_image_dni,
      'image_driving_license' : self.data_partner_image_driving_license,
      'creation_coupon': self.promo_code
    }
    partner = self.env['res.partner'].create(partner_creation_data)
    partner_bank_creation_data = {
      "acc_number": self.data_partner_iban,
      "acc_type": 'iban',
      "partner_id": partner.id,
    }
    partner_bank = self.env['res.partner.bank'].create(partner_bank_creation_data)
    self.write({
      'related_member_id': partner.id
    })
    return True

  # POCKETBOOK
  def register_new_pocketbook_record_if_must(self):
    if self.reward_addmoney > 0:
      company = self.env.user.company_id
      pb_account = company.reward_account_id.id
      pb_analytic_account = company.reward_analytic_account_id.id
      if self.related_analytic_account_id.id != False:
        pb_analytic_account = self.related_analytic_account_id.id
      # TODO: This naming must go to config table / DB
      pb_record_name = _("Recompensa")
      if self.reward_type == 'promocode':
        pb_record_name = pb_record_name + ": " + self.promo_code
      if self.reward_type == 'fleet_maintenance' and self.related_analytic_account_id:
        pb_record_name = self.related_analytic_account_id.name
        if self.related_analytic_account_id.name == 'Feines tècniques i consultoria':
          pb_record_name = 'Recompensa: Som Mobilitat'
      new_pb_record = self.env['pocketbook.pocketbook_record'].create({
        'name': pb_record_name,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'obs': "reward id: "+ str(self.id),
        'related_member_id': self.related_member_id.id,
        'related_account_id': pb_account,
        'related_analytic_account_id': pb_analytic_account,
        'related_reward_id': self.id
      })
      new_pb_record_history = self.env['pocketbook.pocketbook_record_history'].create({
        'name': _("Reward: ") + self.reward_type,
        'date': datetime.now().strftime("%Y-%m-%d"),
        'amount': self.reward_addmoney / 1.21,
        'related_pb_record_id': new_pb_record.id
      })

  # REGISTRATION REQUEST
  def _create_registration_request(self, group_index,ba_behaviour,ba_credits):
    self.env['sm_partago_user.carsharing_registration_request'].create({
      'related_member_id': self.related_member_id.id,
      'force_registration': self.force_register_cs,
      'group_index': group_index,
      'ba_behaviour': ba_behaviour,
      'ba_credits': ba_credits,
      'related_coupon_index': self.promo_code,
      'related_reward_id': self.id
    })

  # TARIFF
  def must_create_user_tariff(self):
    if self.tariff_name and self.tariff_related_model and self.tariff_type and self.tariff_quantity:
      return True
    return False

  def create_new_user_tariff_if_must(self):
    if self.must_create_user_tariff():
      sys_date = sm_utils.get_today_date()
      related_tariff_model = self.env['smp.sm_carsharing_tariff_model'].search([
        ("name", "=", self.tariff_related_model)
      ])
      if related_tariff_model.exists():
        self.env['smp.sm_carsharing_tariff'].create({
          "name": self.tariff_name,
          "related_member_id": self.related_member_id.id,
          "tariff_model_id": related_tariff_model[0].id,
          "tariff_type": self.tariff_type,
          "pocketbook": self.tariff_quantity,
          "pocketbook_initial": self.tariff_quantity,
          "date": sys_date,
          "date_active": sys_date,
          'related_reward_id': self.id
        })

  # DISCOUNT PARAMS
  def get_reservation_date_discount_params(self):
    date_params = {
      'start_datetime' : datetime.strptime(
        str(self.maintenance_reservation_id.startTime), "%Y-%m-%d %H:%M:%S"),
      'effective_start_datetime': datetime.strptime(
        str(self.maintenance_reservation_id.effectiveStartTime), "%Y-%m-%d %H:%M:%S"),
      'effective_end_datetime': datetime.strptime(
        str(self.maintenance_reservation_id.effectiveEndTime), "%Y-%m-%d %H:%M:%S")
    }
    date_params['effective_end_discount_datetime'] = date_params['effective_end_datetime'] + timedelta(minutes=-1*self.reward_addtime)
    return date_params

  # ACTIONS - COMPLETE
  def complete_reward_progressbar_action(self):
    if self.state == 'follower':
      validation = self._validate_completion()
      if validation['valid']:
        self.complete_reward()
      else:
        resources = sm_resources.getInstance()
        return resources.get_successful_action_message(self,validation['error'], self._name)

  def complete_reward_action(self):
    if self.env.context:
      rwds = self.env['sm_rewards.sm_reward'].browse(
        self.env.context['active_ids'])
      if rwds.exists():
        for rwd in rwds:
          if rwd.state == 'follower':
            validation = rwd._validate_completion()
            if validation['valid']:
              rwd.complete_reward()

  def _validate_completion(self):
    # Rel member
    if self.related_member_id.id == False:
      return {
        'error': _("Error: Not related member for reward."),
        'valid': False
      }
    # Maintenance
    if self.maintenance_create_car_service:
      if not self.maintenance_car_id or not self.maintenance_car_service_id:
        return {
          'error': _("Error: Not enough fields for car service."),
          'valid': False
        }
    # Forgive reservation
    if self.maintenance_forgive_reservation:
      if not self.maintenance_reservation_id:
        return {
          'error': _("Error: No related reservation to forgive."),
          'valid': False
        }
    # Discount reservation
    if self.maintenance_discount_reservation:
      if not self.maintenance_reservation_id or self.reward_addtime == 0 or not self.reward_addtime:
        return {
          'error': _("Error: Trying to discount time in reservation. No reservation or no time to discount."),
          'valid': False
        }
      else:
        date_params = self.get_reservation_date_discount_params()
        if date_params['effective_end_discount_datetime'] < date_params['effective_start_datetime'] or \
          date_params['effective_end_discount_datetime'] < date_params['start_datetime']:
            return {
              'error': _("Error: Too much discount for reservation. Reservation would end before it starts."),
              'valid': False
            }
    # Reward for company users
    if self.related_member_id.cs_user_type == 'organisation' and self.related_member_id.parent_id.id == False:
      return {
        'error': _("Error: Company not found for company user."),
        'valid': False
      }
    # Apply reward to blocked user not possible
    if self.related_member_id.cs_state == 'blocked_banned':
      return {
        'error': _("Cannot apply reward to a manually banned user."),
        'valid': False
      }
    # Analytic accounting
    if not self.related_analytic_account_id:
      return {
        'error': _("Error: No analytic account."),
        'valid': False
      }
    # 200 OK
    return {
      'valid': True
    }

  def set_complete_status(self, final_state='reward_completed'):
    self.write({
      'state': 'complete',
      'final_state': final_state,
      'completed': datetime.now()
    })

  def complete_reward(self):
    if self.final_state == "not_completed":
      # CREATE SERVICE
      if self.maintenance_create_car_service:
        if self.reward_date:
          rd = self.reward_date
        else:
          rd = datetime.now()
        self.env['fleet.vehicle.log.services'].create({
          'vehicle_id': self.maintenance_car_id.id,
          'cost_subtype_id': self.maintenance_car_service_id.id,
          'amount': float(self.reward_addmoney),
          'date': rd,
          'related_reward_id': self.id,
          'related_member_id': self.related_member_id.id
        })

      # FORGIVE RESERVATION
      if self.maintenance_forgive_reservation:
        self.maintenance_reservation_id.write({
          'compute_forgiven': True
        })

      # DISCOUNT RESERVATION
      if self.maintenance_discount_reservation:
        date_params = self.get_reservation_date_discount_params()
        self.maintenance_reservation_id.write({
          'effectiveEndTime': str(date_params['effective_end_discount_datetime']),
          'ignore_update': True
        })

      # COMPUTE REWARD
      # 2.- Setup ba_behaviour
      if self.force_dedicated_ba:
        # 2.1.- dedicated ba
        ba_behaviour = 'dedicated_ba'
      else:
        # 2.2.- cs (promo) users
        if self.related_member_id.cs_user_type == 'promo':
          ba_behaviour = 'update_ba'
        # 2.3.- Regular users and maintenance (pb records and tariffs)
        else:
          self.register_new_pocketbook_record_if_must()
          self.create_new_user_tariff_if_must()
          ba_behaviour = 'no_ba'

      # 3.- CS Registration request
      if self.related_member_id.company_type == 'person':
        self._create_registration_request(
          self.coupon_group,
          ba_behaviour,
          self.reward_addtime
        )
        if self.coupon_group_secondary:
          if self.coupon_group_secondary != '':
            # TODO: We impose secondary group for dedicated_ba enters in normal payment group (no promo) need to make this dynamic
            if ba_behaviour == 'dedicated_ba':
              ba_behaviour = 'no_ba'
            self._create_registration_request(
              self.coupon_group_secondary,
              ba_behaviour,
              0
            )
      # 4.- Notification
      if self.reward_addmoney > 0 or self.reward_addtime > 0:
        if self.reward_type == 'promocode':
          # TODO: This must be a configuration field on the model (send_completed_email_to_user)
          if self.reward_info != 'promo Montepio':
            sm_utils.send_email_from_template(self, 'cs_reward_completed_email_template_id')

      self.set_complete_status('reward_completed')
