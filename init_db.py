import sqlite3
import os

# DBファイルの保存先（Flaskの推奨構成に合わせて instance/ 配下）
db_dir = os.path.join(os.path.dirname(__file__), 'instance')
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, 'todo.db')

# DB接続と初期化
conn = sqlite3.connect(db_path)

# todos テーブルを作成（存在しない場合のみ）
conn.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

conn.commit()
conn.close()

print(f"✅ 初期化完了: {db_path}")
