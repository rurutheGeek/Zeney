# Zeney
### 銭 + マネー -> ゼニー
Zeneyは仮想通貨システムのデモプログラムです  
書籍「ゼロから創る暗号通貨」内のプログラムのフォークです  
ライセンスは Apache License 2.0 (元プログラムと同様)  

濵津 誠.ゼロから創る暗号通貨. PEAKS 出版,2018,305p  
https://github.com/peaks-cc/cryptocurrency-samplecode   

# Setup
### 1. 依存関係のインストール
※Windowsの場合
```bash
pip install pycryptodome
```
### 2. IPアドレスの設定
`s1_start.bat`を**実行**。すると,自身のIPアドレスを取得できます(図1)。

`s2_start.bat`及び`wallet_s1_start.bat`を**テキストエディタで開き**、IPアドレスを自身のIPアドレスに変更(図2)
<!--StartFragment-->
図1 | 図2
-- | --
![image](https://github.com/satra-11/Zeney/assets/115873069/8370eeee-0ae7-4b48-94b0-276fe23f7b79) | ![image](https://github.com/satra-11/Zeney/assets/115873069/65245252-3029-4b8e-9961-1230e96dcc5a)

<!--EndFragment-->

### 3. サーバーの起動
`s2_start.bat`及び`wallet_s1_start.bat`を実行すると、walletアプリが起動します。

# Usage

Server1.py は仮想通貨ネットワークの最初のサーバノードを起動するファイルです  
Server2.py は2つめ以降のサーバノードを起動するファイルです  
Wallet_app.py はウォレットノードを起動するファイルです  
```bash
python Server1.py ポート番号 パスフレーズ
python Server2.py  ポート番号 最初に接続するサーバのIPアドレス 最初に接続するサーバのポート番号 パスフレーズ
python Wallet_app.py  ポート番号 最初に接続するサーバのIPアドレス 最初に接続するサーバのポート番号
```
ポート番号は実行するPCで空いているところを使う  
エフェメラルポート(自由に使えるポート)である49513～65535までを使うと良い    

ソケット通信を行うためファイアウォールの設定で動作しないことがある  
