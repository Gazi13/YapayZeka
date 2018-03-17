import numpy as np
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense

# xor gibi aynılar 0 farklılar 1 yani Kırmızı renk 0 Beyaz renk 1 gibi 2 grup yaptık
X = np.matrix([[0,0],[1,0],[0,1],[1,1]])
y = np.array([0,1,1,0])
X2 = np.matrix([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],
     [2,3],[2,8],[7,9],[4, 6],[7, 3],[7, 5],[2, 9],[3, 13],[38, 18],[79, 29],[4, 2],[7, 22]])
y2 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0])

model = Sequential()
model.add(Dense(60,input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss="mean_squared_error",optimizer="adam",metrics=["binary_accuracy"])
model.fit(X2,y2,nb_epoch=50000)
model.save("model3.h5")