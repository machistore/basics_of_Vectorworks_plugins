import vs

# 選択したオブジェクトのハンドルを"selected_object"に代入
selected_object = vs.FSActLayer()

# selected_objectを多角形オブジェクトに変換し(解像度は仮に8とし)、"polygon_object"に代入
polygon_object = vs.ConvertToPolygon(selected_object, 8)

# ここから先のオブジェクトをグループにしたい
vs.BeginGroup()

# polygon_objectの頂点番号1番の頂点座標を"p1"に代入    
p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 1)

# 座標p1にポイントを置く
vs.MoveTo(p1)

# polygon_objectの頂点番号3番の頂点座標を"p1"と更新
p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 3)

# 先に置いたポイント(MoveTo(p1))から頂点番号3番の座標に向かってラインを引く
vs.LineTo(p1)
    
p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 2)
vs.MoveTo(p1)

p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 4)
vs.LineTo(p1)

# ここまでのオブジェクトをグループとする
vs.EndGroup()

# 選択された全てのオブジェクトから選択状態を切る
#vs.DSelectAll()

# 多角形オブジェクトに変換したときに複製された多角形オブジェクトを消去する
vs.DelObject(polygon_object)

# 全ての選択を解除
vs.DSelectAll()

# グループ図形を選択
vs.SelectObj("T=GROUP")
