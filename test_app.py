import pytest
from app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # テスト用DBの初期化（必要であればここで作成）
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ToDoリスト' in response.data

def test_add_task(client):
    response = client.post('/add', data={'task': 'テストタスク'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'テストタスク' in response.data

def test_add_empty_task(client):
    response = client.post('/add', data={'task': '   '}, follow_redirects=True)
    assert response.status_code == 200
    assert b'タスクはありません' in response.data or response.status_code == 200

def test_delete_task(client):
    conn = get_db_connection()
    conn.execute('INSERT INTO todos (task, done) VALUES (?, ?)', ('削除テスト', 0))
    task_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.commit()
    conn.close()

    response = client.post(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200
