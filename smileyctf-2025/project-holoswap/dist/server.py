import base64
import io
import os
import numpy as np
import absl.logging
import warnings
from PIL import Image

### Suppress tensorflow warnings and import
absl.logging.set_verbosity('error')
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['XLA_FLAGS'] = '--xla_hlo_profile'

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

tf.get_logger().setLevel('ERROR')
### End

def load_image(img):
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img = img_to_array(img.resize((96, 96)))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def calculate_l2_norm(image1, image2):
    return np.linalg.norm(image1.squeeze() - image2.squeeze())

try:
    model = load_model('./model.h5')

    original_image = load_image(Image.open('./gura.png'))
    assert np.argmax(model.predict(original_image)) == 5

    image_data = input("Enter the base64 encoded image data: ").strip()
    input_image = load_image(Image.open(io.BytesIO(base64.b64decode(image_data))))

    prediction = model.predict(input_image)

    if np.argmax(prediction) == 9 and prediction[0][9] > 0.999:
        if calculate_l2_norm(input_image, original_image) < 0.9:
            print("Detective Amelia: That's *definitely* not me... but close enough.")
            print(f"{os.getenv('FLAG', '.;,;.{.;,;.}')}")
        else:
            print("a")
    else:
        print("a")
except:
    pass