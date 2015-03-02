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