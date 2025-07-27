import sqlite3

class DatabaseManager:
    def __init__(self, db_name='users.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT PRIMARY KEY,
                email TEXT,
                amount INTEGER
            )
        ''')
        self.conn.commit()

    def add_or_update_user(self, data):
        name, email, amount = data['name'], data['email'], int(float(data['total_amount']))
        self.cursor.execute('SELECT amount FROM users WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            new_amt = result[0] + amount
            self.cursor.execute('UPDATE users SET email=?, amount=? WHERE name=?', (email, new_amt, name))
        else:
            self.cursor.execute('INSERT INTO users (name, email, amount) VALUES (?, ?, ?)', (name, email, amount))
        self.conn.commit()

    def deduct_amount(self, name, email, amount_paid):
        self.cursor.execute('SELECT amount FROM users WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            new_amt = result[0] - amount_paid
            self.cursor.execute('UPDATE users SET amount = ?, email=? WHERE name=?', (new_amt, email, name))
            self.conn.commit()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()
