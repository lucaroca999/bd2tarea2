--
-- PostgreSQL database dump
--

\restrict xsK1w2Bj4vOvKdgBkn8VryH3anVnKHirOJPsDPo2KdcNDH1NklNdzFRy1NgXnlX

-- Dumped from database version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: loanstatus; Type: TYPE; Schema: public; Owner: -
--

CREATE TYPE public.loanstatus AS ENUM (
    'ACTIVE',
    'RETURNED',
    'OVERDUE'
);


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: book_categories; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.book_categories (
    book_id integer NOT NULL,
    category_id integer NOT NULL
);


--
-- Name: books; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.books (
    id bigint NOT NULL,
    title character varying NOT NULL,
    author character varying NOT NULL,
    isbn character varying NOT NULL,
    pages integer NOT NULL,
    published_year integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    stock integer DEFAULT 1 NOT NULL,
    description character varying,
    language character varying NOT NULL,
    publisher character varying
);


--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.books_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.categories (
    id bigint NOT NULL,
    name character varying NOT NULL,
    description character varying,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: loans; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.loans (
    id bigint NOT NULL,
    loan_dt date NOT NULL,
    return_dt date,
    user_id bigint NOT NULL,
    book_id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    status public.loanstatus DEFAULT 'ACTIVE'::public.loanstatus NOT NULL,
    due_date date NOT NULL,
    fine_amount numeric(10,2)
);


--
-- Name: loans_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.loans_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: loans_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.loans_id_seq OWNED BY public.loans.id;


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reviews (
    id bigint NOT NULL,
    rating integer NOT NULL,
    comment character varying NOT NULL,
    review_date date NOT NULL,
    user_id bigint NOT NULL,
    book_id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);


--
-- Name: reviews_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reviews_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reviews_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reviews_id_seq OWNED BY public.reviews.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying NOT NULL,
    fullname character varying NOT NULL,
    password character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    email character varying NOT NULL,
    phone character varying,
    address character varying,
    is_active boolean NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: loans id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.loans ALTER COLUMN id SET DEFAULT nextval('public.loans_id_seq'::regclass);


--
-- Name: reviews id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews ALTER COLUMN id SET DEFAULT nextval('public.reviews_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alembic_version (version_num) FROM stdin;
220beed3b601
\.


--
-- Data for Name: book_categories; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.book_categories (book_id, category_id) FROM stdin;
8	4
3	3
3	5
1	2
1	5
2	5
2	4
6	2
9	4
9	3
4	4
4	5
7	3
7	4
10	5
10	4
5	4
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.books (id, title, author, isbn, pages, published_year, created_at, updated_at, stock, description, language, publisher) FROM stdin;
1	Libro 1	Autor 1	ISBN-BD2-2025-1120	306	2001	2026-01-06 11:55:53.818324-03	2026-01-06 11:55:53.818329-03	5	Descripción genérica del libro.	es	Editorial UMAG
2	Libro 2	Autor 2	ISBN-BD2-2025-1125	293	1958	2026-01-06 11:55:53.81833-03	2026-01-06 11:55:53.81833-03	5	Descripción genérica del libro.	es	Editorial UMAG
3	Libro 3	Autor 3	ISBN-BD2-2025-1130	307	2000	2026-01-06 11:55:53.818331-03	2026-01-06 11:55:53.818332-03	5	Descripción genérica del libro.	es	Editorial UMAG
4	Libro 4	Autor 4	ISBN-BD2-2025-1135	266	1950	2026-01-06 11:55:53.818333-03	2026-01-06 11:55:53.818333-03	5	Descripción genérica del libro.	es	Editorial UMAG
5	Libro 5	Autor 5	ISBN-BD2-2025-1140	286	1967	2026-01-06 11:55:53.818334-03	2026-01-06 11:55:53.818335-03	5	Descripción genérica del libro.	es	Editorial UMAG
6	Libro 6	Autor 6	ISBN-BD2-2025-1145	337	1950	2026-01-06 11:55:53.818335-03	2026-01-06 11:55:53.818336-03	5	Descripción genérica del libro.	es	Editorial UMAG
7	Libro 7	Autor 7	ISBN-BD2-2025-1150	419	1990	2026-01-06 11:55:53.818337-03	2026-01-06 11:55:53.818338-03	5	Descripción genérica del libro.	es	Editorial UMAG
8	Libro 8	Autor 8	ISBN-BD2-2025-1155	344	1951	2026-01-06 11:55:53.818338-03	2026-01-06 11:55:53.818339-03	5	Descripción genérica del libro.	es	Editorial UMAG
9	Libro 9	Autor 9	ISBN-BD2-2025-1160	417	1989	2026-01-06 11:55:53.81834-03	2026-01-06 11:55:53.818341-03	5	Descripción genérica del libro.	es	Editorial UMAG
10	Libro 10	Autor 10	ISBN-BD2-2025-1165	395	1957	2026-01-06 11:55:53.818341-03	2026-01-06 11:55:53.818342-03	5	Descripción genérica del libro.	es	Editorial UMAG
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.categories (id, name, description, created_at, updated_at) FROM stdin;
1	Ficción	Libros de tipo Ficción	2026-01-06 11:55:53.813227-03	2026-01-06 11:55:53.813232-03
2	No Ficción	Libros de tipo No Ficción	2026-01-06 11:55:53.813234-03	2026-01-06 11:55:53.813235-03
3	Ciencia	Libros de tipo Ciencia	2026-01-06 11:55:53.813235-03	2026-01-06 11:55:53.813236-03
4	Historia	Libros de tipo Historia	2026-01-06 11:55:53.813237-03	2026-01-06 11:55:53.813238-03
5	Fantasía	Libros de tipo Fantasía	2026-01-06 11:55:53.813238-03	2026-01-06 11:55:53.813239-03
\.


--
-- Data for Name: loans; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.loans (id, loan_dt, return_dt, user_id, book_id, created_at, updated_at, status, due_date, fine_amount) FROM stdin;
1	2026-01-04	\N	1	1	2026-01-06 11:55:53.906117-03	2026-01-06 11:55:53.90612-03	ACTIVE	2026-01-18	\N
2	2026-01-04	\N	2	2	2026-01-06 11:55:53.906121-03	2026-01-06 11:55:53.906122-03	ACTIVE	2026-01-18	\N
3	2026-01-04	\N	3	3	2026-01-06 11:55:53.906123-03	2026-01-06 11:55:53.906123-03	ACTIVE	2026-01-18	\N
4	2025-12-17	2025-12-27	1	4	2026-01-06 11:55:53.906124-03	2026-01-06 11:55:53.906125-03	RETURNED	2025-12-31	0.00
5	2025-12-17	2025-12-27	2	5	2026-01-06 11:55:53.906126-03	2026-01-06 11:55:53.906126-03	RETURNED	2025-12-31	0.00
6	2025-12-17	2025-12-27	3	6	2026-01-06 11:55:53.906127-03	2026-01-06 11:55:53.906128-03	RETURNED	2025-12-31	0.00
7	2025-12-07	\N	5	7	2026-01-06 11:55:53.906129-03	2026-01-06 11:55:53.906129-03	OVERDUE	2025-12-21	\N
8	2025-12-07	\N	5	8	2026-01-06 11:55:53.90613-03	2026-01-06 11:55:53.906131-03	OVERDUE	2025-12-21	\N
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.reviews (id, rating, comment, review_date, user_id, book_id, created_at, updated_at) FROM stdin;
1	3	Regular.	2025-12-05	4	10	2026-01-06 11:55:53.912868-03	2026-01-06 11:55:53.912872-03
2	4	Regular.	2025-12-04	1	7	2026-01-06 11:55:53.915068-03	2026-01-06 11:55:53.915071-03
3	3	Regular.	2025-12-27	2	8	2026-01-06 11:55:53.916601-03	2026-01-06 11:55:53.916603-03
4	4	Regular.	2025-12-20	2	2	2026-01-06 11:55:53.91809-03	2026-01-06 11:55:53.918093-03
5	2	Regular.	2025-11-15	3	4	2026-01-06 11:55:53.919445-03	2026-01-06 11:55:53.919447-03
6	2	Muy bueno.	2025-12-05	4	4	2026-01-06 11:55:53.921565-03	2026-01-06 11:55:53.921569-03
7	3	Regular.	2025-12-23	3	3	2026-01-06 11:55:53.923127-03	2026-01-06 11:55:53.923129-03
8	1	Regular.	2025-11-12	3	5	2026-01-06 11:55:53.924514-03	2026-01-06 11:55:53.924516-03
9	4	Muy bueno.	2025-12-23	5	5	2026-01-06 11:55:53.925784-03	2026-01-06 11:55:53.925785-03
10	2	Muy bueno.	2025-12-07	1	2	2026-01-06 11:55:53.927155-03	2026-01-06 11:55:53.927157-03
11	1	Muy bueno.	2025-12-16	5	6	2026-01-06 11:55:53.928303-03	2026-01-06 11:55:53.928305-03
12	4	Regular.	2025-12-28	1	8	2026-01-06 11:55:53.929981-03	2026-01-06 11:55:53.929983-03
13	5	Muy bueno.	2025-12-10	5	10	2026-01-06 11:55:53.930985-03	2026-01-06 11:55:53.930987-03
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, username, fullname, password, created_at, updated_at, email, phone, address, is_active) FROM stdin;
1	user1	Usuario Prueba 1	$argon2id$v=19$m=65536,t=3,p=4$4guyYu5FLsZ2coWhn4NW2A$JCgoTHHE9+P0Dtfyb2lmmwDY4N3jNDYKnR+XySrO+mg	2026-01-06 11:55:53.899868-03	2026-01-06 11:55:53.899872-03	user1@example.com	+56912345670	Calle 123	t
2	user2	Usuario Prueba 2	$argon2id$v=19$m=65536,t=3,p=4$4guyYu5FLsZ2coWhn4NW2A$JCgoTHHE9+P0Dtfyb2lmmwDY4N3jNDYKnR+XySrO+mg	2026-01-06 11:55:53.899873-03	2026-01-06 11:55:53.899873-03	user2@example.com	+56912345671	Calle 124	t
3	user3	Usuario Prueba 3	$argon2id$v=19$m=65536,t=3,p=4$4guyYu5FLsZ2coWhn4NW2A$JCgoTHHE9+P0Dtfyb2lmmwDY4N3jNDYKnR+XySrO+mg	2026-01-06 11:55:53.899874-03	2026-01-06 11:55:53.899875-03	user3@example.com	+56912345672	Calle 125	t
4	user4	Usuario Prueba 4	$argon2id$v=19$m=65536,t=3,p=4$4guyYu5FLsZ2coWhn4NW2A$JCgoTHHE9+P0Dtfyb2lmmwDY4N3jNDYKnR+XySrO+mg	2026-01-06 11:55:53.899876-03	2026-01-06 11:55:53.899876-03	user4@example.com	+56912345673	Calle 126	t
5	user5	Usuario Prueba 5	$argon2id$v=19$m=65536,t=3,p=4$4guyYu5FLsZ2coWhn4NW2A$JCgoTHHE9+P0Dtfyb2lmmwDY4N3jNDYKnR+XySrO+mg	2026-01-06 11:55:53.899877-03	2026-01-06 11:55:53.899878-03	user5@example.com	+56912345674	Calle 127	t
\.


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.books_id_seq', 10, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.categories_id_seq', 5, true);


