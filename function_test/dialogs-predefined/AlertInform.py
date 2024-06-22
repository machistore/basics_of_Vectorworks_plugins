import vs

def test_alert_inform():
    # 表示するメッセージ
    text = "コマンドの結果についての情報を表示します。"
    
    # メインメッセージの下に表示するアドバイス（小さなフォント）
    advice = "詳細については、マニュアルを参照してください。"
    
    # アラートの重大度を設定（minorAlert: True = 軽微なアラート, False = 重大なアラート）
    minorAlert = True
    
    # AlertInform関数を呼び出してアラートを表示
    vs.AlertInform(text, advice, minorAlert)

# スクリプトを実行して動作をテスト
test_alert_inform()
