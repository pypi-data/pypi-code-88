# -*- coding: utf-8 -*-

import re
import time
import os
import json
from html.parser import HTMLParser
from datetime import datetime
import hashlib

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.addons.sm_maintenance.models.models_load_data import load_data
from odoo.addons.sm_connect.models.credential_loader import credential_loader
from odoo.addons.sm_connect.models.models_sm_carsharing_api_utils import sm_carsharing_api_utils
from odoo.addons.sm_connect.models.models_sm_carsharing_db_utils import sm_carsharing_db_utils
from odoo.addons.sm_connect.models.models_sm_wordpress_db_utils import sm_wordpress_db_utils
from odoo.addons.sm_partago_db.models.models_smp_db_utils import smp_db_utils
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils
from odoo.addons.sm_maintenance.models.models_sm_resources import sm_resources

class partago_user(models.Model):
  _user_config = load_data.get_instance().get_user_config()
  _inherit = 'res.partner'
  _name = 'res.partner'

  _resources = sm_resources.getInstance()

  cs_person_index = fields.Char(string=_("Carsharing person index"))

  cs_registration_completed_date = fields.Date(
    string=_("Carsharing registration completed date"))
  cs_firebase_uid = fields.Char(string=_("UID"))
  cs_data_ok = fields.Boolean(
    string=_("CS registration attemp user data ok"), compute="_get_cs_data_ok", store=False)
  cs_registration_info_ok = fields.Boolean(
    string=_("CS registration complete info ok"),compute="_get_cs_registration_info_ok",store=True)
  cs_registration_coupon = fields.Char(string=_("Registration coupon for team members"))

  cs_state = fields.Selection([
    ('only_exists_on_db','Person created on APP (nothing more)'),
    ('requested_access', 'Access request sent'),
    ('active', 'Active'),
    ('blocked_banned', 'Manually Blocked'),
    ('no_access', 'No access')
  ], default='no_access', string=_("Carsharing user status"))

  cs_user_type = fields.Selection([
    ('none','None'),
    ('user', 'Regular user'),
    ('promo', 'Promo user'),
    ('maintenance', 'Maintenance user'),
    ('organisation', 'Organisation user')
  ], default='none', string=_("Carsharing user type"))

  registration_link = fields.Char(string=_("Registration link"))

  cs_member_group_ids = fields.One2many(comodel_name='sm_partago_user.carsharing_member_group',
    inverse_name='related_member_id', string=_("CS Groups"))

  cs_registration_request_ids = fields.One2many(comodel_name='sm_partago_user.carsharing_registration_request',
    inverse_name='related_member_id', string=_("CS registration requests"))

  #
  # CS REGISTRATION
  #
  def exists_on_app_db(self):
    if self.cs_state == 'requested_access' \
      or self.cs_state == 'active' \
      or self.cs_state == 'only_exists_on_db':
      return True
    return False

  # Sends the registration email trough the APP
  # This methods returns an error if occurs
  def compute_send_app_registration_email(self):
    if self.cs_person_index and self.cs_person_index != '':
      api_utils = sm_carsharing_api_utils.get_instance()
      r = api_utils.post_persons_send_registration_email(
        self.cs_person_index,
        self.get_cs_lang()
      )
      if r.status_code != 200:
        return ("""API ERROR:
          Send APP registration email returned != 200.
          Member id: %s""") % (str(self.id))
      else:
        self._compute_registration_link()
        return False
    else:
      return ("""USER DATA ERROR:
          Send APP registration email cannot be sent if user has no cs_index
          Member id: %s""") % (str(self.id))

    # TODO: API must return regKey so we can do this via API
  def _compute_registration_link(self):
    credentials_load = credential_loader.get_instance()
    api_credentials = credentials_load.get_carsharing_api_credentials()
    # company_cs_url = self.env.user.company_id.cs_url
    db_utils = sm_carsharing_db_utils.get_instance()
    existing_person = db_utils.firebase_get(
      'persons', self.cs_person_index)
    try:
      registration_key = existing_person['registrationKey']
    except:
      registration_key = False
    if registration_key:
      computed_link = api_credentials["cs_url"] + "/reservatie/?regkey=" + registration_key
      self.write({
        'registration_link': computed_link
      })

  #
  # CS STATUS
  @api.depends('cs_state')
  def _get_cs_data_ok(self):
    for record in self:
      record.cs_data_ok = record.verify_cs_data_fields()

  @api.depends('cs_state','cs_registration_completed_date','cs_person_index','cs_firebase_uid')
  def _get_cs_registration_info_ok(self):
    for record in self:
      if record.exists_on_app_db() and record.cs_registration_completed_date and record.cs_firebase_uid \
        and record.cs_person_index:
          record.cs_registration_info_ok = True
      else:
        record.cs_registration_info_ok = False

  def verify_cs_data_fields(self):
    if not self.firstname:
      return False
    if not self.vat:
      return False
    if not self.image_dni:
      return False
    if not self.email:
      return False
    if not self.mobile:
      return False
    if not self.birthdate_date:
      return False
    if not self.driving_license_expiration_date:
      return False
    if not self.image_driving_license:
      return False
    return True

  def is_cs_person_requested(self):
    if self.cs_state == 'requested_access' or self.cs_state == 'requested_access_second_notification':
      return True
    return False

  def recompute_cs_registration_info(self):
    db_utils = sm_carsharing_db_utils.get_instance()
    firebase_uid = db_utils.get_uid_from_email(self.email)
    if firebase_uid:
      self.write({'cs_firebase_uid':firebase_uid})
      if self.cs_state in ['only_exists_on_db','requested_access']:
        self.write({
          'cs_registration_completed_date': datetime.now(),
          'cs_state': 'active'
        })

  #
  # GETTERS
  #
  def get_app_person_details(self):
    app_db_utils = smp_db_utils.get_instance()
    return app_db_utils.get_app_person_details(self.cs_person_index)

  def get_app_person_groups(self):
    app_db_utils = smp_db_utils.get_instance()
    return app_db_utils.get_app_person_groups(self.cs_person_index)

  def get_member_data_for_app(self):
    member_data = {}
    if self.company_type == 'person':
      firstname = self.firstname
      lastname = self.lastname
    else:
      firstname = self.name
      lastname = ""
    if not firstname:
      firstname = ""
    if not lastname:
      lastname = ""
    member_data["firstname"] = firstname
    member_data["lastname"] = lastname
    #email
    member_data["email"] = self.email
    if not member_data["email"]:
      member_data["email"] = ""
    # address
    city = self.city
    if not city:
      city = ""
    postalCode = self.zip
    if not postalCode:
      postalCode = ""
    street = self.street
    if not street:
      street = ""
    member_data["address"] = {
      'city': city,
      'postalCode': postalCode,
      'street': street
    }
    #phone
    main_phone = self.phone
    if not main_phone:
      main_phone = ""
    member_data["phones"] = {"main": main_phone}
    #DNI
    member_data["nationalIdentificationNumber"] = self.vat
    if not member_data["nationalIdentificationNumber"]:
      member_data["nationalIdentificationNumber"] = ""
    # lang
    member_data["preferredLanguage"] = self.get_cs_lang()
    if not member_data["preferredLanguage"]:
      member_data["preferredLanguage"] = "ca"
    return member_data

  @api.model
  def get_registration_view(self):
    view_ref = self.env['ir.ui.view'].sudo().search(
      [('name', '=', 'partago_user.carsharing_registration_wizard.form')])
    return view_ref.id

  def get_cs_lang(self):
    if self.lang:
      member_language = self.lang.split("_")
      if member_language in self._user_config['allowed_user_langs'].values():
        return member_language
    return self._user_config['default_language']
    # return "ca"

  #
  # REGISTRATION COUPON (COMPANIES)
  #
  def set_registration_coupon(self):
    db_utils = sm_wordpress_db_utils.get_instance()
    if not self.is_company:
      return
    mcargs = {
      'post_type': 'sm_coupon',
      'orderby': 'ID',
      'order': 'DESC'
    }
    # get pages in batches of 20
    offset = 0
    increment = 100
    coupon_found = False
    while coupon_found == False:
      mcargs['number'] = increment
      mcargs['offset'] = offset
      member_coupons = db_utils.get_posts(mcargs)
      if len(member_coupons) == 0:
        break  # no more posts returned
      for coupon in member_coupons:
        for custom_field in coupon.custom_fields:
          if custom_field['key'] == 'coupon_related_company_cif':
            if custom_field['value']:
              if custom_field['value'].upper().strip() == self.vat.upper().strip():
                self.write({'cs_registration_coupon': coupon})
                coupon_found = True
                break
      offset = offset + increment
    return coupon_found

  #
  # CS GROUPS
  #
  def set_carsharing_groups(self):
    cs_person_groups = self.get_app_person_groups()
    if cs_person_groups:
      self._set_carsharing_groups_from_data(cs_person_groups)
    else:
      self._remove_all_carsharing_groups()

  def _set_carsharing_groups_from_data(self,current_cs_groups):
    self._create_update_current_cs_groups( current_cs_groups )
    self._clean_non_existing_cs_groups( current_cs_groups )

  def _create_update_current_cs_groups(self,current_cs_groups):
    for group_name in current_cs_groups.keys():
      db_group = self.env['smp.sm_group'].search([('name','=',group_name)])
      if db_group.exists():
        update_data = self._prepare_cs_group_data(db_group[0],current_cs_groups[group_name])
        cs_member_group = self.env['sm_partago_user.carsharing_member_group'].search([
          ('related_member_id','=',self.id),
          ('related_group_id','=',db_group[0].id)
        ])
        if cs_member_group.exists():
          cs_member_group[0].write( update_data ) # update
        else:
          new_cs_group = self.env['sm_partago_user.carsharing_member_group'].create(update_data)

  def _clean_non_existing_cs_groups(self,current_cs_groups):
    if self.cs_member_group_ids:
      for cs_member_group in self.cs_member_group_ids:
        delete_group = True
        if cs_member_group.related_group_id:
          if cs_member_group.related_group_id.name in current_cs_groups.keys():
            delete_group = False
        if delete_group:
            cs_member_group.unlink()

  def _remove_all_carsharing_groups(self):
    if self.cs_member_group_ids:
      for cs_member_group in self.cs_member_group_ids:
        cs_member_group.unlink()

  def _prepare_cs_group_data(self,db_group,current_cs_group):
    app_db_utils = smp_db_utils.get_instance()
    data = {
      'related_member_id': self.id,
      'related_group_id': db_group.id
    }

    data['role'] = ''
    if 'role' in current_cs_group.keys():
      if current_cs_group['role'] is not None:
        data['role'] = current_cs_group['role']

    data['admin_role'] = ''
    if 'adminRole' in current_cs_group.keys():
      if current_cs_group['adminRole'] is not None:
        data['admin_role'] = current_cs_group['adminRole']

    data['related_billingaccount_id'] = False
    if 'billingAccount' in current_cs_group.keys():
      if current_cs_group['billingAccount']:
        app_db_utils.update_system_ba_from_app_ba(self,current_cs_group['billingAccount'])
      db_ba = self.env['smp.sm_billing_account'].search([('name','=',current_cs_group['billingAccount'])])
      if db_ba.exists():
        data['related_billingaccount_id'] = db_ba[0].id

    return data

  #
  # UI ACTIONS
  #
  @api.model
  def recompute_member_cs_registration_info_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            member.recompute_cs_registration_info()

  @api.multi
  def set_registration_coupon_from_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            if member.vat:
              member.set_registration_coupon()
    return

  @api.model
  def get_carsharing_groups_action(self):
    app_db_utils = smp_db_utils.get_instance()
    app_db_utils.update_all_system_db_data_from_app_db(self)
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            member.set_carsharing_groups()

  @api.model
  def recompute_registration_emaillink_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            error = member.compute_send_app_registration_email()
            if error:
              return self._resources.get_successful_action_message(self,error, self._name)
            else:
              member.write({
                'cs_state' : 'requested_access'
              })
              return self._resources.get_successful_action_message(self,_("Action: OK"), self._name)

  @api.model
  def complete_registration_requests_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            if member.cs_registration_request_ids:
              for registration_request in member.cs_registration_request_ids:
                if registration_request.completed_behaviour == 'not_computed':
                  registration_request.compute_request()


  @api.model
  def get_register_in_carsharing_view_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            data = {'current_member': member.id}
            return {
              'type': 'ir.actions.act_window',
              'name': "Register in carsharings",
              'res_model': 'partago_user.sm_carsharing_registration_wizard',
              'view_type': 'form',
              'view_mode': 'form',
              'res_id': self.env['partago_user.sm_carsharing_registration_wizard'].create(data).id,
              'view_id': self.get_registration_view(),
              'target': 'new'
            }

  @api.model
  def resend_register_email_action(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        members = self.env['res.partner'].browse(
          self.env.context['active_ids'])
        if members.exists():
          for member in members:
            if member.is_company:
              if not member.cs_registration_coupon:
                success = member.set_registration_coupon()
              if success:
                try:
                  sm_utils.send_email_from_template(member, 'cs_company_access_already_requested')
                  return self._resources.get_successful_action_message(self,
                    _("Registration company email correctly sent"), self._name)
                except:
                  return self._resources.get_successful_action_message(self,
                    _("ERROR! There was a problem re-sending cs registration link"), self._name)
              else:
                return self._resources.get_successful_action_message(self,
                  _("Company coupon not found on wordpress. Email not sent."), self._name)
            else:
              if member.registration_link:
                try:
                  sm_utils.send_email_from_template(member, 'cs_already_requested_access')
                  return self._resources.get_successful_action_message(self,
                    _("Registration email correctly sent"), self._name)
                except:
                  return self._resources.get_successful_action_message(self,
                    _("ERROR! There was a problem re-sending cs registration link"), self._name)
              else:
                return self._resources.get_successful_action_message(self,
                  _("ERROR! Registration link not found. Email not sent."), self._name)

  # TODO: This doesn't work because of duplicate action. Find workaround
  #@api.constrains('cs_person_index')
  #def _check_cs_person_index_unique(self):
  #  if self.cs_person_index:
  #    cspi_found = self.env['res.partner'].search(
  #      [('id', '!=', self.id), ('cs_person_index', '=', self.cs_person_index)])
  #    if cspi_found.exists():
  #      raise ValidationError(
  #        _("Carsharing person index must be unique. There is another record with this one."))