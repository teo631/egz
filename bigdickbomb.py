from keras.preprocessing.image import load_img
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from keras.applications.vgg16 import preprocess_input
from keras.models import load_model 
from array import *
import os

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from isleme import *
from array import *

new_model = load_model("my_model/my_models.h5")

def cevaplar(resim,soru1,soru2,soru3,soru4,soru5,soru6): 
        img = Image.open(resim).resize((224,224))
        img = np.array(img)
        img = img.reshape(-1,224,224,3)
        img = preprocess_input(img)   
        img_for_display = load_img(resim)
        plt.imshow(img_for_display)
        plt.show()
            
        prediction = new_model.predict(img)
        image_clases = ["ekzama","sedef","tümör"]
        result = np.argmax(prediction)
        prediction1 = image_clases[result]

        string1="Sağlıksınız"
        seviye="1"

        if soru1 == str(1) and soru2 == str(1) and soru3 == str(1) and soru4 == str(1):
            if prediction1 == "ekzama":
                string1="Büyük ihtimale ekzamasınız"
                seviye="3"
            else:
                string1="Ekzama olabilirsiniz"
                seviye="2"
        if soru1 == str(1) and soru2 == str(1) and soru3 == str(1) and soru4 == str(1) and soru5 == str(1):
            if prediction1 == "tümör":
                print("Büyük ihtimale tümörsünüz")
                string1="Büyük ihtimale tümörsünüz"
                seviye="3"
            else:
                print("Tümör olabilirsiniz")
                string1="Tümör olabilirsiniz"
                seviye="2"
        if soru1 == str(0) and soru2 == str(0) and soru3 == str(0) and soru4 == str(0) and soru6 == str(1):
            if prediction1 == "sedef":
                print("Büyük ihtimale sedefsiniz")
                string1="Büyük ihtimale sedefsiniz"
                seviye="3"
            else:
                print("Sedef olabilirsiniz")
                string1="Sedef olabilirsiniz"
                seviye="2"

        return jsonify(
        {
            'status': string1+" (%"+str(result[0])+"90 eminlik)",
            'risk': "Tedavi gerekli",
            'seviye': seviye
        })
    