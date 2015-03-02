--
-- PostgreSQL database dump
--

-- Dumped from database version 8.4.20
-- Dumped by pg_dump version 9.4.0
-- Started on 2015-03-02 10:02:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 140 (class 1259 OID 16551)
-- Name: j_histories; Type: TABLE; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

CREATE TABLE j_histories (
    id integer NOT NULL,
    process_start timestamp without time zone,
    process_end timestamp without time zone,
    process_seconds integer,
    count_tenders integer
);


ALTER TABLE j_histories OWNER TO nyusatsu_check;

--
-- TOC entry 1814 (class 0 OID 0)
-- Dependencies: 140
-- Name: TABLE j_histories; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE j_histories IS '更新履歴';


--
-- TOC entry 141 (class 1259 OID 16554)
-- Name: j_nyusatsu; Type: TABLE; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

CREATE TABLE j_nyusatsu (
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
    registration_no character varying,
    site_name character varying
);


ALTER TABLE j_nyusatsu OWNER TO nyusatsu_check;

--
-- TOC entry 1815 (class 0 OID 0)
-- Dependencies: 141
-- Name: TABLE j_nyusatsu; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE j_nyusatsu IS '役務入札案件のジャーナル';


--
-- TOC entry 1816 (class 0 OID 0)
-- Dependencies: 141
-- Name: COLUMN j_nyusatsu.registration_no; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON COLUMN j_nyusatsu.registration_no IS '登録番号（1回の登録処理で登録された案件で共通）';


--
-- TOC entry 1817 (class 0 OID 0)
-- Dependencies: 141
-- Name: COLUMN j_nyusatsu.site_name; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON COLUMN j_nyusatsu.site_name IS '登録サイト名(ekimu or ekimu2)';


--
-- TOC entry 142 (class 1259 OID 16560)
-- Name: t_nyusatsu; Type: TABLE; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

CREATE TABLE t_nyusatsu (
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
    upd_date timestamp without time zone
);


ALTER TABLE t_nyusatsu OWNER TO nyusatsu_check;

--
-- TOC entry 1818 (class 0 OID 0)
-- Dependencies: 142
-- Name: TABLE t_nyusatsu; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE t_nyusatsu IS '現在HPで表示されている、役務入札案件';


--
-- TOC entry 143 (class 1259 OID 16566)
-- Name: t_tenders; Type: TABLE; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

CREATE TABLE t_tenders (
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
    registration_no integer,
    site_name character varying
);


ALTER TABLE t_tenders OWNER TO nyusatsu_check;

--
-- TOC entry 1819 (class 0 OID 0)
-- Dependencies: 143
-- Name: TABLE t_tenders; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE t_tenders IS '現在HPで表示されていないものも含めた、すべての役務入札案件';


--
-- TOC entry 1820 (class 0 OID 0)
-- Dependencies: 143
-- Name: COLUMN t_tenders.registration_no; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON COLUMN t_tenders.registration_no IS '登録番号（1回の登録処理で登録された案件で共通）';


--
-- TOC entry 1821 (class 0 OID 0)
-- Dependencies: 143
-- Name: COLUMN t_tenders.site_name; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON COLUMN t_tenders.site_name IS '登録サイト名(ekimu or ekimu2)';


--
-- TOC entry 146 (class 1259 OID 16615)
-- Name: v_latest_tenders; Type: VIEW; Schema: public; Owner: nyusatsu_check
--

CREATE VIEW v_latest_tenders AS
SELECT t1.id, t1.nyusatsu_system, t1.nyusatsu_type, t1.anken_no, t1.anken_url, t1.anken_name, t1.keishu_cd, t1.keishu_name, t1.public_flag, t1.company_area, t1.anken_open_date, t1.anken_close_date, t1.tender_date, t1.tender_place, t1.limit_date, t1.gyoumu_kbn_1, t1.gyoumu_kbn_2, t1.kasitu_name, t1.tanto_name, t1.notes, t1.result_open_date, t1.result_close_date, t1.raku_name, t1.price, t1.version_no, t1.delete_flag, t1.ins_date, t1.upd_date, t1.registration_no, t1.site_name FROM t_tenders t1 WHERE (t1.registration_no = (SELECT max(t2.registration_no) AS max FROM t_tenders t2 WHERE ((t2.site_name)::text = 'ekimu'::text))) UNION ALL SELECT t1.id, t1.nyusatsu_system, t1.nyusatsu_type, t1.anken_no, t1.anken_url, t1.anken_name, t1.keishu_cd, t1.keishu_name, t1.public_flag, t1.company_area, t1.anken_open_date, t1.anken_close_date, t1.tender_date, t1.tender_place, t1.limit_date, t1.gyoumu_kbn_1, t1.gyoumu_kbn_2, t1.kasitu_name, t1.tanto_name, t1.notes, t1.result_open_date, t1.result_close_date, t1.raku_name, t1.price, t1.version_no, t1.delete_flag, t1.ins_date, t1.upd_date, t1.registration_no, t1.site_name FROM t_tenders t1 WHERE (t1.registration_no = (SELECT max(t2.registration_no) AS max FROM t_tenders t2 WHERE ((t2.site_name)::text = 'ekimu2'::text)));


ALTER TABLE v_latest_tenders OWNER TO nyusatsu_check;

--
-- TOC entry 144 (class 1259 OID 16572)
-- Name: v_raku_name; Type: VIEW; Schema: public; Owner: nyusatsu_check
--

CREATE VIEW v_raku_name AS
SELECT t_tenders.raku_name FROM t_tenders GROUP BY t_tenders.raku_name HAVING ((t_tenders.raku_name IS NOT NULL) AND ((t_tenders.raku_name)::text <> ''::text));


ALTER TABLE v_raku_name OWNER TO nyusatsu_check;

--
-- TOC entry 145 (class 1259 OID 16576)
-- Name: v_raku_name_year; Type: VIEW; Schema: public; Owner: nyusatsu_check
--

CREATE VIEW v_raku_name_year AS
SELECT t_tenders.raku_name, to_char(t_tenders.limit_date, 'yyyy'::text) AS l_year FROM t_tenders GROUP BY to_char(t_tenders.limit_date, 'yyyy'::text), t_tenders.raku_name HAVING ((t_tenders.raku_name IS NOT NULL) AND ((t_tenders.raku_name)::text <> ''::text));


ALTER TABLE v_raku_name_year OWNER TO nyusatsu_check;

--
-- TOC entry 1711 (class 2606 OID 16581)
-- Name: j_histories_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY j_histories
    ADD CONSTRAINT j_histories_pkey PRIMARY KEY (id);


--
-- TOC entry 1713 (class 2606 OID 16583)
-- Name: j_nyusatsu_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY j_nyusatsu
    ADD CONSTRAINT j_nyusatsu_pkey PRIMARY KEY (id);


--
-- TOC entry 1715 (class 2606 OID 16585)
-- Name: t_nyusatsu_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY t_nyusatsu
    ADD CONSTRAINT t_nyusatsu_pkey PRIMARY KEY (id);


--
-- TOC entry 1717 (class 2606 OID 16587)
-- Name: t_tenders_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY t_tenders
    ADD CONSTRAINT t_tenders_pkey PRIMARY KEY (id);


--
-- TOC entry 1813 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2015-03-02 10:02:24

--
-- PostgreSQL database dump complete
--

