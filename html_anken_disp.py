# -*- coding: utf-8 -*-

import re
import urllib2

import config
import util
import dao_anken

# 案件情報詳細ページに対応したクラス
class HtmlAnkenDisp:

	def __init__(self):
		# 契約種別コード
		# '1' or '2'
		self.keishu_cd = None
		# 公開フラグ
		# '0' or '1'
		self.public_flag = None
		# 対象URL
		self.url = None
		# 対象HTML
		self.html = None
		# 案件情報
		self.anken = dao_anken.ClassAnken()
		# サイトURL
		self.site_url = None

	# インスタンスに各種パラメータをセット
	# @param : 対象ページのURL
	# TODO => 名前 set_param とか set_info のほうがいいような
	def set_url(self, url, site_url):
		self.url = url
		self.site_url = site_url

		replaced = self.url.replace(site_url, '')
		splits = replaced.split('.')
		splits = splits[0].split('_')

		keishu_key = splits[1]
		public_flag_key = splits[2]


		if(u'gene' == keishu_key):
			self.keishu_cd = u'1'
		elif(u'easy' == keishu_key):
			self.keishu_cd = u'2'

		if(u'pub' == public_flag_key):
			self.public_flag = u'0'
		elif(u'end' == public_flag_key):
			self.public_flag = u'1'

	# 案件情報の取得
	# TODO => 名前 get_anken よりも set_anken のほうがいいんじゃないかな
	def get_anken(self):
		fp = urllib2.urlopen(self.url)
		html = fp.read()
		fp.close()

		html = unicode(html, 'euc_jp', 'ignore')
		self.html = util.clean_string(html)
		
		# print(self.html)

		self.anken = dao_anken.ClassAnken()

		self.anken.nyusatsu_system = 1
		self.anken.nyusatsu_type = 1
		self.anken.anken_url = self.url
		self.anken.keishu_cd = self.keishu_cd
		self.anken.public_flag = self.public_flag

		self.anken.anken_no = self.get_anken_no()
		self.anken.anken_name = self.get_anken_name()
		self.anken.keishu_name = self.get_keishu_name()
		self.anken.company_area = self.get_company_area()
		self.anken.anken_open_date = self.get_anken_open_date()
		self.anken.anken_close_date = self.get_anken_close_date()
		self.anken.tender_date = self.get_tender_date()
		self.anken.tender_place = self.get_tender_place()
		self.anken.limit_date = self.get_limit_date()
		self.anken.gyoumu_kbn_1 = self.get_gyoumu_kbn_1()
		self.anken.gyoumu_kbn_2 = self.get_gyoumu_kbn_2()
		self.anken.kasitu_name = self.get_kasitu_name()
		self.anken.tanto_name = self.get_tanto_name()
		self.anken.notes = self.get_notes()
		self.anken.result_open_date = self.get_result_open_date()
		self.anken.result_close_date = self.get_result_close_date()
		self.anken.raku_name = self.get_raku_name()
		self.anken.price = self.get_price()
		self.anken.attached_file_1 = self.get_attached_file_1()
		self.anken.attached_file_2 = self.get_attached_file_2()
		self.anken.attached_file_3 = self.get_attached_file_3()


	# 和暦日付を西暦日付に変換
	# @param: 日付(文字列 : 平成XX年XX月XX日XX時XX分)
	# @retuen: 西暦日付
	def format_date(self, date_string):
		if(date_string is None):
			return date_string
		date_string_f = ''

		year_j = util.get_block(date_string, u'', u'年')
		month = util.get_block(date_string , u'年', u'月')
		day = util.get_block(date_string , u'月', u'日')
		hour = util.get_block(date_string , u'日', u'時')
		minute = util.get_block(date_string , u'時', u'分')

		year_ad = util.convert_J2AD(year_j)

		if(hour is None):
			date_string_f = '/'.join([year_ad, month, day])
		else:
			date_string_f = '/'.join([year_ad, month, day]) + ' ' + ':'.join([hour, minute])

		return date_string_f

	# @return : 案件番号
	def get_anken_no(self):
		start = u'<tr> <td width="200">案件番号</td> <td>'
		stop = u'</td> </tr>'
		anken_no = util.get_block(self.html, start, stop)
		return anken_no


	# @return : 案件名(事業年度・名称)
	def get_anken_name(self):
		start = u'<tr> <td>案件名(事業年度・名称)</td> <td>'
		stop = u'</td> </tr>'
		anken_name = util.get_block(self.html, start, stop)
		return anken_name

	# @return : 契約種別
	def get_keishu_name(self):
		start = u'<tr> <td>契約種別</td> <td>'
		stop = u'</td> </tr>'
		keishu_name = util.get_block(self.html, start, stop)
		keishu_name = re.sub('<!--.*-->\s*', '', keishu_name)
		return keishu_name

	# @return : 対象業者の地域要件
	def get_company_area(self):
		start = u'<tr> <td>対象業者の地域要件</td> <td>'
		stop = u'</td> </tr>'
		company_area = util.get_block(self.html, start, stop)
		return company_area

	# @return : 公開開始日時
	def get_anken_open_date(self):
		if(1 == int(self.keishu_cd)):
			start = u'<td>公開開始日時<br></td> <td>'
		elif(2 == int(self.keishu_cd)):
			start = u'<tr> <td>公開開始日時<br>（＝見積書受付開始）<br></td> <td>'
		stop = u'</td> </tr>'
		anken_open_date = util.get_block(self.html, start, stop)
		anken_open_date = self.format_date(anken_open_date)
		return anken_open_date

	# @return : 公開終了日時
	def get_anken_close_date(self):
		start = u'<tr> <td>公開終了日時</td> <td>'
		stop = u'</td> </tr>'
		anken_close_date = util.get_block(self.html, start, stop)
		anken_close_date = self.format_date(anken_close_date)
		return anken_close_date

	# @return : 入札日時
	def get_tender_date(self):
		if(1 == int(self.keishu_cd)):
			start = u'<tr> <td>入札日時<br></td> <td>'
		elif(2 == int(self.keishu_cd)):
			start = u' <tr> <td>見積書〆切日時<br></td> <td>'

		stop = u'</td> </tr>'
		tender_date = util.get_block(self.html, start, stop)
		tender_date = self.format_date(tender_date)
		return tender_date

	# @return : 入札場所
	def get_tender_place(self):
		if(1 == int(self.keishu_cd)):
			start = u'<td>入札場所<br></td> <td>'
		elif(2 == int(self.keishu_cd)):
			start = u'<tr> <td>見積書受付場所<br></td> <td>'
		stop = u'</td> </tr>'
		tender_place = util.get_block(self.html, start, stop)
		return tender_place

	# @return : 履行期限
	def get_limit_date(self):
		start = u'<tr> <td>履行期限</td> <td>'
		stop = u'</td> </tr>'
		limit_date = util.get_block(self.html, start, stop)
		limit_date = self.format_date(limit_date)
		return limit_date

	# @return : 業務大分類
	def get_gyoumu_kbn_1(self):
		start = u'<tr> <td>業務大分類</td> <td>'
		stop = u'</td> </tr>'
		gyoumu_kbn_1 = util.get_block(self.html, start, stop)
		return gyoumu_kbn_1

	# @return : 業務小分類
	def get_gyoumu_kbn_2(self):
		start = u'<tr> <td>業務小分類</td> <td>'
		stop = u'</td> </tr>'
		gyoumu_kbn_2 = util.get_block(self.html, start, stop)
		return gyoumu_kbn_2

	# @return : 実施機関
	def get_kasitu_name(self):
		start = u'<tr> <td>実施機関</td> <td>'
		stop = u'</td> </tr>'
		kasitu_name = util.get_block(self.html, start, stop)
		return kasitu_name

	# @return : 担当者名・電話番号
	def get_tanto_name(self):
		start = u'<tr> <td>担当者名・電話番号</td><td>'
		stop = '</td> </tr>'
		tanto_name = util.get_block(self.html, start, stop)
		return tanto_name

	# @return : 特記事項
	def get_notes(self):
		start = u'<tr> <td>特記事項</td><td>'
		stop = u'</td> </tr>'
		notes = util.get_block(self.html, start, stop)
		return notes

	# @return : 結果表示開始日時
	def get_result_open_date(self):
		start = u'<tr> <td width="200">結果表示開始日時</td> <td>'
		stop = u'</option> </td> </tr>'
		result_open_date = util.get_block(self.html, start, stop)
		result_open_date = self.format_date(result_open_date)
		return result_open_date

	# @return : 結果表示終了日時
	def get_result_close_date(self):
		start = u'<tr> <td>結果表示終了日時</td> <td>'
		stop = u'</td> </tr>'
		result_close_date = util.get_block(self.html, start, stop)
		result_close_date = self.format_date(result_close_date)
		return result_close_date

	# @return : 落札業者名等
	def get_raku_name(self):
		start = u'<tr> <td>落札業者名等</td><td>'
		stop = u'</td> </tr>'
		raku_name = util.get_block(self.html, start, stop)
		return raku_name

	# @return : 落札金額（税込・円）
	def get_price(self):
		start = u'<tr> <td>落札金額（税込・円）</td><td>'
		stop = u'</td> </tr>'
		price = util.get_block(self.html, start, stop)

		if(None != price):
			price = re.sub('&nbsp;', '', price)

		return price

	# @return : 添付ファイル１
	def get_attached_file_1(self):
		start = u'<tr> <td>添付ファイル１</td><td> <a href="'
		stop = u'">'
		attached_file_1 = util.get_block(self.html, start, stop)
		# print(attached_file_1)
		if attached_file_1 is not None:		
			attached_file_1 = self.site_url + attached_file_1
		else:
			attached_file_1 = ''
		# print(attached_file_1)
		return attached_file_1;
	# @return : 添付ファイル２
	def get_attached_file_2(self):
		start = u'<tr> <td>添付ファイル２</td><td> <a href="'
		stop = u'">'
		attached_file_2 = util.get_block(self.html, start, stop)
		# print(attached_file_2)
		if attached_file_2 is not None:
			attached_file_2 = self.site_url + attached_file_2
		else:
			attached_file_2 = ''
		# print(attached_file_2)
		return attached_file_2;
	# @return : 添付ファイル３
	def get_attached_file_3(self):
		start = u'<tr> <td>添付ファイル３</td><td> <a href="'
		stop = u'">'
		attached_file_3 = util.get_block(self.html, start, stop)
		# print(attached_file_3)
		if attached_file_3 is not None:
			attached_file_3 = self.site_url + attached_file_3
		else:
			attached_file_3 = ''
		# print(attached_file_3)
		return attached_file_3;
