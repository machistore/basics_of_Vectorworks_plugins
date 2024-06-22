import vs

def test_alert_inform_hlink_n():
    # 表示するメッセージ
    text = "これは無効なアイテムです。"
    
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
    
    # 配列オプション
    arrOptions = (
        'DontShowDialogAgainCategory',  # チェックボックスの値を保存するカテゴリ
        'DontShowDialogAgainItem',      # チェックボックスの値を保存する項目（アラートごとにユニークであるべき）
        ''                              # デフォルトの「このダイアログを再表示しない」チェックボックス文字列を上書きする文字列
    )
    
    # AlertInformHLinkN関数を呼び出してアラートを表示
    vs.AlertInformHLinkN(text, adviceBeforeLink, linkTitle, linkURL, adviceAfterLink, minorAlert, arrOptions)

# スクリプトを実行して動作をテスト
test_alert_inform_hlink_n()
