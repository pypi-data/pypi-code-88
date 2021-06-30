
import os
import sys
import time
import base64
import random
import pickle
import shutil
from sout import sout
from relpath import rel2abs
from fileinit import fileinit
from .parts.AES_crypt import AESCipher

revived_file_dir = "./__tskr_revived__/"

_correct_enc_key = "correct encryption key!"

# 16進数の乱数を生成
def gen_16_rand(n):
	ls16 = "0123456789abcdef"
	ret_ls = [ls16[int(random.random()*16)]
		for _ in range(n)]
	return "".join(ret_ls)

# tskr形式で保存 (file_id: None指定で新規作成)
def tskr_save(org_filename, file_pool_dir, group_enc_key, file_size_limit, file_id):
	# 新規作成の場合
	if file_id is None:
		# ファイルのidとkeyを作成
		file_id = gen_16_rand(n = 16)	# 16進数の乱数を生成
	# # ファイル指定子の決定
	# file_acc = "tskr_%s_%s"%(file_id, file_key)
	# 対象の読み込み
	with open(org_filename, "rb") as f:
		org_cont = f.read()
	# 容量制限
	if len(org_cont) > file_size_limit:
		print("[error] ファイル容量が大きすぎます。(容量制限: %d bytes, 今回のファイル: %d bytes)"%(file_size_limit, len(org_cont)))
		return None	# 以降の処理を実行しない
	# ファイル名とコンテンツをバインド
	raw_bind_obj = pickle.dumps({
		"original_filename": os.path.basename(org_filename),
		"contents": org_cont
	})
	# 暗号化
	base64_str = base64.b64encode(raw_bind_obj).decode()
	aesc = AESCipher(group_enc_key)
	bind_obj = aesc.encrypt(base64_str)
	# 暗号化キーチェック用文字列を併記
	key_check_str = aesc.encrypt(_correct_enc_key)
	save_obj = {
		"bind_obj": bind_obj,	# ファイル本体の内容が記録されたオブジェクト
		"key_check_str": key_check_str,	# 暗号化キーが正しいかをチェックする文字列
	}
	# 対象の保存
	pool_filename = "%s/%s.tskrpool"%(file_pool_dir, file_id)
	fileinit(pool_filename, overwrite = True)
	with open(pool_filename, "wb") as f:
		pickle.dump(save_obj, f)
	return file_id

# tskr形式のファイルを開く
def get_from_pool(file_id, group_enc_key, file_pool_dir):
	# 復号用オブジェクトの初期化
	aesc = AESCipher(group_enc_key)
	# 対象の読み込み
	pool_filename = "%s/%s.tskrpool"%(file_pool_dir, file_id)
	with open(pool_filename, "rb") as f:
		file_obj = pickle.load(f)
	# 暗号化キーが正しいかどうかチェック
	key_check_str = file_obj["key_check_str"]
	if aesc.decrypt(key_check_str) != _correct_enc_key:
		raise Exception("[tskr error] 誤った get_enc_key が使用されました")
	# 復号
	bind_obj = file_obj["bind_obj"]
	base64_str = aesc.decrypt(bind_obj)
	org_bind_obj = base64.b64decode(base64_str.encode())
	# バインドされたコンテンツの解釈
	file_data = pickle.loads(org_bind_obj)
	return file_data

# バイナリデータをファイルとして保存
def put_bin_file(bin_data, path):
	with open(path, "wb") as f:
		f.write(bin_data)

# zipファイルを展開する
def extend_zip(zip_path, put_dir):
	shutil.unpack_archive(zip_path, put_dir)

# 構成を取得 (fullpath・サイズ・最終更新日時)
def get_file_status(root_dir):
	result_ls = []
	for raw_dir_name, _, file_ls in os.walk(root_dir):
		dir_name = os.path.abspath(raw_dir_name)
		result_file_ls = []
		for file_name in file_ls:
			full_path = "%s/%s"%(dir_name, file_name)
			file_stat = os.stat(full_path)
			result_file_ls.append({
				"filename": file_name,
				"最終更新日時": file_stat.st_mtime,
				"size": file_stat.st_size
			})
		result_ls.append((dir_name, result_file_ls))
	# 並べ替える
	result_ls.sort(key = lambda e: e[0])
	for e in result_ls: e[1].sort(key = lambda e: e["filename"])
	return result_ls

