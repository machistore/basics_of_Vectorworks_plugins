#Created by Katsutoshi Machida May. 2023.
import vs


def print_area(sobj):
	area = round(vs.ObjAreaN(sobj),2) #選択した図形の面積(小数第3位で四捨五入)をareaとする
	cent = vs.HCenter(sobj)  #sobjの中心をcentとする

	vs.MoveTo(cent) #選択した図形のセンター座標にハンドルを移動
	vs.CreateText(str(area)+" m2") #面積の文字列オブジェクトを作成


sobj = vs.FSActLayer() #アクティブレイヤ上で選択したオブジェクトの最も上のオブジェクトのハンドルをsobjとする


for i in range(vs.NumSObj(vs.ActLayer())): #アクティブレイヤ上で選択されたオブジェクトの数だけ以下のforでくくった実行文を繰り返し実行する
	print_area(sobj) #先に定義したcross_line(sobj)を14行目で選択したオブジェクトに実行する
	sobj = vs.NextSObj(sobj) #13行目で選択したオブジェクトの次のオブジェクトをtargetとする->16行目のrange()でカウントした数だけ17行目と18行目を繰り返す
