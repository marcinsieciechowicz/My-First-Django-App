import sqlite3
from sqlite3 import Error

class Question():
    def __init__(self):
        self.question_text = ""
        self.pub_date = ""

    def __str__(self):
        return self.question_text


def select_questions(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("select id, question_text, pub_date from polls_question")
        rows = cur.fetchall()
        list_abc = []
        for row in rows:
            q = Question()
            q.question_text = row[1]
            q.pub_date = row[2]
            list_abc.append(q)
        print(list_abc)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    select_questions(r"C:\Users\Acer\Desktop\mysite\myfirstsqldb.sqlite")


