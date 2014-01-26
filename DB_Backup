SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 179 (class 3079 OID 11750)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1973 (class 0 OID 0)
-- Dependencies: 179
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 174 (class 1259 OID 42225)
-- Name: age; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE age (
    _id character varying NOT NULL,
    _age character varying
);


ALTER TABLE public.age OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 42231)
-- Name: book; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE book (
    _id character varying NOT NULL,
    bookname character varying
);


ALTER TABLE public.book OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 42512)
-- Name: links; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE links (
    node1 character varying,
    node2 character varying
);


ALTER TABLE public.links OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 42237)
-- Name: std_book; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE std_book (
    _id character varying NOT NULL,
    std character varying,
    book character varying
);


ALTER TABLE public.std_book OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 42243)
-- Name: student; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE student (
    _id character varying NOT NULL,
    name character varying
);


ALTER TABLE public.student OWNER TO postgres;

--
-- TOC entry 1961 (class 0 OID 42225)
-- Dependencies: 174
-- Data for Name: age; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO age VALUES ('1', '19');
INSERT INTO age VALUES ('2', '19');
INSERT INTO age VALUES ('3', '20');
INSERT INTO age VALUES ('4', '20');
INSERT INTO age VALUES ('5', '21');
INSERT INTO age VALUES ('6', '21');
INSERT INTO age VALUES ('7', '22');


--
-- TOC entry 1962 (class 0 OID 42231)
-- Dependencies: 175
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO book VALUES ('1', 'book1');
INSERT INTO book VALUES ('2', 'book2');
INSERT INTO book VALUES ('3', 'book3');
INSERT INTO book VALUES ('4', 'book4');
INSERT INTO book VALUES ('5', 'book5');
INSERT INTO book VALUES ('6', 'book6');
INSERT INTO book VALUES ('7', 'book7');
INSERT INTO book VALUES ('8', 'book8');
INSERT INTO book VALUES ('9', 'book9');
INSERT INTO book VALUES ('10', 'book10');
INSERT INTO book VALUES ('11', 'book11');
INSERT INTO book VALUES ('12', 'book12');
INSERT INTO book VALUES ('13', 'book13');
INSERT INTO book VALUES ('14', 'book14');
INSERT INTO book VALUES ('15', 'book15');
INSERT INTO book VALUES ('16', 'book16');
INSERT INTO book VALUES ('17', 'book17');
INSERT INTO book VALUES ('18', 'book18');
INSERT INTO book VALUES ('19', 'book19');
INSERT INTO book VALUES ('20', 'book20');
INSERT INTO book VALUES ('21', 'book21');
INSERT INTO book VALUES ('22', 'book22');
INSERT INTO book VALUES ('23', 'book23');
INSERT INTO book VALUES ('24', 'book24');
INSERT INTO book VALUES ('25', 'book25');


--
-- TOC entry 1965 (class 0 OID 42512)
-- Dependencies: 178
-- Data for Name: links; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO links VALUES ('A', 'B');
INSERT INTO links VALUES ('B', 'C');
INSERT INTO links VALUES ('C', 'D');
INSERT INTO links VALUES ('C', 'E');
INSERT INTO links VALUES ('E', 'F');
INSERT INTO links VALUES ('D', 'G');
INSERT INTO links VALUES ('F', 'G');


--
-- TOC entry 1963 (class 0 OID 42237)
-- Dependencies: 176
-- Data for Name: std_book; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO std_book VALUES ('1', '1', '1');
INSERT INTO std_book VALUES ('2', '1', '2');
INSERT INTO std_book VALUES ('3', '1', '3');
INSERT INTO std_book VALUES ('4', '3', '4');
INSERT INTO std_book VALUES ('5', '4', '5');
INSERT INTO std_book VALUES ('6', '5', '6');


--
-- TOC entry 1964 (class 0 OID 42243)
-- Dependencies: 177
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO student VALUES ('1', 'student1');
INSERT INTO student VALUES ('2', 'student2');
INSERT INTO student VALUES ('10', 'student10');
INSERT INTO student VALUES ('3', 'student3');
INSERT INTO student VALUES ('4', 'student4');
INSERT INTO student VALUES ('5', 'student5');
INSERT INTO student VALUES ('6', 'student6');
INSERT INTO student VALUES ('7', 'student7');
INSERT INTO student VALUES ('8', 'student8');
INSERT INTO student VALUES ('9', 'student9');


--
-- TOC entry 1847 (class 2606 OID 42250)
-- Name: age_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY age
    ADD CONSTRAINT age_pkey PRIMARY KEY (_id);


--
-- TOC entry 1849 (class 2606 OID 42252)
-- Name: book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY book
    ADD CONSTRAINT book_pkey PRIMARY KEY (_id);


--
-- TOC entry 1851 (class 2606 OID 42254)
-- Name: std_book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY std_book
    ADD CONSTRAINT std_book_pkey PRIMARY KEY (_id);


--
-- TOC entry 1853 (class 2606 OID 42256)
-- Name: student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY student
    ADD CONSTRAINT student_pkey PRIMARY KEY (_id);


--
-- TOC entry 1972 (class 0 OID 0)
-- Dependencies: 6
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- TOC entry 1974 (class 0 OID 0)
-- Dependencies: 175
-- Name: book; Type: ACL; Schema: public; Owner: postgres
--

REVOKE ALL ON TABLE book FROM PUBLIC;
REVOKE ALL ON TABLE book FROM postgres;
GRANT ALL ON TABLE book TO postgres;
GRANT ALL ON TABLE book TO PUBLIC;


-- Completed on 2014-01-26 20:24:23

--
-- PostgreSQL database dump complete
--

