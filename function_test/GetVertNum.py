import vs


sobj = vs.FSActLayer() #アクティブレイヤ上で選択したオブジェクトの最も上のオブジェクトのハンドルをsobjとする
vertnum = vs.GetVertNum(sobj) # ハンドルで指定した多角形／曲線(sobj)の頂点の数を返す
vs.AlrtDialog(str(vertnum))
