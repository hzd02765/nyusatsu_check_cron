# -*- coding: utf-8 -*-

import sys
import psycopg2
import datetime

import config
import logger

# connectionクラス
class PgConnection:

	# 初期化
	def __init__(self):
		self.conn = None

	# PostgreSQL接続開始
	def set_pg_connection_open(self):
		db_name = config.DB_NAME
		db_user = config.DB_USER
		db_pass = config.DB_PASSWORD
		db_host = config.DB_HOST

		try:
			self.conn = psycopg2.connect("dbname='" + db_name + "' user='" + db_user + "' password='" + db_pass + "' host='" + db_host + "'")
			return True
		except:
			print("dbname='" + db_name + "' user='" + db_user + "' password='" + db_pass + "' host='" + db_host + "'")
			return False

	# connectionの取得
	def get_pg_connection(self):
		return self.conn

	# PostgreSQL接続終了
	def set_pg_connection_close(self, cur):
		cur.close()
		self.conn.close()

# テスト用
if __name__ == '__main__':
	file_name = "access_log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
	logger = logger.Logger(file_name)
	# print(logger.file_path)

	pg_connection = PgConnection()
	pg_connection.set_pg_connection_open(logger)
	connectin = pg_connection.get_pg_connection()
	cursor = connectin.cursor()
	pg_connection.set_pg_connection_close(cursor, logger)

	logger.print_log()
