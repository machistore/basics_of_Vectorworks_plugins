import vs

def test_detail_graphic_opt_dlg():
    # 初期値を設定
    marker = "Default Marker"
    shoulder_length = 10.0
    tag_pos_index = 0
    leader_type = 1
    leader_thick = 1

    # DetailGraphicOptDlg関数を呼び出してダイアログを表示し、ユーザーの入力を受け取る
    result, marker, shoulder_length, tag_pos_index, leader_type, leader_thick = vs.DetailGraphicOptDlg(
        marker, shoulder_length, tag_pos_index, leader_type, leader_thick
    )

    # ユーザーの入力結果を表示
    if result:
        vs.AlrtDialog(f"OKがクリックされました。\nMarker: {marker}\nShoulder Length: {shoulder_length}\nTag Position Index: {tag_pos_index}\nLeader Type: {leader_type}\nLeader Thickness: {leader_thick}")
    else:
        vs.AlrtDialog("キャンセルがクリックされました。")

# スクリプトを実行して動作をテスト
test_detail_graphic_opt_dlg()
