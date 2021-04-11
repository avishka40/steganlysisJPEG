import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from efficientNetClassify import Predicter
import numpy as np

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
predictor = None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file-upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'image' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    file = request.files['image']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        npimg = np.fromstring(file.read(), np.uint8)
        image = predicter.preprocess(npimg,True)
        predictedResults = predicter.predict(image)
        resp = jsonify({'multiClass': predictedResults.multiClassArray.tolist(),
        "binaryClass":predictedResults.binaryArray.tolist()})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(
            {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp


if __name__ == "__main__":
    predicter = Predicter()
    app.run()
