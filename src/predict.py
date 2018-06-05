from keras.optimizers import rmsprop
from keras.models import Sequential, load_model  # ニューラルネットワークのモデルを定義する際にしよう
from keras.layers import Conv2D, MaxPooling2D  # たたみ込みやプーリングをする
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from PIL import Image
import sys
import numpy as np

labels = ("monkey", "boar", "crow")
num_labels = len(labels)
image_size = 50  # 縦横50pxに変換する


def build_model():
    #model = Sequential()
    #model.add(Conv2D(32,(3,3), padding='same', input_shape=(50,50,3)))
    #model.add(Activation('relu'))
    #model.add(Conv2D(32,(3,3)))
    #model.add(Activation('relu'))
    #model.add(MaxPooling2D(pool_size=(2,2)))
    #model.add(Dropout(0.25))

    #model.add(Conv2D(64,(3,3), padding='same'))
    #model.add(Activation('relu'))
    #model.add(Conv2D(64,(3,3)))
    #model.add(Activation('relu'))
    #model.add(MaxPooling2D(pool_size=(2,2)))
    #model.add(Dropout(0.25))

    #model.add(Flatten())
    #model.add(Dense(512))
    #model.add(Activation('relu'))
    #model.add(Dropout(0.25))
    #model.add(Dense(3))
    #model.add(Activation('softmax'))

    #opt = rmsprop(lr=0.0001, decay=1e-6)

    #model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

    # モデルのロード
    model = load_model('../models/model_cnn_augmented.h5')

    return model

def main():
    image = Image.open(sys.argv[1])
    image = image.convert("RGB")
    image = image.resize((image_size,image_size))
    data = np.asarray(image)
    X = []
    X.append(data)
    X = np.array(X)
    model = build_model()

    result = model.predict([X])[0]
    predicted = result.argmax()  # 何番目の確率が大きいか
    percentage = int(result[predicted] * 100)
    print("{0} ({1} %)".format(labels[predicted],percentage))

if __name__ == "__main__":
    main()
