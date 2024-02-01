import DBcm

config = {
    "host": "127.0.0.1",
    "database": "commentsDB",
    "user": "student",
    "password": "itcarlow",
}

SQL_INSERT = (
    "insert into comments (first, last, email, message) values ( %s , %s, %s, %s)"
)
SQL_EVERYTHING = "select * from comments order by time DESC"


def save_data(first, last, email, message):
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_INSERT, (first, last, email, message,))


def display_data():
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL_EVERYTHING)
        results = db.fetchall()

        return results
