# description: 指定した角度で直線を描く
# date: 2024-05-22
# latest update: 2021-05-22
# version: 1.0
# author: Katsutoshi Machida
# license: MIT


import vs # VectorScriptモジュール
import math # 数学関数モジュール

def draw_line_with_angle(start_x, start_y, length, angle): # 直線を描く関数
    # 角度をラジアンに変換
    angle_rad = math.radians(angle)
    
    # 終点の座標を計算
    end_x = start_x + length * math.cos(angle_rad) # 終点のX座標
    end_y = start_y + length * math.sin(angle_rad) # 終点のY座標
    
    # 現在の位置をスタート地点に移動
    vs.MoveTo(start_x, start_y)
    # 指定した角度で直線を描く
    vs.LineTo(end_x, end_y)

# 使用例
start_x = 0  # スタート地点のX座標
start_y = 0  # スタート地点のY座標
length = 1000  # 直線の長さ
angle = 30  # 角度（度単位）

draw_line_with_angle(start_x, start_y, length, angle) # 直線を描く
