# HRC_Idp_plot.pyの使い方

HRCの白色ラウエ測定のデータを800x500のpngファイルにして保存するためのスクリプトです。

生成されたpngファイルは
[Neutron Laue Diffraction Pattern Simulator for HRC(BL12)](https://nakajima.issp.u-tokyo.ac.jp/tools/hrc_laue_sim/)で使用することができます。

Python3のコードです。
必要なライブラリは以下の通り。

* matplotlib
* numpy
````
python HRC_Idp_plot.py [intensity map (csv)] [Upperlimit of the intenity]
````

intensity mapはHANAでI(d,p)の強度マップを表示し、右クリックで「Save CSV」を選択。

Upperlimit of the intensityは、カラースケールの最大値がこの値に設定されることを意味します。
画像を作ってみたものの全体的に暗くてピークが見えにくいという場合は、この値を小さくすると良いと思います。

テスト用のデータとして付属している「Idp_Run14190.csv」の場合は1000くらいを指定すると良いと思います。
