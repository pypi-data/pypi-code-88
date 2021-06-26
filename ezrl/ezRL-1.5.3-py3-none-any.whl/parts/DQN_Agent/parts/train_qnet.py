
# qnetの学習 [train_qnet.py]

import sys
import random
import numpy as np

# 攪拌 + リサンプリングするためのインデックスのリストを生成
def gen_random_idx_ls(n, ratio):
	idx_ls = random.sample(list(range(n)), k = int(n * ratio))
	return idx_ls

# playlogから教師データの生成 [train_qnet.py]
def gen_train_data(playlog, tnet, action_ls, dqn_param):
	# 全レコードを取得 [playlog.py]
	playlog_data = playlog.get_all_data()
	# prev_obsが存在しないデータを除く
	filtered_playlog_ls = [e for e in playlog_data if e.get("prev_obs", None) is not None]
	# 学習データ(入力側)の生成
	input_ls = np.array([one_log["prev_obs"] for one_log in filtered_playlog_ls])
	# 学習データ(出力側)の生成
	esitimated_ls = tnet.predict(input_ls)	# 学習の安定のため、重みを固定したNNによってQ値を計算
	output_ls = np.array(esitimated_ls)
	action_idx_dict = {a:i for i, a in enumerate(action_ls)} # アクション名から通し番号を取り出す辞書
	for log_idx, one_log in enumerate(filtered_playlog_ls):
		# エピソード終了の1つ前のstateのみ遷移先基準のQ値が計算できないため、条件分岐
		if one_log["now_finished"] is True:
			gain = one_log["now_reward"]
		else:
			if log_idx + 1 >= len(esitimated_ls): continue	# 次stepの情報がないやつは学習に加えない
			next_s_max_q = max(esitimated_ls[log_idx + 1])
			gain = one_log["now_reward"] + dqn_param["gamma"] * next_s_max_q
		# 実際に取った行動のQ値のみ更新
		action_idx = action_idx_dict[one_log["prev_action"]]	# アクション名から通し番号を取り出す辞書
		output_ls[log_idx][action_idx] = gain
	# 攪拌 + リサンプリングして学習
	idx_ls = gen_random_idx_ls(n = len(input_ls), ratio = dqn_param["train_data_ratio"])	# 攪拌 + リサンプリングするためのインデックスのリストを生成
	train_x, train_y = input_ls[idx_ls], output_ls[idx_ls]
	return train_x, train_y

# qnetの学習 [train_qnet.py]
def train_qnet(qnet, tnet, playlog, action_ls, dqn_param):
	# playlogから教師データの生成 [train_qnet.py]
	train_x, train_y = gen_train_data(playlog, tnet, action_ls, dqn_param)
	# 学習データが0件のときに学習をスキップする
	if len(train_x) == 0:
		print("[DQN_Agent warning] gen_train_data()の結果生成された学習でーたが0件のため、学習をスキップします。")
		return None
	# サンプル中の1つのバッチで勾配を更新 [normal_cnn]
	loss = qnet.train_on_batch(train_x, train_y)
	# print("loss: %.4f"%loss)
