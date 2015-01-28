# -*- coding: utf-8 -*-

import config

'''
summary
	案件ページから詳細ページのURLリストを取得する
example
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=1
	→
	disp_gene_end.php?AnkNo=000601-H2502171506-11
	disp_gene_end.php?AnkNo=000601-H2502181851-11
	disp_gene_end.php?AnkNo=010500-H2502271453-11
	disp_gene_end.php?AnkNo=010501-H2502141518-11
	disp_gene_end.php?AnkNo=010501-H2502221537-11
	disp_gene_end.php?AnkNo=010700-H2502211929-11
	disp_gene_end.php?AnkNo=010700-H2502251052-11
	disp_gene_end.php?AnkNo=010700-H2502251115-11
	disp_gene_end.php?AnkNo=010700-H2502251530-11
	disp_gene_end.php?AnkNo=010700-H2502251556-11
	disp_gene_end.php?AnkNo=010700-H2502251635-11
	disp_gene_end.php?AnkNo=010700-H2503040952-11
	disp_gene_end.php?AnkNo=010700-H2503181705-11
	disp_gene_end.php?AnkNo=020200-H2502191859-11
	disp_gene_end.php?AnkNo=031301-H2502121851-11
	disp_gene_end.php?AnkNo=031801-H2502190955-11
	disp_gene_end.php?AnkNo=032100-H2503011111-11
	disp_gene_end.php?AnkNo=032100-H2503041344-11
	disp_gene_end.php?AnkNo=032100-H2503041348-11
	disp_gene_end.php?AnkNo=032100-H2503041527-11
'''

# summary : 案件リストページに対応したクラス
class HtmlAnkenList:
	def __init__(self, page_url):
        # URL
		self.anken_page_url = page_url
        # 詳細ページのURL
        self.anken_url_list = None

	# summary : 案件ページリストの取得
	# @return : 案件ページリスト
	def get_anken_list(self):
		replaced = self.anken_page_url.replace(config.SITE_URL, '')
		splits = replaced.split('.')
		splits = splits[0].split('_')

		keishu_string = splits[1]
		public_flag_string = splits[2]

		self.anken_url_list = []

		import urllib2
		fp = urllib2.urlopen(self.anken_page_url)
		html = fp.read()
		html = unicode(html, 'euc_jp', errors='replace')
		fp.close()

		start = 1
		while True:
			sub = '<tr><td width="150"><a href="disp_' + keishu_string + '_' + public_flag_string + '.php?AnkNo='
			start_index = html.find(sub, start)
			if 0 < start_index:
				sub = '</td></tr>'
				end_index = html.find(sub, start_index)
				if 0 < end_index:
					anken_url = html[start_index:end_index + len(sub)]
					anken_url = self.get_anken_url(anken_url);
					self.anken_url_list.append(anken_url)
					start = start_index + 1
				else:
					break
			else:
				break

	# HTMLからURLの取得
    # @param : HTML
    # @return : URL
	def get_anken_url(self, html):
		anken_url = ''
		start_sub = '<a href="'
		start_index = html.find(start_sub)
		if 0 < start_index:
			end_sub = '">'
			end_index = html.find(end_sub, start_index)
			if 0 < end_index:
				anken_url = html[start_index + len(start_sub) : end_index]
				anken_url = config.SITE_URL + anken_url

		return anken_url

# 以下テスト用
if __name__ == '__main__':
	html_anken_list = HtmlAnkenList(u'http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=1')
	html_anken_list.get_anken_list()
	for url in html_anken_list.anken_url_list:
		print(url)

