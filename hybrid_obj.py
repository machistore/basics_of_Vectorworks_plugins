#Created by Katsutoshi Machida Apr. 2023.
import vs

# 立方体のサイズを設定
width = vs.Pwidth
depth = vs.Pdepth
height = vs.Pheight

# 立方体の中心点を設定
x = 0
y = 0
z = 0

# 立方体の定義
vs.BeginXtrd(z, height) # 高さ方向の押し出しを開始
vs.Rect(x-width/2, y-depth/2, x+width/2, y+depth/2) # 底面を定義
vs.EndXtrd() # 押し出しを終了して立方体を作成

vs.Rect(x-width/2, y-depth/2, x+width/2, y+depth/2) # 底面を描く


#パラメータ
# |#|名前    |フィールド名|型     |初期値|
# |---|---|---|---|---|
# |1|width   |w          |Number|910   |
# |2|depth   |d          |Number|910   |
# |3|height  |h          |Number|910   |


#Features
#"1点型オブジェクト"を使用して四角形オブジェクトを生成するプラグインオブジェクト
#1点型オブジェクトの作成方法を理解するためにシンプルにつくってみたプラグインオブジェクトです.
