
# プレイ記録 [playlog.py]

import sys
from sout import souts
from collections import deque

# プレイ記録 [playlog.py]
class DQNPlaylog:
	# 初期化処理
	def __init__(self, buffer_size):
		# プレイ記録の格納場所
		self.data = deque(
			[{"now_finished": True}],
			maxlen = buffer_size
		)
	# playlog追記 [playlog.py]
	def append(self, selected_a, state, obs_img, reward):
		self.data.append({
			"prev_obs": self.__get_prev_log("now_obs"), "prev_action": self.__get_prev_log("now_action"),	# 一つ前Stepのログの要素を参照する [playlog.py]
			"now_obs": obs_img,	"now_action": selected_a,
			"now_reward": reward, "now_finished": state["finished"]
		})
	# 全レコードを取得 [playlog.py]
	def get_all_data(self):
		return list(self.data)	# リスト型にして返す
	# 文字列化
	def __str__(self):
		ret_str = "last data of playlog:\n"
		ret_str += souts(self.data[-1], None) + "\n"
		ret_str += "(playlog entry n = %d)\n"%len(self.data)
		return ret_str
	# 文字列化その2
	def __repr__(self):
		return str(self)
	# 一つ前Stepのログの要素を参照する [playlog.py]
	def __get_prev_log(self, key):
		if self.data[-1]["now_finished"] is True:
			return None
		return self.data[-1][key]
