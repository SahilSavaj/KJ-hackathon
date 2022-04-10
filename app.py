from cv2 import imshow
from flask import Flask, request,render_template,redirect,Response,flash,url_for
import os
import cv2
import numpy as np
import keras.models
import tensorflow
folder=os.path.dirname(__file__)
model = keras.models.load_model('./cnn_model.h5')

app=Flask(__name__,template_folder='templates')
app.secret_key='hack'

@app.route("/")
def main():
    return render_template('app.html')

@app.route("/upload",methods=["POST","GET"])
def home():
    if request.method=='POST':
        f=request.files['file'].read()
        f = np.frombuffer(f, np.uint8)
        img = cv2.imdecode(f, cv2.IMREAD_COLOR)
        img=cv2.resize(img,(224,224),interpolation = cv2.INTER_NEAREST)
        final_img=np.array([img])
        final_img.shape
        
        x=model.predict(final_img)
        if x<0.4:
            return render_template('fake.html')
        elif 0.4<x<0.6:
            return render_template('imagenotclear.html')
        else:
            return render_template('real.html')
        #model image dimention (1,224,224,3)
        
    else:
        return render_template('app.html')

if __name__ == "__main__":
    app.run()