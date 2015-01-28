# -*- coding: utf-8 -*-

# 案件情報ジャーナルクラス
class ClassAnken:
	# ID
	id = None
	# 入札システム
	nyusatsu_system = None
	# 入札タイプ
	nyusatsu_type = None
	# 案件番号
	anken_no = None
	# 案件URL
	anken_url = None
	# 案件名称
	anken_name = None
	# 契約種別コード
	keishu_cd = None
	# 契約種別名称
	keishu_name = None
	# 案件公開中・案件終了（結果表示中）
	public_flag = None
	# 対象業者の地域要件
	company_area = None
	# 公開開始日時
	anken_open_date = None
	# 公開終了日時
	anken_close_date = None
	# 入札日時
	tender_date = None
	# 入札場所
	tender_place = None
	# 履行期限
	limit_date = None
	# 業務大分類
	gyoumu_kbn_1 = None
	# 業務小分類
	gyoumu_kbn_2 = None
	# 実施機関
	kasitu_name = None
	# 担当者名・電話番号
	tanto_name = None
	# 特記事項
	notes = None
	
	# 結果表示開始日時
	result_open_date = None
	# 結果表示終了日時
	result_close_date = None
	# 落札業者名等
	raku_name = None
	# 落札金額（税込・円）
	price = None
	
	# バージョン
	version_no = None
	# 削除フラグ
	delete_flag = None
	# データ作成日
	ins_date = None
	# データ更新日
	upd_date = None