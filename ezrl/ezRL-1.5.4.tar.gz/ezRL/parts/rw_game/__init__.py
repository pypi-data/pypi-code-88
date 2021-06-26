
# 紅白ゲーム [rw_game]

raise Exception("mijisso!")

########## 以下、古い実装

# # テスト用ゲーム (紅白ゲーム)
# class RW_Game:
# 	# 初期化処理
# 	def __init__(self, round_n):
# 		self.round_n = round_n
# 		self.q_idx = 0	# 何問目か
# 		# 次の正解を作る
# 		self.renew_ans()
# 	# 現在のプレーヤーを返す
# 	def now_player(self):
# 		return 0	# 1人用ゲームなので手番は変化しない
# 	# 観測
# 	def observe(self, p_id = None):
# 		# 終了している場合はobserveできない
# 		if self.finished() is True: raise Exception("[error] 既にゲームが終了しています。")
# 		# p_id指定なし(現在の手番)の場合は、p_id==0とする(1人用ゲームなので)
# 		if p_id is None: p_id = 0
# 		# 画像を作る
# 		obs_img = np.zeros((200,200,3), dtype = np.uint8)
# 		obs_img[:,:,:] = 220	# 全て白で塗る
# 		if self.true_ans == 0:
# 			obs_img[:,:,:-1] = 30
# 		return obs_img
# 	# アクションの実行
# 	def action(self, action):
# 		# 終了している場合はactionできない
# 		if self.finished() is True: raise Exception("[error] 既にゲームが終了しています。")
# 		# actionの型の判定
# 		if len(action) != 2: raise Exception("[error] actionの型が不正です")
# 		# action配列のデコード
# 		r_value, w_value = action
# 		rw_action = int(w_value > r_value)
# 		# rewardの設定
# 		reward = int(self.true_ans == rw_action)
# 		# 出題数をインクリメント
# 		self.q_idx += 1
# 		# 次の正解を作る
# 		self.renew_ans()
# 		return reward
# 	# 次の正解を作る
# 	def renew_ans(self):
# 		self.true_ans = int(random.random()*2)
# 	# 終了判定
# 	def finished(self):
# 		if self.q_idx >= self.round_n: return True
# 		return False
