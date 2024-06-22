import vs

def test_alert_critical_hlink():
    # 通知するメッセージ
    text = "重大な問題が発生しました。"
    
    # ハイパーリンクの上部に表示するアドバイス
    adviceBeforeLink = "詳細な解決方法については、以下のリンクを参照してください。"
    
    # ハイパーリンクのテキスト
    linkTitle = "サポートページ"
    
    # ハイパーリンクのURL
    linkURL = "https://www.vectorworks.net"
    
    # ハイパーリンクの下部に表示するアドバイス
    adviceAfterLink = "問題が解決しない場合は、サポートにお問い合わせください。"
    
    # AlertCriticalHLink関数を呼び出してアラートを表示
    vs.AlertCriticalHLink(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink)

# スクリプトを実行して動作をテスト
test_alert_critical_hlink()