# コマンドライン引数 (辞書形式で取得)
def get_argv_dic():
	# コマンドライン引数の取得 (第一引数は無視)
	argv_ls = sys.argv[1:]
	# コマンドライン引数なき場合
	if len(argv_ls) == 0: return {}
	# 区切りメタ文字
	meta_div = "<__META_DIV__>"
	# 「ハイフン」ありの部分でsplitする
	comb_s = meta_div + meta_div.join(argv_ls)
	hyphen_ls = comb_s.split(meta_div + "-")
	# ハイフンなしで始まっている場合
	if hyphen_ls[0] != "": raise Exception("[error] 最初のオプション引数は「-」で始まる必要があります")
	# ハイフンごとに分けて格納
	argv_dic = {}
	for e in hyphen_ls[1:]:
		ls = e.split(meta_div)
		if len(ls) not in [1,2]: raise Exception("[error] 文法エラー")
		key = "-" + ls[0]
		value = None
		if len(ls) == 2: value = ls[1]
		argv_dic[key] = value
	return argv_dic

# tskrのpoolの場所を読み込み
def load_file_pool_dir():
	# 存在しない場合にpath_fileを生成する
	path_file = "./file_pool_path.txt"
	fileinit(rel2abs(path_file), overwrite = False)
	# file_pool_pathの読み込み
	with open(rel2abs(path_file), "r", encoding = "utf-8") as f:
		file_pool_dir = f.read().strip()
	if file_pool_dir == "":
		raise Exception("file_pool_pathが設定されていません。オプション引数「--poolpath」を使って設定してください。")
	return file_pool_dir

# 既存のファイルが存在したら無視する無視
def tonikaku_mkdir(make_dir):
	if os.path.exists(make_dir) is False:
		os.mkdir(make_dir)

# zip圧縮
def make_zip(target_dir, zip_filename):
	temp_basename, _ = os.path.splitext(zip_filename)
	shutil.make_archive(temp_basename, "zip", root_dir = target_dir)

# 空フォルダのzipを作成
def make_empty_zip(zip_filename):
	# zip作業対象ディレクトリ
	target_dir = zip_filename + "/../__tskr_temp_new_empty_folder/"
	# ほぼ空のフォルダを作る
	fileinit(target_dir + "/__tskr_dummy_file", overwrite = True)
	# zip圧縮
	make_zip(target_dir = target_dir, zip_filename = zip_filename)
	# 一時ディレクトリを消す
	shutil.rmtree(target_dir)

