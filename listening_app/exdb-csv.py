import sqlite3
import csv

DB_PATH = 'listening_survey.db'
CSV_PATH = 'exported_results.csv'

def export_to_csv():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # データ取得
    c.execute("SELECT * FROM results")
    rows = c.fetchall()

    # カラム名取得
    col_names = [description[0] for description in c.description]

    # CSV出力
    with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(col_names)  # ヘッダー行
        writer.writerows(rows)      # 本文行

    conn.close()
    print(f"✅ データベース内容を {CSV_PATH} に書き出しました。")

if __name__ == '__main__':
    export_to_csv()