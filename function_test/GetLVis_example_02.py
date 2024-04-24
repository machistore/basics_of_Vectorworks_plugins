# description: レイヤの表示状態を一覧情報として表示するスクリプト
# version: 0.1
# author: Katsutoshi Machida
# created: 2024-04-24
# updated: 2024-04-24
# apply: Vectorworks 2024
# os: Windows 11 home (x64) Version 23H2


import vs

def display_layer_info(): # レイヤの表示状態を一覧情報として表示する関数
    flayer = vs.FLayer()  # 最上位のレイヤのハンドルを取得
    num_layers = vs.NumLayers()  # レイヤの総数を取得
    vs.AlrtDialog(f'アクティブなドキュメントのレイヤの数は「{num_layers}」です') # レイヤの総数を表示

    # 各表示状態のレイヤ名を保持するリスト
    visible_layers = [] # 表示レイヤ
    grayed_layers = [] # グレイ表示レイヤ
    invisible_layers = [] # 非表示レイヤ

    for _ in range(num_layers): # レイヤの数だけ繰り返す
        layer_name = vs.GetLName(flayer)  # レイヤ名を取得
        visibility = vs.GetLVis(flayer)  # レイヤの表示状態を取得

        if visibility == 0: # 表示
            visible_layers.append(layer_name) # 表示レイヤに追加
        elif visibility == 2: # グレイ表示
            grayed_layers.append(layer_name) # グレイ表示レイヤに追加
        elif visibility == -1: # 非表示
            invisible_layers.append(layer_name) # 非表示レイヤに追加

        flayer = vs.NextLayer(flayer)  # 次のレイヤへ

    # 各レイヤ状態をコンマ区切りの文字列として表示
    vs.AlertInform('表示レイヤ', ', '.join(visible_layers), False) # レイヤの表示状態を表示
    vs.AlertInform('グレイ表示レイヤ', ', '.join(grayed_layers), False) # レイヤの表示状態を表示
    vs.AlertInform('非表示レイヤ', ', '.join(invisible_layers), False) # レイヤの表示状態を表示

display_layer_info() # レイヤの表示状態を一覧情報として表示を実行
