"""\
This Python script creates a simple table on Vectorworks using the 'vs' module.\nIt draws rectangular cells and places text in each cell, automatically determining\nthe number of rows and columns from the input data.\n"""

import vs

def create_table_in_vectorworks(
    origin_x, origin_y,
    data,
    cell_width, cell_height
):
    """
    Vectorworks上に表を描画するサンプル関数\n\n    :param origin_x: テーブルの左上X座標\n    :param origin_y: テーブルの左上Y座標\n    :param data: 2次元リスト(行: data[row], 列: data[row][col])\n    :param cell_width:  セルの横幅\n    :param cell_height: セルの高さ\n\n    """

    # 行数と列数をデータから自動的に決定
    rows = len(data)  # dataの要素数が行数
    cols = 0
    if rows > 0:
        # 全行の中で最も列数が多いものをcolsとする
        cols = max(len(row) for row in data)

    # 行数と列数をもとにテーブルを描画
    for r in range(rows):
        for c in range(cols):
            # 左上と右下の座標を計算\n            # 指定した行と列に基づいて枠線を描画するための座標を設定
            left   = origin_x + c * cell_width
            top    = origin_y - r * cell_height
            right  = left + cell_width
            bottom = top + cell_height

            # vs.Rect(...) で長方形を描画しセル枠を作る
            vs.Rect(left, top, right, bottom)

            # 文字列を配置する位置を指定
            text_x = left + cell_width * 0.1
            text_y = top + cell_height * 0.7

            # Vectorworksでのテキスト描画原点を設定
            vs.TextOrigin(text_x, text_y)

            # dataがあり、現在のセルに文字列があるかチェックし、なければ空文字にする
            cell_text = ""
            if r < len(data) and c < len(data[r]):
                cell_text = str(data[r][c])

            # テキストオブジェクトを描画
            vs.CreateText(cell_text)


def main():
    # サンプルデータ
    sample_data = [
        ["用途", "構造", "規模"],           # 一行目(カラム名)
        ["共同住宅", "RC造", "地上3階"],     # 二行目
        ["事務所",   "S造",  "地上2階"],     # 三行目
    ]

    # Vectorworksでの描画開始位置 (テーブル左上)
    origin_x = 0
    origin_y = 0

    # セルの横幅・高さを指定
    cell_w = 20
    cell_h = 8

    # create_table_in_vectorworksに渡す際に、
    # 行数と列数は指定せず、dataの内容から自動判定する
    create_table_in_vectorworks(
        origin_x,     # テーブル左上X座標
        origin_y,     # テーブル左上Y座標
        sample_data,  # テーブル表示に使用する2次元リスト
        cell_width=cell_w,
        cell_height=cell_h
    )

# Vectorworksのメニューコマンド等に登録し、実行時にmain()を呼び出す
main()
