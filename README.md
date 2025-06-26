# 📝 SimpleToDo - Flask製ToDoリストアプリ

## 📌 概要

SimpleToDo は、PythonとFlaskを使って構築されたシンプルなタスク管理アプリです。  
タスクの登録、完了チェック、削除、状態ごとのフィルター表示が可能です。

---

## 🛠 使用技術

- Python 3.x
- Flask 2.x
- SQLite3（ファイル型DB）
- HTML / CSS (Jinja2 + 任意でBootstrap)
- ローカル環境用仮想環境（venv）

---

## 📁 ディレクトリ構成
```
todo-flask/
├── app.py # アプリ本体
├── templates/
│ └── index.html # タスクリスト画面（Jinjaテンプレート）
├── static/
│ └── style.css # スタイルシート
├── instance/
│ └── todo.db # SQLiteデータベース（自動生成）
├── init_db.py # DB初期化スクリプト
├── requirements.txt # 必要パッケージ
├── .gitignore # Git追跡除外設定
└── README.md # このファイル
```


---

## 🚀 セットアップ手順

### 1. 仮想環境の作成と有効化

```bash
python3 -m venv venv
source venv/bin/activate  # Windowsの場合: .\venv\Scripts\activate
```

---
### 2. 必要パッケージのインストール
pip install -r requirements.txt

---
### 3. SQLiteデータベースの初期化
python init_db.py

---
### 4. アプリの起動
python app.py

アプリは http://127.0.0.1:5000/ で動作します。

---
## ✅ 動作確認チェックリスト（手動検証）

| 機能                       | 結果  | 備考                              |
|----------------------------|-------|-----------------------------------|
| タスク追加ができる         | ✅     | 正常に表示されるか確認済み             |
| 空白タスクは追加できない   | ✅     | バリデーションエラーでリダイレクトされる |
| タスク完了チェック切替     | ✅     | 状態が切り替わり、打ち消し線が表示される |
| タスク削除ができる         | ✅     | 該当IDが削除される                  |
| フィルター（完了/未完了）が動作 | ✅     | 表示対象が切り替わる                 |

- テスト環境：macOS Ventura / Python 3.11 / Flask 2.3.3
- ブラウザ：Google Chrome 最新版

---
🎯 機能一覧
・タスクの追加／削除／完了チェック
・「すべて／未完了／完了」の絞り込み表示
・入力バリデーション（空白／100文字制限）
・完了済みタスクは打ち消し線表示
・シンプルで直感的なUI

---
📄 ライセンス
このプロジェクトは MITライセンス のもとで公開されています。

---
👤 作者
名前：Hiroto Ito（または任意の表示名）
GitHub：Hiroto-Libe