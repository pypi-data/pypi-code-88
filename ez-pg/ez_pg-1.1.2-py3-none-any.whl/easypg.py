import psycopg2
from psycopg2 import sql
from psycopg2 import extras
import re
import json

class dbActions:
	def __init__(self, database, username, password=None, **kwargs):
		self.conn = psycopg2.connect(dbname=database, user=username, password=None, cursor_factory=extras.RealDictCursor, **kwargs)
		self.cur = self.conn.cursor()
		return
	def __enter__(self):
		return self
	def __exit__(self):
		return self

	#**kwargs gives availibilty to add different sql args in the order of execution
	#ie select(table, limit='5') will execute:
	#         select * from table limit 5
	#   select(table2, [column1, column2], left_outer_join='table1 on table1.id = table2.id', limit='100') will execute:
	#         select column1, column2 from table2 left outer join table1 on table1.id = table2.id limit 100

	def cte(self, table, columns="*", **kwargs):
		#{alias1:{table:table1, columns:[column1, column2, column3], where}}
		statement = sql.SQL("Select {} from {} {}").format(sql.SQL(', '.join(f'{c}' for c in columns)), sql.SQL(table), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items())))
		return statement.as_string(self.conn)
			
	def select(self, table, columns="*", cte=None, **kwargs):
		if cte:
			cte_statement = sql.SQL('WITH {}').format(sql.SQL(', '.join(f'{k} as ({v})' for k,v in cte.items())))
		else:
			cte_statement = sql.SQL('')

		self.cur.execute(sql.SQL("{} Select {} from {} {};").format(cte_statement ,sql.SQL(', '.join(f'{c}' for c in columns)), sql.SQL(table), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))))
		
		self.results = self.cur.fetchall()
		return self.results

	def insert(self, table, values, **kwargs):
		self.query = self.cur.execute(sql.SQL("INSERT into {} ({}) values ({}) {};").format(sql.Identifier(table), sql.SQL(', ').join(map(sql.Identifier, values)), sql.SQL(', ').join(map(sql.Placeholder, values)), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))), values)
		self.conn.commit()
		#will return nothing if there was a conflict
		self.results = self.cur.fetchall()
		return self.results

	def update(self, table, updates, **kwargs):
		self.query = self.cur.execute(sql.SQL("Update {} set {} {};").format(sql.Identifier(table), sql.SQL(', ').join(sql.Composed([sql.Identifier(k), sql.SQL('='), sql.Placeholder(k)]) for k in updates.keys()), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))), updates)
		self.conn.commit()
		return self.cur.rowcount

	def delete(self, table, **kwargs):
		self.query = self.cur.execute(sql.SQL("DELETE from {} {};").format(sql.Identifier(table), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))))
		self.conn.commit()
		return self.cur.rowcount

	def create_db(self, name, **kwargs):
		self.conn.set_session(autocommit=True)
		try:
			self.query = self.cur.execute(sql.SQL("CREATE DATABASE {} {};").format(sql.SQL(name), sql.Identifier(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))))
			self.results = f'Database {name} successfully created!'
		except Exception as e:
			self.results = f'Error creating database:{e}'
		return self.results

	def create_table(self, name, table_args, *args, **kwargs):
		try:
			self.query = self.cur.execute(sql.SQL("CREATE {} TABLE {}({}) {}").format(sql.SQL(' '.join(f'{a}' for a in args)), sql.SQL(name), sql.SQL(', ').join(sql.Composed([sql.SQL(key), sql.SQL(' '), sql.SQL(values['type']), sql.SQL(' '), sql.SQL(values.get('constraint', ''))]) for key, values in table_args.items()), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))))
			self.results = f'Created table {name} with columns: {table_args}'
			self.conn.commit()
		except Exception as e:
			self.results = f'Error creating table: {e}'
		return self.results
	
	def drop(self, obj, name, **kwargs):
		try:
			self.query = self.cur.execute(sql.SQL("DROP {} {}").format(sql.SQL(obj), sql.SQL(name), sql.SQL(' '.join(f'{k.replace("_", " ")} {v}' for k, v in kwargs.items()))))
			self.results = f'Successfully dropped {obj} of {name}'
			self.conn.commit()
		except Exception as e:
			self.results = f'Error Dropping {obj} of {name}: {e}'
		return self.results