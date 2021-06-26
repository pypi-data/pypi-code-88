
import sys
import random
# from .utils import show_img 

# ランダムAI
class RandomPlayer:
	# 初期化処理
	def __init__(self, action_ls):
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
	def __init__(self, action_ls, human_obs):
		raise Exception("HumanPlayerを動作させるためには、画像出力をresoutの仕様に合わせる必要があります。")
		self.action_ls = action_ls
		self.human_obs = human_obs
	# アクションを考える
	def think(self, state, reward):
		print("報酬を%.2fもらえました"%reward)
		obs_img = self.human_obs(state)
		show_img(obs_img, waitKey = 100, ratio = 0.5, interpolation = "INTER_CUBIC")	# 状態の表示
		while True:
			print("action: %s"%(", ".join(self.action_ls)))
			action = input("action>").strip()
			if action in self.action_ls: return action
			print("【！】actionが不正です")