# tskrツールのコア機能
class Tskr_Core:
	# 初期化処理
	def __init__(self):
		# tskrのpoolの場所を読み込み
		self.file_pool_dir = load_file_pool_dir()
		# ファイル容量制限
		self.file_size_limit = 10 * (1024**2)	# 10MB
		# 「.tskr」ファイルの保存場所
		self.tskr_save_dir = "./"
	# 新規作成
	def create(self, argv_dic):
		share_group = argv_dic.get("--share", argv_dic.get("-s", None))
		if share_group is None: raise Exception("[error] --share もしくは -sの指定が必要です")
		# 暗号化キーを取得
		group_enc_key = self.get_enc_key(share_group)
		# 空フォルダのzipを作成
		empty_zip_filename = rel2abs("./__tskr_temp_data.zip")
		make_empty_zip(empty_zip_filename)
		# tskr形式で保存 (file_id: None指定で新規作成)
		file_id = tskr_save(empty_zip_filename, self.file_pool_dir, group_enc_key, self.file_size_limit, file_id = None)
		# 空フォルダのzipを削除
		os.remove(empty_zip_filename)
		# 「～.tskr」ファイルの作成 (ショートカットのような役割のファイル)
		with open("./new_tskr_file.tskr", "w", encoding = "utf-8") as f:
			f.write(file_id)
	# 開く
	def read(self, argv_dic):
		share_group = argv_dic.get("--share", argv_dic.get("-s", None))
		# file_idの取得
		with open(argv_dic["--tskr_filename"], "r", encoding = "utf-8") as f:
			file_id = f.read().strip()
		# 暗号化キーを取得
		group_enc_key = self.get_enc_key(share_group)
		# tskr形式のファイルを開く
		file_data = get_from_pool(file_id, group_enc_key, self.file_pool_dir)
		# zip形式でファイル仮設置
		put_bin_file(bin_data = file_data["contents"], path = rel2abs("./__tskr_temp_data.zip"))	# バイナリデータをファイルとして保存
		# 16進数の乱数を生成
		temp_put_folder_name = gen_16_rand(n = 16)
		# zipファイルを展開する
		extend_zip(zip_path = rel2abs("./__tskr_temp_data.zip"), put_dir = rel2abs("./__tskr_temp_data/%s/"%temp_put_folder_name))
		# 一時的なzipファイルを消す
		os.remove(rel2abs("./__tskr_temp_data.zip"))
		# 構成を取得 (fullpath・サイズ・最終更新日時)
		file_status = get_file_status(root_dir = rel2abs("./__tskr_temp_data/%s/"%temp_put_folder_name))
		# 設置したフォルダを自動的に開く (エクスプローラーで)
		os.system("start %s"%rel2abs("./__tskr_temp_data/%s/"%temp_put_folder_name))
		# 変更監視・上書き保存 (update)
		self.update(file_status, temp_put_folder_name, argv_dic, file_id)
	# 対象のディレクトリをpoolに保存する
	def save_dir(self, argv_dic, editing_dir, file_id):
		share_group = argv_dic.get("--share", argv_dic.get("-s", None))
		if share_group is None: raise Exception("[error] --share もしくは -sの指定が必要です")
		# 暗号化キーを取得
		group_enc_key = self.get_enc_key(share_group)
		# フォルダの内容をzip化
		zip_filename = rel2abs("./__tskr_temp_data.zip")
		make_zip(target_dir = editing_dir, zip_filename = zip_filename)	# zip圧縮
		# tskr形式で保存 (file_id: None指定で新規作成)
		tskr_save(zip_filename, self.file_pool_dir, group_enc_key, self.file_size_limit, file_id)
		# print("ほぞんしたよ")
		# sys.exit()
		# zipを削除
		os.remove(zip_filename)
	# 変更監視・上書き保存 (update)
	def update(self, file_status, temp_put_folder_name, argv_dic, file_id):
		pre_file_status = file_status
		editing_dir = rel2abs("./__tskr_temp_data/%s/"%temp_put_folder_name)
		while True:
			# 構成を取得 (fullpath・サイズ・最終更新日時)
			file_status = get_file_status(root_dir = editing_dir)
			if file_status != pre_file_status:
				# 対象のディレクトリをpoolに保存する
				self.save_dir(argv_dic, editing_dir, file_id)
				pre_file_status = file_status
			# 少し待つ (環境にもよるが、2048個のファイル走査に0.14秒ほどかかる)
			time.sleep(3)
	# 暗号化キーを取得
	def get_enc_key(self, share_group):
		# ！！！！！仮実装
		group_enc_key = {"debug_group": "080cb8a3e27bf5a95e19549642103a42"}
		# share_groupが不正の場合
		if share_group not in group_enc_key:
			raise Exception("[tskr error] 未登録のshare_groupが指定されました")
		# 引き当てて返す
		return group_enc_key[share_group]

# tskrツールのコア機能 (ツール起動時に1度きり自動的に初期化)
tskr_core = Tskr_Core()	# tskrツールのコア機能

# コンソールからの命令の受付
def tskr_command():
	# コマンドライン引数 (辞書形式で取得)
	argv_dic = get_argv_dic()
	# コマンドで分岐
	if "-c" in argv_dic or "--create" in argv_dic:
		# 新規作成
		tskr_core.create(argv_dic)
	elif "-r" in argv_dic or "--read" in argv_dic:
		# 開く
		tskr_core.read(argv_dic)
	else:
		raise Exception("[error] ハンドルされていないコマンドが呼ばれました (%s)"%str(sys.argv))
	# debbug
	sys.exit()
	### pool_path書き換えモード
	if len(argv_ls) == 3 and argv_ls[1] == "--poolpath":
		with open(rel2abs(path_file), "w", encoding = "utf-8") as f:
			f.write(argv_ls[2])
		print("file_pool_pathを設定しました")
		return None
	### 保存モード
	if len(argv_ls) == 2:
		# 保存対象ファイル名の取得
		org_filename = argv_ls[1]
		# tskr形式で保存
		file_acc = tskr_save(org_filename, file_pool_dir, file_size_limit)
		# ファイル指定子(file_acc)の表示
		if file_acc is not None:
			print("ファイル指定子は以下のとおりです:")
			print("\n%s\n"%file_acc)
			print("【！】忘れずにクリップボード等にコピーしてください")
		input("[Enter] で終了...")
	### 開くモード
	if len(argv_ls) == 1:
		# 対象の入力
		print("※ファイルをtskr形式に変換する際は、コマンドライン引数でファイル名を指定してください")
		file_acc = input("ファイル指定子>")
		# tskr形式のファイルを開く
		tskr_open(file_acc, file_pool_dir)
		return None

# # モジュールオブジェクトと関数を同一視
# sys.modules[__name__] = tskr
