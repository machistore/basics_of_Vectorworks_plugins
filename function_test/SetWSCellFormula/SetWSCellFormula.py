# desc: ワークシートのセルに数式を設定するサンプルスクリプト
# created: 2024-04-20
# update: 2024-04-20
# application: Vectorworks 2024
# os: Windows 11 home
# auth: Katsutoshi Machida
# note: 
##    ファイルに「Sample Worksheet」というワークシートが作成される.
##    4行2列に「=3*2」の数式が設定される.
##    1行1列から2行10列に<empty>という文字列が書かれたセルが設定される.
##    3行0列に「=DATABASE(L='レイヤ-1')」の数式が設定される(0列目は条件式を指定するための列).
##    ワークシートが表示される.
## quote source: Vectorworks Developer
## Retrieved 2024-04-20 from: https://developer.vectorworks.net/index.php?title=VS:SetWSCellFormula
# ---------------------------------------------------------------------


import vs

ws_name = 'Sample Worksheet' # ワークシート名
ws_handle = vs.CreateWS(ws_name, 10, 10)  # 10行10列のワークシートを作成

vs.SetWSCellFormula(ws_handle,4,2,4,2,'=3*2') # 4行2列に数式を設定
vs.SetWSCellFormula(ws_handle,1,1,2,10,'<empty>') # 1行1列から2行10列に<empty>という文字列を設定
vs.SetWSCellFormula(ws_handle,3,0,3,0,"=DATABASE(L='レイヤ-1')") # 3行0列に数式を設定(0列目は条件式を指定するための列)

vs.ShowWS(ws_handle, True) # ワークシートを表示(True: 表示, False: 非表示)