

CREATE TABLE IF NOT EXISTS users (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
email text NOT NULL,
psw text NOT NULL,
avatar BLOB DEFAULT NULL,
comments_numb integer,
time integer NOT NULL
);

CREATE TABLE IF NOT EXISTS mfk (
id integer PRIMARY KEY AUTOINCREMENT,
name text,
faculty text,
desc text,
online text,
openclose text,
score text,
score_numb integer
);


CREATE TABLE IF NOT EXISTS comments (
id integer PRIMARY KEY AUTOINCREMENT,
username text,
mfkname text,
score text,
mfktitle text,
reason text
);
