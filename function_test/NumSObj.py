# NumSObj()はハンドルで指定したレイヤ上の、選択されている図形の数を返します。

import vs

vs.AlrtDialog(str(vs.NumSObj(vs.ActLayer())))

vs.AlrtDialog(str(vs.NumSelectedObjects()))
