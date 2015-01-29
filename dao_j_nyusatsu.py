# -*- coding: utf-8 -*-

# テーブル「j_nyusatsu」クラス
class DaoJNyusatsu:
	# 初期化
	def __init__(self):
		self.sql = ""

	# SQL作成(IDの最大値を取得)
	def make_sql_select_max_id(self):
		self.sql = u"select max(id) from j_nyusatsu"

	# SQLの作成(追加)
	def make_sql_insert(self):
		self.sql = u'''
insert into j_nyusatsu(
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
	upd_date,
	registration_no,
	site_name
)
values(
	%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0, now(), now(), %s, %s
)

'''

	# SQLを取得
	def get_sql(self):
		return self.sql

	# SQLの実行
	# @param: connection
	# @param: cursol
	# @retuen: cursol
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
	dao_j_nyusatsu = DaoJNyusatsu()

	# Max_id取得用SQL 生成
	dao_j_nyusatsu.make_sql_select_max_id()

	# sqlをlogに書き出す
	logger.set_log(dao_j_nyusatsu.get_sql())

	# sql実行
	cursor = dao_j_nyusatsu.exec_sql(connection, cursor)
	record =  cursor.fetchone()
	max_id = record[0]
	# print(record[0])

	# insert用SQL 生成
	dao_j_nyusatsu.make_sql_insert()

	# sqlをlogに書き出す
	logger.set_log(dao_j_nyusatsu.get_sql())

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
	dao_j_nyusatsu.exec_sql_params(connection, cursor, sql_params)

	# pg_connectin クローズ
	pg_connection.set_pg_connection_close(cursor, logger)

	# ログ出力
	logger.print_log()

# ここから下は使っているのだろうか？
# 使っていないのであれば、削除するべき

# 案件情報ジャーナルクラス
class ClassJNyusatsu:
	id = None
	nyusatsu_system = None
	nyusatsu_type = None
	anken_no = None
	anken_url = None
	anken_name = None
	keishu_cd = None
	keishu_name = None
	public_flag = None
	company_area = None
	anken_open_date = None
	anken_close_date = None
	tender_date = None
	tender_place = None
	limit_date = None
	gyoumu_kbn_1 = None
	gyoumu_kbn_2 = None
	kasitu_name = None
	tanto_name = None
	notes = None
	result_open_date = None
	result_close_date = None
	raku_name = None
	price = None
	version_no = None
	delete_flag = None
	ins_date = None
	upd_date = None

# 案件情報ジャーナルのMaxIDを取得
# @param  : なし
# @return : 案件情報ジャーナルのMaxID
def get_max_id(cur):
	sql = u"select max(id) from j_nyusatsu"
	cur.execute(sql)
	record =  cur.fetchone()

	if(record[0] is None):
		max_id = 0
	else:
		max_id = record[0]

	return max_id

# 案件情報ジャーナルに新規情報を登録
# @param  : 案件情報クラス
# @return : なし
def add_nyusatsu(conn, cur, anken):
	sql = u'''
insert into j_nyusatsu(
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
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	%s,
	0,
	0,
	now(),
	now()
)

'''
	sql_arg = []
	sql_arg.append(anken.id)
	sql_arg.append(anken.nyusatsu_system)
	sql_arg.append(anken.nyusatsu_type)
	sql_arg.append(anken.anken_no)
	sql_arg.append(anken.anken_url)
	sql_arg.append(anken.anken_name)
	sql_arg.append(anken.keishu_cd)
	sql_arg.append(anken.keishu_name)
	sql_arg.append(anken.public_flag)
	sql_arg.append(anken.company_area)
	sql_arg.append(anken.anken_open_date)
	sql_arg.append(anken.anken_close_date)
	sql_arg.append(anken.tender_date)
	sql_arg.append(anken.tender_place)
	sql_arg.append(anken.limit_date)
	sql_arg.append(anken.gyoumu_kbn_1)
	sql_arg.append(anken.gyoumu_kbn_2)
	sql_arg.append(anken.kasitu_name)
	sql_arg.append(anken.tanto_name)
	sql_arg.append(anken.notes)
	sql_arg.append(anken.result_open_date)
	sql_arg.append(anken.result_close_date)
	sql_arg.append(anken.raku_name)
	sql_arg.append(anken.price)

	cur.execute(sql, sql_arg)
	conn.commit()

