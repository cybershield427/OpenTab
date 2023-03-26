import sqlite3


class Database:
	def __init__(self):
		self.db_name = "opentab_user.db"
		self.connection = sqlite3.connect(self.db_name)
		self.cursor = self.connection.cursor()

	def create_table(self):
		self.cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS users (
				username TEXT PRIMARY KEY, 
				password TEXT
			)
			"""
		)
		self.connection.commit()

	def insert_user(self, username, password):
		self.cursor.execute(
			"""
			INSERT INTO users (username, password)
			VALUES (?,?)
			""",
			(username, password)
		)
		self.connection.commit()

	def get_user(self, username, password):
		self.cursor.execute(
			"""
			SELECT * FROM users WHERE username = ? AND password = ?
			""",
			(username, password)
		)
		return self.cursor.fetchone()

	def close_connection(self):
		self.connection.close()
