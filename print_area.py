#Created by Katsutoshi Machida Apr. 2023.
import vs

target = vs.FSActLayer() #選択図形の中で一番上の図形をtargetとする
area = round(vs.ObjAreaN(target),2) #選択した図形の面積をareaとする
cent = vs.HCenter(target)  #targetの中心をcentとする

vs.MoveTo(cent) #選択した図形のセンター座標にハンドルを移動
vs.CreateText(str(area)+"m2") #面積の文字列オブジェクトを作成
