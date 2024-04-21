### 仕様書1: 数式設定スクリプト

**識別子**: 数式設定スクリプト  
**作成日**: 2024-04-20  
**更新日**: 2024-04-20  
**適用ソフトウェア**: Vectorworks 2024  
**対応OS**: Windows 11 Home (23H2)  
**作成者**: Katsutoshi Machida  
**注意事項**:  
- 「Sample Worksheet」という名のワークシートが生成されます。
- 4行2列に「=3*2」の数式が設定されます。
- 1行1列から2行10列に空文字列「<empty>」を設定します。
- 3行0列に「=DATABASE(L='レイヤー1')」の数式を設定します（0列目は条件式を指定するための列）。
- ワークシートを表示します。

**ソース**: [Vectorworks Developer](https://developer.vectorworks.net/index.php?title=VS:SetWSCellFormula)

```python
import vs

ws_name = 'Sample Worksheet'
ws_handle = vs.CreateWS(ws_name, 10, 10)

vs.SetWSCellFormula(ws_handle,4,2,4,2,'=3*2')
vs.SetWSCellFormula(ws_handle,1,1,2,10,'<empty>')
vs.SetWSCellFormula(ws_handle,3,0,3,0,"=DATABASE(L='レイヤ-1')")

vs.ShowWS(ws_handle, True)
```

### 仕様書2: ヘッダー付きワークシート作成スクリプト

**識別子**: ヘッダー付きワークシート作成スクリプト  
**作成日**: 2024-04-21  
**更新日**: 2024-04-21  
**適用ソフトウェア**: Vectorworks 2024  
**対応OS**: Windows 11 Home (version 23H2)  
**作成者**: Katsutoshi Machida  
**機能**:  
- 'Sample_Worksheet_2'という名のワークシートを生成します。
- ヘッダー「ID」と「NAME」を1行目に設定します。
- 2行目にデータ「1」と「ippan」を設定します。
- ワークシートを表示します。

```python
import vs

def create_worksheet_with_headers():
    ws_name = 'Sample_Worksheet_2'
    ws_handle = vs.CreateWS(ws_name, 2, 2)

    vs.SetWSCellFormula(ws_handle, 1, 1, 1, 1, 'ID')
    vs.SetWSCellFormula(ws_handle, 1, 2, 1, 2, 'NAME')
    vs.SetWSCellFormula(ws_handle, 2, 1, 2, 1, '1')
    vs.SetWSCellFormula(ws_handle, 2, 2, 2, 2, '\'ippan\'')

    vs.ShowWS(ws_handle, True)

create_worksheet_with_headers()
```
