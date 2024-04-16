from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from isleme import *

import os
#flask --app test run
#"liveServer.settings.ignoreFiles": [ "**/**",   ]
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/upload_image", methods=['POST'])
@cross_origin()
def upload_image():

    image_file = request.files['image']
    bool_value1 = request.form.get('boolValue1')
    bool_value2 = request.form.get('boolValue2')
    bool_value3 = request.form.get('boolValue3')
    bool_value4 = request.form.get('boolValue4')
    bool_value5 = request.form.get('boolValue5')
    bool_value6 = request.form.get('boolValue6')

    image_file.save(os.getcwd()+"/resimler/uploaded_image.jpg")

    print(bool_value4)

    x=hastaMi(os.getcwd()+"/resimler/uploaded_image.jpg",bool_value1,bool_value2)
    print(bool_value2)
    if(bool_value1==bool_value2):
        x="adsa"
    else:
        x="dasdasds"

    return jsonify({'status': x})