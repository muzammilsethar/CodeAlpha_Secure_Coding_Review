import sqlite3
DB_PASSWORD = "AdminPassword123!"

def get_user_profile(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM accounts WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

print(get_user_profile("admin' OR '1'='1"))
