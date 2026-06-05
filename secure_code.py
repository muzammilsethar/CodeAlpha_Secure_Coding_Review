import os, sqlite3
DB_PASSWORD = os.getenv("DB_ADMIN_PASSWORD")

def get_user_profile_secure(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM accounts WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

print(get_user_profile_secure("admin"))
