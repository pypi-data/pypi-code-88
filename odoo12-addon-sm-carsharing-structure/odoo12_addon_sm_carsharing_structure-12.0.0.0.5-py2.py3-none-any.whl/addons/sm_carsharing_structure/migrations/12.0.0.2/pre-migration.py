# Copyright 2019 Eficent <http://www.eficent.com>
# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade
from psycopg2 import sql

def cs_car_fill_analytic_account(cr):
  openupgrade.logged_query(
    cr, """
    ALTER TABLE
      fleet_vehicle 
    ADD
      analytic_account_id integer
    """
  )

  openupgrade.logged_query(
    cr, """
    UPDATE 
      fleet_vehicle fv 
    SET
      analytic_account_id = p.analytic_account_id
    FROM 
      project_project p
    WHERE 
      fv.project_id = p.id
    """
  )

@openupgrade.migrate()
def migrate(env, version):
  cr = env.cr
  cs_car_fill_analytic_account(cr)
  