--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Attachment; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Attachment" (
    attach_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    message_id integer NOT NULL,
    type text NOT NULL,
    url text NOT NULL,
    size double precision NOT NULL
);


ALTER TABLE public."Attachment" OWNER TO matveyturkov;

--
-- Name: Attachment_attach_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Attachment_attach_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachment_attach_id_seq" OWNER TO matveyturkov;

--
-- Name: Attachment_attach_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Attachment_attach_id_seq" OWNED BY public."Attachment".attach_id;


--
-- Name: Attachment_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Attachment_chat_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachment_chat_id_seq" OWNER TO matveyturkov;

--
-- Name: Attachment_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Attachment_chat_id_seq" OWNED BY public."Attachment".chat_id;


--
-- Name: Attachment_message_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Attachment_message_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachment_message_id_seq" OWNER TO matveyturkov;

--
-- Name: Attachment_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Attachment_message_id_seq" OWNED BY public."Attachment".message_id;


--
-- Name: Attachment_user_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Attachment_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Attachment_user_id_seq" OWNER TO matveyturkov;

--
-- Name: Attachment_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Attachment_user_id_seq" OWNED BY public."Attachment".user_id;


--
-- Name: Chat; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Chat" (
    chat_id integer NOT NULL,
    is_group_chat boolean NOT NULL,
    last_message integer NOT NULL,
    name text,
    unread integer,
    key integer,
    avatar text,
    user_id integer
);


ALTER TABLE public."Chat" OWNER TO matveyturkov;

--
-- Name: Chat_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Chat_chat_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Chat_chat_id_seq" OWNER TO matveyturkov;

--
-- Name: Chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Chat_chat_id_seq" OWNED BY public."Chat".chat_id;


--
-- Name: Chat_last_message_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Chat_last_message_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Chat_last_message_seq" OWNER TO matveyturkov;

--
-- Name: Chat_last_message_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Chat_last_message_seq" OWNED BY public."Chat".last_message;


--
-- Name: Member; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Member" (
    user_id integer NOT NULL,
    chat_id integer NOT NULL,
    last_unread_message_id integer NOT NULL
);


ALTER TABLE public."Member" OWNER TO matveyturkov;

--
-- Name: Member_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Member_chat_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Member_chat_id_seq" OWNER TO matveyturkov;

--
-- Name: Member_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Member_chat_id_seq" OWNED BY public."Member".chat_id;


--
-- Name: Member_last_unread_message_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Member_last_unread_message_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Member_last_unread_message_id_seq" OWNER TO matveyturkov;

--
-- Name: Member_last_unread_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Member_last_unread_message_id_seq" OWNED BY public."Member".last_unread_message_id;


--
-- Name: Member_user_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Member_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Member_user_id_seq" OWNER TO matveyturkov;

--
-- Name: Member_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Member_user_id_seq" OWNED BY public."Member".user_id;


--
-- Name: Message; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."Message" (
    message_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    content text NOT NULL,
    sent timestamp without time zone NOT NULL
);


ALTER TABLE public."Message" OWNER TO matveyturkov;

--
-- Name: Message_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Message_chat_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Message_chat_id_seq" OWNER TO matveyturkov;

--
-- Name: Message_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Message_chat_id_seq" OWNED BY public."Message".chat_id;


--
-- Name: Message_message_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Message_message_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Message_message_id_seq" OWNER TO matveyturkov;

--
-- Name: Message_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Message_message_id_seq" OWNED BY public."Message".message_id;


--
-- Name: Message_user_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."Message_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Message_user_id_seq" OWNER TO matveyturkov;

--
-- Name: Message_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."Message_user_id_seq" OWNED BY public."Message".user_id;


--
-- Name: User; Type: TABLE; Schema: public; Owner: matveyturkov
--

CREATE TABLE public."User" (
    user_id integer NOT NULL,
    name text NOT NULL,
    nick text NOT NULL,
    avatar text
);


ALTER TABLE public."User" OWNER TO matveyturkov;

--
-- Name: User_user_id_seq; Type: SEQUENCE; Schema: public; Owner: matveyturkov
--

CREATE SEQUENCE public."User_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."User_user_id_seq" OWNER TO matveyturkov;

--
-- Name: User_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: matveyturkov
--

