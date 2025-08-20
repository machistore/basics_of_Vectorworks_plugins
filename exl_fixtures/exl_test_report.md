# VectorworksのExcel API動作検証報告書

**作成日**: 2025年1月
**検証環境**: Vectorworks 2021以降

## 1. 検証の背景
`EXL_NewBook`関数でExcelファイルを作成しようとしたが、物理ファイルが生成されない問題が発生。

## 2. 判明した仕様

### ❌ 動作しない例
```python
vs.EXL_NewBook(file_path)
vs.EXL_SaveAndCloseBook(file_path)  # ファイル作成されず
```

### ✅ 動作する例
```python
vs.EXL_NewBook(file_path)
vs.EXL_AddSheet("シート名")  # この行が必須！
vs.EXL_SaveAndCloseBook(file_path)  # ファイル作成成功
```

## 3. Excel API必須要件

1. **`EXL_NewBook`** - メモリ上にワークブック作成
2. **`EXL_AddSheet`** - シート追加（**省略不可**）
3. **`EXL_SaveAndCloseBook`** - 物理ファイルとして保存

## 4. 実用コード例

```python
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
```
## 5. テストコード例
```python
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
```

## 6. 重要な注意点

- インデックスは**すべて0から開始**（sheet=0, row=0, column=0）
- `EXL_AddSheet`を呼ばないと、保存関数を実行してもファイルは作成されない
- `EXL_CloseBook`関数は存在しない（`EXL_SaveAndCloseBook`を使用）

## 7. トラブルシューティング

| 症状 | 原因 | 対策 |
|------|------|------|
| ファイルが作成されない | `EXL_AddSheet`の呼び出し忘れ | シート追加を必ず実行 |
| データが書き込まれない | インデックスの誤り | 0ベースで指定 |

---

**検証完了**: 内容を確認し、必須要件の`EXL_AddSheet`の重要性と0ベースインデックスの仕様を明確に記載済み。