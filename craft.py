#ブロックのクラス (関数もセットの構造体みたいなもの)
class Block: #あとでjsonになる
	def __init__(self, transaction, previous_block_hash):
		self.timestamp = time() #タイムスタンプ
		self.transaction = transaction #トランザクション
		self.previous_block = previous_block_hash #前ブロックのハッシュ値
		#ナンス値どこいった
"""
ブロッククラスを辞書型,json変換
ブロックからハッシュ値を算出
"""
#トランザクションの構造
transaction2 = {
'sender': 'test1',
'recipient': 'test3',
'value' : 2
}
"""
Blockchain Manager
UI
Block Builder
Transaction Pool
"""
#トランザクションをまとめる.ブロックチェーンを短くする

#P2Pネットワークと接続
#PoW コンセンサス
#ブロックの検証機能

"""
トランザクションの構造
ブロックの構造
ブロックチェーンの構造
ジェネシスブロック
ブロックの生成
ハッシュ値の生成 sha256

ディフカルティ
ナンス値計算
ブロックの検証 132
"""


transaction={}


MSG_NEW_TRANSACTION = 7
MSG_NEW_BLOCK = 8
MSG_REQUEST_FULL_CHAIN = 9
RSP_FULL_CHAIN = 10

message = {
	'protocol': 'zeney_protocol', 	#プロトコルの名前
	'version': '0.1.0', 			#プロトコルのバージョン
	'msg_type': MSG_NEW_TRANSACTION,#メッセージの種別
	'my_port': 50082,				#送信者のポート番号
	'payload': transaction			#追加のデータ
}

def handle_message(msg, is_core, peer=None):
		"""
        受信したメッセージを確認して、内容に応じた処理を行う
        
        params :
            msg : 受信したメッセージ
            is_core : 送信元がサーバであるか
            peer : 送信元のアドレス情報(返信先)
        """
		if peer != None:
			if msg['msg_type'] == MSG_REQUEST_FULL_CHAIN:
				pass	#持っているブロックチェーンを送信
		else:
			if msg['msg_type'] == MSG_NEW_TRANSACTION:
				pass	#新しいトランザクションを処理
			elif msg['msg_type'] == MSG_NEW_BLOCK:
				if not is_core:
					pass#サーバでない場合は無視
				pass	#新しいブロックを検証

			elif msg['msg_type'] == RSP_FULL_CHAIN:
				if not is_core:
					pass#サーバでない場合は無視
				pass	#送信されたブロックチェーンの検証

