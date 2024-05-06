# desc: 選択されたオブジェクトを中央揃えにするスクリプト
# auth: Katsutoshi Machida
# date: 2024-05-03
# update: 2024-05-03
# version: 1.0
# lang: Python
# tool: Vectorworks 2024


import vs

def align_center(): # 選択されたオブジェクトを中央揃えにする関数
    obj = vs.FSActLayer()  # 最初の選択されたオブジェクト
    if obj == 0: # オブジェクトが選択されていない場合
        vs.AlrtDialog("オブジェクトが選択されていません。") # ダイアログを表示
        return # 関数を終了
    
    # 初期化
    objs = [] # オブジェクトのリスト
    total_x = 0 # オブジェクトの中心座標の合計
    total_y = 0 # オブジェクトの中心座標の合計
    count = 0 # オブジェクトの数
    
    # 選択されたオブジェクトの中心座標を取得
    while obj: # オブジェクトが存在する間
        x, y = vs.HCenter(obj)  # オブジェクトの中心座標を取得
        objs.append((obj, x, y)) # オブジェクトのリストに追加
        total_x += x # オブジェクトの中心座標の合計に加算
        total_y += y # オブジェクトの中心座標の合計に加算
        count += 1 # オブジェクトの数に加算
        obj = vs.NextSObj(obj)  # 次の選択されたオブジェクト
    
    if count == 0: # オブジェクトが見つからなかった場合
        vs.AlrtDialog("オブジェクトが見つかりませんでした。") # ダイアログを表示
        return # 関数を終了

    # 全オブジェクトの平均中心座標を計算
    center_x = total_x / count # オブジェクトの中心座標の合計をオブジェクトの数で割る
    center_y = total_y / count # オブジェクトの中心座標の合計をオブジェクトの数で割る

    # 各オブジェクトを平均中心座標に向かって移動
    for obj, x, y in objs: # オブジェクトのリストからオブジェクトと座標を取得
        vs.HMove(obj, center_x - x, center_y - y) # オブジェクトを平均中心座標に向かって移動

# 選択されたオブジェクトを中央揃えに実行
align_center()


'''
```mermaid
flowchart TD
    A[スクリプト開始] --> B{オブジェクトが選択されているか?}
    B -->|いいえ| C[アラート: オブジェクトが選択されていません]
    B -->|はい| D[初期化]
    D --> E{オブジェクトが存在するか?}
    E -->|いいえ| F[アラート: オブジェクトが見つかりませんでした]
    E -->|はい| G[オブジェクトの中心座標を取得しリストに追加]
    G --> H[次のオブジェクトを取得]
    H -->|ある| G
    H -->|ない| I[全オブジェクトの平均中心座標を計算]
    I --> J[各オブジェクトを平均中心座標に移動]
    J --> K[スクリプト終了]
```
'''