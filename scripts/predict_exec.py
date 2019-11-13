# Note the sys declaration here is to sync with the server's python run time.
import sys
import logging
import warnings
logging.disable(logging.WARNING)
with warnings.catch_warnings():  
    warnings.filterwarnings("ignore",category=FutureWarning)
    import tensorflow as tf
    import keras
    import numpy as np
    # Run the pythons cript
    from keras.applications.resnet50 import ResNet50
    # from keras.preprocessing import image
    from keras.applications.resnet50 import preprocess_input, decode_predictions
import cv2

# needed when dealing with multi threading
sess = tf.Session()
keras.backend.set_session(sess)

model = ResNet50(weights='imagenet')

img = cv2.imread(img_path)
x = cv2.resize(img,(224,224))
x = x[...,::-1].astype(np.float32) #Switch BGR to RGB
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
decoded = decode_predictions(preds, top=3)[0]
id,label,proba = decoded[0]
proba = str(proba)