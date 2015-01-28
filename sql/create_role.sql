-- Role: nyusatsu_check

-- DROP ROLE nyusatsu_check;

CREATE ROLE nyusatsu_check LOGIN
  ENCRYPTED PASSWORD 'md5ca54db983f647af30cc5a78b19eae57e'
  NOSUPERUSER INHERIT CREATEDB NOCREATEROLE;


-- Database: nyusatsu_check

-- DROP DATABASE nyusatsu_check;

CREATE DATABASE nyusatsu_check
  WITH OWNER = nyusatsu_check
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'ja_JP.UTF-8'
       LC_CTYPE = 'ja_JP.UTF-8'
       CONNECTION LIMIT = -1;

-- Table: j_nyusatsu

-- DROP TABLE j_nyusatsu;

CREATE TABLE j_nyusatsu
(
  id integer NOT NULL,
  nyusatsu_system integer,
  nyusatsu_type integer,
  anken_no character varying,
  anken_url character varying,
  anken_name character varying,
  keishu_cd integer,
  keishu_name character varying,
  public_flag integer,
  company_area character varying,
  anken_open_date timestamp without time zone,
  anken_close_date timestamp without time zone,
  tender_date timestamp without time zone,
  tender_place character varying,
  limit_date timestamp without time zone,
  gyoumu_kbn_1 character varying,
  gyoumu_kbn_2 character varying,
  kasitu_name character varying,
  tanto_name character varying,
  notes character varying,
  result_open_date timestamp without time zone,
  result_close_date timestamp without time zone,
  raku_name character varying,
  price character varying,
  version_no integer,
  delete_flag integer,
  ins_date timestamp without time zone,
  upd_date timestamp without time zone,
  CONSTRAINT j_nyusatsu_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE j_nyusatsu OWNER TO nyusatsu_check;

-- Table: t_nyusatsu

-- DROP TABLE t_nyusatsu;

CREATE TABLE t_nyusatsu
(
  id integer NOT NULL,
  nyusatsu_system integer,
  nyusatsu_type integer,
  anken_no character varying,
  anken_url character varying,
  anken_name character varying,
  keishu_cd integer,
  keishu_name character varying,
  public_flag integer,
  company_area character varying,
  anken_open_date timestamp without time zone,
  anken_close_date timestamp without time zone,
  tender_date timestamp without time zone,
  tender_place character varying,
  limit_date timestamp without time zone,
  gyoumu_kbn_1 character varying,
  gyoumu_kbn_2 character varying,
  kasitu_name character varying,
  tanto_name character varying,
  notes character varying,
  result_open_date timestamp without time zone,
  result_close_date timestamp without time zone,
  raku_name character varying,
  price character varying,
  version_no integer,
  delete_flag integer,
  ins_date timestamp without time zone,
  upd_date timestamp without time zone,
  CONSTRAINT t_nyusatsu_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE t_nyusatsu OWNER TO nyusatsu_check;


-- Table: histories

-- DROP TABLE histories;

CREATE TABLE histories
(
  modified timestamp without time zone NOT NULL,
  CONSTRAINT logs_pkey PRIMARY KEY (modified)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE histories OWNER TO nyusatsu_check;


-- Table: t_tenders

-- DROP TABLE t_tenders;

CREATE TABLE t_tenders
(
  id integer NOT NULL,
  nyusatsu_system integer,
  nyusatsu_type integer,
  anken_no character varying,
  anken_url character varying,
  anken_name character varying,
  keishu_cd integer,
  keishu_name character varying,
  public_flag integer,
  company_area character varying,
  anken_open_date timestamp without time zone,
  anken_close_date timestamp without time zone,
  tender_date timestamp without time zone,
  tender_place character varying,
  limit_date timestamp without time zone,
  gyoumu_kbn_1 character varying,
  gyoumu_kbn_2 character varying,
  kasitu_name character varying,
  tanto_name character varying,
  notes character varying,
  result_open_date timestamp without time zone,
  result_close_date timestamp without time zone,
  raku_name character varying,
  price character varying,
  version_no integer,
  delete_flag integer,
  ins_date timestamp without time zone,
  upd_date timestamp without time zone,
  CONSTRAINT t_tenders_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE t_tenders OWNER TO nyusatsu_check;
