# description: ワークシートのセルに数式や数値、文字列などを設定したり、条件式を設定したりするサンプルスクリプト
# author: Katsutoshi Machida
# created: 2024-04-21
# last update: 2024-04-21
# app_version: Vectorworks 2024
# os_version: Windows 11 home
# language: Python


import vs

ws_name = 'Sample Worksheet' # ワークシート名
ws_handle = vs.CreateWS(ws_name, 10, 10)  # 10行10列のワークシート

vs.SetWSCellFormula(ws_handle,4,2,4,2,'=3*2') # セルに数式を設定
vs.SetWSCellFormula(ws_handle,1,1,2,10,'<empty>') # セルに空白を設定
vs.SetWSCellFormula(ws_handle,3,0,3,0,"=DATABASE(L='レイヤ-1')") # セルにデータベース関数を設定 

vs.ShowWS(ws_handle, True) # ワークシートを表示