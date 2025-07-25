import vs  # Vectorworks用のモジュールをインポート


def read_file_to_dict(file_path):
    """
    テキストファイルを読み込み、その内容を辞書に変換します。
    各行はコロンで区切られたキーと値のペアである必要があります。

    Vectorworks API関数 Open, EOF, ReadLn, Close を使用してファイル操作を行います。
    """
    data_dict = {}

    # vs.Open はファイルパスのみでファイルを開きます。
    file_id = vs.Open(file_path)
    if not file_id:
        vs.AlrtDialog(f"File not found or cannot be opened: {file_path}")
        return data_dict

    try:
        # vs.EOF をファイルの終端まで繰り返しチェック
        while not vs.EOF(file_id):
            line = vs.ReadLn(file_id)
            if not line:
                continue
            # 余分な空白を削除し、最初のコロンで分割する
            parts = line.strip().split(":", 1)
            if len(parts) == 2:
                key, value = parts
                data_dict[key.strip()] = value.strip()
            else:
                vs.AlrtDialog(f"Invalid line format: {line.strip()}")
    except Exception as e:
        vs.AlrtDialog(f"An error occurred: {e}")
    finally:
        vs.Close(file_id)

    return data_dict


# Example usage
if __name__ == "__main__":
    title = 'Select the text file...'
    defaultFolder = ''
    mask = 'txt'
    # GetFileN はタプル (boolean, fileName) を返します。
    success, file_path = vs.GetFileN(title, defaultFolder, mask)
    if success:
        dictionary = read_file_to_dict(file_path)
        vs.AlrtDialog(str(dictionary))
    else:
        vs.AlrtDialog("No file selected.")
