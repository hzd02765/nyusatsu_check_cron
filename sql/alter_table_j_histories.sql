/*
�@�e�[�u���ɐV�K�J�����쐬
*/

ALTER TABLE j_histories ADD COLUMN id integer;
ALTER TABLE j_histories ADD COLUMN process_start timestamp without time zone;
ALTER TABLE j_histories ADD COLUMN process_end timestamp without time zone;
ALTER TABLE j_histories ADD COLUMN process_seconds integer;
ALTER TABLE j_histories ADD COLUMN count_tenders integer;

/*
	�f�[�^���C���|�[�g
	modified => process_end
	�J����id�ɁA�A�Ԃ�t����
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
	�J����id��PK�ɂ���
*/
ALTER TABLE j_histories DROP CONSTRAINT j_histories_pkey;
ALTER TABLE j_histories ADD CONSTRAINT j_histories_pkey PRIMARY KEY(id);

/*
	�J����[modified]���폜����
*/
ALTER TABLE j_histories DROP modified;

/*
	�v���O�����R�[�h�̏C��
*/