ALTER SEQUENCE public."User_user_id_seq" OWNED BY public."User".user_id;


--
-- Name: Attachment attach_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment" ALTER COLUMN attach_id SET DEFAULT nextval('public."Attachment_attach_id_seq"'::regclass);


--
-- Name: Attachment chat_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment" ALTER COLUMN chat_id SET DEFAULT nextval('public."Attachment_chat_id_seq"'::regclass);


--
-- Name: Attachment user_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment" ALTER COLUMN user_id SET DEFAULT nextval('public."Attachment_user_id_seq"'::regclass);


--
-- Name: Attachment message_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment" ALTER COLUMN message_id SET DEFAULT nextval('public."Attachment_message_id_seq"'::regclass);


--
-- Name: Chat chat_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat" ALTER COLUMN chat_id SET DEFAULT nextval('public."Chat_chat_id_seq"'::regclass);


--
-- Name: Chat last_message; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat" ALTER COLUMN last_message SET DEFAULT nextval('public."Chat_last_message_seq"'::regclass);


--
-- Name: Member user_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member" ALTER COLUMN user_id SET DEFAULT nextval('public."Member_user_id_seq"'::regclass);


--
-- Name: Member chat_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member" ALTER COLUMN chat_id SET DEFAULT nextval('public."Member_chat_id_seq"'::regclass);


--
-- Name: Member last_unread_message_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member" ALTER COLUMN last_unread_message_id SET DEFAULT nextval('public."Member_last_unread_message_id_seq"'::regclass);


--
-- Name: Message message_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message" ALTER COLUMN message_id SET DEFAULT nextval('public."Message_message_id_seq"'::regclass);


--
-- Name: Message chat_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message" ALTER COLUMN chat_id SET DEFAULT nextval('public."Message_chat_id_seq"'::regclass);


--
-- Name: Message user_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message" ALTER COLUMN user_id SET DEFAULT nextval('public."Message_user_id_seq"'::regclass);


--
-- Name: User user_id; Type: DEFAULT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User" ALTER COLUMN user_id SET DEFAULT nextval('public."User_user_id_seq"'::regclass);


--
-- Data for Name: Attachment; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Attachment" (attach_id, chat_id, user_id, message_id, type, url, size) FROM stdin;
\.


--
-- Data for Name: Chat; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Chat" (chat_id, is_group_chat, last_message, name, unread, key, avatar, user_id) FROM stdin;
6765	f	15931	Todd	0	80	\N	4665
8903	f	44850	Fred	0	80	\N	4665
6038	f	21979	Fred	0	68	\N	626
8688	f	31478	Jack	0	68	\N	626
6731	f	15179	Jack	0	11	\N	4797
9672	f	29360	Todd	0	11	\N	4797
5214	f	11111	Jack	0	9	\N	2236
8294	f	48934	Fred	0	9	\N	2236
6564	f	21189	Sam	0	75	\N	4348
8830	f	26148	Glen	0	75	\N	4348
\.


--
-- Data for Name: Member; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Member" (user_id, chat_id, last_unread_message_id) FROM stdin;
\.


