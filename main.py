# -*- coding: utf-8 -*-

import codecs
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

sys.stdin = codecs.getreader("utf-8")(sys.stdin)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# 案件情報取得のためのパラメータ
class MainParam:
	keishu_cd = None
	public_flag = None


'''
以下デバッグ用　そのうち消すこと

print u'# スクリプトへの相対パス'
print __file__
print u'# スクリプトへの相対パス'
print sys.argv[0]
print u'# スクリプトのあるディレクトリへの相対パス'
print os.path.dirname(__file__)

print u'# スクリプト名'
print os.path.basename(__file__) 
print u'# スクリプトの絶対パス'
print os.path.abspath(__file__)  
print u'# スクリプトあるディレクトリの絶対パス'
print os.path.abspath(os.path.dirname(__file__))  
print u'# 実行時カレントディレクトリの絶対パス'
print os.getcwd()                
print
'''

# ログファイル用のディレクトリの存在チェック
# os.path.abspath(os.path.dirname(__file__)) => スクリプトあるディレクトリの絶対パス'
log_dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), config.LOG_FILE_DIR_PATH)
print log_dir_path
exist_log_dir = os.path.isdir(log_dir_path)
print exist_log_dir
if(not exist_log_dir):
	os.mkdir(log_dir_path)
	os.chmod(log_dir_path, 0777)

log_file_path = log_dir_path + "access_log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
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
logger.set_log('Delete t_nyusatsu')
t_nyusatsu.exec_sql(connection, cursor)

# 登録番号の取得
sql = u'select max(registration_no) from t_tenders;'
cursor.execute(sql)
record =  cursor.fetchone()
max_registration_no = record[0]
if max_registration_no == None:
	max_registration_no = 0
registration_no = max_registration_no + 1
# print(registration_no)

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

# 処理開始時間
process_start = datetime.datetime.now()
# 案件件数
count_tenders = 0;

for param in params:
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

		html_list.get_anken_list()
		for url in html_list.anken_url_list:
			logger.set_log(url)

			count_tenders = count_tenders + 1

			html_disp = html_anken_disp.HtmlAnkenDisp()

			html_disp.set_url(url)
			# 案件情報を取得
			html_disp.get_anken()


			# テーブル：t_nyusatsu　の更新

			# t_nyusatsu.make_sql_select_max_id()
			# cursor = t_nyusatsu.exec_sql(connection, cursor)
			# record =  cursor.fetchone()
			# max_id = record[0]
			# if max_id == None:
				# max_id = 0

			# t_nyusatsu.make_sql_insert()
			# id = max_id + 1
			# sql_params = []
			# sql_params.append(id)
			# sql_params.append(html_disp.anken.nyusatsu_system)
			# sql_params.append(html_disp.anken.nyusatsu_type)
			# sql_params.append(html_disp.anken.anken_no)
			# sql_params.append(html_disp.anken.anken_url)
			# sql_params.append(html_disp.anken.anken_name)
			# sql_params.append(html_disp.anken.keishu_cd)
			# sql_params.append(html_disp.anken.keishu_name)
			# sql_params.append(html_disp.anken.public_flag)
			# sql_params.append(html_disp.anken.company_area)
			# sql_params.append(html_disp.anken.anken_open_date)
			# sql_params.append(html_disp.anken.anken_close_date)
			# sql_params.append(html_disp.anken.tender_date)
			# sql_params.append(html_disp.anken.tender_place)
			# sql_params.append(html_disp.anken.limit_date)
			# sql_params.append(html_disp.anken.gyoumu_kbn_1)
			# sql_params.append(html_disp.anken.gyoumu_kbn_2)
			# sql_params.append(html_disp.anken.kasitu_name)
			# sql_params.append(html_disp.anken.tanto_name)
			# sql_params.append(html_disp.anken.notes)
			# sql_params.append(html_disp.anken.result_open_date)
			# sql_params.append(html_disp.anken.result_close_date)
			# sql_params.append(html_disp.anken.raku_name)
			# sql_params.append(html_disp.anken.price)
			# t_nyusatsu.exec_sql_params(connection, cursor, sql_params)

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
				sql_params.append(registration_no)
				sql_params.append(config.SITE_NAME)

				t_tenders.exec_sql_params(connection, cursor, sql_params)
				# print "insert"
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
				sql_params.append(registration_no)
				sql_params.append(config.SITE_NAME)
				sql_params.append(html_disp.anken.anken_no)

				t_tenders.exec_sql_params(connection, cursor, sql_params)
				# print util.clean_string(t_tenders.get_sql())
				# print cursor.query.decode('utf-8')
				# logger.set_log(cursor.query.decode('utf-8'))
				# logger.set_log(util.clean_string(cursor.query.encode('utf-8')))
				# print cursor.query
				# print "update"

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
			# 登録番号
			sql_params.append(registration_no)
			# サイト名
			sql_params.append(config.SITE_NAME)

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
