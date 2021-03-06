# -*- coding: utf-8 -*-

import util

# テーブル「j_histories」クラス
class DaoJHistories:
	# 初期化
	def __init__(self):
		self.sql = ""

	# SQLを作成(IDの最大値を取得)
	def make_sql_select_max_id(self):
		self.sql = "select COALESCE(max(id), 0) from j_histories"

	# SQLを作成(追加)
	def make_sql_insert(self):
		self.sql = u'''
insert into j_histories(
	id
	, process_start
	, process_end
	, process_seconds
	, count_tenders
)
values(
	(select COALESCE(max(id), 0) from j_histories) + 1
	, %s
	, %s
	, %s
	, %s
)
'''

	# SQLを取得
	def get_sql(self):
		return  util.clean_string(self.sql)

	# SQLを実行
	# param: connection
	# param: cursol
	# param: params(配列)
	def exec_sql_params(self, conn, cur, params):
		cur.execute(self.sql, params)
		conn.commit()

# テスト用
if __name__ == '__main__':
	import logger

	import datetime

	# 処理開始日時
	process_start = datetime.datetime.today()

	import time
	time.sleep(3)

	# 処理終了日時
	process_end = datetime.datetime.today()

	# 処理時間
	process_seconds = (process_end - process_start).seconds

	# 案件件数
	count_tenders = 15

	print(process_start)
	print(process_end)
	print(process_seconds)
	print(count_tenders)

	import dao_pg_connection
	pg_con = dao_pg_connection.PgConnection()
	pg_con.set_pg_connection_open();
	connection = pg_con.get_pg_connection()
	cursor = connection.cursor()

	dao_j_histories = DaoJHistories()

	dao_j_histories.make_sql_insert()
	print(dao_j_histories.get_sql())

	params = []
	params.append(process_start)
	params.append(process_end)
	params.append(process_seconds)
	params.append(count_tenders)

	dao_j_histories.exec_sql_params(connection, cursor, params)

	pg_con.set_pg_connection_close(cursor)
