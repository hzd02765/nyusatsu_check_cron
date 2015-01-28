# -*- coding: utf-8 -*-
import sys
import os
import datetime

# common
import config
import util
import logger

# HTML
import html_anken_page
import html_anken_list
import html_anken_disp

# DB
import dao_pg_connection
import dao_t_nyusatsu
import dao_j_histories
import dao_j_nyusatsu
import dao_t_tenders

# 案件情報取得のためのパラメータ
class MainParam:
	keishu_cd = None
	public_flag = None

# ログファイル用のディレクトリの存在チェック
exist_log_dir = os.path.isdir(config.LOG_FILE_DIR_PATH)
if(not exist_log_dir):
	os.mkdir(config.LOG_FILE_DIR_PATH)
	os.chmod(config.LOG_FILE_DIR_PATH, 0777)

log_file_path = config.LOG_FILE_DIR_PATH + "access_log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
#ログファイルの存在チェック
exist_log_file = os.path.exists(log_file_path)
if(not exist_log_file):
	# 無ければ作る
	f = open(log_file_path, 'w')
	# パーミッションを変更
	os.chmod(log_file_path, 0777)
	f.close()

logger = logger.Logger(log_file_path)
logger.set_log(u'start')

logger.set_log(u'DB HOST : ' + config.DB_HOST)
logger.set_log(u'DB NAME : ' + config.DB_NAME)
logger.set_log(u'SITE URL : ' + config.SITE_URL)
logger.set_log(u'LOG DIR : ' + config.LOG_FILE_DIR_PATH)

# DBコネクション開始
pg_con = dao_pg_connection.PgConnection()
result = pg_con.set_pg_connection_open();
if not result :
	logger.set_log('DB Connection failure')
	logger.print_log()
	sys.exit()

logger.set_log('DB Connection Success')
connection = pg_con.get_pg_connection()
cursor = connection.cursor()

# トランザクションテーブルのレコードを削除
t_nyusatsu = dao_t_nyusatsu.DaoTNyusatsu()
t_nyusatsu.make_sql_delete()
# print t_nyusatsu.get_sql()
logger.set_log('Delete t_nyusatsu')
t_nyusatsu.exec_sql(connection, cursor)

# 案件情報取得のためのパラメータ（リスト）
params = []

# 現在公開分 => 一般競争入札
param = MainParam()
param.keishu_cd = u'1'
param.public_flag = u'0'
params.append(param)

# 現在公開分 => 簡易公開調達
param = MainParam()
param.keishu_cd = u'2'
param.public_flag = u'0'
params.append(param)

# 既に終了分 => 一般競争入札
param = MainParam()
param.keishu_cd = u'1'
param.public_flag = u'1'
params.append(param)

# 既に終了分 => 簡易公開調達
param = MainParam()
param.keishu_cd = u'2'
param.public_flag = u'1'
params.append(param)

# for debug
'''
'''

# 処理開始時間
process_start = datetime.datetime.now()
# 案件件数
count_tenders = 0;

