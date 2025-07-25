# description: 重複するオブジェクトを検出するスクリプト
# version: 1.0
# target app: Vectorworks
# autor: Katsutoshi Machida
# date: 2024-05-07
# update: 2024-05-07
# license: MIT


import vs

def handle_object(obj_handle): # オブジェクトを処理する関数
    x, y = vs.HCenter(obj_handle)  # オブジェクトの中心座標を取得
    key = (x, y)  # 2D座標をキーとする
    if key not in location_dict: # キーが存在しない場合は空リストを追加
        location_dict[key] = [] # キーに空リストを追加
    location_dict[key].append(vs.GetName(obj_handle))  # 座標キーにオブジェクト名を追加

def detect_overlapping_objects(): # 重複するオブジェクトを検出する関数
    global location_dict # グローバル変数を使用するための宣言
    location_dict = {} # 座標をキーとする辞書を初期化
    
    # 条件"(ALL)"で全オブジェクトを対象に処理を行う
    vs.ForEachObject(handle_object, "(ALL)")
    
    # 重複が見つかった場合の報告
    report = "" # レポートの初期化
    for location, names in location_dict.items(): # 座標とオブジェクト名のリストを取得
        if len(names) > 1: # オブジェクト名のリストが2つ以上の場合
            report += f"重複座標 {location} に以下のオブジェクトが存在します: {', '.join(names)}\n" # レポートに追加
    
    if report: # レポートがある場合
        vs.AlrtDialog(report)  # アラートダイアログでレポートを表示

# スクリプトを実行
detect_overlapping_objects()
