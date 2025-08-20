import vs
import os

# 基本設定
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
excel_file_path = os.path.join(desktop, "sample.xlsx")

# 必須3ステップ
vs.EXL_NewBook(excel_file_path)
vs.EXL_AddSheet("データ")  # 必須！
vs.EXL_SetCellString(0, 0, 0, "A1セルのデータ")  # 0ベースインデックス
vs.EXL_SaveAndCloseBook(excel_file_path)
