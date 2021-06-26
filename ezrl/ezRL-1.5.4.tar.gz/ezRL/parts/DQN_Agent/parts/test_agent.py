
# Deep Q Network AI for testing [test_agent.py]

import sys
# DQNの行動決定 (eps greedy戦略) [policy.py]
from .policy import eps_greedy_policy

# Deep Q Network AI for testing [test_agent.py]
class DQN_Test_Agent:
	# 初期化処理
	def __init__(self, ai_obs, qnet, action_ls, eps):
		# 各種パラメータ
		self.ai_obs, self.action_ls, self.eps = ai_obs, action_ls, eps
		# この時点のqnetをコピー
		self.fixed_qnet = qnet.clone_model(	# 複製体を作る (返り値はNormal_CNN型) [normal_cnn]
			untrained_check = False)
	# 行動決定
	def think(self, state, reward):
		obs_img = self.ai_obs(state)
		selected_a = eps_greedy_policy(obs_img, self.fixed_qnet, self.action_ls, self.eps)	# DQNの行動決定 (eps greedy戦略) [policy.py]
		if state["finished"] is True: selected_a = "finish_action"
		return selected_a	# 選択したactionを返す
