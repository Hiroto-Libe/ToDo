# 🔍 ToDoリストアプリ - 詳細設計（Flask + SQLite）

## 1. 🧱 ディレクトリ構成

<pre><code>'''
todo-flask/
├── app.py # アプリ本体
├── templates/
│ └── index.html # メイン画面（Jinja2テンプレート）
├── static/
│ └── style.css # CSSファイル（Bootstrapで代替も可）
├── instance/
│ └── todo.db # SQLiteデータベース（Flaskの推奨構成）
├── requirements.txt # パッケージ一覧
├── README.md # プロジェクト説明
├── LICENSE # MITライセンス
└── .gitignore # Git追跡除外ファイル
'''</code></pre>


## 2. 🧩 モジュール・関数設計

| 関数／処理名        | 内容・役割                                 |
|---------------------|--------------------------------------------|
| `get_db_connection()` | SQLiteの接続取得（共通関数）                |
| `index()`           | 全タスクの取得と一覧表示                     |
| `add()`             | タスクをPOSTで受け取りDBに追加                |
| `complete(id)`      | ID指定で `done` 状態をトグル                  |
| `delete(id)`        | タスクの削除処理                             |
| `filter(status)`    | `done` / `undone` に応じてフィルタ表示         |

---

## 3. 🔁 処理フロー例：タスク追加

1. フォームにタスク入力 → 「追加」ボタン押下
2. `POST /add` にフォームデータ送信
3. バリデーション（空白・長すぎなど）
4. SQLiteにデータ追加（INSERT）
5. `/` にリダイレクトし、一覧に反映

---

## 4. 📄 テンプレート構成（`index.html`）

### 主な要素

- `<form>`：タスク追加用
- `<ul>` or `<table>`：タスク一覧
- `<input type="checkbox">`：完了チェック
- `<button>`：削除ボタン
- 状態フィルターナビ（すべて／未完了／完了）

### Jinja2使用例

```html
{% for todo in todos %}
  <li>
    <input type="checkbox" {% if todo.done %}checked{% endif %}>
    {{ todo.task }}
    <form method="post" action="/delete/{{ todo.id }}">
      <button>削除</button>
    </form>
  </li>
{% endfor %}
```
---

## 5. ⚙ データベース接続（`get_db_connection()`）

```python
import sqlite3
from flask import g

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect('instance/todo.db')
        g.db.row_factory = sqlite3.Row
    return g.db
```
---

## 6. 🔐 バリデーション・セキュリティ対応

- 空文字や空白のみの入力はサーバー側でバリデーションして拒否する
- Jinja2の**自動エスケープ**機能によりXSS（クロスサイトスクリプティング）を防止
- SQLクエリは `?` を用いた**プレースホルダ（バインディング）**を使って安全に実行し、SQLインジェクションを防ぐ

---

## 7. 🧪 開発補助・ツール

| 項目           | 設定例／推奨                           |
|----------------|----------------------------------------|
| 仮想環境        | `python -m venv venv`                 |
| パッケージ管理   | `pip freeze > requirements.txt`       |
| Flask再起動     | `flask run --reload` または `debug=True` |
| 静的ファイル    | `/static/style.css` に配置             |

---

## 8. ✅ 完成条件（Doneの定義）

- タスクの**追加／削除／完了切り替え**が正常に動作する
- タスクの状態（完了／未完了）で**フィルター表示**が可能
- UIがシンプルでわかりやすく、**直感的に操作できる**
- `README.md`、`LICENSE`、`.gitignore` が**整備されている**
- GitHubに**push済み**で、Renderなどへの**デプロイも完了している**

