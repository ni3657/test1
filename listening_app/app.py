from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def save_to_db(data):
    conn = sqlite3.connect('listening_survey.db')
    c = conn.cursor()
    keys = ', '.join(data.keys())
    values = [data[k] for k in data]
    placeholders = ', '.join(['?'] * len(values))
    sql = f"INSERT INTO results ({keys}) VALUES ({placeholders})"
    c.execute(sql, values)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {}
    for i in range(1, 11):
        data[f'listen_q{i}'] = request.form.get(f'listen_q{i}', '')
    for i in range(1, 13):
        data[f'survey_q{i}'] = request.form.get(f'survey_q{i}', None)
    save_to_db(data)
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)