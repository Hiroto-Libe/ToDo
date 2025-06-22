from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

# アプリ初期化
app = Flask(__name__, instance_relative_config=True)

# DBファイルのパス設定
DB_PATH = os.path.join(app.instance_path, 'todo.db')
os.makedirs(app.instance_path, exist_ok=True)

# DB接続関数
def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# タスクリスト表示（全件）
@app.route('/')
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    return render_template('index.html', todos=todos)

# タスク追加
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    if not task.strip() or len(task) > 100:
        return redirect(url_for('index'))
    conn = get_db_connection()
    conn.execute('INSERT INTO todos (task, done) VALUES (?, ?)', (task.strip(), 0))
    conn.commit()
    return redirect(url_for('index'))

# 完了状態の切り替え
@app.route('/complete/<int:id>', methods=['POST'])
def complete(id):
    conn = get_db_connection()
    task = conn.execute('SELECT done FROM todos WHERE id = ?', (id,)).fetchone()
    if task:
        new_status = 0 if task['done'] else 1
        conn.execute('UPDATE todos SET done = ? WHERE id = ?', (new_status, id))
        conn.commit()
    return redirect(url_for('index'))

# タスク削除
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()
    return redirect(url_for('index'))

# 状態フィルター表示
@app.route('/filter/<status>')
def filter_status(status):
    conn = get_db_connection()
    if status == 'done':
        todos = conn.execute('SELECT * FROM todos WHERE done = 1 ORDER BY id DESC').fetchall()
    elif status == 'undone':
        todos = conn.execute('SELECT * FROM todos WHERE done = 0 ORDER BY id DESC').fetchall()
    else:
        todos = conn.execute('SELECT * FROM todos ORDER BY id DESC').fetchall()
    return render_template('index.html', todos=todos)

# アプリ起動
if __name__ == '__main__':
    app.run(debug=True)