--
-- Name: loans_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.loans_id_seq', 8, true);


--
-- Name: reviews_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reviews_id_seq', 13, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: book_categories pk_book_categories; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book_categories
    ADD CONSTRAINT pk_book_categories PRIMARY KEY (book_id, category_id);


--
-- Name: books pk_books; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT pk_books PRIMARY KEY (id);


--
-- Name: categories pk_categories; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT pk_categories PRIMARY KEY (id);


--
-- Name: loans pk_loans; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.loans
    ADD CONSTRAINT pk_loans PRIMARY KEY (id);


--
-- Name: reviews pk_reviews; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT pk_reviews PRIMARY KEY (id);


--
-- Name: users pk_users; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT pk_users PRIMARY KEY (id);


--
-- Name: books uq_books_isbn; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT uq_books_isbn UNIQUE (isbn);


--
-- Name: books uq_books_title; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT uq_books_title UNIQUE (title);


--
-- Name: categories uq_categories_name; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT uq_categories_name UNIQUE (name);


--
-- Name: users uq_users_email; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT uq_users_email UNIQUE (email);


--
-- Name: users uq_users_username; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT uq_users_username UNIQUE (username);


--
-- Name: book_categories fk_book_categories_book_id_books; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book_categories
    ADD CONSTRAINT fk_book_categories_book_id_books FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: book_categories fk_book_categories_category_id_categories; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book_categories
    ADD CONSTRAINT fk_book_categories_category_id_categories FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- Name: loans fk_loans_book_id_books; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.loans
    ADD CONSTRAINT fk_loans_book_id_books FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: loans fk_loans_user_id_users; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.loans
    ADD CONSTRAINT fk_loans_user_id_users FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: reviews fk_reviews_book_id_books; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT fk_reviews_book_id_books FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: reviews fk_reviews_user_id_users; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT fk_reviews_user_id_users FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict xsK1w2Bj4vOvKdgBkn8VryH3anVnKHirOJPsDPo2KdcNDH1NklNdzFRy1NgXnlX

