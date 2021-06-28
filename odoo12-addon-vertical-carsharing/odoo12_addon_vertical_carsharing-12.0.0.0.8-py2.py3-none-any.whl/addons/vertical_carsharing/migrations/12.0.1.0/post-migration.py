# Copyright 2019 Eficent <http://www.eficent.com>
# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade
from psycopg2.extensions import AsIs

def fill_partners_mobile(cr):
  openupgrade.logged_query(
    cr, """
    UPDATE res_partner
    SET
        mobile = phone
    WHERE
        mobile IS NULL
    """
  )

def fill_partners_phone(cr):
  openupgrade.logged_query(
    cr, """
    UPDATE res_partner
    SET
        phone = phone_2
    WHERE
        phone_2 IS NOT NULL
    """
  )

def fill_partners_vat(cr):
  openupgrade.logged_query(
    cr, """
    UPDATE res_partner
    SET
        vat = cif
    WHERE
        ((vat = '') AND (cif != '')) OR ((vat IS NULL) AND (cif IS NOT NULL))
    """
  )
  openupgrade.logged_query(
    cr, """
    UPDATE res_partner
    SET
        vat = dni
    WHERE
        ((vat = '') AND (dni != '')) OR ((vat IS NULL) AND (dni IS NOT NULL))
    """
  )

def cleanup_system_name(env):
  coop_members = env['res.partner'].search([])
  if coop_members.exists():
    print("*\n**\n***\n****\n*****\n******\nFOUND COOP MEMBERS")
    print(coop_members[1])
    print("*\n**\n***\n****\n*****\n******\nFOUND COOP MEMBERS")

@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    fill_partners_mobile(cr)
    fill_partners_phone(cr)
    fill_partners_vat(cr)
    cleanup_system_name(env)

