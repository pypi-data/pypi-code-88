
# エピソード関係処理 [episode.py]

import sys
import resout as rout
import matplotlib.pyplot as plt

# エピソードを実行 [episode.py]
def do_episode(game, ai, game_params, save_img = False):
	# state, actionの初期化
	action, state = "initial_action", game.gen_init_state(game_params)
	# ゲーム進行
	reward_ls = []
	while state["finished"] is False:
		if save_img is True:
			rout.save_img(game.human_obs(state), ratio = 2)	# 画像の保存 [resout]
		state, reward = game.game_step(state, action)
		action = ai.think(state, reward) # 行動決定
		reward_ls.append(reward)
	return reward_ls

# 複数エピソード実行 [episode.py]
def do_episodes(game, train_ai, game_params, episode_n, save_img = False, save_reward_ls = False):
	total_reward_ls = []
	for episode_idx in range(episode_n):
		reward_ls = do_episode(game, train_ai, game_params, save_img)	# エピソードを実行
		total_reward_ls.append(sum(reward_ls))
		print("Episode #%d, Reward: %.1f"%(episode_idx, total_reward_ls[-1]))
	# 獲得報酬の推移を表示
	if save_reward_ls is True:
		plt.plot(total_reward_ls)
		plt.savefig(rout.gen_save_path(".png"))	# 保存ファイル名の生成(自動で連番になる) [resout]
