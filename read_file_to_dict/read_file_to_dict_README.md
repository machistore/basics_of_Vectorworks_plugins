# read_file_to_dict

Vectorworks Python APIを使用してテキストファイルを読み込み、辞書形式に変換するユーティリティスクリプトです。

## 概要

このスクリプトは、コロン（`:`）で区切られたキー-値ペアが記述されたテキストファイルを読み込み、Python辞書として変換します。Vectorworks APIの標準ファイル操作関数を使用してファイルの読み込みを行います。

## 機能

- テキストファイルの読み込み
- コロン区切りフォーマットの解析
- Python辞書への変換
- エラーハンドリング
- ファイル選択ダイアログ

## 使用方法

### 1. 直接実行
スクリプトをVectorworksで直接実行すると、ファイル選択ダイアログが表示されます：

```python
read_file_to_dict.py
```

### 2. 関数として使用
[`read_file_to_dict`](read_file_to_dict.py)関数を他のスクリプトから呼び出すことも可能です：

```python
from read_file_to_dict import read_file_to_dict

# ファイルパスを指定して実行
result = read_file_to_dict("path/to/your/file.txt")
print(result)
```

## ファイル形式

入力ファイルは以下の形式である必要があります：

```
key1: value1
key2: value2
key3: value3
```

### 例
```
name: John Doe
age: 30
city: Tokyo
email: john@example.com
```

上記のファイルは以下の辞書に変換されます：
```python
{
    'name': 'John Doe',
    'age': '30',
    'city': 'Tokyo',
    'email': 'john@example.com'
}
```

## 要件

- Vectorworks Python環境
- `vs`モジュール（Vectorworks API）

## エラーハンドリング

- ファイルが見つからない場合や開けない場合
- 無効な行フォーマット（コロンが含まれない行）
- ファイル読み込み中の例外

すべてのエラーは`vs.AlrtDialog`を通じてユーザーに通知されます。

## 注意事項

- このスクリプトはVectorworks環境でのみ動作します
- ファイルは自動的に閉じられるため、リソースリークの心配はありません
- 空行は自動的にスキップされます
- キーと値の前後の空白は自動的にトリミングされます

---

# English Version

# read_file_to_dict

A utility script for reading text files and converting them to dictionary format using the Vectorworks Python API.

## Overview

This script reads text files containing key-value pairs separated by colons (`:`) and converts them to Python dictionaries. It uses Vectorworks API standard file operation functions for file reading.

## Features

- Text file reading
- Colon-separated format parsing
- Conversion to Python dictionary
- Error handling
- File selection dialog

## Usage

### 1. Direct Execution
If you run the script directly in Vectorworks, a file selection dialog will appear:

```python
read_file_to_dict.py
```

### 2. Function Usage
The [`read_file_to_dict`](read_file_to_dict.py) function can also be called from other scripts:

```python
from read_file_to_dict import read_file_to_dict

# Execute with specified file path
result = read_file_to_dict("path/to/your/file.txt")
print(result)
```

## File Format

Input files must be in the following format:

```
key1: value1
key2: value2
key3: value3
```

### Example
```
name: John Doe
age: 30
city: Tokyo
email: john@example.com
```

The above file will be converted to the following dictionary:
```python
{
    'name': 'John Doe',
    'age': '30',
    'city': 'Tokyo',
    'email': 'john@example.com'
}
```

## Requirements

- Vectorworks Python environment
- `vs` module (Vectorworks API)

## Error Handling

- When files are not found or cannot be opened
- Invalid line format (lines without colons)
- Exceptions during file reading

All errors are notified to users through `vs.AlrtDialog`.

## Notes

- This script only works in the Vectorworks environment
- Files are automatically closed, so there's no concern about resource leaks
- Empty lines are automatically skipped
- Leading and trailing whitespace in keys and values are automatically trimmed
