import sqlite3

conn = sqlite3.connect('listening_survey.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    listen_q1 TEXT, listen_q2 TEXT, listen_q3 TEXT, listen_q4 TEXT, listen_q5 TEXT,
    listen_q6 TEXT, listen_q7 TEXT, listen_q8 TEXT, listen_q9 TEXT, listen_q10 TEXT,
    survey_q1 INTEGER, survey_q2 INTEGER, survey_q3 INTEGER, survey_q4 INTEGER, survey_q5 INTEGER,
    survey_q6 INTEGER, survey_q7 INTEGER, survey_q8 INTEGER, survey_q9 INTEGER, survey_q10 INTEGER,
    survey_q11 INTEGER, survey_q12 INTEGER,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("✅ listening_survey.db を初期化しました。")