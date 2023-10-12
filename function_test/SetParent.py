# Created by Katsutoshi Machida Oct. 2023.

import vs


# アクティブなレイヤ上で選択されている最上位の図形のハンドルを返し「sobj」に代入
sobj = vs.FSActLayer()

# 最上位のレイヤのハンドルを返し「layer_h」に代入
layer_h = vs.FLayer()

# 現在のレイヤから図形（「sobj」）を削除し、指定したレイヤ（「layer_h」）へ置く
## つまりはレイヤを現在のレイヤから最上位のレイヤに変更する
boo = vs.SetParent(sobj, layer_h)

# SetParentの返り値（BOOLEAN型）をアラートダイアログで表示する
vs.AlrtDialog(str(boo))


# Script Function Reference
## A&AウェブサイトRetrieved 2023-10-12 from (https://www.aanda.co.jp/develop/ScriptReference/Pages/DocumentListHandling.html#SetParent)
## Vectorworks 開発者ウェブサイトRetrieved 2023-10-12 from (https://developer.vectorworks.net/index.php/VS:SetParent)
### I would like to thank the people who developed it and those who helped me.
