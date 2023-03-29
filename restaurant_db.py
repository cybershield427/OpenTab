import sqlite3


class Database:
	def __init__(self):
		self.db_name = "restaurant.db"
		self.connection = sqlite3.connect(self.db_name)
		self.cursor = self.connection.cursor()

	def create_table(self):
		self.cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS customers (
				name TEXT PRIMARY KEY, 
				credit_card TEXT,
				table_number TEXT,
				phone TEXT
			)
			"""
		)
		self.connection.commit()

	def insert_customer(self, name, credit_card, table_number, phone):
		self.cursor.execute(
			"""
			INSERT INTO users (name, credit_card, table_number, phone)
			VALUES (?,?,?,?,?)
			""",
			(name, credit_card, table_number, phone)
		)
		self.connection.commit()

	def get_customer(self, name):
		self.cursor.execute(
			"""
			SELECT * FROM customers WHERE name = ?
			""",
			(name)
		)
		return self.cursor.fetchone()

	def close_connection(self):
		self.connection.close()
