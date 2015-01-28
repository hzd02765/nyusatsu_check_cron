--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: j_histories; Type: TABLE; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

CREATE TABLE j_histories (
    id integer NOT NULL,
    process_start timestamp without time zone,
    process_end timestamp without time zone,
    process_seconds integer,
    count_tenders integer
);


ALTER TABLE public.j_histories OWNER TO nyusatsu_check;

--
-- Name: TABLE j_histories; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE j_histories IS '更新履歴';


--
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
    upd_date timestamp without time zone
);


ALTER TABLE public.j_nyusatsu OWNER TO nyusatsu_check;

--
-- Name: TABLE j_nyusatsu; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE j_nyusatsu IS '役務入札案件の履歴';


--
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


ALTER TABLE public.t_nyusatsu OWNER TO nyusatsu_check;

--
-- Name: TABLE t_nyusatsu; Type: COMMENT; Schema: public; Owner: nyusatsu_check
--

COMMENT ON TABLE t_nyusatsu IS '現在HPで表示されている、役務入札案件';


--
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
    upd_date timestamp without time zone
);


ALTER TABLE public.t_tenders OWNER TO nyusatsu_check;

--
-- Name: v_raku_name; Type: VIEW; Schema: public; Owner: nyusatsu_check
--

CREATE VIEW v_raku_name AS
    SELECT t_tenders.raku_name FROM t_tenders GROUP BY t_tenders.raku_name HAVING ((t_tenders.raku_name IS NOT NULL) AND ((t_tenders.raku_name)::text <> ''::text));


ALTER TABLE public.v_raku_name OWNER TO nyusatsu_check;

--
-- Name: v_raku_name_year; Type: VIEW; Schema: public; Owner: nyusatsu_check
--

CREATE VIEW v_raku_name_year AS
    SELECT t_tenders.raku_name, to_char(t_tenders.limit_date, 'yyyy'::text) AS l_year FROM t_tenders GROUP BY to_char(t_tenders.limit_date, 'yyyy'::text), t_tenders.raku_name HAVING ((t_tenders.raku_name IS NOT NULL) AND ((t_tenders.raku_name)::text <> ''::text));


ALTER TABLE public.v_raku_name_year OWNER TO nyusatsu_check;

--
-- Name: j_histories_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY j_histories
    ADD CONSTRAINT j_histories_pkey PRIMARY KEY (id);


--
-- Name: j_nyusatsu_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY j_nyusatsu
    ADD CONSTRAINT j_nyusatsu_pkey PRIMARY KEY (id);


--
-- Name: t_nyusatsu_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY t_nyusatsu
    ADD CONSTRAINT t_nyusatsu_pkey PRIMARY KEY (id);


--
-- Name: t_tenders_pkey; Type: CONSTRAINT; Schema: public; Owner: nyusatsu_check; Tablespace: 
--

ALTER TABLE ONLY t_tenders
    ADD CONSTRAINT t_tenders_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

