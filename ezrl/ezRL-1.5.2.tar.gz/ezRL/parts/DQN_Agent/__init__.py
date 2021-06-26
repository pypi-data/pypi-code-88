
# Deep Q Network AI [DQN_Agent]

import sys
# Triggerオブジェクト [trigger.py]
from .parts.trigger import Trigger
# eps値のスケジュール管理 [utils.py]
from .parts.utils import EpsAdmin
# プレイ記録 [playlog.py]
from .parts.playlog import DQNPlaylog
# 未学習時における予測関数の生成
from .parts.utils import gen_rand_pred_func
# qnetの双子 (qnetと重みを時々同期する) [target_twin.py]
from .parts.target_twin import TargetTwin
# DQNの行動決定 (eps greedy戦略) [policy.py]
from .parts.policy import eps_greedy_policy
# qnetの学習 [train_qnet.py]
from .parts.train_qnet import train_qnet
# Deep Q Network AI for testing [test_agent.py]
from .parts.test_agent import DQN_Test_Agent
from relpath import add_import_path
add_import_path("../")
# シンプルなCNN [normal_cnn]
from normal_cnn import Normal_CNN

# qnetのネットワーク構成 (default構成)
default_nn_param = {
	"conv_layer_info": [
		# {"n_filter": 8, "kernel_size": (5, 5)},
		# {"n_filter": 16, "kernel_size": (5, 5)},
		# {"n_filter": 32, "kernel_size": (5, 5)},
	],
	"dense_layer_info": [
		{"unit_n": 512, "activation": "relu"},
		{"unit_n": 128, "activation": "relu"},
		{"unit_n": 32, "activation": "relu"},
		{"unit_n": 8, "activation": "relu"},
	],
	"output_activation": None
}

# Deep Q Network AI
class DQN_Agent:
	# 初期化処理
	def __init__(self,
		action_ls, ai_obs, gamma = 0.9, buffer_size = 5000,
		train_data_ratio = 0.1, # Experience Replay時にlogから取り出すデータの割合
		learning_trigger = ["step_n", 100],	# qnet学習のタイミング (["finished_n", 3], ["step_n", 300], 関数指定など)
		target_update_trigger = ["step_n", 300],	# target_net更新のタイミング (["finished_n", 3], ["step_n", 300], 関数指定など)
		eps_schedule = [0.5, 0.0, "finished_n", 500],	# epsの変化スケジュール ([start, end, n_type, n]または関数指定)
		nn_param = default_nn_param
	):
		self.action_ls = action_ls
		self.ai_obs = ai_obs	# ai_obs_imgを生成する関数
		self.dqn_param = {"gamma": gamma, "train_data_ratio": train_data_ratio}	# dqnの学習等設定パラメータ
		self.learning_trigger = Trigger(learning_trigger)	# Triggerオブジェクトの初期化 (指定方法: ["finished", 3]または関数指定) [trigger.py]
		self.target_update_trigger = Trigger(target_update_trigger)	# Triggerオブジェクトの初期化 (指定方法: ["finished", 3]または関数指定) [trigger.py]
		self.eps_admin = EpsAdmin(eps_schedule)	# eps値のスケジュール管理 [utils.py]
		self.playlog = DQNPlaylog(buffer_size)	# プレイ記録 [playlog.py]
		rand_pred_func = gen_rand_pred_func(len(self.action_ls))	# 未学習時における予測関数の生成 (numpy配列の型で生成)
		self.qnet = Normal_CNN(len(self.action_ls), nn_param, loss = "mse", optimizer = "RMSprop", untrained_pred_func = rand_pred_func)	# シンプルなCNN [normal_cnn]
		self.tnet = TargetTwin(self.qnet)	# qnetの双子 (qnetと重みを時々同期する) [target_twin.py]
		self.step_cnt, self.finished_cnt = 0, 0	# アクションのステップ数・finishedを通過した回数 (多くの場合エピソードの回数に対応)
	# 行動決定
	def think(self, state, reward):
		obs_img = self.ai_obs(state)
		selected_a = eps_greedy_policy(obs_img, self.qnet, self.action_ls, self.eps_admin.get_eps())	# DQNの行動決定 (eps greedy戦略) [policy.py]
		if state["finished"] is True: selected_a = "finish_action"
		self.playlog.append(selected_a, state, obs_img, reward)	# playlog追記 [playlog.py]
		self.__train_and_update(state["finished"])	# 学習や状態更新 (finished_cntの更新など)
		return selected_a	# 選択したactionを返す
	# 学習や状態更新 (finished_cntの更新など)
	def __train_and_update(self, finished_flag):
		# カウンターのインクリメント
		self.step_cnt += 1
		if finished_flag is True: self.finished_cnt += 1
		# モデルの学習
		if self.learning_trigger.judge(self.step_cnt, self.finished_cnt):	# triggerタイミングの判断 [trigger.py]
			train_qnet(self.qnet, self.tnet, self.playlog, self.action_ls, self.dqn_param)	# qnetの学習 [train_qnet.py]
		# tnet(target)の更新
		if self.target_update_trigger.judge(self.step_cnt, self.finished_cnt):	# triggerタイミングの判断 [trigger.py]
			self.tnet.update_by_twin_weight()	# weightを更新 (双子の姉のweightに基づく) [target_twin.py]
		# EpsAdminの更新
		self.eps_admin.update(self.step_cnt, self.finished_cnt)	# eps値算出根拠の更新
	# テスト用プレーヤーを生成 [DQN_Agent]
	def gen_test(self):
		# Deep Q Network AI for testing [test_agent.py]
		test_ai = DQN_Test_Agent(self.ai_obs, self.qnet, self.action_ls, eps = 0.0)
		return test_ai
