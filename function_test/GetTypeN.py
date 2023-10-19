import vs

sobj = vs.FSActLayer() #アクティブレイヤ上で選択したオブジェクトの最も上のオブジェクトのハンドルをsobjとする
objtype = vs.GetTypeN(sobj) # ハンドルで指定した図形(sobj)の種類を番号で返す
vs.AlrtDialog(str(objtype))
