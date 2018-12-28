import sqlite3


class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.users_cursor = self.conn.cursor()
        self.history_cursor = self.conn.cursor()

        self.users_cursor.execute(
            """ CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT unique) """)

        self.history_cursor.execute(
            """ CREATE TABLE IF NOT EXISTS history (username TEXT PRIMARY KEY, message TEXT) """)

    def add_user(self, username, password):
        self.users_cursor.execute("INSERT INTO users VALUES(?, ?)", (username, password))
        self.conn.commit()

    def user_exists(self, username, password):
        """ checks if the password and username entered are correct """
        self.users_cursor.execute('select * from users')
        for user in self.users_cursor:
            if user[0] == username and user[1] == password:
                return True
        return False


def main():
    d = Database()
    print d.user_exists('nadav', '123')



if __name__ == '__main__':
    main()
