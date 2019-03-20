--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Attachment; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Attachment" (
    id integer NOT NULL,
    type character varying(20) NOT NULL,
    size integer NOT NULL
);


ALTER TABLE public."Attachment" OWNER TO matveyturkov;

--
-- Name: Attachment_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Attachment_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachment_id_seq" OWNER TO matveyturkov;

--
-- Name: Attachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Attachment_id_seq" OWNED BY public."Attachment".id;


--
-- Name: Chat; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Chat" (
    id integer NOT NULL,
    is_group_chat boolean,
    name character varying(100) NOT NULL,
    unread integer,
    key integer,
    avatar character varying(100)
);


ALTER TABLE public."Chat" OWNER TO matveyturkov;

--
-- Name: Chat_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Chat_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Chat_id_seq" OWNER TO matveyturkov;

--
-- Name: Chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Chat_id_seq" OWNED BY public."Chat".id;


--
-- Name: Member; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Member" (
    id integer NOT NULL,
    user_id integer NOT NULL,
    chat_id integer NOT NULL,
    last_unread_message_id integer NOT NULL
);


ALTER TABLE public."Member" OWNER TO matveyturkov;

--
-- Name: Member_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Member_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Member_id_seq" OWNER TO matveyturkov;

--
-- Name: Member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Member_id_seq" OWNED BY public."Member".id;


--
-- Name: Message; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Message" (
    id integer NOT NULL,
    content character varying(500) NOT NULL,
    sent timestamp without time zone NOT NULL
);


ALTER TABLE public."Message" OWNER TO matveyturkov;

--
-- Name: Message_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Message_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Message_id_seq" OWNER TO matveyturkov;

--
-- Name: Message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Message_id_seq" OWNED BY public."Message".id;


--
-- Name: User; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."User" (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    nick character varying(100) NOT NULL,
    avatar character varying(100)
);


ALTER TABLE public."User" OWNER TO matveyturkov;

--
-- Name: User_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."User_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."User_id_seq" OWNER TO matveyturkov;

--
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."User_id_seq" OWNED BY public."User".id;


--
-- Name: Attachment id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment" ALTER COLUMN id SET DEFAULT nextval('public."Attachment_id_seq"'::regclass);


--
-- Name: Chat id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat" ALTER COLUMN id SET DEFAULT nextval('public."Chat_id_seq"'::regclass);


--
-- Name: Member id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member" ALTER COLUMN id SET DEFAULT nextval('public."Member_id_seq"'::regclass);


--
-- Name: Message id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message" ALTER COLUMN id SET DEFAULT nextval('public."Message_id_seq"'::regclass);


--
-- Name: User id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User" ALTER COLUMN id SET DEFAULT nextval('public."User_id_seq"'::regclass);


--
-- Data for Name: Attachment; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Attachment" (id, type, size) FROM stdin;
\.


--
-- Data for Name: Chat; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Chat" (id, is_group_chat, name, unread, key, avatar) FROM stdin;
\.


--
-- Data for Name: Member; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Member" (id, user_id, chat_id, last_unread_message_id) FROM stdin;
\.


--
-- Data for Name: Message; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Message" (id, content, sent) FROM stdin;
\.


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."User" (id, name, nick, avatar) FROM stdin;
\.


--
-- Name: Attachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Attachment_id_seq"', 1, false);


--
-- Name: Chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Chat_id_seq"', 1, false);


--
-- Name: Member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Member_id_seq"', 1, false);


--
-- Name: Message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Message_id_seq"', 1, false);


--
-- Name: User_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."User_id_seq"', 1, false);


--
-- Name: Attachment Attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment"
    ADD CONSTRAINT "Attachment_pkey" PRIMARY KEY (id);


--
-- Name: Chat Chat_key_key; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT "Chat_key_key" UNIQUE (key);


--
-- Name: Chat Chat_pkey; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT "Chat_pkey" PRIMARY KEY (id);


--
-- Name: Member Member_pkey; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_pkey" PRIMARY KEY (id);


--
-- Name: Message Message_pkey; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_pkey" PRIMARY KEY (id);


--
-- Name: User User_nick_key; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_nick_key" UNIQUE (nick);


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- Name: Member Member_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_chat_id_fkey" FOREIGN KEY (chat_id) REFERENCES public."Chat"(id) ON DELETE CASCADE;


--
-- Name: Member Member_last_unread_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_last_unread_message_id_fkey" FOREIGN KEY (last_unread_message_id) REFERENCES public."Message"(id) ON DELETE CASCADE;


--
-- Name: Member Member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_user_id_fkey" FOREIGN KEY (user_id) REFERENCES public."User"(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

