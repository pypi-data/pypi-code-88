
# シンプルなCNN [normal_cnn]

import sys
import numpy as np
# デフォルトの「未学習時における予測関数」 (エラーで落ちる挙動)
from .parts.utils import default_untrained_pred_func

# 標準的な畳み込み層
def normal_conv_layer(x, n_filter, kernel_size):
	from keras import layers
	x = layers.Conv2D(n_filter, kernel_size, padding = "same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.Activation("relu")(x)
	return x

# skip-connection有りの畳み込み層
def residual_layer(x, n_filter, kernel_size):
	from keras import layers
	prev_x = x # skip_connection用に退避
	x = layers.Conv2D(n_filter, kernel_size, padding = "same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.Activation("relu")(x)
	x = layers.Conv2D(n_filter, kernel_size, padding = "same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.add([x, prev_x])	# 合流部
	x = layers.Activation("relu")(x)
	return x

# 全結合層
def dense_layer(x, unit_n, activation = None):
	from keras import layers
	x = layers.Dense(unit_n, activation = activation)(x)
	return x

# シンプルなCNN [normal_cnn]
class Normal_CNN:
	# 初期化処理
	def __init__(self, n_out, nn_param, loss = "mse", optimizer = "sgd", untrained_pred_func = "default"):
		self.keras_model = None
		self.n_out = n_out
		self.nn_param = nn_param
		self.loss = loss
		self.optimizer = optimizer
		if untrained_pred_func == "default":
			self.untrained_pred_func = default_untrained_pred_func	# デフォルトの「未学習時における予測関数」 (エラーで落ちる挙動)
		else:
			self.untrained_pred_func = untrained_pred_func
	# 学習
	def fit(self, input_ls, output_ls, epochs = 10):
		if self.keras_model is None:
			image_shape = input_ls[0].shape
			# keras-cnnの初期化
			ret_nn = self.instantiate_nn(input_shape = image_shape)
			self.keras_model = ret_nn
		self.keras_model.fit(input_ls, output_ls, epochs = epochs)
	# サンプル中の1つのバッチで勾配を更新 [normal_cnn]
	def train_on_batch(self, input_ls, output_ls):
		if self.keras_model is None:
			image_shape = input_ls[0].shape
			# keras-cnnの初期化
			ret_nn = self.instantiate_nn(input_shape = image_shape)
			self.keras_model = ret_nn
		loss_value = self.keras_model.train_on_batch(input_ls, output_ls)
		return loss_value
	# 未学習判定 (1度でも学習されたかどうか) [normal_cnn]
	def is_trained(self):
		return (self.keras_model is not None)
	# 予測
	def predict(self, input_ls):
		if self.is_trained() is True:	# 未学習判定 (1度でも学習されたかどうか)
			# 通常時
			pred_ls = self.keras_model.predict(input_ls)
		else:
			# 未学習時
			pred_ls = self.untrained_pred_func(input_ls)
		return pred_ls
	# 複製体を作る (返り値はNormal_CNN型) [normal_cnn]
	def clone_model(self, untrained_check = True):
		# 新たに初期化 (同じ型のオブジェクト)
		cloned_obj = self.__class__(n_out = self.n_out, nn_param = self.nn_param, loss = self.loss, optimizer = self.optimizer, untrained_pred_func = self.untrained_pred_func)
		# 未学習のチェック
		if untrained_check is True:
			if self.keras_model is None:
				raise Exception("[Normal_CNN error] 未学習状態でclone_model()が呼ばれました。学習済みになってからclone_model()を実行するか、untrained_checkをFalseに設定して利用してください。")
		# keras_modelを複製して注入
		if self.keras_model is None:
			cloned_obj.keras_model = None
		else:
			from keras.models import clone_model as keras_clone_model
			copied_keras_model = keras_clone_model(self.keras_model)
			cloned_obj.keras_model = copied_keras_model
			# kerasのclone_modelがweightのコピーをしてくれないため、ここで実施
			cloned_obj.weight_update(self)	# weightを複写する (別のNormal_CNNオブジェクトから) [normal_cnn]
		return cloned_obj
	# weightを複写する (別のNormal_CNNオブジェクトから) [normal_cnn]
	def weight_update(self, source_obj):
		weight = source_obj.keras_model.get_weights()
		self.keras_model.set_weights(weight)
	# keras-cnnの初期化
	def instantiate_nn(self, input_shape):
		from keras import layers
		# 入力層の定義
		inputs = layers.Input(shape = input_shape)
		# 畳み込み層の定義
		feature = inputs
		for one_info in self.nn_param["conv_layer_info"]:
			n_filter = one_info["n_filter"]
			kernel_size = one_info["kernel_size"]
			feature = normal_conv_layer(feature, n_filter, kernel_size)	# skip-connection有りの畳み込み層
		# Flatten
		feature = layers.Flatten()(feature)
		# 全結合層、出力層の定義
		for one_info in self.nn_param["dense_layer_info"]:
			unit_n = one_info["unit_n"]
			activation = one_info["activation"]
			feature = dense_layer(feature, unit_n = unit_n, activation = activation)	# 全結合層
		output_activation = self.nn_param["output_activation"]
		outputs = dense_layer(feature, unit_n = self.n_out, activation = output_activation)	# 出力層
		# 層をまとめる
		from keras.models import Model
		model = Model(inputs = inputs, outputs = outputs)
		model.compile(loss = self.loss, optimizer = self.optimizer)
		return model
