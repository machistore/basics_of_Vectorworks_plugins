"""\
このPythonスクリプトは、'vs' モジュールを使ってVectorworksのワークシートを作成し、\nSetWSCellFormulaNでテキストを挿入する方法を示します。\n\n式としてセルに直接テキストを渡すため、両端に余分なダブルクォートは表示されません。\n"""

import vs


def create_worksheet_from_data(name, data):
    """
    指定した 'name' で新しいVectorworksワークシートを作成し、\n    2次元リスト data の内容を各セルに入力します。\n\n    このバージョンでは vs.SetWSCellFormulaN を5つのパラメータ\n    (worksheet, topRow, leftColumn, bottomRow, rightColumn, formula)\n    で呼び出す必要があるVectorworks APIを想定しています。\n\n    :param name: 作成するワークシートの名称\n    :param data: 行と列を持つ2次元リスト\n    """
    # data から行数と列数を判定
    rows = len(data)
    cols = 0
    if rows > 0:
        cols = max(len(row) for row in data)

    # 指定した名前・サイズでワークシートを作成
    ws_handle = vs.CreateWS(name, rows, cols)

    # もともとの自動再計算状態を保存
    auto_recalc = vs.GetWSAutoRecalcState(ws_handle)

    # パフォーマンス向上のため、一時的に自動再計算をオフに
    vs.SetWSAutoRecalcState(ws_handle, False)

    # テーブルの全セルをループし、内容を設定
    for r in range(rows):
        for c in range(cols):
            # セルに書き込む文字を取得。未定義の場合は空文字
            cell_text = ""
            if r < len(data) and c < len(data[r]):
                cell_text = str(data[r][c])

            # 余分なダブルクォートを付けずに、式として文字列を渡す
            formula_str = f"{cell_text}"

            # 単一セルに対して数式をセット
            vs.SetWSCellFormulaN(ws_handle, r+1, c+1, r+1, c+1, formula_str)

    # 自動再計算の状態を元に戻す
    vs.SetWSAutoRecalcState(ws_handle, auto_recalc)

    # ワークシートを再計算
    vs.RecalculateWS(ws_handle)

    # ワークシートをウィンドウ表示(オプション)
    vs.ShowWS(ws_handle, True)

    # 図面上にワークシートイメージを配置する(オプション)
    # vs.CreateWSImage(ws_handle, 0, 0)


def main():
    # サンプルのテーブルデータ
    sample_data = [
        ["用途", "構造", "規模"],
        ["共同住宅", "RC造", "地上3階"],
        ["事務所", "S造", "地上2階"],
    ]

    # ワークシートの名称
    ws_name = "MyVectorworksWorksheet"

    # SetWSCellFormulaNを使用してワークシートにデータを反映
    create_worksheet_from_data(ws_name, sample_data)

# Vectorworksで__name__=='__main__'が呼ばれない場合もあるので、main()を直接呼ぶ
main()
