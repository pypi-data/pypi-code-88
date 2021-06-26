
# 画像等の結果出力パス管理 [resout]

import os
import sys
from datetime import datetime

# resoutの設定値群
_config = {
	"root_save_dir": "./output_img/",	# 保存パスのデフォルト値
	"index": {},	# ファイル名に付与するindex
}

# 現在時刻のタイムスタンプを取得
def get_timestamp():
	now_dt = datetime.now()
	return now_dt.strftime("%Y%m%dT%H%M%S")

# 保存パスの設定 [resout]
def set_save_dir(save_dir):
	_config["root_save_dir"] = save_dir

# indexの取得 [resout]
def _get_index(label, increment = False):
	# 初回の場合
	if label not in _config["index"]:
		_config["index"][label] = 0
	# 現在のindexの取得
	idx = _config["index"][label]
	# インクリメント
	if increment is True:
		_config["index"][label] += 1
	return idx

# 保存ファイル名の生成(自動で連番になる) [resout]
def gen_save_path(ext, label = "resout"):
	# 保存フォルダの特定 (ない場合は作成)
	save_dir = "%s/%s/"%(_config["root_save_dir"], _config["boot_time"])
	os.makedirs(save_dir, exist_ok = True)
	# ファイル名を生成して返す
	idx = _get_index(label, increment = True)	# indexの取得 [resout]
	raw_fullpath = "%s/%s_%d%s"%(save_dir, label, idx, ext)
	return os.path.abspath(raw_fullpath)

# 画像の保存 [resout]
def save_img(img, ratio = 1.0, ext = ".png", label = "resout_img", interpolation = "INTER_CUBIC"):
	import cv2
	interpolation_dic = {"INTER_CUBIC": cv2.INTER_CUBIC, "INTER_NEAREST": cv2.INTER_NEAREST}
	if interpolation not in interpolation_dic: raise Exception("[resout error] 未対応のinterpolation値が指定されました")
	resized_img = cv2.resize(img, None, fx = ratio, fy = ratio, interpolation = interpolation_dic[interpolation])
	# 保存ファイル名の生成(自動で連番になる) [resout]
	fullpath = gen_save_path(ext, label)
	cv2.imwrite(fullpath, resized_img)

# モジュールの初期化処理
_config["boot_time"] = get_timestamp()	# 現在時刻のタイムスタンプを取得
