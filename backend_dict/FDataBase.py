import sqlite3
import math
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # def getMenu(self):
    #     sql = '''SELECT * FROM mainmenu'''
    #     try:
    #         self.__cur.execute(sql)
    #         res = self.__cur.fetchall()
    #         if res: return res
    #     except:
    #         print("Ошибка чтения из БД")
    #     return []
    #
    # def addPost(self, title, text, url):
    #     try:
    #         self.__cur.execute("SELECT COUNT() as `count` FROM posts WHERE url LIKE ?", (url,))
    #         res = self.__cur.fetchone()
    #         if res['count'] > 0:
    #             print("Статья с таким url уже существует")
    #             return False
    #
    #         tm = math.floor(time.time())
    #         self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
    #         self.__db.commit()
    #     except sqlite3.Error as e:
    #         print("Ошибка добавления статьи в БД " + str(e))
    #         return False
    #
    #     return True
    #
    # def getPost(self):
    #     try:
    #         self.__cur.execute(f"SELECT title, text FROM posts")
    #         res = self.__cur.fetchone()
    #         if res:
    #             return res
    #     except sqlite3.Error as e:
    #         print("Ошибка получения статьи из БД " + str(e))
    #
    #     return (False, False)

    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)", (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД " + str(e))
            return False

        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False

    def updateUserAvatar(self, avatar, user_id):
        if not avatar:
            return False

        try:
            binary = sqlite3.Binary(avatar)
            self.__cur.execute(f"UPDATE users SET avatar = ? WHERE id = ?", (binary, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка обновления аватара в БД: " + str(e))
            return False
        return True

    def getMfk(self, alias):
        try:
            self.__cur.execute(f"SELECT name, faculty, online FROM mfk WHERE id LIKE '{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return (False, False)

    def getMfkAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, name, faculty, online FROM mfk ORDER BY id DESC")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []


    def addComment(self, username, text, mfkname, score):
        try:
            # self.__cur.execute("SELECT COUNT() as `count` FROM comments WHERE url LIKE ?", (url,))
            # res = self.__cur.fetchone()
            # if res['count'] > 0:
            #     print("Статья с таким url уже существует")
            #     return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO comments VALUES(NULL, ?, ?, ?, ?)", (username, text, mfkname, score))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False

        return True

    def getComment(self, alias):
        try:
            self.__cur.execute(f"SELECT username, text, mfkname, score FROM comments WHERE mfkname LIKE {alias}")
            # self.__cur.execute(f"SELECT * FROM comments")
            # self.__cur.execute("SELECT * FROM comments")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return ()


















# id
# name text
# faculty text
# online text
# openclose
# discribe
# teachers
# whereis
# whenis
# complexity
# semester
# record
# score
# url
# time


































