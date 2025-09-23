# EC2のAMI作成手順

1. 各種Windows設定
   - Dark Mode
   - ゴミ箱削除確認
   - ファイル拡張子
   - 隠しファイル表示
   - VSCode
     - VS Keymap
     - Python拡張
   - Powershell最新バージョン
   - Windows Terminal設定
   - x64再頒布可能パッケージなどがインストールされていることを確認
   - Windows Defender設定
2. semiauto_set_up.ps1を実行
3. 不要ファイル削除
4. EC2のインスタンス一覧から
   1. アクション > イメージとテンプレート > イメージを作成
   2. イメージ名と説明を入力、「インスタンスを再起動」と「終了時に削除」にチェックが入っていることを確認\
      (これは仮のイメージになるので最終的なイメージ名は使わない方が良い。)
   3. イメージを作成をクリック。
5. EC2のAMIの欄にイメージが表示される。
   5-20分ほど待つと利用可能ステータスになった。
6. この時点で元のインスタンスは終了して良い。
7. AMIを選択し、「AMIからインスタンスを起動」をクリック。
   - 元と同じインスタンスタイプやネットワーク設定を選択
8. 起動したインスタンスにRDP
   - 元のインスタンスと同じパスワードでつながる。
   1. スタートメニューからAmazon EC2Launch settings
   2. Administrator password settingsがRandom (retrieve from console)になっていることを確認。
   3. Shutdown with Sysprepをクリック
      You have unsaved changes...というダイアログが出るがシャットダウン。
      この後このインスタンスは起動しないこと。
   4. 停止済みになるのを待つ。
9. 4-5を再度起動中のインスタンスに対して実施。
   (最終的なイメージ名をつける。)
10. AMIからインスタンスを起動する。
    Windowsのパスワード復号には10分弱待つ必要があった。

AMIの削除
1. AMI一覧からAMIを選択し「AMIを登録解除」
2. EBS > スナップショットから関連するスナップショットを削除。

AMIの公開
1, AMI一覧からAMIを選択し「AMI許可を編集」
2. AMIの可用性をパブリックに変更。

userdata.xmlの実行結果格納場所
C:\Windows\System32\config\systemprofile\AppData\Local\Temp\