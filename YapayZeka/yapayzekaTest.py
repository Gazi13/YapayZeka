import numpy as np
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense


"""Aynı olursa   --> 0 
   Farklı Olursa --> 1 """
model = load_model("model3.h5")
d1 = int(input("Enter number 1 : "))
d2 = int(input("Enter number 2 : "))
Sonuc = model.predict(np.array([[d1,d2]]))
SonucYazi =""
if(Sonuc>=0.5):
    SonucYazi="AYNI"
elif(Sonuc<0.5):
    SonucYazi="FARKLI"
print(Sonuc)
print(SonucYazi)