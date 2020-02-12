# 虹彩検出システム
pythonによるOpenCVとdlibを利用した虹彩検出システムです。


# 環境
* python 3.6
* OpenCV 4.1
* dlib 19.18

# 学習モデル
学習済みモデルはdlibの公式サイトの以下から入手しました。

* **dlib ～Index of /files～**<br>
http://dlib.net/files/
<br>→「shape_predictor_68_face_landmarks.dat.bz2 」を選択

余談ですが上記の学習済みモデルは以下のサイトのデータを元に生成されています。

* **i・bug ～Facial point annotations～**<br>
https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/


# 使い方
本プロジェクトをダウンロード後、適切なディレクトリに配置し、「gaze_cv」ディレクトリ配下で以下を実行します。
```
python main.py <数字>
```
<数字>には使用するWebカメラの番号を入力してください。<br>
0から始まる接続されているカメラの番号です。<br>
1台しか接続していない場合は「0」を、3台接続されている内2番めを使いたい場合は「1」を指定してください。<br>
※デフォルト(=引数未設定の場合)には「0」が指定されます。<br>

コマンド実行後、カメラ画像が表示され、顔が映ると虹彩を緑の円で検出します。<br>
本システムを終了する場合、「q」キーを入力してください。


# デモ
![デモ動画](https://github.com/33taro/gaze_cv/blob/master/readme_img/demo.gif "デモ動画")


