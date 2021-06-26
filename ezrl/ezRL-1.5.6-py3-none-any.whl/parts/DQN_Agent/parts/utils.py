
import random
import numpy as np

# schedule_configの指定方法が不正の例外を投げる
def raise_schedule_config_syntax_ex():
	raise Exception("schedule_configの指定方法が不正です")

# 端部耳あり線形スケジューラー (start, end, nの指定に基づく)
def linear_ear_scheduler(cnt, start, end, n):
	# 無次元化cntを求める
	raw_cnt_ratio = cnt / n
	# 無次元化cntをクリッピング
	cnt_ratio = min(max(raw_cnt_ratio, 0), 1)
	# 配分して返す
	return start + cnt_ratio * (end - start)

# eps値のスケジュール管理 [utils.py]
class EpsAdmin:
	# 初期化処理
	def __init__(self, eps_schedule):
		# 誤った型・形式で指定されている場合の対処
		if type(eps_schedule) == type([]):
			if len(eps_schedule) != 4: raise_schedule_config_syntax_ex()	# schedule_configの指定方法が不正の例外を投げる
			self.n_type = eps_schedule[2]
		elif type(eps_schedule) == type(lambda:None):
			self.n_type = "function"	# そのまま通す
		else:
			raise_schedule_config_syntax_ex()	# schedule_configの指定方法が不正の例外を投げる
		# クラスの持ち物
		self.eps_schedule = eps_schedule
		self.update(step_cnt = 0, finished_cnt = 0)	# 初期値の設定
	# eps値算出根拠の更新
	def update(self, step_cnt, finished_cnt):
		self.step_cnt, self.finished_cnt = step_cnt, finished_cnt
	# eps値の取得
	def get_eps(self):
		if self.n_type == "function":
			schedule_func = self.eps_schedule
			return schedule_func(self.step_cnt, self.finished_cnt)
		elif self.n_type == "step_n":
			start, end, _, n = self.eps_schedule	# 指定を解釈
			return linear_ear_scheduler(self.step_cnt, start, end, n)	# 端部耳あり線形スケジューラー (start, end, nの指定に基づく)
		elif self.n_type == "finished_n":
			start, end, _, n = self.eps_schedule	# 指定を解釈
			return linear_ear_scheduler(self.finished_cnt, start, end, n)	# 端部耳あり線形スケジューラー (start, end, nの指定に基づく)
		else:
			raise Exception("[EpsAdmin error] 未定義のn_typeが指定されています")

# 未学習時における予測関数の生成 (numpy配列の型で生成)
def gen_rand_pred_func(action_n):
	# 未学習時における予測関数
	def rand_pred_func(test_x):
		return np.array([
			[random.random() for _ in range(action_n)]
			for _ in test_x
		])
	return rand_pred_func
