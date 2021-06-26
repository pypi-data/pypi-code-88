
# DQNの行動決定 [policy.py]

import sys
import random
import numpy as np

def arg_max(arg_ls):
	# インデックス付きリストの作成
	idx_e_ls = list(enumerate(arg_ls))
	# 最大値のインデックスを取得
	idx = max(idx_e_ls, key = lambda x: x[1])[0]
	return idx

# 1枚の画像に対する予測
def one_pred(obs_img, qnet):
	test_x = np.array([obs_img])
	raw_result = qnet.predict(test_x)
	q_ls = raw_result[0]
	return q_ls

# DQNの行動決定 (eps greedy戦略) [policy.py]
def eps_greedy_policy(obs_img, qnet, action_ls, eps):
	# Epsilon Greedyにより、一定確率でランダムな行動を選ぶ
	if random.random() < eps:
		# ランダムに行動を選ぶ
		selected_a = random.choice(action_ls)
	else:
		q_ls = one_pred(obs_img, qnet)	# 1枚の画像に対する予測
		selected_a = action_ls[arg_max(q_ls)]	# Q値が最も高いactionを選ぶ
	return selected_a
