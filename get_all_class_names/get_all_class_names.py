# discription: ファイル内の全てのクラス名を取得してアラートダイアログで表示するスクリプト
# created: 2024-04-21
# last update: 2024-04-21
# author: Katsutoshi Machida
# app_version: Vectorworks 2024
# os_version: Windows 11 home
# note: このスクリプトはVectorworks 2024で動作します。それ以前のバージョンでは動作しない可能性があります。
# note: このスクリプトはWindows 11 homeで動作します。それ以外のOSでは動作しない可能性があります。
# note: indexは1から始まります。


import vs

def get_all_class_names(): # 全てのクラス名を取得する関数
    class_names = [] # クラス名を格納するリスト
    index = 1 # クラス名のインデックス
    class_name = vs.ClassList(index) # クラス名を取得
    while class_name: # クラス名が取得できる間
        class_names.append(class_name) # クラス名をリストに追加
        index += 1 # インデックスをインクリメント
        class_name = vs.ClassList(index) # クラス名を取得
    return class_names # クラス名のリストを返す

def show_class_names_in_alert(class_names): # クラス名のリストをアラートダイアログで表示する関数
    if class_names: # クラス名が取得できた場合
        # クラス名リストを改行で区切って一つの文字列にまとめる
        class_names_str = '\n'.join(class_names)
        # アラートダイアログで表示
        vs.AlertInform('クラス名リスト', class_names_str, False)
    else:
        # クラス名が一つも取得できなかった場合
        vs.AlrtDialog('警告: ', 'クラス名が一つも取得できませんでした。') # 警告ダイアログを表示

# クラス名のリストを取得してアラートダイアログで表示
all_class_names = get_all_class_names() # 全てのクラス名を取得
show_class_names_in_alert(all_class_names) # クラス名のリストをアラートダイアログで表示
