#Created by Katsutoshi Machida Sep. 2023.
import vs
import random


# 四角形を作成する関数
def create_random_rectangle(x, y, width, height):
    vs.Rect(x, y, x + width, y + height)  # 四角形を描画


# 四角形を10個作成する
for _ in range(10):
    x = random.randint(0, 100)  # ランダムなx座標（整数）
    y = random.randint(0, 100)  # ランダムなy座標（整数）
    width = random.randint(1, 10)  # ランダムな幅（整数）
    height = random.randint(1, 10)  # ランダムな高さ（整数）    
    create_random_rectangle(x, y, width, height)
