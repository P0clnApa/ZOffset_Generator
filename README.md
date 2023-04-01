# Zoffset_Generator

# 概要
Pymeshlabを用いてZbrushのメッシュ表面を (Tool:Deformation:Inflate)よりは正確にオフセットするスクリプト郡です。

# インストール方法
このスクリプトはUsers\Public\Documents\Script_Workspaceというフォルダを受け渡しフォルダとして扱い動作します

Zoffset_Generator_Package/ INSTALL-FOLDER_MAKER.bat でデータ受け渡し用フォルダを作成、表示までしてくれます。

Zoffset_Generator_Package/→Users...この中身を上記フォルダに移してください。

Zoffset_Generator_Package/→Zplugs64  この中身を任意のZbrushのZplugs64フォルダに入れてください。

# 使い方
![Screenshot_2023-04-01 134835](https://user-images.githubusercontent.com/17403397/229266221-200d03c1-adf1-4196-b79f-78b775a9a75c.png)

Offset Distance = mm単位の数値スライダーです。0.1mmが下限、50mmを上限としてます。

Offset Positive = オフセット方向を指定するトグルボタンです。オフ = 内側 オン =外側

Start Offset（見切れてるボタン）= 処理開始ボタンです。 オフセット処理中はZbrushが停止したように振る舞うのですが、コマンドラインが表示されてる間は外部で処理を実行中なので気長に待ってください。