--
-- Data for Name: Message; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."Message" (message_id, chat_id, user_id, content, sent) FROM stdin;
105294	6765	4665	stupid	2019-03-19 16:20:23
76419	6765	4665	fine	2019-03-22 17:21:27
86239	6765	4665	i love it	2019-03-18 16:20:22
63814	6765	4665	fine	2019-03-20 16:20:24
100488	6765	4665	good morning	2019-03-21 16:21:21
71591	6765	4665	so do i	2019-03-18 16:20:18
84945	6765	4665	super	2019-03-22 16:20:18
86687	6765	4665	hi	2019-03-22 16:20:24
88321	6765	4665	ok	2019-03-20 16:21:25
15931	6765	4665	so do i	2019-03-18 16:20:22
52086	8903	4665	sorry	2019-03-20 16:20:19
54765	8903	4665	fine	2019-03-21 16:20:26
68402	8903	4665	so do i	2019-03-22 17:20:24
77672	8903	4665	asap	2019-03-19 16:21:23
84613	8903	4665	see you	2019-03-22 17:21:24
102070	8903	4665	i love it	2019-03-21 17:20:23
69210	8903	4665	i love it	2019-03-21 17:20:20
103163	8903	4665	U fine?	2019-03-22 16:20:20
90514	8903	4665	fine	2019-03-20 17:20:22
44850	8903	4665	4fun	2019-03-21 16:20:18
72496	6038	626	hahahahaha	2019-03-20 17:20:25
80234	6038	626	ok	2019-03-20 17:21:20
99900	6038	626	so do i	2019-03-20 16:21:27
69499	6038	626	asap	2019-03-18 16:21:27
87736	6038	626	acab	2019-03-20 17:21:18
93682	6038	626	lol	2019-03-19 17:21:21
60951	6038	626	not funny	2019-03-18 16:21:27
85967	6038	626	lol	2019-03-21 16:21:20
93601	6038	626	acab	2019-03-22 16:20:19
21979	6038	626	bye	2019-03-22 17:20:27
109100	8688	626	bye	2019-03-21 16:20:20
88660	8688	626	lmao	2019-03-20 16:21:27
113880	8688	626	how are you	2019-03-19 17:21:24
113724	8688	626	sorry	2019-03-18 16:21:27
102962	8688	626	ok	2019-03-20 16:21:23
98813	8688	626	jk	2019-03-20 17:21:22
50762	8688	626	lmao	2019-03-21 17:21:22
56609	8688	626	good morning	2019-03-19 16:20:25
68319	8688	626	bye	2019-03-18 16:20:28
31478	8688	626	acab	2019-03-21 17:20:20
101560	6731	4797	super	2019-03-22 17:21:28
72757	6731	4797	4fun	2019-03-19 16:21:28
94579	6731	4797	good morning	2019-03-21 17:20:21
95337	6731	4797	acab	2019-03-18 16:20:25
102281	6731	4797	good morning	2019-03-19 17:20:20
64671	6731	4797	not funny	2019-03-19 16:21:28
58868	6731	4797	stupid	2019-03-21 16:20:26
87305	6731	4797	U fine?	2019-03-21 16:20:22
116116	6731	4797	bye	2019-03-22 17:21:19
15179	6731	4797	bye	2019-03-21 16:20:19
80172	9672	4797	lol	2019-03-21 16:20:26
60815	9672	4797	bye	2019-03-22 16:20:25
65766	9672	4797	whats up	2019-03-19 17:20:19
90933	9672	4797	jk	2019-03-20 16:21:23
84565	9672	4797	i love it	2019-03-22 17:20:20
106484	9672	4797	i h8 u	2019-03-18 17:21:19
109663	9672	4797	so do i	2019-03-22 17:21:20
75648	9672	4797	not funny	2019-03-19 16:21:22
113614	9672	4797	good morning	2019-03-18 16:21:23
29360	9672	4797	sorry	2019-03-19 17:21:28
68265	5214	2236	sorry	2019-03-18 16:20:21
96225	5214	2236	acab	2019-03-20 16:21:24
64614	5214	2236	4fun	2019-03-20 17:21:20
92354	5214	2236	4fun	2019-03-20 16:20:23
113794	5214	2236	whats up	2019-03-22 16:21:20
76945	5214	2236	good morning	2019-03-18 16:20:20
77394	5214	2236	thnx	2019-03-22 17:20:21
70262	5214	2236	acab	2019-03-19 16:20:21
65935	5214	2236	jk	2019-03-19 16:20:22
11111	5214	2236	strange	2019-03-22 17:21:22
101802	8294	2236	not funny	2019-03-18 16:21:26
98887	8294	2236	so do i	2019-03-19 17:20:22
106370	8294	2236	bye	2019-03-21 17:21:22
85430	8294	2236	fine	2019-03-20 16:21:27
87191	8294	2236	hahahahaha	2019-03-21 17:20:28
73410	8294	2236	super	2019-03-20 17:20:26
58683	8294	2236	hi	2019-03-19 17:21:19
102609	8294	2236	ok	2019-03-20 16:20:22
88963	8294	2236	hahahahaha	2019-03-22 16:21:25
48934	8294	2236	so do i	2019-03-18 16:21:28
92056	6564	4348	lol	2019-03-18 16:20:24
52074	6564	4348	acab	2019-03-19 16:20:21
54010	6564	4348	4fun	2019-03-20 16:21:20
107354	6564	4348	stupid	2019-03-22 16:20:27
51096	6564	4348	how are you	2019-03-18 16:21:25
98250	6564	4348	see you	2019-03-20 16:21:24
74102	6564	4348	acab	2019-03-21 16:21:19
94675	6564	4348	lmao	2019-03-19 17:21:20
110808	6564	4348	asap	2019-03-21 16:21:28
21189	6564	4348	i love it	2019-03-19 16:21:28
95597	8830	4348	asap	2019-03-19 16:21:28
93933	8830	4348	not funny	2019-03-18 17:20:28
101997	8830	4348	lmao	2019-03-19 17:21:21
75661	8830	4348	fine	2019-03-22 16:21:25
59749	8830	4348	i h8 u	2019-03-22 17:20:25
89219	8830	4348	ok	2019-03-19 16:21:20
62459	8830	4348	sorry	2019-03-20 16:20:28
59079	8830	4348	4fun	2019-03-22 16:20:28
55017	8830	4348	so do i	2019-03-18 17:20:20
26148	8830	4348	sorry	2019-03-20 17:21:27
\.


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: matveyturkov
--

