
# debug用プレーヤー [debug_players]
# 【動作確認 / 使用例】

import sys
import resout as rout
import ezpip
ezRL = ezpip.load_develop("ezRL", "../../../")
game = ezRL.catcher_game

def human_obs_func(state):
	rout.save_img(game.human_obs(state), ratio = 2)	# 画像の保存 [resout]

rout.set_save_dir("./results/")	# 保存パスの設定 [resout]
h_player = ezRL.HumanPlayer(action_ls = game.action_ls, human_obs_func = human_obs_func)	# 人間プレーヤー [ezRL]
ezRL.do_episodes(game, h_player, game_params = {}, episode_n = 1)	# 複数エピソード実行
