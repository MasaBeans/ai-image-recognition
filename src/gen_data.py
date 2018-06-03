from PIL import Image
import os, glob  # globはファイルの一覧を取得するためのパッケージ
import numpy as np
# from sklearn import cross_validation
from sklearn import model_selection  # 上のcross_validationは近々廃止される

labels = ("monkey", "boar", "crow")
num_labels = len(labels)
image_size = 50  # 縦横50pxに変換する

# 画像の読み込み

X = []
Y = []
for label_id, label_str in enumerate(labels):
    images_dir = "../images/" + label_str
    files = glob.glob(images_dir + "/*.jpg")
    for i, image_file in enumerate(files):
        if i >= 152: break  # 画像ファイル数の最小値が152枚のため
        image_data = Image.open(image_file)
        image_data = image_data.convert("RGB")
        image_data = image_data.resize((image_size, image_size))
        image_data_array = np.asarray(image_data)  # Tensorflowが扱いやすい型にする
        X.append(image_data_array)
        Y.append(label_id)

X = np.array(X)
Y = np.array(Y)

# trainとevalにX, Yを分割
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("../data/train_test_xy.npy", xy)
