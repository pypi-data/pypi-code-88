
# Deep Q Network AI [DQN_Agent]
# 【動作確認・使用例】

import sys
import resout as rout
import matplotlib.pyplot as plt
from relpath import add_import_path, rel2abs
add_import_path("../")
# Catcherゲーム [catcher_game]
from catcher_game import game_step, action_ls, human_obs, ai_obs, gen_init_state
# Deep Q Network AI [DQN_Agent]
from DQN_Agent import DQN_Agent

# 保存パスの設定 [resout]
rout.set_save_dir("./output_img/")

train_ai = DQN_Agent(action_ls = action_ls, ai_obs = ai_obs) # Deep Q Network AI
episode_n = 700	# エピソード数
total_reward_ls = []
for episode_idx in range(episode_n):
	# state, actionの初期化
	action, state = "initial_action", gen_init_state(game_params = {})
	reward_ls = []
	# ゲーム進行
	while state["finished"] is False:
		state, reward = game_step(state, action)
		action = train_ai.think(state, reward) # 行動決定
		reward_ls.append(reward)
	total_reward_ls.append(sum(reward_ls))
	print("Episode #%d, Reward: %.1f"%(episode_idx, total_reward_ls[-1]))
# 獲得報酬の推移を表示
plt.plot(total_reward_ls)
plt.savefig(rout.gen_save_path(".png"))	# 保存ファイル名の生成(自動で連番になる) [resout]
# テスト用プレーヤーを生成 [DQN_Agent]
test_ai = train_ai.gen_test()
# state, actionの初期化
action, state = "initial_action", gen_init_state(game_params = {})
# テストプレイ
while state["finished"] is False:
	img = human_obs(state)	# 人間用の観測関数
	rout.save_img(img, ratio = 2)	# 画像の保存 [resout]
	state, reward = game_step(state, action)
	action = test_ai.think(state, reward)
