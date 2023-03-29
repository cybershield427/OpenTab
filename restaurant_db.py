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
				table_number TEXT PRIMARY KEY, 
				customer_name TEXT,
				phone TEXT,
				credit_card TEXT,
				attendant TEXT
			)
			"""
		)
		self.connection.commit()

	def insert_customer(self, table_number, customer_name, phone, credit_card, attendant):
		self.cursor.execute(
			"""
			INSERT INTO customers (table_number, customer_name, phone, credit_card, attendant)
			VALUES (?,?,?,?,?)
			""",
			(table_number, customer_name, phone, credit_card, attendant)
		)
		self.connection.commit()

	def get_customer(self, table_number):
		self.cursor.execute(
			"""
			SELECT * FROM customers WHERE table_number = ?
			""",
			(table_number,)
		)
		return self.cursor.fetchone()

	def close_connection(self):
		self.connection.close()
