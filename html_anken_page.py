# -*- coding: utf-8 -*-

import config

'''
summary
	案件一覧から案件ページURLのリストを取得する
example
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php
	→
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=1
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=2
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=3
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=4
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=5
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=6
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=7
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=8
	http://wave.pref.wakayama.lg.jp/ekimu2/anken_gene_end.php?NextPage=9
'''

# 案件ページに対応したクラス
class HtmlAnkenPage:
	def __init__(self):
        # 1 or 2
		self.keishu_cd = None
        # 0 or 1
		self.public_flag = None
    	# gene or easy
	    self.keishu_string = ''
    	# pub or end
    	self.public_flag_string = ''

    	self.html = None
    	self.page_list = None

	def set_keishu_cd(self, keishu_cd):
		self.keishu_cd = keishu_cd
		if(u'1' == self.keishu_cd):
			self.keishu_string = 'gene'
		elif(u'2' == self.keishu_cd):
			self.keishu_string = 'easy'

	def set_public_flag(self, public_flag):
		self.public_flag = public_flag
		if(u'0' == self.public_flag):
			self.public_flag_string = 'pub'
		elif(u'1' == self.public_flag):
			self.public_flag_string = 'end'

	def get_html(self):
		url = config.SITE_URL + 'anken_' + self.keishu_string + '_' + self.public_flag_string + '.php'

		import urllib2
		fp = urllib2.urlopen(url)
		html = fp.read()
		self.html = unicode(html, 'euc_jp', errors='replace')
		fp.close()

	def get_page_list(self):
		self.page_list=[]
		page_number = 0
		while True:
			page_number = page_number + 1
			sub = 'anken_' + self.keishu_string + '_' + self.public_flag_string + '.php?NextPage=' + str(page_number)
			if 0 < self.html.find(sub):
				page_url = config.SITE_URL + sub
				self.page_list.append(page_url)
			else:
				break

# 以下テスト用
if __name__ == '__main__':
	html_anken_page = HtmlAnkenPage()
	html_anken_page.set_keishu_cd('1')
	html_anken_page.set_public_flag('0')
	html_anken_page.get_html()
	html_anken_page.get_page_list()
	print('PAGE_LIST : ' + str(len(html_anken_page.page_list)))
	for page_url in html_anken_page.page_list:
		print('PAGE : ' + page_url)

	html_anken_page = HtmlAnkenPage()
	html_anken_page.set_keishu_cd('1')
	html_anken_page.set_public_flag('1')
	html_anken_page.get_html()
	html_anken_page.get_page_list()
	print('PAGE_LIST : ' + str(len(html_anken_page.page_list)))
	for page_url in html_anken_page.page_list:
		print('PAGE : ' + page_url)

