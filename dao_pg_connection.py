# -*- coding: utf-8 -*-

import sys
# import util
import psycopg2
import datetime

import config
import logger

# def get_connection():
	# conn = None
	# try:
		# conn = psycopg2.connect("dbname='nyusatsu_check' user='nyusatsu_check' password='nyusatsu_check' host='localhost'")
		# util.print_log('DB Connection Success')
	# except:
		# util.print_log( "DB Connection failure")
		# sys.exit()
	# return conn
	
# def set_close_connection(conn, cur):
	# cur.close()
	# conn.close()
	# util.print_log('DB Connection Close')


	
class PgConnection:
	
	def __init__(self):
		self.conn = None
	
	# PostgreSQL接続開始
	def set_pg_connection_open(self):
		try:
			self.conn = psycopg2.connect("dbname='" + config.DB_NAME + "' user='" + config.DB_USER + "' password='" + config.DB_PASSWORD + "' host='" + config.DB_HOST + "'")
			# print('DB Connection Success')
			# logger.set_log('DB Connection Success')
			return True
		except:
			# print( "DB Connection failure")
			# logger.set_log('DB Connection failure')
			# sys.exit()
			print("dbname='" + config.DB_NAME + "' user='" + config.DB_USER + "' password='" + config.DB_PASSWORD + "' host='" + config.DB_HOST + "'")
			return False
		
	def get_pg_connection(self):
		return self.conn
	
	# PostgreSQL接続終了
	def set_pg_connection_close(self, cur):
		cur.close()
		self.conn.close()
		# print('DB Connection Close')
		# logger.set_log('DB Connection Close')
		
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
