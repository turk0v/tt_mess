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
    topic text NOT NULL,
    last_message integer NOT NULL
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

