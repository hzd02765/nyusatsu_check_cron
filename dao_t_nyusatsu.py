# -*- coding: utf-8 -*-

# テーブル「t_nyusatsu」クラス
class DaoTNyusatsu:
	# 初期化
	def __init__(self):
		self.sql = ""

	# SQL作成(削除)
	def make_sql_delete(self):
		self.sql = u"delete from t_nyusatsu"

	# SQL作成(IDの最大値を取得)
	def make_sql_select_max_id(self):
		self.sql = u"select max(id) from t_nyusatsu"

	# SQLの作成(追加)
	def make_sql_insert(self):
		self.sql = u'''
insert into t_nyusatsu(
	id,
	nyusatsu_system,
	nyusatsu_type,
	anken_no,
	anken_url,
	anken_name,
	keishu_cd,
	keishu_name,
	public_flag,
	company_area,
	anken_open_date,
	anken_close_date,
	tender_date,
	tender_place,
	limit_date,
	gyoumu_kbn_1,
	gyoumu_kbn_2,
	kasitu_name,
	tanto_name,
	notes,
	result_open_date,
	result_close_date,
	raku_name,
	price,
	version_no,
	delete_flag,
	ins_date,
	upd_date
)
values(
	%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0,0,now(),now()
)

'''

	# SQLの取得
	def get_sql(self):
		return self.sql

	# SQLの実行
	# @param: connection
	# @param: cursol
	# @return: cursol
	def exec_sql(self, conn, cur):
		cur.execute(self.sql)
		conn.commit()
		return cur

	# SQLの実行
	# @param: connection
	# @param: cursol
	# @param: params
	def exec_sql_params(self, conn, cur, params):
		cur.execute(self.sql, params)
		conn.commit()

# テスト用
if __name__ == '__main__':

	# ロガー作成
	import datetime
	import logger
	file_name = "access_log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
	logger = logger.Logger(file_name)

	# pg_connectin 作成
	import dao_pg_connection
	pg_connection = dao_pg_connection.PgConnection()
	pg_connection.set_pg_connection_open(logger)
	connection = pg_connection.get_pg_connection()
	cursor = connection.cursor()

	# インスタンス生成
	dao_t_nyusatsu = DaoTNyusatsu()

	# テーブルの初期化SQL　生成
	dao_t_nyusatsu.make_sql_delete()

	# sqlをlogに書き出す
	logger.set_log(dao_t_nyusatsu.get_sql())

	# sql実行
	cursor = dao_t_nyusatsu.exec_sql(connection, cursor)

	# Max_id取得用SQL 生成
	dao_t_nyusatsu.make_sql_select_max_id()

	# sqlをlogに書き出す
	logger.set_log(dao_t_nyusatsu.get_sql())

	# sql実行
	cursor = dao_t_nyusatsu.exec_sql(connection, cursor)
	record =  cursor.fetchone()
	max_id = record[0]
	if max_id == None:
		max_id = 0
	print(max_id)

	# insert用SQL 生成
	dao_t_nyusatsu.make_sql_insert()

	# sqlをlogに書き出す
	logger.set_log(dao_t_nyusatsu.get_sql())

	# パラメータ作成
	import dao_anken
	anken = dao_anken.ClassAnken()

	anken.id = max_id + 1
	anken.nyusatsu_system = "1"
	anken.nyusatsu_type = "1"
	anken.anken_no = "560700-H2503081217-21"
	anken.anken_url = "http://wave.pref.wakayama.lg.jp/ekimu2/disp_easy_end.php?AnkNo=560700-H2503081217-21"
	anken.anken_name = "平成２５年度　和歌山県立たちばな支援学校　貯水槽衛生管理等業務"
	anken.keishu_cd = "2"
	anken.keishu_name = "簡易公開調達　終了分"
	anken.public_flag = "1"
	anken.company_area = "全域（県内本店）"
	anken.anken_open_date = "2013-03-11 09:00:00"
	anken.anken_close_date = "2013-03-18 16:00:00"
	anken.tender_date = "2013-03-18 16:00:00"
	anken.tender_place = "和歌山県立たちばな支援学校　事務室"
	anken.limit_date = "2014-03-31 00:00:00"
	anken.gyoumu_kbn_1 = "建築物の保守管理"
	anken.gyoumu_kbn_2 = "建築物飲料水貯水槽清掃"
	anken.kasitu_name = "和歌山県立たちばな支援学校"
	anken.tanto_name = "池側　良彦・０７３７－６２－３５９９"
	anken.notes = ""
	anken.result_open_date = "2013-03-19 12:00:00"
	anken.result_close_date = "2013-04-19 12:00:00"
	anken.raku_name = "有限会社　大都環境サービス"
	anken.price = "96,600"

	sql_params = []
	sql_params.append(anken.id)
	sql_params.append(anken.nyusatsu_system)
	sql_params.append(anken.nyusatsu_type)
	sql_params.append(anken.anken_no)
	sql_params.append(anken.anken_url)
	sql_params.append(anken.anken_name)
	sql_params.append(anken.keishu_cd)
	sql_params.append(anken.keishu_name)
	sql_params.append(anken.public_flag)
	sql_params.append(anken.company_area)
	sql_params.append(anken.anken_open_date)
	sql_params.append(anken.anken_close_date)
	sql_params.append(anken.tender_date)
	sql_params.append(anken.tender_place)
	sql_params.append(anken.limit_date)
	sql_params.append(anken.gyoumu_kbn_1)
	sql_params.append(anken.gyoumu_kbn_2)
	sql_params.append(anken.kasitu_name)
	sql_params.append(anken.tanto_name)
	sql_params.append(anken.notes)
	sql_params.append(anken.result_open_date)
	sql_params.append(anken.result_close_date)
	sql_params.append(anken.raku_name)
	sql_params.append(anken.price)

	# sql実行(引数にパラメータを指定)
	dao_t_nyusatsu.exec_sql_params(connection, cursor, sql_params)

	# pg_connectin クローズ
	pg_connection.set_pg_connection_close(cursor, logger)

	# ログ出力
	logger.print_log()
