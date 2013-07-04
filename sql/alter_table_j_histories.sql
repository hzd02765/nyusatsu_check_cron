/*
　テーブルに新規カラム作成
*/

ALTER TABLE j_histories ADD COLUMN id integer;
ALTER TABLE j_histories ADD COLUMN process_start timestamp without time zone;
ALTER TABLE j_histories ADD COLUMN process_end timestamp without time zone;
ALTER TABLE j_histories ADD COLUMN process_seconds integer;
ALTER TABLE j_histories ADD COLUMN count_tenders integer;

/*
	データをインポート
	modified => process_end
	カラムidに、連番を付ける
*/
select 
	row_number() over ()
	, * 
from (
	select 
		 modified
		, id
		, process_start
		, process_end
		, process_seconds
		, count_tenders
	from 
		j_histories
	order by 
		j_histories.modified
	) as t

/*
	カラムidをPKにする
*/
ALTER TABLE j_histories DROP CONSTRAINT j_histories_pkey;
ALTER TABLE j_histories ADD CONSTRAINT j_histories_pkey PRIMARY KEY(id);

/*
	カラム[modified]を削除する
*/
ALTER TABLE j_histories DROP modified;

/*
	プログラムコードの修正
*/