# 以下テスト用
if __name__ == '__main__':
	print(0)
	html_anken_disp = HtmlAnkenDisp()
	html_anken_disp.set_url(u'http://wave.pref.wakayama.lg.jp/ekimu2/disp_gene_pub.php?AnkNo=011400-H2504121059-11')
	html_anken_disp.get_anken()

	print(html_anken_disp.anken.nyusatsu_system)
	print(html_anken_disp.anken.nyusatsu_type)
	print(html_anken_disp.anken.anken_url)
	print(html_anken_disp.anken.keishu_cd)
	print(html_anken_disp.anken.public_flag)
	print(html_anken_disp.anken.anken_no)
	print(html_anken_disp.anken.anken_name)
	print(html_anken_disp.anken.keishu_name)
	print(html_anken_disp.anken.company_area)
	print(html_anken_disp.anken.anken_open_date)
	print(html_anken_disp.anken.anken_close_date)
	print(html_anken_disp.anken.tender_date)
	print(html_anken_disp.anken.tender_place)
	print(html_anken_disp.anken.limit_date)
	print(html_anken_disp.anken.gyoumu_kbn_1)
	print(html_anken_disp.anken.gyoumu_kbn_2)
	print(html_anken_disp.anken.kasitu_name)
	print(html_anken_disp.anken.tanto_name)
	print(html_anken_disp.anken.notes)
	print(html_anken_disp.anken.result_open_date)
	print(html_anken_disp.anken.result_close_date)
	print(html_anken_disp.anken.raku_name)
	print(html_anken_disp.anken.price)
