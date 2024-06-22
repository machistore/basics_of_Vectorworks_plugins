import vs

def test_did_cancel():
    # 整数を入力するダイアログを表示
    user_input = vs.IntDialog('整数を入力してください:', '0')
    
    # キャンセルボタンが押されたかどうかを確認
    if not vs.DidCancel():
        # 入力された整数を3倍にして表示
        result = int(user_input) * 3
        vs.Message(result)
    else:
        # キャンセルが押された場合の処理
        vs.Message("キャンセルされました。")

# スクリプトを実行して動作をテスト
test_did_cancel()
