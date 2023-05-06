import tensorflow as tf
import tensorflow_hub as hub
from scipy.spatial import distance

model_layers = hub.KerasLayer("https://tfhub.dev/tensorflow/efficientnet/lite0/feature-vector/2")
threshold = 0.35

def decode_image(filepath):
    img = tf.io.read_file(filepath)
    img = tf.image.decode_image(img, channels=3, dtype=tf.dtypes.float64)
    img = tf.image.resize(img, (224, 224))
    img = tf.expand_dims(img, axis = 0)
    
    return img

def preprocess_image(filepath):
    img = decode_image(filepath)
    img_results = model_layers(img)
    img_features_squeezed = tf.squeeze(img_results)
    
    return img_features_squeezed

def authenticate(original, to_authenticate):
    dc = distance.cdist([original], [to_authenticate], 'correlation')[0][0]
    print(dc)
    if dc < threshold:
        print('matched')
    else:
        print('not matched')



