
# Triggerオブジェクト [trigger.py]

import sys

# triggerの指定方法が不正の例外を投げる
def raise_trigger_syntax_ex():
	raise Exception("triggerの指定方法が不正です")

# step, finishedから選ぶ
def switch_history(step_cnt_history, finished_cnt_history, config_type):
	if config_type == "step_n":
		return step_cnt_history
	elif config_type == "finished_n":
		return finished_cnt_history
	else:
		raise_trigger_syntax_ex()	# triggerの指定方法が不正の例外を投げる

# nの倍数を超えた瞬間を検知するトリガー
def sequence_trigger(sequence, n):
	if len(sequence) < 2: return False
	pre, now = sequence[-2:]
	flag = pre//n != now//n
	return flag

# triggerの指定に従ってjudge_funcを生成 (["finished_n", 3]など)
def gen_judge_func(trigger_config):
	# 関数指定されている場合
	if type(trigger_config) == type(lambda:None):
		judge_func = trigger_config
		return judge_func
	# 型の正当性の判定
	elif type(trigger_config) != type([]): raise_trigger_syntax_ex()	# triggerの指定方法が不正の例外を投げる
	if len(trigger_config) != 2: raise_trigger_syntax_ex()	# triggerの指定方法が不正の例外を投げる
	# リスト指定の場合
	config_type, n = trigger_config	# 設定値の解釈
	def judge_func(step_cnt_history, finished_cnt_history):
		# step, finishedから選ぶ
		history = switch_history(step_cnt_history, finished_cnt_history, config_type)
		# nの倍数を初めて超えた瞬間を検知するトリガー
		flag = sequence_trigger(sequence = history, n = n)
		return flag
	return judge_func

# Triggerオブジェクト [trigger.py]
class Trigger:
	# Triggerオブジェクトの初期化 (指定方法: ["finished", 3]または関数指定) [trigger.py]
	def __init__(self, trigger_config):
		# 履歴
		self.step_cnt_history = []
		self.finished_cnt_history = []
		# triggerの指定に従ってjudge_funcを生成 (["finished_n", 3]など)
		self.judge_func = gen_judge_func(trigger_config)
	# triggerタイミングの判断 [trigger.py]
	def judge(self, step_cnt, finished_cnt):
		# historyの更新
		self.step_cnt_history.append(step_cnt)
		self.finished_cnt_history.append(finished_cnt)
		# judge関数の呼び出し
		return self.judge_func(self.step_cnt_history, self.finished_cnt_history)
