import vs

def test_alert_set_always_do_val():
    # カテゴリ名とアイテム名を設定
    category = "DontShowDialogAgainCategory"
    item = "DontShowDialogAgainItem"
    
    # 新しいデフォルト値を設定 (-1 を指定するとエントリがクリアされ、ダイアログが再表示される)
    value = -1  # 例えば -1 でエントリをクリア

    # AlertSetAlwaysDoVal関数を呼び出して値を設定
    vs.AlertSetAlwaysDoVal(category, item, value)

# スクリプトを実行して動作をテスト
test_alert_set_always_do_val()
