# -*- coding: utf-8 -*-

# 和暦を西暦に変換
def convert_J2AD(str_year_j):
	year = 0
	if(0 >= str_year_j.find(u'平成')):
		year_j = str_year_j.replace(u'平成','')
		year = int(year_j) + 1988
	return str(year)

# 改行、タブ、スペースを削除し、1行の文字列を返す
def clean_string(string):
	string_f = string

	# キャリッジ リターン
	char_CR = "\r\n"
	# ライン フィード
	char_LF = "\n"
	# タブ
	char_TAB = "\t"

	# スペース
	char_SPACE = ' '

	string_f = string_f.replace(char_CR, char_SPACE)
	string_f = string_f.replace(char_LF, char_SPACE)
	string_f = string_f.replace(char_TAB, char_SPACE)

	# strpos => 文字列の中で、引数の文字が最初に現れた位置を数字で返します
	while 0 <= string_f.find('  '):
		string_f = string_f.replace('  ',' ')

	return	string_f

# ブロック要素の取得
def get_block(source, start, stop):
	value_string = ''
	start_index = 0
	stop_index = 0

	start_index = source.find(start)
	if 0 <= start_index:
		start_index = start_index + len(start)
		stop_index = source.find(stop, start_index)
		if 0 <= stop_index:
			value_string = source[start_index : stop_index]
		else:
			return None
	else:
		return None

	return value_string.strip()

# 以下テスト用
if __name__ == '__main__':
	jp_year = u"平成 25"
	ad_year = convert_J2AD(jp_year)
	print(ad_year)

	string = u'''
あいうえお
かきくけこ



	'''
	string_f = clean_string(string)
	print(string_f)
