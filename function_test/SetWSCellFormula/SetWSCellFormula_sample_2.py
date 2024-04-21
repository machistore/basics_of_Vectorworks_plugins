# Description: ワークシートにヘッダーを設定してデータを設定するサンプル
# Author: Katsutoshi Machida
# created: 2024-04-21
# last update: 2024-04-21
# Apps that have been confirmed to work: Vectorworks 2024
# os: Windows 11 home (version 23H2) 


import vs

def create_worksheet_with_headers(): # ワークシートにヘッダーを設定してデータを設定する関数
    # ワークシートを作成
    ws_name = 'Sample_Worksheet_2'
    # すでに同じ名前のワークシートが存在するかチェックし、存在する場合はそのハンドルを取得
    ws_handle = vs.CreateWS(ws_name, 2, 2)  # 2行2列のワークシート

    # ヘッダーを設定
    vs.SetWSCellFormula(ws_handle, 1, 1, 1, 1, 'ID')  # 1行1列目に"ID"という文字列
    vs.SetWSCellFormula(ws_handle, 1, 2, 1, 2, 'NAME')  # 1行2列目に"NAME"という文字列

    # サンプルデータを設定
    vs.SetWSCellFormula(ws_handle, 2, 1, 2, 1, '1')  # 2行1列目に数値1
    vs.SetWSCellFormula(ws_handle, 2, 2, 2, 2, '\'ippan\'')  # 2行2列目に"ippan"という文字列

    # ワークシートを表示
    vs.ShowWS(ws_handle, True)

# 関数を実行してワークシートを生成
create_worksheet_with_headers()
