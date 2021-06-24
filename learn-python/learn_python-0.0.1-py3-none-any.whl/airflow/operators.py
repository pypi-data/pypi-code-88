from datetime import datetime, timedelta

from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow import DAG

default_args = {
    'owner': 'massi',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 26),
    'email': ['massipssa.kerrache@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(default_args) as default_args:
    mysql_task = MySqlOperator(
        task_id="create_table_mysql",
        sql="/scripts/sql/create_mysql_table.sql",
        mysql_conn_id="mysql_cnx"
    )
    postgres_table = PostgresOperator(
        task_id="create_table_postgres",
        sql="/scripts/sql/create_postgres_table.sql",
        mysql_conn_id="postgres_cnx"
    )

    mysql_task >> postgres_table
