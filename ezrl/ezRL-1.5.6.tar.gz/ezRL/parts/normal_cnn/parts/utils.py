
# 共通処理群 [normal_cnn]

import sys

# デフォルトの「未学習時における予測関数」 (エラーで落ちる挙動)
def default_untrained_pred_func(test_x):
	raise Exception("[normal_cnn error] 未学習の状態でprediction()関数が呼ばれました (未学習時の挙動は、NormalCNNクラス初期化時の引数untrained_pred_funcにより指定することができます。)")