COPY public."User" (user_id, name, nick, avatar) FROM stdin;
4665	Jack	jack237	\N
626	Sam	helo2	\N
4797	Glen	username	\N
2236	Todd	123456qwerty	\N
4348	Fred	frog	\N
\.


--
-- Name: Attachment_attach_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Attachment_attach_id_seq"', 1, false);


--
-- Name: Attachment_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Attachment_chat_id_seq"', 1, false);


--
-- Name: Attachment_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Attachment_message_id_seq"', 1, false);


--
-- Name: Attachment_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Attachment_user_id_seq"', 1, false);


--
-- Name: Chat_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Chat_chat_id_seq"', 9, true);


--
-- Name: Chat_last_message_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Chat_last_message_seq"', 9, true);


--
-- Name: Member_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Member_chat_id_seq"', 1, false);


--
-- Name: Member_last_unread_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Member_last_unread_message_id_seq"', 1, false);


--
-- Name: Member_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Member_user_id_seq"', 1, false);


--
-- Name: Message_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Message_chat_id_seq"', 4, true);


--
-- Name: Message_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Message_message_id_seq"', 4, true);


--
-- Name: Message_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."Message_user_id_seq"', 4, true);


--
-- Name: User_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: matveyturkov
--

SELECT pg_catalog.setval('public."User_user_id_seq"', 1, false);


--
-- Name: User User_nick_key; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_nick_key" UNIQUE (nick);


--
-- Name: Attachment attachment_pk; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment"
    ADD CONSTRAINT attachment_pk PRIMARY KEY (attach_id);


--
-- Name: Chat chat_pk; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT chat_pk PRIMARY KEY (chat_id);


--
-- Name: Message message_pk; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT message_pk PRIMARY KEY (message_id);


--
-- Name: User user_pk; Type: CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT user_pk PRIMARY KEY (user_id);


--
-- Name: Attachment Attachment_fk0; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment"
    ADD CONSTRAINT "Attachment_fk0" FOREIGN KEY (chat_id) REFERENCES public."Chat"(chat_id);


--
-- Name: Attachment Attachment_fk1; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment"
    ADD CONSTRAINT "Attachment_fk1" FOREIGN KEY (user_id) REFERENCES public."User"(user_id);


--
-- Name: Attachment Attachment_fk2; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Attachment"
    ADD CONSTRAINT "Attachment_fk2" FOREIGN KEY (message_id) REFERENCES public."Message"(message_id);


--
-- Name: Member Member_fk0; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_fk0" FOREIGN KEY (user_id) REFERENCES public."User"(user_id);


--
-- Name: Member Member_fk1; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_fk1" FOREIGN KEY (chat_id) REFERENCES public."Chat"(chat_id);


--
-- Name: Member Member_fk2; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_fk2" FOREIGN KEY (last_unread_message_id) REFERENCES public."Message"(message_id);


--
-- Name: Message Message_fk0; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_fk0" FOREIGN KEY (chat_id) REFERENCES public."Chat"(chat_id);


--
-- Name: Message Message_fk1; Type: FK CONSTRAINT; Schema: public; Owner: matveyturkov
--

ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_fk1" FOREIGN KEY (user_id) REFERENCES public."User"(user_id);


--
-- PostgreSQL database dump complete
--

