import vs

def test_alert_inform_dont_show_again():
    # 表示するメッセージ
    text = "これは無効なアイテムです。"
    
    # メインメッセージの下に表示するアドバイス（小さなフォント）
    advice = "詳細な情報についてはサポートにお問い合わせください。"
    
    # アラートの重大度を設定（minorAlert: True = 軽微なアラート, False = 重大なアラート）
    minorAlert = False
    
    # 配列オプション
    arrOptions = (
        'DontShowDialogAgainCategory',  # チェックボックスの値を保存するカテゴリ
        'DontShowDialogAgainItem',      # チェックボックスの値を保存する項目（アラートごとにユニークであるべき）
        ''                              # デフォルトの「このダイアログを再表示しない」チェックボックス文字列を上書きする文字列
    )
    
    # AlertInformDontShowAgain関数を呼び出してアラートを表示
    vs.AlertInformDontShowAgain(text, advice, minorAlert, arrOptions)

# スクリプトを実行して動作をテスト
test_alert_inform_dont_show_again()