for param in params:
	# print param.keishu_cd
	# print param.public_flag

	# HTMLを取得
	html_page = html_anken_page.HtmlAnkenPage()
	logger.set_log('class HtmlAnkenPage')

	html_page.set_keishu_cd(param.keishu_cd)
	html_page.set_public_flag(param.public_flag)
	html_page.get_html()
	# HTMLから案件情報ページURLリストを取得
	html_page.get_page_list()

	# 案件情報ページURLリストから案件情報のリストを取得
	for page in html_page.page_list:
		logger.set_log(page)
		html_list = html_anken_list.HtmlAnkenList(page)
		# logger.set_log('class HtmlAnkenList')

		html_list.get_anken_list()
		for url in html_list.anken_url_list:
			logger.set_log(url)

			count_tenders = count_tenders + 1

			html_disp = html_anken_disp.HtmlAnkenDisp()
			# logger.set_log('class HtmlAnkenDisp')

			html_disp.set_url(url)
			# 案件情報を取得
			html_disp.get_anken()

			# print html_disp.anken.nyusatsu_system
			# print html_disp.anken.nyusatsu_type
			# print html_disp.anken.anken_url
			# print html_disp.anken.keishu_cd
			# print html_disp.anken.public_flag
			# print html_disp.anken.anken_no
			# print html_disp.anken.anken_name
			# print html_disp.anken.keishu_name
			# print html_disp.anken.company_area
			# print html_disp.anken.anken_open_date
			# print html_disp.anken.anken_close_date
			# print html_disp.anken.tender_date
			# print html_disp.anken.tender_place
			# print html_disp.anken.limit_date
			# print html_disp.anken.gyoumu_kbn_1
			# print html_disp.anken.gyoumu_kbn_2
			# print html_disp.anken.kasitu_name
			# print html_disp.anken.tanto_name
			# print html_disp.anken.notes
			# print html_disp.anken.result_open_date
			# print html_disp.anken.result_close_date
			# print html_disp.anken.raku_name
			# print html_disp.anken.price

			# テーブル：t_nyusatsu　の更新

			t_nyusatsu.make_sql_select_max_id()
			cursor = t_nyusatsu.exec_sql(connection, cursor)
			record =  cursor.fetchone()
			max_id = record[0]
			if max_id == None:
				max_id = 0
			# print(max_id)

			t_nyusatsu.make_sql_insert()
			id = max_id + 1
			sql_params = []
			sql_params.append(id)
			sql_params.append(html_disp.anken.nyusatsu_system)
			sql_params.append(html_disp.anken.nyusatsu_type)
			sql_params.append(html_disp.anken.anken_no)
			sql_params.append(html_disp.anken.anken_url)
			sql_params.append(html_disp.anken.anken_name)
			sql_params.append(html_disp.anken.keishu_cd)
			sql_params.append(html_disp.anken.keishu_name)
			sql_params.append(html_disp.anken.public_flag)
			sql_params.append(html_disp.anken.company_area)
			sql_params.append(html_disp.anken.anken_open_date)
			sql_params.append(html_disp.anken.anken_close_date)
			sql_params.append(html_disp.anken.tender_date)
			sql_params.append(html_disp.anken.tender_place)
			sql_params.append(html_disp.anken.limit_date)
			sql_params.append(html_disp.anken.gyoumu_kbn_1)
			sql_params.append(html_disp.anken.gyoumu_kbn_2)
			sql_params.append(html_disp.anken.kasitu_name)
			sql_params.append(html_disp.anken.tanto_name)
			sql_params.append(html_disp.anken.notes)
			sql_params.append(html_disp.anken.result_open_date)
			sql_params.append(html_disp.anken.result_close_date)
			sql_params.append(html_disp.anken.raku_name)
			sql_params.append(html_disp.anken.price)
			t_nyusatsu.exec_sql_params(connection, cursor, sql_params)

			# テーブル：t_tenders　の更新
			t_tenders = dao_t_tenders.DaoTTenders()
			t_tenders.make_sql_exist()
			sql_params = []
			sql_params.append(html_disp.anken.anken_no)
			cursor = t_tenders.exec_sql_params(connection, cursor, sql_params)
			if 0 == cursor.rowcount:
				t_tenders.make_sql_select_max_id()
				cursor = t_tenders.exec_sql(connection, cursor)
				record =  cursor.fetchone()
				max_id = record[0]
				if max_id == None:
					max_id = 0
				t_tenders.make_sql_insert()
				sql_params = []
				id = max_id + 1
				sql_params.append(id)
				sql_params.append(html_disp.anken.nyusatsu_system)
				sql_params.append(html_disp.anken.nyusatsu_type)
				sql_params.append(html_disp.anken.anken_no)
				sql_params.append(html_disp.anken.anken_url)
				sql_params.append(html_disp.anken.anken_name)
				sql_params.append(html_disp.anken.keishu_cd)
				sql_params.append(html_disp.anken.keishu_name)
				sql_params.append(html_disp.anken.public_flag)
				sql_params.append(html_disp.anken.company_area)
				sql_params.append(html_disp.anken.anken_open_date)
				sql_params.append(html_disp.anken.anken_close_date)
				sql_params.append(html_disp.anken.tender_date)
				sql_params.append(html_disp.anken.tender_place)
				sql_params.append(html_disp.anken.limit_date)
				sql_params.append(html_disp.anken.gyoumu_kbn_1)
				sql_params.append(html_disp.anken.gyoumu_kbn_2)
				sql_params.append(html_disp.anken.kasitu_name)
				sql_params.append(html_disp.anken.tanto_name)
				sql_params.append(html_disp.anken.notes)
				sql_params.append(html_disp.anken.result_open_date)
				sql_params.append(html_disp.anken.result_close_date)
				sql_params.append(html_disp.anken.raku_name)
				sql_params.append(html_disp.anken.price)

				t_tenders.exec_sql_params(connection, cursor, sql_params)
			else:
				t_tenders.make_sql_update()

				sql_params = []
				sql_params.append(html_disp.anken.nyusatsu_system)
				sql_params.append(html_disp.anken.nyusatsu_type)
				sql_params.append(html_disp.anken.anken_url)
				sql_params.append(html_disp.anken.anken_name)
				sql_params.append(html_disp.anken.keishu_cd)
				sql_params.append(html_disp.anken.keishu_name)
				sql_params.append(html_disp.anken.public_flag)
				sql_params.append(html_disp.anken.company_area)
				sql_params.append(html_disp.anken.anken_open_date)
				sql_params.append(html_disp.anken.anken_close_date)
				sql_params.append(html_disp.anken.tender_date)
				sql_params.append(html_disp.anken.tender_place)
				sql_params.append(html_disp.anken.limit_date)
				sql_params.append(html_disp.anken.gyoumu_kbn_1)
				sql_params.append(html_disp.anken.gyoumu_kbn_2)
				sql_params.append(html_disp.anken.kasitu_name)
				sql_params.append(html_disp.anken.tanto_name)
				sql_params.append(html_disp.anken.notes)
				sql_params.append(html_disp.anken.result_open_date)
				sql_params.append(html_disp.anken.result_close_date)
				sql_params.append(html_disp.anken.raku_name)
				sql_params.append(html_disp.anken.price)
				sql_params.append(html_disp.anken.anken_no)

				t_tenders.exec_sql_params(connection, cursor, sql_params)

			# テーブル：j_nyusatsu　の更新
			j_nyusatsu = dao_j_nyusatsu.DaoJNyusatsu()
			j_nyusatsu.make_sql_select_max_id()
			cursor = j_nyusatsu.exec_sql(connection, cursor)
			record =  cursor.fetchone()
			max_id = record[0]
			if max_id == None:
				max_id = 0
			# print max_id

			j_nyusatsu.make_sql_insert()

			sql_params = []
			id = max_id + 1

			# id,
			sql_params.append(id)
			# nyusatsu_system,
			sql_params.append(html_disp.anken.nyusatsu_system)
			# nyusatsu_type,
			sql_params.append(html_disp.anken.nyusatsu_type)
			# anken_no,
			sql_params.append(html_disp.anken.anken_no)
			# anken_url,
			sql_params.append(html_disp.anken.anken_url)
			# anken_name,
			sql_params.append(html_disp.anken.anken_name)
			# keishu_cd,
			sql_params.append(html_disp.anken.keishu_cd)
			# keishu_name,
			sql_params.append(html_disp.anken.keishu_name)
			# public_flag,
			sql_params.append(html_disp.anken.public_flag)
			# company_area,
			sql_params.append(html_disp.anken.company_area)
			# anken_open_date,
			sql_params.append(html_disp.anken.anken_open_date)
			# anken_close_date,
			sql_params.append(html_disp.anken.anken_close_date)
			# tender_date,
			sql_params.append(html_disp.anken.tender_date)
			# tender_place,
			sql_params.append(html_disp.anken.tender_place)
			# limit_date,
			sql_params.append(html_disp.anken.limit_date)
			# gyoumu_kbn_1,
			sql_params.append(html_disp.anken.gyoumu_kbn_1)
			# gyoumu_kbn_2,
			sql_params.append(html_disp.anken.gyoumu_kbn_2)
			# kasitu_name,
			sql_params.append(html_disp.anken.kasitu_name)
			# tanto_name,
			sql_params.append(html_disp.anken.tanto_name)
			# notes,
			sql_params.append(html_disp.anken.notes)
			# result_open_date,
			sql_params.append(html_disp.anken.result_open_date)
			# result_close_date,
			sql_params.append(html_disp.anken.result_close_date)
			# raku_name,
			sql_params.append(html_disp.anken.raku_name)
			# price,
			sql_params.append(html_disp.anken.price)

			j_nyusatsu.exec_sql_params(connection, cursor, sql_params)


# 処理終了時間
process_end = datetime.datetime.now()
# 処理時間（秒）
process_seconds = (process_end - process_start).seconds

# テーブル：j_histories　の更新
j_histories = dao_j_histories.DaoJHistories()
j_histories.make_sql_insert()
sql_params = []
sql_params.append(process_start)
sql_params.append(process_end)
sql_params.append(process_seconds)
sql_params.append(count_tenders)
j_histories.exec_sql_params(connection, cursor, sql_params)


# DBコネクション終了
pg_con.set_pg_connection_close(cursor)
logger.set_log(u'DB Connection Close')

logger.set_log(u'end')
logger.print_log()
