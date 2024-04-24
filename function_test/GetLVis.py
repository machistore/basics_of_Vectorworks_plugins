# Created by Katsutoshi Machida Oct. 2023.
# description: アクティブなドキュメント内のレイヤの表示状態を取得し、アラートダイアログで表示する

import vs

# 最上位のレイヤのハンドルを返し、"flayer"に代入
flayer = vs.FLayer()

# アクティブなドキュメント内のレイヤの数を返し、"num_layer"に代入
num_layer = vs.NumLayers()

# アラートダイアログでアクティブなドキュメントのレイヤ数を表示
vs.AlrtDialog('アクティブなドキュメントの\nレイヤの数は「' + str(num_layer) + '」です')

# アクティブなドキュメント内のレイヤの数だけ以下の処理を繰り返し実行する
for i in range(num_layer):
    
    # "flayer"のレイヤの名前を返し、"layer_name"に代入
    layer_name = vs.GetLName(flayer)

    # レイヤの表示状態が表示(Normal: 0)の場合は以下の処理をする
    if vs.GetLVis(flayer) == 0:
        vs.AlrtDialog('「' + layer_name + '」は表示レイヤです')
        
	# レイヤの表示状態がグレイ表示(Grayed: 2)の場合は以下の処理をする
    elif vs.GetLVis(flayer) == 2:
        vs.AlrtDialog('「' + layer_name + '」はグレイ表示レイヤです')    
        
	# レイヤの表示状態が非表示(Invisible: -1)の場合は以下の処理をする
    elif vs.GetLVis(flayer) == -1:
        vs.AlrtDialog('「' + layer_name + '」は非表示レイヤです')

    # 指定したレイヤ("flayer")の次にあるレイヤのハンドルを返し、"flayer"に代入し、"flayer"の値を更新
    flayer = vs.NextLayer(flayer)

