import vs

def test_alert_question():
    # 表示する質問
    question = "このアクションを実行しますか？"
    
    # 質問の下に表示するアドバイス（小さなフォント）
    advice = "このアクションは元に戻せません。実行してよろしいですか？"
    
    # デフォルトボタンの設定（1: OK, 0: Cancel）
    defaultButton = 1
    
    # OKボタンのテキストを上書き
    OKOverrideText = "実行"
    
    # Cancelボタンのテキストを上書き
    CancelOverrideText = "キャンセル"
    
    # カスタムボタンAのテキスト
    customButtonAText = "オプションA"
    
    # カスタムボタンBのテキスト
    customButtonBText = "オプションB"
    
    # AlertQuestion関数を呼び出してアラートを表示し、ユーザーの入力を取得
    result = vs.AlertQuestion(question, advice, defaultButton, OKOverrideText, CancelOverrideText, customButtonAText, customButtonBText)
    
    # ユーザーの選択に応じてメッセージを表示
    if result == 0:
        vs.AlrtDialog("キャンセルが選択されました。")
    elif result == 1:
        vs.AlrtDialog("実行が選択されました。")
    elif result == 2:
        vs.AlrtDialog("オプションAが選択されました。")
    elif result == 3:
        vs.AlrtDialog("オプションBが選択されました。")

# スクリプトを実行して動作をテスト
test_alert_question()
