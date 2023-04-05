#Created by Katsutoshi Machida Apr. 2023.
import vs #モジュールの呼び出し

orgin = (0, 0) #原点(x, y) (変数定義)
direction = (1, 0) #傾き(x, y) (変数定義)
width = vs.Px #オブジェクト情報パレットで指定された幅 (変数定義)
height = vs.Py #オブジェクト情報パレットで指定された高さ(奥行き) (変数定義)

vs.RectangleN(orgin, direction, width, height) #2D四角形オブジェクトの生成API


#パラメータ
# |#|名前|フィールド名|型     |初期値|
#---
# |1|x   |width      |Number|910   |
# |2|y   |height     |Number|910   |
