#Created by Katsutoshi Machida May. 2023.
import vs


def area_print(target):
	area = round(vs.ObjAreaN(target),2) #選択した図形の面積をareaとする
	cent = vs.HCenter(target)  #targetの中心をcentとする

	vs.MoveTo(cent) #選択した図形のセンター座標にハンドルを移動
	vs.CreateText(str(area)+" m2") #面積の文字列オブジェクトを作成


target = vs.FSActLayer() #アクティブレイヤ上で選択したオブジェクトの最も上のオブジェクトのハンドルをtargetとする


for i in range(vs.NumSObj(vs.ActLayer())): #アクティブレイヤ上で選択されたオブジェクトの数だけ以下のforでくくった実行文を繰り返し実行する
	area_print(target) #先に定義したcross_line(target)を14行目で選択したオブジェクトに実行する
	target = vs.NextSObj(target) #14行目で選択したオブジェクトの次のオブジェクトをtargetとする->17行目のrange()でカウントした数だけ18行目と19行目を繰り返す
