from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
from keras.models import load_model
from PIL import Image
import numpy as np

def predict(): 
    desired_size=224
    model = load_model("./model2.hd5")
    x_test = np.empty((1, 224, 224, 3), dtype=np.uint8)
  #  image = load_img(image1, target_size=(224, 224))
    # convert the image pixels to a numpy array
    im = Image.open("./00001.jpg")
    im = im.resize((desired_size, desired_size))
    im = np.array(im) / 255
    x_test[0, :, :, :] = im
    # label = label[0][0]
    test =model.predict(x_test)
    print(test)
    return test 

predict()
