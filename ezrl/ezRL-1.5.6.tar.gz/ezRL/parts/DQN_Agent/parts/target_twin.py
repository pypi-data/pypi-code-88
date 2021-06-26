
# qnetの双子 (qnetと重みを時々同期する) [target_twin.py]

import sys

# qnetの双子 (qnetと重みを時々同期する) [target_twin.py]
class TargetTwin:
	# 初期化処理
	def __init__(self, original_net):
		self.original_net = original_net
		# 未学習時の予測関数 (双子の姉のやつ)
		self.original_untrained_pred_func = self.original_net.untrained_pred_func
		self.model = None
	# 予測
	def predict(self, test_x):
		if self.model is None:
			return self.original_untrained_pred_func(test_x)
		else:
			return self.model.predict(test_x)
	# weightを更新 (双子の姉のweightに基づく) [target_twin.py]
	def update_by_twin_weight(self):
		if self.original_net.is_trained() is True:	# 未学習判定 (1度でも学習されたかどうか)
			if self.model is None:
				self.model = self.original_net.clone_model()	# 複製体を作る (返り値はNormal_CNN型) [normal_cnn]
			else:
				self.model.weight_update(self.original_net)	# weightを複写する (別のNormal_CNNオブジェクトから) [normal_cnn]
		else:
			# 未初期化時
			pass	# 何もしない
