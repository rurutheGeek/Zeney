# Zeney
### 銭 + マネー -> ゼニー
Zeneyは仮想通貨システムのデモプログラムです  
書籍「ゼロから創る暗号通貨」内のプログラムのフォークです  
ライセンスは Apache License 2.0 (元プログラムと同様)  

濵津 誠.ゼロから創る暗号通貨. PEAKS 出版,2018,305p  
https://github.com/peaks-cc/cryptocurrency-samplecode   

# Requirement

* PyCrypto

# Installation

※Windowsの場合
```bash
pip install pycryptodome
```

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
