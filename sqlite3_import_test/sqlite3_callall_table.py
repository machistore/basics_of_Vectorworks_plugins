import vs
import sqlite3


def sqlite_table_import():
    # データベースに接続(引数にSQLiteファイルのパスを記入)
    conn = sqlite3.connect('C:\\Users\\Users_name\\Desktop\\test_sqlite3_module.db')

    # カーソルオブジェクトを作成
    cur = conn.cursor()

    # SQLクエリを実行(引数に実行したいクエリを記入)
    cur.execute("SELECT * FROM names")

    # 結果を取得
    rows = cur.fetchall()

    # 結果を表示
    for row in rows:
        # 各レコード(行)をリストとしてアラート表示    
        vs.AlrtDialog(str(row))

    # 接続を閉じる
    conn.close()


sqlite_table_import()
