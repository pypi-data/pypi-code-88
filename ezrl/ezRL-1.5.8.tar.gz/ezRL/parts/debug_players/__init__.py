
import sys
import random

# ランダムAI
class RandomPlayer:
	# 初期化処理
	def __init__(self, action_ls):
		raise Exception("注意: 未テストです")
		self.action_ls = action_ls
	# テスト用プレーヤーを生成
	def gen_test(self):
		test_ai = self
		return test_ai
	# アクションを考える
	def think(self, state, reward):
		action = random.choice(self.action_ls)
		return action

# 人間プレーヤー [ezRL]
class HumanPlayer:
	# 初期化処理
	def __init__(self, action_ls, human_obs_func):
		self.action_ls = action_ls
		self.human_obs_func = human_obs_func
	# テスト用プレーヤーを生成
	def gen_test(self):
		test_ai = self
		return test_ai
	# アクションを考える
	def think(self, state, reward):
		print("報酬を%.2fもらえました"%reward)
		self.human_obs_func(state)
		while True:
			print("action: %s"%(", ".join(self.action_ls)))
			action = input("action>").strip()
			if action in self.action_ls: return action
			print("【！】actionが不正です")
