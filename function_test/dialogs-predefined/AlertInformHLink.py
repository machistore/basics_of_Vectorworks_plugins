import vs

def test_alert_inform_hlink():
    # 表示するメッセージ
    text = "そのアイテムは有効なアイテムではありません。"
    
    # ハイパーリンクの上部に表示するアドバイス
    adviceBeforeLink = "詳細な情報については、"
    
    # ハイパーリンクのテキスト
    linkTitle = "弊社のウェブサイト"
    
    # ハイパーリンクのURL
    linkURL = "https://www.vectorworks.net"
    
    # ハイパーリンクの下部に表示するアドバイス
    adviceAfterLink = "を参照してください。"
    
    # アラートの重大度を設定（minorAlert: True = 軽微なアラート, False = 重大なアラート）
    minorAlert = False
    
    # AlertInformHLink関数を呼び出してアラートを表示
    vs.AlertInformHLink(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink, minorAlert)

# スクリプトを実行して動作をテスト
test_alert_inform_hlink()
