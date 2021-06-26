
# デモ [demo.py]

import sys

# エピソードを実行
def do_episode(game, ai, game_params, save_img = False):
	import resout as rout
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

# 複数エピソード実行
def do_episodes(game, train_ai, game_params, episode_n, save_img = False, save_reward_ls = False):
	import resout as rout
	import matplotlib.pyplot as plt
	total_reward_ls = []
	for episode_idx in range(episode_n):
		reward_ls = do_episode(game, train_ai, game_params, save_img)	# エピソードを実行
		total_reward_ls.append(sum(reward_ls))
		print("Episode #%d, Reward: %.1f"%(episode_idx, total_reward_ls[-1]))
	# 獲得報酬の推移を表示
	if save_reward_ls is True:
		plt.plot(total_reward_ls)
		plt.savefig(rout.gen_save_path(".png"))	# 保存ファイル名の生成(自動で連番になる) [resout]

# デモ (DQN-catcher) [demo.py]
def dqn_catcher_demo():
	import resout as rout
	from relpath import add_import_path
	add_import_path("./")
	import catcher_game as game	# Catcherゲーム [catcher_game]
	from DQN_Agent import DQN_Agent	# Deep Q Network AI [DQN_Agent]
	rout.set_save_dir("./ezRL_demo_output/")	# 保存パスの設定 [resout]
	train_ai = DQN_Agent(action_ls = game.action_ls, ai_obs = game.ai_obs) # Deep Q Network AI
	do_episodes(game, train_ai, game_params = {}, episode_n = 700, save_reward_ls = True)	# 複数エピソード実行
	test_ai = train_ai.gen_test()	# テスト用プレーヤーを生成 [DQN_Agent]
	do_episodes(game, test_ai, game_params = {}, episode_n = 1, save_img = True)	# 複数エピソード実行
	print("demo finished! (results are in \"./ezRL_demo_output/\".)")

# デモ [demo.py]
def demo(demo_name = "DQN-catcher"):
	if demo_name == "DQN-catcher":
		dqn_catcher_demo()
	else:
		raise Exception("[ezRL error] invalid demo name.")
