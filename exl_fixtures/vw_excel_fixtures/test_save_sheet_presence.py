import vs
import os


def test_sheet_requirement():
    """シートの有無による保存動作の検証"""

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # テスト1: シートなしで保存を試みる
    test1_path = os.path.join(desktop, "test_no_sheet.xlsx")
    vs.AlrtDialog("テスト1: シートなしで保存")

    vs.EXL_NewBook(test1_path)
    # EXL_AddSheetを呼ばない
    result1 = vs.EXL_SaveAndCloseBook(test1_path)

    if os.path.exists(test1_path):
        vs.AlrtDialog(f"✓ ファイル作成された: {test1_path}")
    else:
        vs.AlrtDialog(f"✗ ファイル作成されず: {test1_path}")

    # テスト2: シートありで保存
    test2_path = os.path.join(desktop, "test_with_sheet.xlsx")
    vs.AlrtDialog("\nテスト2: シートありで保存")

    vs.EXL_NewBook(test2_path)

    sheet_added = vs.EXL_AddSheet("MySheet")  # シートを追加
    if sheet_added:
        vs.AlrtDialog("新しいシートを追加しました")
    result2 = vs.EXL_SaveAndCloseBook(test2_path)

    if os.path.exists(test2_path):
        vs.AlrtDialog(f"✓ ファイル作成された: {test2_path}")
    else:
        vs.AlrtDialog(f"✗ ファイル作成されず: {test2_path}")


# 実行
test_sheet_requirement()
